"""Deterministic synthetic financial series for unit tests."""

from __future__ import annotations

from typing import List, Sequence, Tuple

import numpy as np
import pandas as pd


def _rng(seed: int) -> np.random.Generator:
    return np.random.default_rng(seed)


def random_walk_prices(
    n: int,
    *,
    seed: int = 42,
    drift: float = 0.0001,
    vol: float = 0.01,
    start: float = 100.0,
    freq: str = "B",
) -> pd.Series:
    """Geometric random walk price levels."""
    rng = _rng(seed)
    r = drift + vol * rng.standard_normal(n)
    idx = pd.date_range("2020-01-01", periods=n, freq=freq)
    p = start * np.exp(np.cumsum(r))
    return pd.Series(p, index=idx)


def synthetic_ohlcv(
    n: int,
    *,
    seed: int = 1,
    start: float = 50.0,
) -> pd.DataFrame:
    """OHLCV from a random walk close with synthetic open/high/low."""
    close = random_walk_prices(n, seed=seed, start=start)
    rng = _rng(seed + 7)
    noise = 0.002 * rng.standard_normal(n)
    open_ = close.shift(1).fillna(close.iloc[0])
    high = pd.concat([open_, close], axis=1).max(axis=1) * (1 + np.abs(noise))
    low = pd.concat([open_, close], axis=1).min(axis=1) * (1 - np.abs(noise))
    vol = rng.integers(1_000_000, 10_000_000, size=n)
    return pd.DataFrame({"Open": open_, "High": high, "Low": low, "Close": close, "Volume": vol})


def random_returns_panel(
    n_days: int,
    n_assets: int,
    *,
    seed: int = 0,
    freq: str = "B",
) -> pd.DataFrame:
    """IID normal returns with mild cross-sectional correlation."""
    rng = _rng(seed)
    idx = pd.date_range("2018-06-01", periods=n_days, freq=freq)
    common = rng.standard_normal(n_days)[:, None]
    idio = rng.standard_normal((n_days, n_assets))
    r = 0.1 * common + 0.9 * idio
    cols = [f"S{i:03d}" for i in range(n_assets)]
    return pd.DataFrame(r * 0.01, index=idx, columns=cols)


def synthetic_portfolio_weights(
    symbols: Sequence[str],
    *,
    seed: int = 3,
    long_only: bool = True,
) -> pd.Series:
    """Dirichlet-like random weights."""
    rng = _rng(seed)
    raw = rng.random(len(symbols))
    if long_only:
        raw = np.abs(raw)
    s = raw.sum()
    w = raw / s if s else raw
    return pd.Series(w, index=list(symbols))


def factor_structure_returns(
    n: int,
    assets: List[str],
    loadings: Sequence[float],
    *,
    seed: int = 99,
) -> Tuple[pd.DataFrame, pd.Series]:
    """Returns = loadings * F + idio with single factor F."""
    rng = _rng(seed)
    idx = pd.date_range("2019-01-01", periods=n, freq="B")
    f = rng.standard_normal(n) * 0.01
    factor_series = pd.Series(f, index=idx)
    idio = rng.standard_normal((n, len(assets))) * 0.005
    loadings_matrix = np.array(loadings)
    returns_matrix = loadings_matrix * f[:, None] + idio
    return pd.DataFrame(returns_matrix, index=idx, columns=assets), factor_series


def build_cov_from_factor(
    loadings: np.ndarray,
    factor_var: float,
    idio_var: np.ndarray,
) -> np.ndarray:
    """Covariance = l l' f + diag(idio)."""
    loading_vector = loadings.reshape(-1, 1)
    return float(factor_var) * (loading_vector @ loading_vector.T) + np.diag(idio_var)


def sparse_signal_matrix(
    days: int,
    assets: int,
    *,
    sparsity: float = 0.3,
    seed: int = 11,
) -> pd.DataFrame:
    """Mostly NaN signal matrix."""
    rng = _rng(seed)
    idx = pd.date_range("2021-01-01", periods=days, freq="B")
    m = rng.standard_normal((days, assets))
    mask = rng.random((days, assets)) > sparsity
    m[mask] = np.nan
    cols = [f"A{i}" for i in range(assets)]
    return pd.DataFrame(m, index=idx, columns=cols)


def monotone_curve(n: int, *, start: float = 1.0, end: float = 2.0) -> pd.Series:
    """Strictly increasing test series."""
    x = np.linspace(start, end, n)
    idx = pd.date_range("2022-01-01", periods=n, freq="D")
    return pd.Series(x, index=idx)


def piecewise_constant(n: int, segments: int) -> pd.Series:
    """Step function."""
    rng = _rng(7)
    vals = rng.standard_normal(segments)
    seg_len = n // segments
    out = []
    for v in vals:
        out.extend([v] * seg_len)
    while len(out) < n:
        out.append(vals[-1])
    return pd.Series(out[:n], index=pd.RangeIndex(n))


def correlation_block_matrix(
    block_size: int,
    blocks: int,
    rho_in: float,
    rho_out: float,
) -> np.ndarray:
    """Constant correlation blocks."""
    n = block_size * blocks
    c = np.full((n, n), rho_out)
    for b in range(blocks):
        sl = slice(b * block_size, (b + 1) * block_size)
        sub = np.full((block_size, block_size), rho_in)
        np.fill_diagonal(sub, 1.0)
        c[sl, sl] = sub
    np.fill_diagonal(c, 1.0)
    return c


def psd_from_corr(corr: np.ndarray, vols: np.ndarray) -> np.ndarray:
    """Covariance from correlation and vols."""
    d = np.diag(vols)
    return d @ corr @ d


def ladder_prices(levels: Sequence[float]) -> pd.Series:
    """Staircase price path."""
    idx = pd.date_range("2023-01-01", periods=len(levels), freq="B")
    return pd.Series(levels, index=idx)


def with_outliers(s: pd.Series, positions: Sequence[int], scale: float = 5.0) -> pd.Series:
    """Inject spike outliers at integer positions."""
    out = s.copy()
    for p in positions:
        if 0 <= p < len(out):
            out.iloc[p] *= scale
    return out


def rolling_stationary_ar1(n: int, phi: float, ephemeral: float, seed: int) -> pd.Series:
    """AR(1) stationary series."""
    rng = _rng(seed)
    x = np.zeros(n)
    x[0] = rng.standard_normal()
    eps = rng.standard_normal(n) * ephemeral
    for t in range(1, n):
        x[t] = phi * x[t - 1] + eps[t]
    return pd.Series(x, index=pd.date_range("2017-01-01", periods=n, freq="B"))
