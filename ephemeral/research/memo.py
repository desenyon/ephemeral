"""Composable investment memo structure (Markdown-oriented)."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from ephemeral.research.sources import SourceRef, format_citations_markdown, merge_sources


@dataclass
class MemoSection:
    """One section of a research memo."""

    title: str
    body_md: str = ""
    bullets: List[str] = field(default_factory=list)

    def render(self) -> str:
        lines = [f"## {self.title}", ""]
        if self.body_md.strip():
            lines.append(self.body_md.strip())
            lines.append("")
        for b in self.bullets:
            lines.append(f"- {b}")
        if self.bullets:
            lines.append("")
        return "\n".join(lines).rstrip() + "\n"


@dataclass
class ResearchMemo:
    """Full memo document."""

    title: str
    thesis: str = ""
    sections: List[MemoSection] = field(default_factory=list)
    risks: List[str] = field(default_factory=list)
    catalysts: List[str] = field(default_factory=list)
    valuation_notes: str = ""
    sources: List[SourceRef] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def render_markdown(self) -> str:
        parts: List[str] = [f"# {self.title}", ""]
        if self.thesis.strip():
            parts.extend(["## Thesis", "", self.thesis.strip(), ""])
        for sec in self.sections:
            parts.append(sec.render())
            parts.append("")
        if self.catalysts:
            parts.extend(["## Catalysts", ""])
            parts.extend(f"- {c}" for c in self.catalysts)
            parts.append("")
        if self.risks:
            parts.extend(["## Risks", ""])
            parts.extend(f"- {r}" for r in self.risks)
            parts.append("")
        if self.valuation_notes.strip():
            parts.extend(["## Valuation", "", self.valuation_notes.strip(), ""])
        cit = format_citations_markdown(self.sources)
        if cit:
            parts.extend(["", cit, ""])
        return "\n".join(parts).strip() + "\n"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "title": self.title,
            "thesis": self.thesis,
            "sections": [{"title": s.title, "body_md": s.body_md, "bullets": s.bullets} for s in self.sections],
            "risks": list(self.risks),
            "catalysts": list(self.catalysts),
            "valuation_notes": self.valuation_notes,
            "sources": [s.to_dict() for s in self.sources],
            "metadata": dict(self.metadata),
        }


class ResearchMemoBuilder:
    """Fluent builder for `ResearchMemo`."""

    def __init__(self, title: str) -> None:
        self._memo = ResearchMemo(title=title)

    def set_thesis(self, text: str) -> "ResearchMemoBuilder":
        self._memo.thesis = text
        return self

    def add_section(self, title: str, body_md: str = "", bullets: Optional[List[str]] = None) -> "ResearchMemoBuilder":
        self._memo.sections.append(MemoSection(title=title, body_md=body_md, bullets=list(bullets or [])))
        return self

    def add_risk(self, text: str) -> "ResearchMemoBuilder":
        self._memo.risks.append(text)
        return self

    def add_catalyst(self, text: str) -> "ResearchMemoBuilder":
        self._memo.catalysts.append(text)
        return self

    def set_valuation(self, notes_md: str) -> "ResearchMemoBuilder":
        self._memo.valuation_notes = notes_md
        return self

    def add_source(self, ref: SourceRef) -> "ResearchMemoBuilder":
        self._memo.sources.append(ref)
        return self

    def add_sources(self, *refs: SourceRef) -> "ResearchMemoBuilder":
        self._memo.sources = merge_sources(self._memo.sources, list(refs))
        return self

    def meta(self, **kwargs: Any) -> "ResearchMemoBuilder":
        self._memo.metadata.update(kwargs)
        return self

    def build(self) -> ResearchMemo:
        return self._memo

    def render(self) -> str:
        return self._memo.render_markdown()


def memo_from_tool_bundle(
    symbol: str,
    bundle_dict: Dict[str, Any],
    *,
    title: Optional[str] = None,
) -> ResearchMemo:
    """Heuristic memo skeleton from a `MarketDataBundle.to_tool_dict()`-like payload."""
    q = bundle_dict.get("quote") or {}
    nm = title or f"{symbol.upper()} — Quick research snapshot"
    b = ResearchMemoBuilder(nm)
    price = q.get("price")
    chg = q.get("change_percent")
    thesis = f"**{symbol.upper()}** last **{price}**"
    if chg is not None:
        thesis += f" ({chg:+.2f}% vs prior)."
    b.set_thesis(thesis)
    if bundle_dict.get("info_summary"):
        lines = [f"- **{k}**: {v}" for k, v in bundle_dict["info_summary"].items() if v is not None]
        b.add_section("Context", "\n".join(lines))
    if bundle_dict.get("news"):
        bullets = []
        for n in bundle_dict["news"][:8]:
            if isinstance(n, dict) and n.get("title"):
                bullets.append(n["title"][:200])
        if bullets:
            b.add_section("Recent headlines", bullets=bullets)
    b.add_sources(SourceRef.from_tool("market_data_bundle", symbol))
    return b.build()
