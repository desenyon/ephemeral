"""Regression tests for IntentParser LLM routing conditions."""

from __future__ import annotations

import asyncio
from types import SimpleNamespace
from unittest.mock import patch

from ephemeral.core.intent import IntentParser
from ephemeral.core.models import DeliverableType, ResearchPlan


def test_intent_parser_uses_ollama_host_for_llm_path() -> None:
    parser = IntentParser()
    settings = SimpleNamespace(
        openai_api_key=None,
        anthropic_api_key=None,
        google_api_key=None,
        ollama_host="http://localhost:11434",
    )
    sentinel_plan = ResearchPlan(
        goal="Use Ollama-backed intent parsing",
        assets=["AAPL"],
        deliverable=DeliverableType.ANALYSIS,
        context={"source": "llm"},
    )
    calls = {"llm": 0}

    async def fake_parse_with_llm(query: str, router: object) -> ResearchPlan:
        calls["llm"] += 1
        return sentinel_plan

    parser._parse_with_llm = fake_parse_with_llm  # type: ignore[method-assign]

    with patch("ephemeral.config.get_settings", return_value=settings), patch(
        "ephemeral.llm.router.get_router", return_value=object()
    ):
        result = asyncio.run(parser.parse("Analyze AAPL"))

    assert calls["llm"] == 1
    assert result == sentinel_plan
