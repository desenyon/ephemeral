"""Strategy-to-backtest closed loop: an LLM describes a strategy, writes it, and
runs it — Ephemeral supplies the data, simulation engine, and chart artifact."""

from ..backtest.custom_strategies import (
    StrategyError,
    list_custom_strategies,
    run_custom_backtest,
    write_strategy,
)
from .registry import TOOL_REGISTRY


@TOOL_REGISTRY.register(
    name="write_strategy",
    description=(
        "Write a custom trading strategy as Python code. The code must define "
        "`def generate_signals(hist, **params):` returning a pandas Series aligned to "
        "hist.index with values 1 (long), -1 (exit/short), or 0 (flat). `hist` is a "
        "yfinance OHLCV DataFrame with columns Open/High/Low/Close/Volume. Use this "
        "before run_custom_backtest."
    ),
)
def write_strategy_tool(name: str, code: str) -> dict:
    try:
        return write_strategy(name, code)
    except StrategyError as exc:
        return {"error": str(exc)}


@TOOL_REGISTRY.register(
    name="run_custom_backtest",
    description=(
        "Run a backtest for a strategy previously saved with write_strategy, and "
        "produce an equity-curve chart artifact. Returns performance, risk, and trade "
        "metrics plus a chart_path."
    ),
)
def run_custom_backtest_tool(
    symbol: str,
    strategy_name: str,
    period: str = "1y",
    initial_capital: float = 100000,
) -> dict:
    result = run_custom_backtest(
        symbol=symbol,
        strategy_name=strategy_name,
        period=period,
        initial_capital=initial_capital,
    )
    if "error" in result:
        return result

    equity_curve = result.pop("equity_curve", None)
    if equity_curve:
        from ..charts import create_performance_chart

        result["chart_path"] = create_performance_chart(
            equity_curve,
            title=f"{result.get('symbol', symbol)} · {strategy_name}",
        )
    return result


@TOOL_REGISTRY.register(
    name="list_custom_strategies",
    description="List custom strategies previously saved with write_strategy.",
)
def list_custom_strategies_tool() -> dict:
    return list_custom_strategies()
