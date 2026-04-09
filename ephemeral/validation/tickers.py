"""Symbol normalization and lightweight validation helpers."""

from __future__ import annotations

import re
from typing import Iterable, List, Set

_SYMBOL_RE = re.compile(r"^[A-Z0-9.\-^]+$")


def normalize_symbol(raw: str) -> str:
    """Uppercase strip; reject empty."""
    s = (raw or "").strip().upper()
    if not s:
        raise ValueError("symbol must be non-empty")
    return s


def parse_symbol_list(
    text: str,
    *,
    delimiter: str = ",",
    max_symbols: int = 200,
) -> List[str]:
    """Split comma/whitespace separated tickers into normalized unique list."""
    parts = re.split(r"[\s,;]+", text.strip())
    out: List[str] = []
    seen: Set[str] = set()
    for p in parts:
        if not p:
            continue
        sym = normalize_symbol(p)
        if sym in seen:
            continue
        seen.add(sym)
        out.append(sym)
        if len(out) >= max_symbols:
            break
    return out


def validate_symbol_shape(sym: str) -> str:
    """Ensure symbol looks like a US equity/ETF ticker (loose)."""
    s = normalize_symbol(sym)
    if not _SYMBOL_RE.match(s):
        raise ValueError(f"invalid symbol characters: {sym!r}")
    if len(s) > 64:
        raise ValueError("symbol too long")
    return s


def validate_iso_currency(code: str) -> str:
    """Three-letter ISO currency."""
    c = (code or "").strip().upper()
    if len(c) != 3 or not c.isalpha():
        raise ValueError("currency must be ISO 4217 alpha-3")
    return c


def expand_index_symbols(symbols: Iterable[str]) -> List[str]:
    """Pass-through list with normalization; no network calls."""
    return [normalize_symbol(s) for s in symbols if s and str(s).strip()]
