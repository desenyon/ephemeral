"""OpenAI-compatible HTTP APIs (Groq, xAI) — same tool/stream semantics as OpenAI."""

from __future__ import annotations

from typing import Optional

from .openai_provider import OpenAIProvider


class GroqProvider(OpenAIProvider):
    """Groq (Llama, Mixtral, etc.) via OpenAI-compatible endpoint."""

    provider_name = "groq"

    def __init__(self, api_key: str, rate_limiter=None, base_url: Optional[str] = None):
        super().__init__(
            api_key,
            rate_limiter,
            base_url=base_url or "https://api.groq.com/openai/v1",
        )


class XaiProvider(OpenAIProvider):
    """xAI Grok via OpenAI-compatible endpoint."""

    provider_name = "xai"

    def __init__(self, api_key: str, rate_limiter=None, base_url: Optional[str] = None):
        super().__init__(
            api_key,
            rate_limiter,
            base_url=base_url or "https://api.x.ai/v1",
        )
