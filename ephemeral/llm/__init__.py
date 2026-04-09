"""LLM routing, providers, and convenience constructors."""

from __future__ import annotations

from ephemeral.config import EphemeralError, ErrorCode, LLMProvider, get_settings

from .providers.anthropic_provider import AnthropicProvider
from .providers.base import BaseLLM
from .providers.google_provider import GoogleProvider
from .providers.ollama_provider import OllamaProvider
from .providers.openai_compatible import GroqProvider, XaiProvider
from .providers.openai_provider import OpenAIProvider
from .rate_limit import RateLimiter
from .registry import REGISTRY
from .router import LLMRouter, get_router

# Legacy-friendly class names (tests and external scripts)
GoogleLLM = GoogleProvider
OpenAILLM = OpenAIProvider
AnthropicLLM = AnthropicProvider
OllamaLLM = OllamaProvider
GroqLLM = GroqProvider
XaiLLM = XaiProvider

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
        raise EphemeralError(
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
    if provider == LLMProvider.GROQ:
        return GroqProvider(api_key=key, rate_limiter=_rate_limiters["groq"])
    if provider == LLMProvider.XAI:
        return XaiProvider(api_key=key, rate_limiter=_rate_limiters["xai"])

    raise EphemeralError(
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
    "GroqProvider",
    "XaiProvider",
    "OllamaProvider",
    "GoogleLLM",
    "OpenAILLM",
    "AnthropicLLM",
    "OllamaLLM",
    "GroqLLM",
    "XaiLLM",
    "_rate_limiters",
]
