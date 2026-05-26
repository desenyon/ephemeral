"""Workspace read models for the Ink Research Desk."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List

from ephemeral.services.market_data import MarketDataService

DEFAULT_WATCHLIST = ["SPY", "QQQ", "DIA", "IWM"]


def build_status() -> Dict[str, Any]:
    return {}


def _clean_symbol(value: Any) -> str:
    raw = str(value or "").strip().upper()
    return raw if raw.isalnum() and 1 <= len(raw) <= 12 else ""


def _symbols(values: Iterable[Any]) -> List[str]:
    out: List[str] = []
    for value in values:
        symbol = _clean_symbol(value)
        if symbol and symbol not in out:
            out.append(symbol)
    return out


def _safe_quote(
    service: MarketDataService,
    symbol: str,
    warnings: List[str],
) -> Dict[str, Any]:
    try:
        quote = dict(service.get_quote(symbol))
        quote.setdefault("symbol", symbol)
        quote["state"] = "ok"
        return quote
    except Exception as exc:
        warnings.append(f"quote:{symbol}:{exc}")
        return {"symbol": symbol, "state": "error", "error": str(exc)}


def _safe_news(
    service: MarketDataService,
    symbol: str,
    warnings: List[str],
) -> List[Dict[str, Any]]:
    try:
        return service.get_news_yf(symbol, limit=8)
    except Exception as exc:
        warnings.append(f"news:{symbol}:{exc}")
        return []


def _artifact_rows(root: Path | None = None, *, limit: int = 6) -> List[Dict[str, str]]:
    base = root or Path.home() / ".ephemeral" / "artifacts"
    if not base.exists():
        return []
    rows: List[Dict[str, str]] = []
    for path in sorted(base.iterdir(), key=lambda item: item.stat().st_mtime, reverse=True)[
        :limit
    ]:
        rows.append({"name": path.name, "path": str(path)})
    return rows


def build_workspace_snapshot(
    payload: Dict[str, Any],
    *,
    build_status: Callable[[], Dict[str, Any]] | None = None,
    service: MarketDataService | None = None,
) -> Dict[str, Any]:
    warnings: List[str] = []
    status = build_status() if build_status else globals()["build_status"]()
    market_data = service or MarketDataService()
    requested = _clean_symbol(payload.get("symbol") or payload.get("active_symbol"))
    requested_watchlist = _symbols(payload.get("watchlist") or [])
    watchlist = requested_watchlist or DEFAULT_WATCHLIST
    active_symbol = requested or watchlist[0]

    return {
        "active_symbol": active_symbol,
        "status": status,
        "watchlist": [_safe_quote(market_data, symbol, warnings) for symbol in watchlist[:8]],
        "quote": _safe_quote(market_data, active_symbol, warnings),
        "news": _safe_news(market_data, active_symbol, warnings),
        "artifacts": _artifact_rows(),
        "setup_issues": status.get("setup_issues", []),
        "panel_warnings": warnings,
    }
