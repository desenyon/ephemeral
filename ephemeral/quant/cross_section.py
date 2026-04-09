"""Cross-sectional ranking, neutralization, and industry bucketing."""

from __future__ import annotations

from typing import Dict, Mapping, Optional, Sequence

import numpy as np
import pandas as pd


def winsorize_cs(
    df: pd.DataFrame,
    *,
    lower: float = 0.01,
    upper: float = 0.99,
) -> pd.DataFrame:
    """Winsorize each column independently."""
    out = df.copy().astype(float)
    for c in out.columns:
        lo = out[c].quantile(lower)
        hi = out[c].quantile(upper)
        out[c] = out[c].clip(lo, hi)
    return out


def rank_cs(df: pd.DataFrame, *, pct: bool = True) -> pd.DataFrame:
    """Cross-sectional rank per row."""
    return df.rank(axis=1, pct=pct)


def zscore_cs(df: pd.DataFrame) -> pd.DataFrame:
    """Cross-sectional z-score per row."""
    m = df.mean(axis=1)
    s = df.std(axis=1).replace(0, np.nan)
    return df.sub(m, axis=0).div(s, axis=0)


def demean_industry(
    scores: pd.Series,
    industry: pd.Series,
) -> pd.Series:
    """Subtract industry mean from each score."""
    d = pd.DataFrame({"s": scores, "i": industry})
    mu = d.groupby("i")["s"].transform("mean")
    return d["s"] - mu


def neutralize_linear(
    y: pd.Series,
    x: pd.DataFrame,
) -> pd.Series:
    """Residuals of OLS y ~ X (one intercept per call via column of ones)."""
    df = pd.concat([y.rename("y"), x], axis=1).dropna()
    if len(df) < x.shape[1] + 2:
        return y * np.nan
    design_matrix = np.column_stack([np.ones(len(df)), df[x.columns].values])
    yy = df["y"].values
    beta, _, _, _ = np.linalg.lstsq(design_matrix, yy, rcond=None)
    pred = design_matrix @ beta
    resid = yy - pred
    out = pd.Series(index=y.index, dtype=float)
    out.loc[df.index] = resid
    return out


def bucket_quintiles(s: pd.Series) -> pd.Series:
    """Assign 1..5 quintile labels."""
    return pd.qcut(s.rank(method="first"), 5, labels=False) + 1


def peer_demean_map(
    values: Mapping[str, float],
    peer_groups: Mapping[str, Sequence[str]],
) -> Dict[str, float]:
    """For each symbol, subtract mean of its peer group (including self)."""
    out: Dict[str, float] = {}
    for sym, v in values.items():
        peers = list(peer_groups.get(sym, ()))
        group = [sym] + [p for p in peers if p in values]
        mu = float(np.mean([values[g] for g in group])) if group else 0.0
        out[sym] = float(v) - mu
    return out


def assign_percentile_bucket(x: float, edges: Sequence[float]) -> int:
    """Return bucket index for monotonic edges."""
    for i in range(len(edges) - 1):
        if edges[i] <= x < edges[i + 1]:
            return i
    return len(edges) - 2


def cs_median_fill(df: pd.DataFrame) -> pd.DataFrame:
    """Fill NaN with cross-sectional median per row."""
    return df.T.fillna(df.median(axis=1)).T


def relative_strength_vs_benchmark(
    asset_ret: pd.Series,
    bench_ret: pd.Series,
    window: int = 63,
) -> pd.Series:
    """Rolling sum of asset minus benchmark."""
    a, b = asset_ret.align(bench_ret, join="inner")
    diff = a - b
    return diff.rolling(window).sum()


def breadth(
    signals: pd.DataFrame,
    *,
    threshold: float = 0.0,
) -> pd.Series:
    """Fraction of columns above threshold each row."""
    return (signals > threshold).sum(axis=1) / signals.shape[1]


def dispersion(
    df: pd.DataFrame,
) -> pd.Series:
    """Cross-sectional std per row."""
    return df.std(axis=1)


def correlation_to_market(
    returns: pd.DataFrame,
    market: pd.Series,
) -> pd.Series:
    """Correlation of each column to market over full sample."""
    out = {}
    for c in returns.columns:
        pair = pd.concat([returns[c], market], axis=1).dropna()
        if len(pair) > 10:
            out[c] = pair.corr().iloc[0, 1]
        else:
            out[c] = np.nan
    return pd.Series(out)


def assign_size_bucket(
    mcap: pd.Series,
    *,
    breakpoints: Optional[Sequence[float]] = None,
) -> pd.Series:
    """Size buckets by market cap quantiles."""
    if breakpoints is None:
        breakpoints = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
    q = mcap.rank(pct=True)
    labels = list(range(len(breakpoints) - 1))
    return pd.cut(q, bins=breakpoints, labels=labels, include_lowest=True)


def long_short_weights(
    signal: pd.Series,
    *,
    long_frac: float = 0.2,
    short_frac: float = 0.2,
) -> pd.Series:
    """Dollar-neutral weights from cross-sectional signal at one point in time."""
    s = signal.dropna().sort_values()
    n = len(s)
    if n < 5:
        return signal * np.nan
    k_long = max(1, int(long_frac * n))
    k_short = max(1, int(short_frac * n))
    long_syms = s.tail(k_long).index
    short_syms = s.head(k_short).index
    w = pd.Series(0.0, index=signal.index)
    w.loc[long_syms] = 0.5 / k_long
    w.loc[short_syms] = -0.5 / k_short
    return w


def information_coefficient_series(
    signal: pd.DataFrame,
    forward_ret: pd.DataFrame,
) -> pd.Series:
    """Daily Spearman IC mean across assets."""
    ic = []
    idx = signal.index.intersection(forward_ret.index)
    for t in idx:
        a = signal.loc[t].dropna()
        b = forward_ret.loc[t].reindex(a.index).dropna()
        common = a.index.intersection(b.index)
        if len(common) < 5:
            ic.append(np.nan)
            continue
        ic.append(a.loc[common].corr(b.loc[common], method="spearman"))
    return pd.Series(ic, index=idx)


def realized_beta_vs_factor(
    asset: pd.Series,
    factor: pd.Series,
    window: int = 252,
) -> pd.Series:
    """Rolling CAPM beta."""
    df = pd.concat([asset, factor], axis=1).dropna()
    betas = []
    for i in range(window, len(df)):
        sub = df.iloc[i - window : i]
        c = sub.cov().iloc[0, 1]
        v = sub.iloc[:, 1].var()
        betas.append(c / v if v else np.nan)
    return pd.Series(betas, index=df.index[window:])
