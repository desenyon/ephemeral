"""Unified market data access with optional TTL cache and Polygon enrichment."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

import numpy as np
import pandas as pd
import yfinance as yf

from ephemeral.services.cache import FileTTLCache, cache_key_for_symbol, default_cache_dir


def _dataframe_from_history_records(records: List[Dict[str, Any]]) -> pd.DataFrame:
    """Rebuild a yfinance-like OHLCV frame from cached JSON records."""
    if not records:
        return pd.DataFrame()
    df = pd.DataFrame(records)
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], utc=False)
        df = df.set_index("Date").sort_index()
    preferred = [c for c in ("Open", "High", "Low", "Close", "Volume") if c in df.columns]
    extra = [c for c in df.columns if c not in preferred]
    return df[preferred + extra]


@dataclass
class MarketDataBundle:
    """One symbol snapshot for research and tools."""

    symbol: str
    quote: Dict[str, Any] = field(default_factory=dict)
    history: Optional[pd.DataFrame] = None
    info: Dict[str, Any] = field(default_factory=dict)
    news_headlines: List[Dict[str, Any]] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)

    def to_tool_dict(self) -> Dict[str, Any]:
        out: Dict[str, Any] = {
            "symbol": self.symbol,
            "quote": self.quote,
            "info_summary": {
                k: self.info.get(k)
                for k in ("sector", "industry", "marketCap", "trailingPE", "longName")
                if k in self.info
            },
            "news": self.news_headlines[:15],
        }
        if self.history is not None and not self.history.empty:
            out["history"] = {
                "rows": len(self.history),
                "start": str(self.history.index[0]),
                "end": str(self.history.index[-1]),
                "last_close": float(self.history["Close"].iloc[-1]),
            }
        if self.errors:
            out["errors"] = self.errors
        return out


class MarketDataService:
    """Fetch and cache quotes, history, and headlines for equities."""

    def __init__(
        self,
        *,
        cache: Optional[FileTTLCache] = None,
        quote_ttl: float = 45.0,
        history_ttl: float = 900.0,
    ) -> None:
        self.cache = cache or FileTTLCache(default_cache_dir(), default_ttl=quote_ttl)
        self.quote_ttl = quote_ttl
        self.history_ttl = history_ttl

    def _quote_yf(self, symbol: str) -> Dict[str, Any]:
        sym = symbol.upper()
        t = yf.Ticker(sym)
        fi = dict(t.fast_info)
        last = fi.get("lastPrice") or fi.get("regularMarketPreviousClose") or 0
        prev = fi.get("previousClose") or fi.get("regularMarketPreviousClose") or 0
        chg = float(last) - float(prev) if prev else 0.0
        pct = (chg / float(prev) * 100.0) if prev else 0.0
        return {
            "symbol": sym,
            "price": last,
            "change": chg,
            "change_percent": pct,
            "volume": fi.get("lastVolume", 0),
            "market_cap": fi.get("marketCap", 0),
            "source": "yfinance",
        }

    def get_quote(self, symbol: str, *, use_cache: bool = True) -> Dict[str, Any]:
        key = f"quote:{cache_key_for_symbol(symbol, 'v1')}"

        def build() -> Dict[str, Any]:
            return self._quote_yf(symbol)

        if not use_cache:
            return build()
        return self.cache.get_or_set(key, build, ttl=self.quote_ttl, tag="quote")

    def get_history(
        self,
        symbol: str,
        *,
        period: str = "6mo",
        interval: str = "1d",
        use_cache: bool = True,
    ) -> pd.DataFrame:
        sym = symbol.upper()
        key = f"hist:{cache_key_for_symbol(sym, period, interval)}"

        def build() -> pd.DataFrame:
            t = yf.Ticker(sym)
            df = t.history(period=period, interval=interval)
            if df.empty:
                return df
            return df

        if not use_cache:
            return build()
        cached = self.cache.get(key)
        if cached is not None and isinstance(cached, dict) and "records" in cached:
            return _dataframe_from_history_records(cached["records"])
        df = build()
        if df.empty:
            return df
        reset = df.reset_index()
        if "Date" not in reset.columns and reset.columns.size > 0:
            reset.rename(columns={reset.columns[0]: "Date"}, inplace=True)
        payload = {"records": reset.to_dict("records")}
        self.cache.set(key, payload, ttl=self.history_ttl, tag="history")
        return df

    def get_info_light(self, symbol: str) -> Dict[str, Any]:
        sym = symbol.upper()
        key = f"info:{cache_key_for_symbol(sym)}"

        def build() -> Dict[str, Any]:
            t = yf.Ticker(sym)
            info = t.info or {}
            keep = (
                "longName",
                "shortName",
                "sector",
                "industry",
                "marketCap",
                "trailingPE",
                "forwardPE",
                "dividendYield",
                "beta",
                "fiftyTwoWeekHigh",
                "fiftyTwoWeekLow",
                "averageVolume",
                "website",
                "longBusinessSummary",
            )
            return {k: info.get(k) for k in keep if k in info}

        return self.cache.get_or_set(key, build, ttl=3600.0, tag="info")

    def get_news_yf(self, symbol: str, *, limit: int = 10) -> List[Dict[str, Any]]:
        sym = symbol.upper()
        try:
            t = yf.Ticker(sym)
            raw = t.news or []
        except Exception as e:
            return [{"error": str(e)}]
        out: List[Dict[str, Any]] = []
        for item in raw[:limit]:
            c = item.get("content") or {}
            out.append(
                {
                    "title": c.get("title", ""),
                    "summary": (c.get("summary") or "")[:500],
                    "published": c.get("pubDate") or c.get("displayTime") or "",
                }
            )
        return out

    def build_bundle(
        self,
        symbol: str,
        *,
        period: str = "6mo",
        include_news: bool = True,
    ) -> MarketDataBundle:
        b = MarketDataBundle(symbol=symbol.upper())
        try:
            b.quote = self.get_quote(symbol)
        except Exception as e:
            b.errors.append(f"quote:{e}")
        try:
            b.history = self.get_history(symbol, period=period)
        except Exception as e:
            b.errors.append(f"history:{e}")
        try:
            b.info = self.get_info_light(symbol)
        except Exception as e:
            b.errors.append(f"info:{e}")
        if include_news:
            try:
                b.news_headlines = self.get_news_yf(symbol)
            except Exception as e:
                b.errors.append(f"news:{e}")
        return b

    async def build_bundle_async(
        self,
        symbol: str,
        *,
        period: str = "6mo",
        include_news: bool = True,
    ) -> MarketDataBundle:
        return await asyncio.to_thread(self.build_bundle, symbol, period=period, include_news=include_news)


def returns_from_prices(prices: pd.Series) -> pd.Series:
    """Simple log returns."""
    return np.log(prices / prices.shift(1)).dropna()


def rolling_volatility(returns: pd.Series, window: int = 21, annualize: int = 252) -> pd.Series:
    return returns.rolling(window).std() * np.sqrt(float(annualize))


def correlation_pair(a: pd.Series, b: pd.Series) -> float:
    aligned = pd.concat([a, b], axis=1).dropna()
    if len(aligned) < 10:
        return float("nan")
    return float(aligned.iloc[:, 0].corr(aligned.iloc[:, 1]))


def load_returns_matrix(
    symbols: List[str],
    *,
    period: str = "1y",
) -> pd.DataFrame:
    """Close-to-close simple returns matrix for multiple tickers."""
    series_list: Dict[str, pd.Series] = {}
    for sym in symbols:
        t = yf.Ticker(sym.upper())
        hist = t.history(period=period)
        if hist.empty:
            continue
        series_list[sym.upper()] = hist["Close"].pct_change().dropna()
    if not series_list:
        return pd.DataFrame()
    return pd.DataFrame(series_list).dropna(how="all")
