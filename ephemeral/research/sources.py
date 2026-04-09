"""Source attribution for research outputs (tool-backed or external)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional
from urllib.parse import urlparse


@dataclass
class SourceRef:
    """A single citable source line."""

    label: str
    kind: str = "tool"
    detail: str = ""
    url: Optional[str] = None
    retrieved_at: str = field(default_factory=lambda: datetime.utcnow().strftime("%Y-%m-%dT%H:%MZ"))

    def to_markdown_line(self) -> str:
        parts = [f"- **{self.label}** ({self.kind})"]
        if self.detail:
            parts.append(f" — {self.detail}")
        if self.url:
            host = urlparse(self.url).netloc or self.url
            parts.append(f" — [{host}]({self.url})")
        parts.append(f" _{self.retrieved_at}_")
        return "".join(parts)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "label": self.label,
            "kind": self.kind,
            "detail": self.detail,
            "url": self.url,
            "retrieved_at": self.retrieved_at,
        }

    @classmethod
    def from_tool(cls, tool_name: str, symbol: str = "", extra: str = "") -> "SourceRef":
        d = f"`{symbol}`" if symbol else ""
        if extra:
            d = f"{d} {extra}".strip()
        return cls(label=tool_name, kind="tool", detail=d)


def format_citations_markdown(sources: List[SourceRef], title: str = "### Sources") -> str:
    if not sources:
        return ""
    lines = [title, ""]
    lines.extend(s.to_markdown_line() for s in sources)
    return "\n".join(lines)


def merge_sources(*groups: List[SourceRef]) -> List[SourceRef]:
    seen: set[str] = set()
    out: List[SourceRef] = []
    for g in groups:
        for s in g:
            key = f"{s.label}|{s.detail}|{s.url or ''}"
            if key in seen:
                continue
            seen.add(key)
            out.append(s)
    return out
