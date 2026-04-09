"""Portfolio weights, variance, and marginal risk contributions."""

from __future__ import annotations

from typing import Dict, Mapping, MutableMapping, Optional, Sequence, Union

import numpy as np
import pandas as pd


def to_weights(
    values: Union[Sequence[float], np.ndarray, pd.Series],
    *,
    long_only: bool = True,
) -> np.ndarray:
    """Normalize a vector to sum to 1; negative weights allowed unless long_only."""
    v = np.asarray(values, dtype=float).ravel()
    if long_only:
        v = np.clip(v, 0, None)
    s = float(np.nansum(v))
    if s == 0:
        n = len(v)
        return np.ones(n, dtype=float) / max(n, 1)
    return v / s


def herfindahl(weights: Union[Sequence[float], np.ndarray]) -> float:
    """Concentration index in [1/n, 1]."""
    w = np.asarray(weights, dtype=float).ravel()
    w = w / np.sum(np.abs(w)) if np.sum(np.abs(w)) else w
    return float(np.sum(w**2))


def effective_n_assets(weights: Union[Sequence[float], np.ndarray]) -> float:
    """Inverse Herfindahl: effective number of independent bets."""
    h = herfindahl(weights)
    return 1.0 / h if h > 0 else float(len(weights))


def portfolio_variance(
    weights: np.ndarray,
    cov: np.ndarray,
) -> float:
    """Portfolio variance ``w' C w`` for column vector weights."""
    w = np.asarray(weights, dtype=float).reshape(-1, 1)
    ephemeral = np.asarray(cov, dtype=float)
    return float(np.squeeze(w.T @ ephemeral @ w))


def risk_contributions(
    weights: Union[Sequence[float], np.ndarray],
    cov: np.ndarray,
) -> np.ndarray:
    """Marginal risk contributions: ``w_i * (C w)_i / sqrt(w' C w)``."""
    w = np.asarray(weights, dtype=float).ravel()
    ephemeral = np.asarray(cov, dtype=float)
    pw = ephemeral @ w
    vol = np.sqrt(float(w @ pw))
    if vol <= 0 or not np.isfinite(vol):
        return np.zeros_like(w)
    mrc = w * pw / vol
    return mrc


def risk_budget_weights(
    target_rc: Union[Sequence[float], np.ndarray],
    cov: np.ndarray,
    *,
    max_iter: int = 5000,
    tol: float = 1e-10,
) -> np.ndarray:
    """Iterative risk parity style: match relative risk contributions (spinu-like simplified)."""
    n = len(target_rc)
    t = np.asarray(target_rc, dtype=float).ravel()
    t = t / np.sum(t) if np.sum(t) > 0 else np.ones(n) / n
    w = np.ones(n, dtype=float) / n
    ephemeral = np.asarray(cov, dtype=float)
    for _ in range(max_iter):
        vol = np.sqrt(float(w @ ephemeral @ w))
        if vol <= 0:
            break
        rc = w * (ephemeral @ w) / vol
        rc_sum = np.sum(rc)
        if rc_sum <= 0:
            break
        rc_n = rc / rc_sum
        w_new = w * (t / np.maximum(rc_n, 1e-16))
        w_new = w_new / np.sum(w_new)
        if float(np.max(np.abs(w_new - w))) < tol:
            w = w_new
            break
        w = w_new
    return w / np.sum(w)


def implied_returns(
    cov: np.ndarray,
    weights: np.ndarray,
    *,
    risk_aversion: float = 3.0,
) -> np.ndarray:
    """Reverse optimization: ``pi = delta * C w`` for the Black-Litterman prior."""
    ephemeral = np.asarray(cov, dtype=float)
    w = np.asarray(weights, dtype=float).ravel()
    return risk_aversion * (ephemeral @ w)


def turnover(
    weights_before: Sequence[float],
    weights_after: Sequence[float],
) -> float:
    """One-way turnover: half the L1 distance."""
    a = np.asarray(weights_before, dtype=float).ravel()
    b = np.asarray(weights_after, dtype=float).ravel()
    n = max(len(a), len(b))
    if len(a) < n:
        a = np.pad(a, (0, n - len(a)))
    if len(b) < n:
        b = np.pad(b, (0, n - len(b)))
    return 0.5 * float(np.sum(np.abs(a - b)))


def rebalance_to_targets(
    current_weights: Sequence[float],
    target_weights: Sequence[float],
    *,
    max_trade: Optional[float] = None,
) -> np.ndarray:
    """Proportional step toward targets; optional cap on total trade size."""
    c = to_weights(current_weights, long_only=False)
    t = to_weights(target_weights, long_only=False)
    delta = t - c
    if max_trade is not None:
        tot = float(np.sum(np.abs(delta)))
        if tot > max_trade > 0:
            delta = delta * (max_trade / tot)
    return to_weights(c + delta, long_only=False)


def factor_portfolio_variance(
    weights: np.ndarray,
    loadings: np.ndarray,
    idio_var: np.ndarray,
) -> float:
    """w' (L F L' + D) w with diagonal idiosyncratic D."""
    w = np.asarray(weights, dtype=float).ravel()
    loadings_matrix = np.asarray(loadings, dtype=float)
    d = np.asarray(idio_var, dtype=float).ravel()
    systematic = loadings_matrix @ loadings_matrix.T
    cov = systematic + np.diag(d)
    return portfolio_variance(w, cov)


def group_neutral_weights(
    weights: Mapping[str, float],
    groups: Mapping[str, str],
) -> Dict[str, float]:
    """Demean weights within each group (names must match)."""
    df = pd.DataFrame({"w": pd.Series(weights), "g": pd.Series(groups)})
    df = df.dropna()
    out: Dict[str, float] = {}
    for _g, sub in df.groupby("g"):
        mu = sub["w"].mean()
        for sym, row in sub.iterrows():
            out[str(sym)] = float(row["w"] - mu)
    s = sum(abs(v) for v in out.values())
    if s > 0:
        for k in list(out.keys()):
            out[k] /= s
    return out


def exposure_vector(
    weights: Mapping[str, float],
    exposures: Mapping[str, Mapping[str, float]],
) -> Dict[str, float]:
    """Portfolio-level factor exposures: sum_s w_s * exp_s[f]."""
    agg: MutableMapping[str, float] = {}
    for sym, w in weights.items():
        exp = exposures.get(sym) or {}
        for f, val in exp.items():
            agg[f] = agg.get(f, 0.0) + float(w) * float(val)
    return dict(agg)
