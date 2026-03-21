"""LLM routing, providers, and convenience constructors."""

from __future__ import annotations

from typing import Any, AsyncIterator, Callable, Dict, List, Optional, Union

from sigma.config import ErrorCode, LLMProvider, SigmaError, get_settings

from .providers.anthropic_provider import AnthropicProvider
from .providers.base import BaseLLM
from .providers.google_provider import GoogleProvider
from .providers.ollama_provider import OllamaProvider
from .providers.openai_provider import OpenAIProvider
from .rate_limit import RateLimiter
from .registry import REGISTRY
from .router import LLMRouter, get_router

# Legacy-friendly class names (tests and external scripts)
GoogleLLM = GoogleProvider
OpenAILLM = OpenAIProvider
AnthropicLLM = AnthropicProvider
OllamaLLM = OllamaProvider


class GroqLLM(BaseLLM):
    """Reserved Groq client surface (router integration pending)."""

    provider_name = "groq"

    async def generate(
        self,
        messages: List[Dict[str, str]],
        model: str,
        tools: Optional[List[Dict[str, Any]]] = None,
        on_tool_call: Optional[Callable] = None,
        stream: bool = True,
        json_mode: bool = False,
    ) -> Union[str, AsyncIterator[str]]:
        raise NotImplementedError("Groq client is not enabled in this build")


class XaiLLM(BaseLLM):
    """Reserved xAI client surface (router integration pending)."""

    provider_name = "xai"

    async def generate(
        self,
        messages: List[Dict[str, str]],
        model: str,
        tools: Optional[List[Dict[str, Any]]] = None,
        on_tool_call: Optional[Callable] = None,
        stream: bool = True,
        json_mode: bool = False,
    ) -> Union[str, AsyncIterator[str]]:
        raise NotImplementedError("xAI client is not enabled in this build")

_rate_limiters = {
    "google": RateLimiter(60, 0.2),
    "openai": RateLimiter(60, 0.2),
    "anthropic": RateLimiter(40, 0.5),
    "groq": RateLimiter(30, 0.5),
    "xai": RateLimiter(30, 0.5),
    "ollama": RateLimiter(100, 0.01),
}


def get_llm(provider: LLMProvider) -> BaseLLM:
    """Instantiate the configured client for a provider (used by tests and tooling)."""
    settings = get_settings()

    if provider == LLMProvider.OLLAMA:
        return OllamaProvider(
            base_url=settings.ollama_host,
            rate_limiter=_rate_limiters["ollama"],
        )

    key = settings.get_api_key(provider)
    if not key:
        raise SigmaError(
            ErrorCode.API_KEY_MISSING,
            f"API key not configured for {provider.value}",
            {"provider": provider.value},
        )

    if provider == LLMProvider.GOOGLE:
        return GoogleProvider(api_key=key, rate_limiter=_rate_limiters["google"])
    if provider == LLMProvider.OPENAI:
        return OpenAIProvider(api_key=key, rate_limiter=_rate_limiters["openai"])
    if provider == LLMProvider.ANTHROPIC:
        return AnthropicProvider(api_key=key, rate_limiter=_rate_limiters["anthropic"])

    raise SigmaError(
        ErrorCode.PROVIDER_UNAVAILABLE,
        f"Provider {provider.value} is not wired in this build",
        {"provider": provider.value},
    )


__all__ = [
    "LLMRouter",
    "get_router",
    "get_llm",
    "get_settings",
    "REGISTRY",
    "BaseLLM",
    "GoogleProvider",
    "OpenAIProvider",
    "AnthropicProvider",
    "OllamaProvider",
    "GoogleLLM",
    "OpenAILLM",
    "AnthropicLLM",
    "OllamaLLM",
    "GroqLLM",
    "XaiLLM",
    "_rate_limiters",
]
