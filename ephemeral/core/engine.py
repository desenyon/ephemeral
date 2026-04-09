"""Main research engine orchestrating all Ephemeral capabilities."""

import asyncio
from datetime import datetime
from typing import Any, Dict, List, Optional

from ephemeral.analytics import PerformanceAnalytics
from ephemeral.backtest import get_available_strategies, run_backtest
from ephemeral.charts import create_candlestick_chart, create_comparison_chart, create_line_chart
from ephemeral.comparison import ComparisonEngine
from ephemeral.io.artifacts import ArtifactBundle, write_artifact_bundle
from ephemeral.portfolio import Constraint as PortfolioConstraint
from ephemeral.portfolio import OptimizationMethod, PortfolioOptimizer
from ephemeral.research.memo import memo_from_tool_bundle
from ephemeral.research.session import ResearchPhase, ResearchSession
from ephemeral.research.sources import SourceRef
from ephemeral.services.market_data import MarketDataBundle, MarketDataService, load_returns_matrix
from ephemeral.tools.library import compare_stocks

from .intent import DecisivenessEngine, IntentParser, PromptPresets
from .models import DeliverableType, ResearchPlan


class Engine:
    """Main research engine for Ephemeral."""

    def __init__(self):
        self.intent_parser = IntentParser()
        self.decisiveness = DecisivenessEngine()
        self.presets = PromptPresets()
        self.data_cache = {}
        self.lineage_tracker = []
        self.market_data = MarketDataService()
        self.performance = PerformanceAnalytics()
        self.comparison_engine = ComparisonEngine()
        self.portfolio_optimizer = PortfolioOptimizer()

    async def process_query(self, query: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Process a user query end-to-end."""
        # Parse intent
        plan = await self.intent_parser.parse(query)

        # Check if clarifications needed
        if plan.clarifications_needed:
            return {
                "type": "clarification",
                "questions": plan.clarifications_needed,
                "partial_plan": plan.model_dump(),
            }

        # Handle vague queries with decisiveness engine
        vague_translation = self.decisiveness.translate_vague_query(query)
        if vague_translation["criteria"]:
            plan.context["measurable_criteria"] = vague_translation

        # Route to appropriate handler
        result = await self._route_deliverable(plan)

        return {
            "type": "result",
            "plan": plan.model_dump(),
            "result": result,
        }

    async def _route_deliverable(self, plan: ResearchPlan) -> Dict[str, Any]:
        """Route to appropriate handler based on deliverable type."""
        handlers = {
            DeliverableType.ANALYSIS: self._handle_analysis,
            DeliverableType.COMPARISON: self._handle_comparison,
            DeliverableType.BACKTEST: self._handle_backtest,
            DeliverableType.PORTFOLIO: self._handle_portfolio,
            DeliverableType.STRATEGY: self._handle_strategy,
            DeliverableType.CHART: self._handle_chart,
            DeliverableType.REPORT: self._handle_report,
            DeliverableType.ALERT: self._handle_alert,
        }

        handler = handlers.get(plan.deliverable, self._handle_analysis)
        return await handler(plan)

    async def _handle_analysis(self, plan: ResearchPlan) -> Dict[str, Any]:
        """Handle general analysis request."""
        symbols = self._symbols_for_plan(plan)
        period = plan.lookback_period or "6mo"
        session = ResearchSession(topic=plan.goal)
        session.default_equity_checklist()
        session.advance(ResearchPhase.DATA_GATHER)

        analyses: Dict[str, Any] = {}
        sources: List[Dict[str, Any]] = []
        for symbol in symbols:
            bundle = await self._build_bundle(symbol, period=period)
            analysis = self._analyze_bundle(bundle, period=period)
            analyses[symbol] = analysis
            if analysis.get("quote"):
                session.check("Quote & liquidity")
            if analysis.get("metrics"):
                session.check("Key metrics / valuation")
            if analysis.get("recent_headlines"):
                session.check("News / sentiment scan")
            sources.append(SourceRef.from_tool("market_data_bundle", symbol, extra=period).to_dict())

        session.advance(ResearchPhase.SYNTHESIS)
        session.set_artifact("analyses", analyses)
        return {
            "analyses": analyses,
            "period": period,
            "summary": self._summarize_analysis(analyses),
            "session": {
                "phase": session.phase.value,
                "completion_ratio": session.completion_ratio(),
                "checklist": dict(session.checklist),
            },
            "sources": sources,
        }

    async def _handle_comparison(self, plan: ResearchPlan) -> Dict[str, Any]:
        """Handle comparison request."""
        symbols = self._symbols_for_plan(plan)
        period = plan.lookback_period or "1y"
        criteria = plan.context.get("measurable_criteria", {})
        result: Dict[str, Any] = {
            "comparison_type": "multi_asset",
            "assets": symbols,
            "criteria": criteria.get("criteria", []),
            "interpretation": criteria.get("interpretation", ""),
            "period": period,
        }
        if len(symbols) < 2:
            result["warning"] = "Comparison needs at least two assets."
            return result

        matrix = await asyncio.to_thread(load_returns_matrix, symbols, period=period)
        if matrix.empty:
            result["comparison"] = await asyncio.to_thread(compare_stocks, symbols, period)
            result["warning"] = "Fell back to lightweight comparison because returns matrix was empty."
            return result

        returns_data = {symbol: matrix[symbol].dropna() for symbol in matrix.columns}
        benchmark_symbol = plan.benchmark or "SPY"
        benchmark_matrix = await asyncio.to_thread(load_returns_matrix, [benchmark_symbol], period=period)
        benchmark_returns = benchmark_matrix[benchmark_symbol] if benchmark_symbol in benchmark_matrix else None
        result["comparison"] = await self.comparison_engine.compare(
            list(matrix.columns),
            returns_data,
            benchmark=benchmark_symbol,
            benchmark_returns=benchmark_returns,
        )
        result["matrix_shape"] = {"rows": int(matrix.shape[0]), "columns": int(matrix.shape[1])}
        result["best_performer"] = self._best_performer_from_matrix(matrix)
        return result

    async def _handle_backtest(self, plan: ResearchPlan) -> Dict[str, Any]:
        """Handle backtest request."""
        symbols = self._symbols_for_plan(plan)
        strategy_id = self._pick_strategy_id(plan)
        period = plan.lookback_period or "2y"
        symbol = symbols[0]
        backtest = await asyncio.to_thread(run_backtest, symbol, strategy_id, period)
        return {
            "backtest_type": "strategy",
            "assets": symbols,
            "period": period,
            "constraints": [c.model_dump() for c in plan.constraints],
            "strategy_id": strategy_id,
            "available_strategies": get_available_strategies(),
            "backtest": backtest,
        }

    async def _handle_portfolio(self, plan: ResearchPlan) -> Dict[str, Any]:
        """Handle portfolio construction request."""
        symbols = self._symbols_for_plan(plan)
        period = plan.lookback_period or "1y"
        result: Dict[str, Any] = {
            "portfolio_type": "optimization",
            "assets": symbols,
            "risk_profile": plan.risk_profile,
            "constraints": [c.model_dump() for c in plan.constraints],
        }
        if len(symbols) < 2:
            result["warning"] = "Portfolio optimization needs at least two assets."
            return result

        returns = await asyncio.to_thread(load_returns_matrix, symbols, period=period)
        if returns.empty:
            result["warning"] = "No return history available for optimization."
            return result

        cleaned = returns.dropna()
        portfolio_constraints = [
            PortfolioConstraint(name=c.name, type=c.type, value=c.value)
            for c in plan.constraints
        ]
        optimized = await asyncio.to_thread(
            self.portfolio_optimizer.optimize,
            cleaned,
            OptimizationMethod.MAX_SHARPE,
            portfolio_constraints,
        )
        result["optimization"] = optimized.model_dump()
        result["period"] = period
        result["input_rows"] = int(cleaned.shape[0])
        return result

    async def _handle_strategy(self, plan: ResearchPlan) -> Dict[str, Any]:
        """Handle strategy discovery request."""
        symbols = self._symbols_for_plan(plan)
        period = plan.lookback_period or "6mo"
        ideas: List[Dict[str, Any]] = []
        for symbol in symbols:
            bundle = await self._build_bundle(symbol, period=period, include_news=False)
            ideas.append(self._strategy_idea_from_bundle(bundle, period=period))
        return {
            "strategy_type": "discovery",
            "assets": symbols,
            "horizon": plan.horizon,
            "ideas": ideas,
            "available_strategies": get_available_strategies(),
        }

    async def _handle_chart(self, plan: ResearchPlan) -> Dict[str, Any]:
        """Handle chart generation request."""
        symbols = self._symbols_for_plan(plan)
        period = plan.lookback_period or "6mo"
        histories: Dict[str, Any] = {}
        for symbol in symbols:
            bundle = await self._build_bundle(symbol, period=period, include_news=False)
            if bundle.history is not None and not bundle.history.empty:
                histories[symbol] = bundle.history

        result: Dict[str, Any] = {
            "chart_type": "price",
            "assets": symbols,
            "period": period,
        }
        if not histories:
            result["warning"] = "No price history available for chart generation."
            return result

        try:
            if len(histories) == 1:
                symbol, history = next(iter(histories.items()))
                if {"Open", "High", "Low", "Close"}.issubset(history.columns):
                    chart_path = await asyncio.to_thread(create_candlestick_chart, symbol, history)
                else:
                    chart_path = await asyncio.to_thread(create_line_chart, symbol, history)
            else:
                chart_path = await asyncio.to_thread(
                    create_comparison_chart,
                    list(histories.keys()),
                    histories,
                )
            result["chart_path"] = chart_path
        except Exception as exc:
            result["warning"] = f"Chart generation failed: {exc}"
        result["series"] = {
            symbol: {
                "rows": int(history.shape[0]),
                "start": str(history.index[0]),
                "end": str(history.index[-1]),
            }
            for symbol, history in histories.items()
        }
        return result

    async def _handle_report(self, plan: ResearchPlan) -> Dict[str, Any]:
        """Handle report generation request."""
        symbols = self._symbols_for_plan(plan)
        period = plan.lookback_period or "6mo"
        artifact = ArtifactBundle(
            name=f"research-report-{'-'.join(symbols[:3]).lower()}",
            meta={"goal": plan.goal, "assets": symbols, "period": period},
        )
        reports: Dict[str, Any] = {}
        for symbol in symbols:
            bundle = await self._build_bundle(symbol, period=period)
            memo = memo_from_tool_bundle(symbol, bundle.to_tool_dict(), title=f"{symbol} research report")
            markdown = memo.render_markdown()
            artifact.add_text(f"{symbol.lower()}_report.md", markdown)
            artifact.add_json(f"{symbol.lower()}_bundle.json", bundle.to_tool_dict())
            reports[symbol] = {"title": memo.title, "markdown": markdown}

        artifact_path = await asyncio.to_thread(write_artifact_bundle, artifact)
        return {
            "report_type": "research_memo",
            "assets": symbols,
            "period": period,
            "reports": reports,
            "artifact_path": str(artifact_path),
        }

    async def _handle_alert(self, plan: ResearchPlan) -> Dict[str, Any]:
        """Handle alert setup request."""
        symbols = self._symbols_for_plan(plan)
        alerts: List[Dict[str, Any]] = []
        for symbol in symbols:
            bundle = await self._build_bundle(symbol, period="1mo", include_news=False)
            quote = bundle.quote or {}
            price = float(quote.get("price") or 0.0)
            if price <= 0:
                alerts.append(
                    {
                        "symbol": symbol,
                        "status": "unavailable",
                        "message": "No live quote available to seed alert thresholds.",
                    }
                )
                continue
            alerts.append(
                {
                    "symbol": symbol,
                    "status": "draft",
                    "current_price": price,
                    "suggested_alerts": [
                        {"type": "pullback", "threshold": round(price * 0.95, 2)},
                        {"type": "breakout", "threshold": round(price * 1.05, 2)},
                    ],
                }
            )
        return {
            "alert_type": "watchlist",
            "assets": symbols,
            "alerts": alerts,
        }

    async def _build_bundle(
        self,
        symbol: str,
        *,
        period: str,
        include_news: bool = True,
    ) -> MarketDataBundle:
        try:
            return await self.market_data.build_bundle_async(symbol, period=period, include_news=include_news)
        except Exception as exc:
            return MarketDataBundle(symbol=symbol.upper(), errors=[str(exc)])

    def _symbols_for_plan(self, plan: ResearchPlan) -> List[str]:
        return list(dict.fromkeys([symbol.upper() for symbol in (plan.assets or ["SPY"])]))

    def _analyze_bundle(self, bundle: MarketDataBundle, *, period: str) -> Dict[str, Any]:
        analysis: Dict[str, Any] = {
            "symbol": bundle.symbol,
            "analysis_type": "comprehensive",
            "quote": bundle.quote,
            "metrics": {},
            "insights": [],
            "recent_headlines": bundle.news_headlines[:5],
            "info_summary": {
                key: bundle.info.get(key)
                for key in ("longName", "sector", "industry", "marketCap", "trailingPE", "beta")
                if bundle.info.get(key) is not None
            },
            "errors": list(bundle.errors),
        }
        history = bundle.history
        if history is None or history.empty or "Close" not in history:
            analysis["insights"].append(f"No historical price data available for {bundle.symbol}.")
            return analysis

        closes = history["Close"].dropna()
        returns = closes.pct_change().dropna()
        if returns.empty:
            analysis["insights"].append(f"Not enough return history to score {bundle.symbol}.")
            return analysis

        metrics = self.performance.calculate_metrics(returns)
        current_price = float(closes.iloc[-1])
        sma_20 = float(closes.rolling(20).mean().iloc[-1]) if len(closes) >= 20 else current_price
        sma_50 = float(closes.rolling(50).mean().iloc[-1]) if len(closes) >= 50 else sma_20
        total_return = float((closes.iloc[-1] / closes.iloc[0]) - 1) if len(closes) > 1 else 0.0

        analysis["metrics"] = {
            "period": period,
            "current_price": current_price,
            "total_return": total_return,
            "volatility": metrics.get("volatility"),
            "max_drawdown": metrics.get("max_drawdown"),
            "sharpe_ratio": metrics.get("sharpe_ratio"),
            "win_rate": metrics.get("win_rate"),
            "sma_20": sma_20,
            "sma_50": sma_50,
        }

        if current_price >= sma_20:
            analysis["insights"].append(f"{bundle.symbol} is trading above its 20-day average, indicating near-term trend support.")
        else:
            analysis["insights"].append(f"{bundle.symbol} is below its 20-day average, which weakens the near-term trend.")

        if current_price >= sma_50:
            analysis["insights"].append(f"The 50-day trend remains constructive for {bundle.symbol}.")
        else:
            analysis["insights"].append(f"The 50-day trend remains under pressure for {bundle.symbol}.")

        if bundle.news_headlines:
            lead = bundle.news_headlines[0]
            if lead.get("title"):
                analysis["insights"].append(f"Recent headline catalyst: {lead['title']}")
        return analysis

    def _summarize_analysis(self, analyses: Dict[str, Any]) -> List[str]:
        summary: List[str] = []
        for symbol, payload in analyses.items():
            metrics = payload.get("metrics") or {}
            current_price = metrics.get("current_price")
            total_return = metrics.get("total_return")
            if current_price is None or total_return is None:
                continue
            summary.append(
                f"{symbol}: {current_price:.2f} with {total_return * 100:+.2f}% return over {metrics.get('period', 'the period')}."
            )
        return summary

    def _pick_strategy_id(self, plan: ResearchPlan) -> str:
        available = get_available_strategies()
        candidates = [
            str(plan.context.get("strategy") or ""),
            str(plan.context.get("strategy_id") or ""),
            str(plan.context.get("original_query") or ""),
            plan.goal,
        ]
        haystack = " ".join(candidates).lower()
        for strategy_id in available:
            if strategy_id.lower() in haystack:
                return strategy_id
        return "sma_crossover"

    def _best_performer_from_matrix(self, matrix: Any) -> Optional[str]:
        if matrix.empty:
            return None
        scores = ((1 + matrix).prod() - 1).sort_values(ascending=False)
        return str(scores.index[0]) if not scores.empty else None

    def _strategy_idea_from_bundle(self, bundle: MarketDataBundle, *, period: str) -> Dict[str, Any]:
        idea: Dict[str, Any] = {
            "symbol": bundle.symbol,
            "period": period,
            "strategy_id": "sma_crossover",
            "rationale": [],
        }
        history = bundle.history
        if history is None or history.empty or "Close" not in history:
            idea["rationale"].append("No history available; defaulting to trend-following starter strategy.")
            return idea

        closes = history["Close"].dropna()
        returns = closes.pct_change().dropna()
        if returns.empty:
            idea["rationale"].append("Not enough returns to score behavior.")
            return idea

        volatility = float(returns.std() * (252 ** 0.5))
        total_return = float((closes.iloc[-1] / closes.iloc[0]) - 1) if len(closes) > 1 else 0.0
        if volatility > 0.45:
            idea["strategy_id"] = "rsi_mean_reversion"
            idea["rationale"].append("High realized volatility favors mean-reversion entries.")
        elif total_return > 0.1:
            idea["strategy_id"] = "dual_momentum"
            idea["rationale"].append("Positive medium-term momentum favors trend continuation.")
        else:
            idea["strategy_id"] = "sma_crossover"
            idea["rationale"].append("Trend profile is mixed, so a simple moving-average regime filter is a reasonable baseline.")
        idea["realized_volatility"] = volatility
        idea["period_return"] = total_return
        return idea

    # ========================================================================
    # UTILITY METHODS
    # ========================================================================

    def get_presets(self) -> List[Dict[str, str]]:
        """Get available prompt presets."""
        return self.presets.list_presets()

    def apply_preset(self, preset_name: str, **kwargs) -> Optional[str]:
        """Apply a prompt preset."""
        return self.presets.get_preset(preset_name, **kwargs)

    def get_show_work_mode(self) -> bool:
        """Check if show work mode is enabled."""
        return getattr(self, "_show_work", False)

    def set_show_work_mode(self, enabled: bool):
        """Enable/disable show work mode."""
        self._show_work = enabled

    def explain_technical(self, concept: str) -> str:
        """Explain a concept with formulas and definitions."""
        explanations = {
            "sharpe_ratio": """
**Sharpe Ratio**
Formula: (Rp - Rf) / σp
Where:
- Rp = Portfolio return
- Rf = Risk-free rate
- σp = Portfolio standard deviation

Interpretation: Risk-adjusted return per unit of volatility. Higher is better.
Typical values: <1 = poor, 1-2 = good, >2 = excellent
            """,
            "sortino_ratio": """
**Sortino Ratio**
Formula: (Rp - Rf) / σd
Where:
- Rp = Portfolio return
- Rf = Risk-free rate (or target return)
- σd = Downside deviation (only negative returns)

Interpretation: Like Sharpe but only penalizes downside volatility.
Better for asymmetric return distributions.
            """,
            "max_drawdown": """
**Maximum Drawdown**
Formula: (Peak - Trough) / Peak
Measures the largest peak-to-trough decline.

Interpretation: Worst-case loss from a peak.
Context: A 50% drawdown requires 100% gain to recover.
            """,
            "beta": """
**Beta (β)**
Formula: Cov(Ri, Rm) / Var(Rm)
Where:
- Ri = Asset return
- Rm = Market return

Interpretation: Sensitivity to market movements.
β = 1: Moves with market
β > 1: More volatile than market
β < 1: Less volatile than market
            """,
            "var": """
**Value at Risk (VaR)**
Formula: Quantile of return distribution at confidence level
Example: 95% VaR = 5th percentile of returns

Interpretation: Maximum expected loss at given confidence level.
95% VaR of -3% means 95% of the time, loss won't exceed 3%.
            """,
            "cvar": """
**Conditional VaR (CVaR) / Expected Shortfall**
Formula: E[Loss | Loss > VaR]
Average loss in the worst cases beyond VaR.

Interpretation: Expected loss when VaR is breached.
Better captures tail risk than VaR alone.
            """,
        }

        return explanations.get(concept.lower(), f"No detailed explanation available for: {concept}")


# ============================================================================
# AUTOCOMPLETE ENGINE
# ============================================================================

class AutocompleteEngine:
    """Provide intelligent autocomplete suggestions."""

    # Common commands
    COMMANDS = [
        "/help",
        "/shortcuts",
        "/keys",
        "/models",
        "/provider",
        "/model",
        "/backtest",
        "/status",
        "/tools",
        "/export",
        "/clear",
        "/compare",
        "/chart",
        "/report",
        "/alert",
        "/watchlist",
        "/portfolio",
        "/strategy",
        "/preset",
        "/news",
        "/quote",
        "/digest",
        "/setup-help",
        "/reload",
    ]

    # Common phrases
    PHRASES = [
        "analyze {ticker}",
        "compare {ticker1} vs {ticker2}",
        "backtest {strategy} on {ticker}",
        "show me a chart of {ticker}",
        "what's the sentiment on {ticker}",
        "build a portfolio with {tickers}",
        "run technical analysis on {ticker}",
        "how does {ticker} compare to {benchmark}",
        "what's the Sharpe ratio of {ticker}",
        "show factor exposures for {ticker}",
        "detect regime for {ticker}",
        "run stress test on {portfolio}",
        "generate research memo for {ticker}",
        "set alert when {ticker} drops below {price}",
    ]

    # Strategy names
    STRATEGIES = [
        "sma_crossover", "rsi_mean_reversion", "macd_momentum",
        "bollinger_bands", "dual_momentum", "breakout",
        "trend_following", "mean_reversion", "carry",
        "value", "quality", "momentum", "low_volatility",
    ]

    # Common tickers
    TICKERS = [
        "AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "META", "TSLA",
        "SPY", "QQQ", "IWM", "DIA", "VTI", "VOO",
        "XLK", "XLF", "XLE", "XLV", "XLI",
        "GLD", "SLV", "TLT", "BND",
        "BTC", "ETH",
        "AMD", "INTC", "AVGO", "SMCI", "PLTR", "COIN", "MSTR",
        "JPM", "BAC", "XOM", "WMT", "JNJ", "UNH", "MA", "V",
    ]

    @classmethod
    def get_suggestions(cls, text: str, max_results: int = 12) -> List[str]:
        """Get autocomplete suggestions for partial input."""
        raw = text.strip()
        low = raw.lower()
        suggestions: List[str] = []

        # Slash commands: dedicated path (no ticker/phrase noise)
        if low.startswith("/"):
            if low == "/":
                suggestions.extend(cls.COMMANDS)
            else:
                suggestions.extend(
                    [cmd for cmd in cls.COMMANDS if cmd.lower().startswith(low)]
                )
            return suggestions[:max_results]

        text_lc = low
        words = text_lc.split()

        # Ticker completion on last token
        if words:
            last_word = words[-1].upper()
            if len(last_word) >= 1 and last_word.isalnum():
                matching_tickers = [t for t in cls.TICKERS if t.startswith(last_word)]
                suggestions.extend(
                    [" ".join(words[:-1] + [t]) for t in matching_tickers[:8]]
                )

        # Strategy hints when discussing backtests
        if "backtest" in text_lc or "strategy" in text_lc:
            for strategy in cls.STRATEGIES[:6]:
                if strategy not in text_lc:
                    suggestions.append(text_lc + " " + strategy)

        # Phrase completion (short list)
        for phrase in cls.PHRASES:
            phrase_lower = phrase.lower()
            if text_lc and text_lc in phrase_lower and len(text_lc) >= 4:
                suggestions.append(phrase)

        return suggestions[:max_results]

    @classmethod
    def get_ticker_suggestions(cls, partial: str) -> List[str]:
        """Get ticker suggestions for partial input."""
        partial = partial.upper()
        return [t for t in cls.TICKERS if t.startswith(partial)][:10]

    @classmethod
    def get_command_help(cls, command: str) -> str:
        """Get help text for a command."""
        help_texts = {
            "/help": "Show all available commands",
            "/shortcuts": "Keyboard shortcuts and input tips",
            "/keys": "API key presence (masked)",
            "/models": "List reference models by provider",
            "/provider": "Show active AI provider",
            "/model": "Show default model id",
            "/backtest": "List built-in backtest strategies",
            "/status": "Provider, model, Ollama, keys",
            "/tools": "List registered data tools",
            "/export": "Save this chat to ~/.ephemeral/exports/",
            "/clear": "Clear the transcript (Ctrl+L)",
            "/compare": "Tip: use natural language or CLI ephemeral compare",
            "/chart": "Tip: ephemeral chart TICKER or ask in chat",
            "/report": "Ask the assistant for a structured report",
            "/alert": "Ask the assistant to set watch criteria",
            "/watchlist": "Ask the assistant about a watchlist",
            "/portfolio": "Portfolio prompts via chat",
            "/strategy": "Strategy ideas via chat or local_backtest tools",
            "/preset": "Use Engine prompt presets via chat",
            "/news": "Headlines: /news AAPL or /news NVDA 12",
            "/quote": "Quick quote: /quote TSLA",
            "/digest": "Same as /news (unified digest)",
            "/setup-help": "How to configure API keys and models",
            "/reload": "Reload LLM router after key changes",
        }
        return help_texts.get(command, "No help available for this command")


# ============================================================================
# SHOW WORK MODE
# ============================================================================

class ShowWorkLogger:
    """Log and display the agent's reasoning process."""

    def __init__(self):
        self.steps = []
        self.assumptions = []
        self.scoring_rubric = {}

    def log_step(self, step: str, details: Optional[Dict[str, Any]] = None):
        """Log a reasoning step."""
        self.steps.append({
            "timestamp": datetime.now().isoformat(),
            "step": step,
            "details": details or {},
        })

    def log_assumption(self, assumption: str):
        """Log an assumption being made."""
        self.assumptions.append(assumption)

    def set_scoring_rubric(self, rubric: Dict[str, float]):
        """Set the scoring rubric being used."""
        self.scoring_rubric = rubric

    def get_work_log(self) -> str:
        """Get formatted work log."""
        lines = []
        lines.append("## Reasoning Process\n")

        if self.assumptions:
            lines.append("### Assumptions")
            for a in self.assumptions:
                lines.append(f"- {a}")
            lines.append("")

        if self.scoring_rubric:
            lines.append("### Scoring Rubric")
            for criterion, weight in self.scoring_rubric.items():
                lines.append(f"- {criterion}: {weight:.1%}")
            lines.append("")

        if self.steps:
            lines.append("### Steps Taken")
            for i, step in enumerate(self.steps, 1):
                lines.append(f"{i}. {step['step']}")
                if step.get("details"):
                    for k, v in step["details"].items():
                        lines.append(f"   - {k}: {v}")
            lines.append("")

        return "\n".join(lines)

    def clear(self):
        """Clear the work log."""
        self.steps = []
        self.assumptions = []
        self.scoring_rubric = {}


# ============================================================================
# SAFETY GUARDRAILS
# ============================================================================

class SafetyGuardrails:
    """Enforce safety and correctness checks."""

    @staticmethod
    def check_lookahead_bias(code: str) -> List[str]:
        """Check for potential lookahead bias in code."""
        warnings = []

        # Common lookahead patterns
        patterns = [
            (r"shift\(-", "Negative shift may cause lookahead bias"),
            (r"\.future", "Future reference detected"),
            (r"iloc\[-\d+\]", "Negative indexing without proper offset"),
            (r"fillna\(method='bfill'\)", "Backward fill can cause lookahead"),
        ]

        import re
        for pattern, message in patterns:
            if re.search(pattern, code):
                warnings.append(message)

        return warnings

    @staticmethod
    def check_sample_size(n_samples: int, n_parameters: int) -> Dict[str, Any]:
        """Check if sample size is sufficient."""
        min_recommended = n_parameters * 50  # Rule of thumb

        return {
            "sample_size": n_samples,
            "parameters": n_parameters,
            "min_recommended": min_recommended,
            "sufficient": n_samples >= min_recommended,
            "warning": f"Sample size ({n_samples}) may be too small for {n_parameters} parameters. Recommend at least {min_recommended}." if n_samples < min_recommended else None,
        }

    @staticmethod
    def validate_indicator_timing(indicator_name: str, window: int, data_length: int) -> Dict[str, Any]:
        """Validate that indicator uses only past data."""
        warmup_needed = window
        valid_start = warmup_needed

        return {
            "indicator": indicator_name,
            "window": window,
            "data_length": data_length,
            "warmup_needed": warmup_needed,
            "valid_start_index": valid_start,
            "warning": f"First {warmup_needed} observations are warmup period" if warmup_needed > 0 else None,
        }

    @staticmethod
    def disclaimer() -> str:
        """Get standard disclaimer."""
        return """
**Disclaimer**: This analysis is for informational and educational purposes only.
It does not constitute financial advice, investment recommendations, or a solicitation
to buy or sell securities. Past performance does not guarantee future results.
Always consult with a qualified financial advisor before making investment decisions.
        """.strip()

    @staticmethod
    def separate_research_from_advice(content: str) -> Dict[str, str]:
        """Explicitly separate research findings from advice."""
        return {
            "research_findings": content,
            "advice_section": "For personalized advice, please consult a licensed financial advisor.",
            "disclaimer": SafetyGuardrails.disclaimer(),
        }
