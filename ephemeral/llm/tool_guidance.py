"""Helpers to steer models toward broader, parallel tool use."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ephemeral.tools.registry import ToolRegistry

USER_TOOL_NUDGE = (
    "\n\n---\n"
    "**Reminder:** Answer using tools—not training memory alone. "
    "When the question involves prices, catalysts, fundamentals, peers, or risk together, "
    "issue **multiple** tool calls in this turn (e.g. quote + `fetch_news_digest` + risk or fundamentals). "
    "For comparisons, call tools for **each** symbol or use `compare_stocks` where appropriate."
)


def tool_catalog_markdown(registry: "ToolRegistry", max_desc_len: int = 100) -> str:
    """Compact name + description list for the system prompt."""
    lines: list[str] = []
    for t in sorted(registry.list_tools(), key=lambda x: x.name):
        desc = (t.description or "").replace("\n", " ").strip()
        if len(desc) > max_desc_len:
            desc = desc[: max_desc_len - 3] + "..."
        lines.append(f"- `{t.name}` — {desc}")
    return "\n".join(lines)


def build_augmented_system_prompt(base: str, registry: "ToolRegistry") -> str:
    """Append tool catalog so the model maps tasks to tool names (reduces under-calling)."""
    return (
        base.rstrip()
        + "\n\n## Full tool catalog (names match function calls)\n"
        "Issue **several** of these in parallel when the user needs a complete picture.\n\n"
        + tool_catalog_markdown(registry)
    )
