"""Dynamic strategy loader: run agent-authored strategy files through the same
simulate/metrics pipeline as the built-in strategies in :mod:`simple_engine`.

A custom strategy is a Python file exposing:

    def generate_signals(hist: pd.DataFrame, **params) -> pd.Series

returning a signal series aligned to ``hist.index`` with values in {1, 0, -1}
(1 = long, -1 = exit/short, 0 = flat) — the same contract the built-in
``_sma_crossover_signals``-style functions use. This is what lets an LLM (native,
Pi, or Codex) describe a strategy in English, write it out, and have Ephemeral
run and chart it in the same turn.
"""

from __future__ import annotations

import importlib.util
import re
from pathlib import Path
from typing import Any, Dict, Optional

import pandas as pd
import yfinance as yf

from .simple_engine import _calculate_metrics, _simulate_trades

STRATEGIES_DIR = Path.home() / ".ephemeral" / "custom_strategies"
_NAME_RE = re.compile(r"^[a-zA-Z_][a-zA-Z0-9_]{0,63}$")


class StrategyError(Exception):
    """Raised for invalid strategy names or malformed strategy code."""


def _validate_name(name: str) -> str:
    candidate = (name or "").strip()
    if not _NAME_RE.match(candidate):
        raise StrategyError(
            "Strategy name must be a valid identifier (letters, numbers, underscore, "
            "starting with a letter or underscore), max 64 chars."
        )
    return candidate


def write_strategy(name: str, code: str) -> Dict[str, Any]:
    """Persist an agent-authored strategy file under ~/.ephemeral/custom_strategies."""
    validated = _validate_name(name)
    if "def generate_signals" not in code:
        raise StrategyError("Strategy code must define `def generate_signals(hist, **params):`.")

    STRATEGIES_DIR.mkdir(parents=True, exist_ok=True)
    path = STRATEGIES_DIR / f"{validated}.py"
    path.write_text(code, encoding="utf-8")
    return {"name": validated, "path": str(path)}


def _load_strategy_module(name: str):
    validated = _validate_name(name)
    path = STRATEGIES_DIR / f"{validated}.py"
    if not path.exists():
        raise StrategyError(
            f"No custom strategy named '{validated}'. Write it first with write_strategy."
        )

    spec = importlib.util.spec_from_file_location(f"ephemeral_custom_strategy_{validated}", path)
    if spec is None or spec.loader is None:
        raise StrategyError(f"Could not load strategy '{validated}'.")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    fn = getattr(module, "generate_signals", None)
    if not callable(fn):
        raise StrategyError(f"Strategy '{validated}' does not define generate_signals().")
    return fn


def list_custom_strategies() -> Dict[str, Any]:
    STRATEGIES_DIR.mkdir(parents=True, exist_ok=True)
    return {"strategies": sorted(p.stem for p in STRATEGIES_DIR.glob("*.py"))}


def run_custom_backtest(
    symbol: str,
    strategy_name: str,
    period: str = "1y",
    initial_capital: float = 100000,
    params: Optional[dict] = None,
    transaction_cost_pct: float = 0.001,
) -> Dict[str, Any]:
    """Run a backtest against an agent-authored custom strategy file."""
    try:
        signal_fn = _load_strategy_module(strategy_name)

        ticker = yf.Ticker(symbol.upper())
        hist = ticker.history(period=period)
        if hist.empty or len(hist) < 50:
            return {"error": "Insufficient data for backtest", "symbol": symbol}

        signals = signal_fn(hist, **(params or {}))
        if not isinstance(signals, pd.Series):
            return {
                "error": "generate_signals must return a pandas Series aligned to hist.index",
                "symbol": symbol,
            }

        results = _simulate_trades(hist, signals, initial_capital, transaction_cost_pct)
        metrics = _calculate_metrics(results, hist, initial_capital)

        return {
            "symbol": symbol.upper(),
            "strategy": strategy_name,
            "period": period,
            "initial_capital": initial_capital,
            "parameters": params or {},
            "performance": metrics["performance"],
            "risk": metrics["risk"],
            "trades": metrics["trades"],
            "monthly_returns": metrics["monthly_returns"],
            "equity_curve": results["equity_curve"],
        }
    except StrategyError as exc:
        return {"error": str(exc), "symbol": symbol}
    except Exception as exc:  # noqa: BLE001 - surfaced to caller, not a crash
        return {"error": str(exc), "symbol": symbol}
