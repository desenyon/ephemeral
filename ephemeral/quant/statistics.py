"""Classical time-series tests and covariance estimators."""

from __future__ import annotations

from typing import Optional, Tuple

import numpy as np
import pandas as pd
from scipy import stats


def ljung_box(
    series: pd.Series,
    lags: int,
) -> Tuple[float, float]:
    """Ljung-Box Q statistic and p-value for randomness of returns."""
    x = series.dropna().astype(float)
    if len(x) < lags + 5:
        return float("nan"), float("nan")
    r = x - x.mean()
    n = len(r)
    acf = []
    for k in range(1, lags + 1):
        num = (r * r.shift(k)).sum()
        den = (r**2).sum()
        acf.append(num / den if den else 0.0)
    q = n * (n + 2) * sum(acf[i] ** 2 / (i + 1) for i in range(lags))
    pval = 1 - stats.chi2.cdf(q, lags)
    return float(q), float(pval)


def variance_ratio(
    returns: pd.Series,
    *,
    k: int = 2,
) -> float:
    """Lo-MacKinlay style variance ratio at horizon k vs 1."""
    r = returns.dropna().astype(float)
    if len(r) < k * 10:
        return float("nan")
    rk = r.rolling(k).sum().dropna()
    var_k = rk.var()
    var_1 = r.var()
    return float(var_k / (k * var_1)) if var_1 and np.isfinite(var_1) else float("nan")


def newey_west_covariance(
    x_values: np.ndarray,
    *,
    lags: Optional[int] = None,
) -> np.ndarray:
    """Newey-West HAC covariance for rows of regressors/moments (T x K)."""
    x = np.asarray(x_values, dtype=float)
    t, k = x.shape
    if t < 2:
        return np.zeros((k, k))
    lag = lags if lags is not None else int(np.floor(4 * (t / 100) ** (2 / 9)))
    lag = max(0, min(lag, t - 1))
    x0 = x - x.mean(axis=0)
    gamma0 = (x0.T @ x0) / t
    cov = gamma0.copy()
    for lag_idx in range(1, lag + 1):
        w = 1.0 - lag_idx / (lag + 1)
        gl = (x0[lag_idx:].T @ x0[:-lag_idx]) / t
        cov += w * (gl + gl.T)
    return cov * (t / (t - 1))


def hurst_exponent(
    series: pd.Series,
    *,
    max_lag: int = 100,
) -> float:
    """Scaled range heuristic Hurst on log prices (not robust for small samples)."""
    s = series.dropna().astype(float)
    if len(s) < max_lag * 2:
        return float("nan")
    lags = range(10, max_lag)
    rs_vals = []
    for lag in lags:
        sub = s.iloc[-lag * 20 :]
        if len(sub) < lag * 2:
            continue
        ret = np.log(sub / sub.shift(1)).dropna()
        mean = ret.mean()
        dev = (ret - mean).cumsum()
        r = dev.max() - dev.min()
        std = ret.std()
        if std > 0:
            rs_vals.append((np.log(lag), np.log(r / std)))
    if len(rs_vals) < 5:
        return float("nan")
    xs = np.array([a[0] for a in rs_vals])
    ys = np.array([a[1] for a in rs_vals])
    slope, _intercept, _, _, _ = stats.linregress(xs, ys)
    return float(slope)


def half_life_ou(
    spread: pd.Series,
) -> float:
    """AR(1) half-life of mean reversion for a spread series."""
    x = spread.dropna().astype(float)
    if len(x) < 30:
        return float("nan")
    y = x.shift(1).dropna()
    z = x.loc[y.index]
    beta, _intercept, _, _, _ = stats.linregress(y, z)
    if beta <= 0 or beta >= 1:
        return float("nan")
    return float(np.log(2) / -np.log(beta))


def jarque_bera_test(series: pd.Series) -> Tuple[float, float]:
    """Jarque-Bera normality test statistic and p-value."""
    x = series.dropna().astype(float)
    if len(x) < 8:
        return float("nan"), float("nan")
    res = stats.jarque_bera(x)
    return float(res.statistic), float(res.pvalue)


def rolling_jb_stat(returns: pd.Series, window: int = 252) -> pd.Series:
    """Rolling Jarque-Bera statistic."""
    out = []
    idx = []
    for i in range(window, len(returns)):
        sub = returns.iloc[i - window : i]
        stat, _ = jarque_bera_test(sub)
        out.append(stat)
        idx.append(returns.index[i])
    return pd.Series(out, index=idx)


def spearman_ic(
    signal: pd.Series,
    forward_returns: pd.Series,
) -> float:
    """Spearman information coefficient."""
    a, b = signal.align(forward_returns, join="inner")
    a = a.dropna()
    b = b.loc[a.index].dropna()
    common = a.index.intersection(b.index)
    if len(common) < 10:
        return float("nan")
    return float(stats.spearmanr(a.loc[common], b.loc[common]).statistic)


def deflated_sharpe_ratio(
    sharpe: float,
    n: int,
    *,
    skew: float = 0.0,
    kurt: float = 3.0,
) -> float:
    """Bailey & Lopez de Prado deflated SR (simplified)."""
    if n < 2:
        return float("nan")
    sr_var = (1.0 - skew * sharpe + ((kurt - 1) / 4.0) * sharpe**2) / (n - 1)
    if sr_var <= 0:
        return float("nan")
    return float(stats.norm.cdf(sharpe / np.sqrt(sr_var)))
