"""Time-series alignment, cleaning, and return transforms."""

from __future__ import annotations

from typing import Literal, Optional, Tuple

import numpy as np
import pandas as pd


def clean_price_series(
    s: pd.Series,
    *,
    fill_method: Literal["ffill", "none"] = "ffill",
    drop_inf: bool = True,
) -> pd.Series:
    """Drop NaN/inf and optionally forward-fill small gaps in price levels."""
    out = s.astype(float)
    if drop_inf:
        out = out.replace([np.inf, -np.inf], np.nan)
    out = out.dropna()
    if fill_method == "ffill":
        out = out.reindex(s.index).ffill().dropna()
    return out


def log_returns(prices: pd.Series) -> pd.Series:
    """Natural log returns; first observation is NaN and dropped for callers."""
    p = clean_price_series(prices, fill_method="none")
    return np.log(p / p.shift(1)).dropna()


def simple_returns(prices: pd.Series) -> pd.Series:
    """Simple percentage returns from price levels."""
    p = clean_price_series(prices, fill_method="none")
    return p.pct_change().dropna()


def winsorize(
    s: pd.Series,
    *,
    lower_q: float = 0.01,
    upper_q: float = 0.99,
) -> pd.Series:
    """Clip series to given quantile bounds (inclusive)."""
    if s.empty:
        return s
    lo = float(s.quantile(lower_q))
    hi = float(s.quantile(upper_q))
    return s.clip(lower=lo, upper=hi)


def align_on_index(
    *series: pd.Series,
    how: Literal["inner", "outer"] = "inner",
) -> Tuple[pd.Series, ...]:
    """Align multiple series on a common datetime index."""
    if not series:
        return tuple()
    if len(series) == 1:
        return (series[0].dropna(),)
    df = pd.concat(series, axis=1, join=how)
    df = df.dropna(how="any") if how == "inner" else df
    cols = list(range(len(series)))
    out = [df.iloc[:, i] for i in cols]
    return tuple(out)


def rolling_correlation_matrix(
    returns: pd.DataFrame,
    window: int,
    *,
    min_periods: Optional[int] = None,
) -> pd.DataFrame:
    """Stack rolling correlation matrices into a long-panel MultiIndex frame."""
    if returns.empty or window < 2:
        return pd.DataFrame()
    mp = min_periods or max(2, window // 2)
    rows = []
    for end_idx in range(len(returns)):
        if end_idx + 1 < mp:
            continue
        start = max(0, end_idx - window + 1)
        sub = returns.iloc[start : end_idx + 1]
        if len(sub) < mp:
            continue
        c = sub.corr()
        ts = returns.index[end_idx]
        for i, a in enumerate(c.index):
            for j, b in enumerate(c.columns):
                if i <= j:
                    rows.append((ts, str(a), str(b), float(c.iloc[i, j])))
    if not rows:
        return pd.DataFrame()
    df = pd.DataFrame(rows, columns=["date", "a", "b", "corr"])
    return df.set_index(["date", "a", "b"])


def resample_returns(
    returns: pd.Series,
    rule: str,
    *,
    how: Literal["sum", "mean"] = "sum",
) -> pd.Series:
    """Resample intraday or daily returns to a lower frequency."""
    r = returns.copy()
    if how == "sum":
        return r.resample(rule).sum().dropna()
    return r.resample(rule).mean().dropna()


def zscore_series(s: pd.Series, window: int = 60) -> pd.Series:
    """Rolling z-score of a series."""
    m = s.rolling(window).mean()
    sd = s.rolling(window).std()
    return (s - m) / sd.replace(0, np.nan)


def cumulative_returns(
    returns: pd.Series,
    *,
    compound: bool = True,
) -> pd.Series:
    """Cumulative return path from simple returns."""
    r = returns.dropna()
    if compound:
        return (1 + r).cumprod() - 1
    return r.cumsum()


def drawdown_series(cumulative_wealth: pd.Series) -> pd.Series:
    """Drawdown from a wealth index starting at 1.0."""
    w = cumulative_wealth.astype(float)
    peak = w.cummax()
    return (w - peak) / peak.replace(0, np.nan)


def max_drawdown_from_returns(returns: pd.Series, *, periods_per_year: int = 252) -> float:
    """Maximum drawdown on compounded wealth (not annualized)."""
    r = returns.dropna()
    if r.empty:
        return 0.0
    w = (1 + r).cumprod()
    dd = drawdown_series(w)
    return float(dd.min()) if len(dd) else 0.0


def rolling_volatility_annualized(
    returns: pd.Series,
    window: int,
    *,
    periods_per_year: int = 252,
) -> pd.Series:
    """Rolling sample volatility scaled to annual units."""
    return returns.rolling(window).std() * np.sqrt(float(periods_per_year))


def pairwise_beta(
    asset_returns: pd.Series,
    market_returns: pd.Series,
    *,
    window: int = 252,
    min_periods: int = 50,
) -> pd.Series:
    """Rolling CAPM beta using covariance / market variance."""
    a, m = align_on_index(asset_returns, market_returns)
    cov = a.rolling(window, min_periods=min_periods).cov(m)
    var_m = m.rolling(window, min_periods=min_periods).var()
    return cov / var_m.replace(0, np.nan)
