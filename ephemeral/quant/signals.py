"""Technical and quantitative trading signals on price/return series."""

from __future__ import annotations

from typing import Literal, Tuple

import numpy as np
import pandas as pd

from ephemeral.quant.timeseries import zscore_series


def sma_cross(
    prices: pd.Series,
    fast: int = 10,
    slow: int = 50,
) -> pd.Series:
    """1 when fast SMA > slow SMA else -1 (with NaN until warm)."""
    f = prices.rolling(fast).mean()
    s = prices.rolling(slow).mean()
    sig = pd.Series(np.where(f > s, 1.0, -1.0), index=prices.index)
    sig[f.isna() | s.isna()] = np.nan
    return sig


def rsi(prices: pd.Series, period: int = 14) -> pd.Series:
    """Wilder RSI on closing prices."""
    delta = prices.diff()
    gain = delta.clip(lower=0)
    loss = (-delta).clip(lower=0)
    avg_gain = gain.ewm(alpha=1 / period, min_periods=period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1 / period, min_periods=period, adjust=False).mean()
    rs = avg_gain / avg_loss.replace(0, np.nan)
    return 100 - (100 / (1 + rs))


def bollinger_bands(
    prices: pd.Series,
    window: int = 20,
    num_std: float = 2.0,
) -> Tuple[pd.Series, pd.Series, pd.Series]:
    """Middle, upper, lower Bollinger bands."""
    mid = prices.rolling(window).mean()
    std = prices.rolling(window).std()
    upper = mid + num_std * std
    lower = mid - num_std * std
    return mid, upper, lower


def macd(
    prices: pd.Series,
    fast: int = 12,
    slow: int = 26,
    signal: int = 9,
) -> Tuple[pd.Series, pd.Series, pd.Series]:
    """MACD line, signal line, histogram."""
    ema_fast = prices.ewm(span=fast, adjust=False).mean()
    ema_slow = prices.ewm(span=slow, adjust=False).mean()
    line = ema_fast - ema_slow
    sig = line.ewm(span=signal, adjust=False).mean()
    hist = line - sig
    return line, sig, hist


def atr(
    high: pd.Series,
    low: pd.Series,
    close: pd.Series,
    period: int = 14,
) -> pd.Series:
    """Average true range."""
    prev_close = close.shift(1)
    tr = pd.concat(
        [
            (high - low).abs(),
            (high - prev_close).abs(),
            (low - prev_close).abs(),
        ],
        axis=1,
    ).max(axis=1)
    return tr.rolling(period).mean()


def obv(close: pd.Series, volume: pd.Series) -> pd.Series:
    """On-balance volume."""
    direction = np.sign(close.diff().fillna(0))
    return (direction * volume).cumsum()


def momentum_rank(
    returns: pd.DataFrame,
    lookback: int = 126,
) -> pd.DataFrame:
    """Cross-sectional momentum rank each day (higher = stronger past return)."""
    cum = (1 + returns).rolling(lookback).apply(lambda x: float(np.prod(1 + x) - 1), raw=True)
    return cum.rank(axis=1, pct=True)


def volatility_breakout(
    returns: pd.Series,
    vol_window: int = 20,
    threshold: float = 2.0,
) -> pd.Series:
    """Flag days where abs return exceeds threshold * rolling vol."""
    vol = returns.rolling(vol_window).std()
    return (returns.abs() > threshold * vol).astype(float)


def trend_strength_adx(
    high: pd.Series,
    low: pd.Series,
    close: pd.Series,
    period: int = 14,
) -> pd.Series:
    """Simplified ADX-like trend strength in [0, 100]."""
    up_move = high.diff()
    down_move = -low.diff()
    plus_dm = np.where((up_move > down_move) & (up_move > 0), up_move, 0.0)
    minus_dm = np.where((down_move > up_move) & (down_move > 0), down_move, 0.0)
    plus_dm = pd.Series(plus_dm, index=high.index)
    minus_dm = pd.Series(minus_dm, index=high.index)
    tr = atr(high, low, close, period=1)
    plus_di = 100 * (plus_dm.rolling(period).mean() / tr.replace(0, np.nan))
    minus_di = 100 * (minus_dm.rolling(period).mean() / tr.replace(0, np.nan))
    dx = (plus_di - minus_di).abs() / (plus_di + minus_di).replace(0, np.nan) * 100
    return dx.rolling(period).mean()


def kalman_trend(
    prices: pd.Series,
    *,
    process_var: float = 1e-5,
    meas_var: float = 1e-3,
) -> pd.Series:
    """1D Kalman filter level estimate (local linear trend simplified to RW)."""
    x = 0.0
    p = 1.0
    est = []
    for z in prices.astype(float).values:
        p = p + process_var
        k = p / (p + meas_var)
        x = x + k * (z - x)
        p = (1 - k) * p
        est.append(x)
    return pd.Series(est, index=prices.index)


def cusum_filter(
    returns: pd.Series,
    *,
    threshold: float = 0.02,
    drift: float = 0.0,
) -> pd.Series:
    """CUSUM event times for mean shift detection."""
    pos = 0.0
    neg = 0.0
    events = []
    for r in returns.fillna(0).values:
        pos = max(0.0, pos + r - drift)
        neg = min(0.0, neg + r - drift)
        hit = 1.0 if pos > threshold or -neg > threshold else 0.0
        if hit:
            pos = 0.0
            neg = 0.0
        events.append(hit)
    return pd.Series(events, index=returns.index)


def hysteresis_signal(
    raw: pd.Series,
    *,
    upper: float = 0.5,
    lower: float = -0.5,
) -> pd.Series:
    """Apply hysteresis to avoid churn; outputs -1, 0, 1 state machine."""
    state = 0
    out = []
    for v in raw.fillna(0).values:
        if state <= 0 and v > upper:
            state = 1
        elif state >= 0 and v < lower:
            state = -1
        out.append(float(state))
    return pd.Series(out, index=raw.index)


def regime_gate(
    vol_ratio: pd.Series,
    *,
    high: float = 1.5,
    low: float = 0.75,
) -> pd.Series:
    """Gate strategies: 0 in extreme vol, 1 in calm."""
    return ((vol_ratio > low) & (vol_ratio < high)).astype(float)


def pair_spread_zscore(
    a: pd.Series,
    b: pd.Series,
    window: int = 60,
) -> pd.Series:
    """Z-score of log price ratio for pairs."""
    la = np.log(a)
    lb = np.log(b)
    spread = la - lb
    return zscore_series(spread, window=window)


def signal_aggregate(
    signals: pd.DataFrame,
    *,
    how: Literal["mean", "vote", "prod"] = "mean",
) -> pd.Series:
    """Combine per-asset signals across columns."""
    if how == "mean":
        return signals.mean(axis=1)
    if how == "vote":
        return np.sign(signals).sum(axis=1) / signals.shape[1]
    prod = signals.prod(axis=1)
    return prod


def turnover_from_signal_changes(signal: pd.Series) -> float:
    """Average absolute day-over-day change in discrete signal."""
    return float(signal.diff().abs().mean())


def holding_periods(signal: pd.Series) -> pd.DataFrame:
    """Segment lengths where signal sign is constant."""
    s = np.sign(signal.fillna(0))
    grp = (s != s.shift()).cumsum()
    lengths = s.groupby(grp).apply(len)
    return pd.DataFrame({"group": lengths.index, "len": lengths.values})
