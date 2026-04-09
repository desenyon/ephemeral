"""Highlight stock tickers in plain text and Markdown for the TUI."""

from __future__ import annotations

import re
from functools import lru_cache
from typing import FrozenSet, List, Tuple

from rich.text import Text


def _extended_tickers() -> FrozenSet[str]:
    from ephemeral.core.engine import AutocompleteEngine

    extra = {
        "AMD", "INTC", "AVGO", "CRM", "ORCL", "ADBE", "CSCO", "IBM",
        "JPM", "BAC", "GS", "MS", "C", "WFC", "SCHW",
        "XOM", "CVX", "COP", "WMT", "COST", "HD", "NKE", "DIS", "NFLX",
        "COIN", "MSTR", "PLTR", "SOFI", "RIVN", "LCID", "F", "GM",
        "SMCI", "ARM", "QCOM", "MU", "LRCX", "ASML", "TSM",
        "GME", "AMC", "BBBY", "HOOD", "SQ", "PYPL", "SHOP", "UBER", "LYFT",
        "XOM", "MRNA", "PFE", "JNJ", "UNH", "LLY", "ABBV",
        "SOL", "ETH", "BTC", "DOGE",
    }
    return frozenset(AutocompleteEngine.TICKERS) | extra


@lru_cache(maxsize=1)
def _ticker_list_longest_first() -> Tuple[str, ...]:
    return tuple(sorted(_extended_tickers(), key=len, reverse=True))


def enhance_markdown_tickers(markdown: str) -> str:
    """Wrap known tickers in backticks outside fenced code blocks."""
    if not markdown:
        return markdown
    segments = re.split(r"(```[\s\S]*?```)", markdown)
    out: List[str] = []
    for seg in segments:
        if seg.startswith("```"):
            out.append(seg)
        else:
            out.append(_wrap_tickers_plain_segment(seg))
    return "".join(out)


def _wrap_tickers_plain_segment(segment: str) -> str:
    if not segment:
        return segment
    out = segment
    for t in _ticker_list_longest_first():
        pat = re.compile(r"(?<!`)(?<![A-Za-z])" + re.escape(t) + r"(?![A-Za-z])")
        out = pat.sub(f"`{t}`", out)
    return out


def last_ticker_token(text: str) -> str | None:
    """Return the most recent plausible ticker token in the input line."""
    if not text:
        return None
    tickers = _extended_tickers()
    words = re.findall(r"\$?([A-Z]{1,5})\b", text.upper())
    for w in reversed(words):
        w = w.lstrip("$")
        if w in tickers or (len(w) >= 2 and w.isalpha()):
            return w
    return None


def rich_text_user_line(line: str) -> Text:
    """Render a user chat line with tickers emphasized."""
    t = Text()
    if not line:
        return t
    tickers = _ticker_list_longest_first()
    alt = "|".join(re.escape(x) for x in tickers)
    pattern = re.compile(rf"(\$[A-Z]{{1,5}}\b|\b(?:{alt})\b)")
    pos = 0
    for m in pattern.finditer(line):
        if m.start() > pos:
            t.append(line[pos : m.start()], style="bold #cdd6f4")
        tok = m.group(0)
        if tok.startswith("$"):
            t.append(tok, style="bold #f9e2af")
        else:
            t.append(tok, style="bold #2ac3de")
        pos = m.end()
    if pos < len(line):
        t.append(line[pos:], style="bold #cdd6f4")
    return t
