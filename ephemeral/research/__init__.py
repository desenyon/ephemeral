"""Structured research workflows: memos, sessions, and citation helpers."""

from ephemeral.research.memo import MemoSection, ResearchMemo, ResearchMemoBuilder
from ephemeral.research.session import ResearchPhase, ResearchSession
from ephemeral.research.sources import SourceRef, format_citations_markdown
from ephemeral.research.templates import MEMO_TEMPLATE_INVESTMENT_THESIS, render_memo_skeleton

__all__ = [
    "ResearchMemo",
    "ResearchMemoBuilder",
    "MemoSection",
    "ResearchPhase",
    "ResearchSession",
    "SourceRef",
    "format_citations_markdown",
    "MEMO_TEMPLATE_INVESTMENT_THESIS",
    "render_memo_skeleton",
]
