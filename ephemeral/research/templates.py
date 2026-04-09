"""Markdown skeletons for research deliverables."""

from __future__ import annotations

from typing import List

MEMO_TEMPLATE_INVESTMENT_THESIS = """# {title}

## Executive summary
{executive_summary}

## Thesis
{thesis}

## Evidence
{evidence}

## Risks
{risks}

## Catalysts
{catalysts}

## Action / sizing (illustrative)
{sizing}

## Sources
{sources}
"""


def render_memo_skeleton(
    *,
    title: str,
    executive_summary: str = "_TBD_",
    thesis: str = "_TBD_",
    evidence: str = "_TBD_",
    risks: str = "_TBD_",
    catalysts: str = "_TBD_",
    sizing: str = "_TBD_",
    sources: str = "_TBD_",
) -> str:
    return MEMO_TEMPLATE_INVESTMENT_THESIS.format(
        title=title,
        executive_summary=executive_summary,
        thesis=thesis,
        evidence=evidence,
        risks=risks,
        catalysts=catalysts,
        sizing=sizing,
        sources=sources,
    )


def checklist_markdown(items: List[str], done: List[bool] | None = None) -> str:
    done = done or [False] * len(items)
    lines = []
    for i, it in enumerate(items):
        box = "[x]" if i < len(done) and done[i] else "[ ]"
        lines.append(f"- {box} {it}")
    return "\n".join(lines)
