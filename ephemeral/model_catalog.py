"""Single source of truth for bundled model metadata."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass(frozen=True)
class ModelCatalogEntry:
    provider: str
    model_id: str
    capabilities: Tuple[str, ...]
    context_window: int
    cost_tier: str


MODEL_CATALOG: Tuple[ModelCatalogEntry, ...] = (
    ModelCatalogEntry(
        "google", "gemini-3.1-pro", ("tools", "vision", "json", "reasoning"), 1_000_000, "high"
    ),
    ModelCatalogEntry(
        "google", "gemini-3-pro", ("tools", "vision", "json", "reasoning"), 1_000_000, "high"
    ),
    ModelCatalogEntry("google", "gemini-3-flash", ("tools", "vision", "json"), 1_000_000, "free"),
    ModelCatalogEntry("google", "gemini-3-pro-image", ("vision", "json"), 1_000_000, "high"),
    ModelCatalogEntry(
        "openai", "gpt-5.4", ("tools", "json", "vision", "reasoning"), 256_000, "high"
    ),
    ModelCatalogEntry(
        "openai", "gpt-5.2", ("tools", "json", "vision", "reasoning"), 256_000, "high"
    ),
    ModelCatalogEntry(
        "openai", "gpt-5.1", ("tools", "json", "vision", "reasoning"), 256_000, "high"
    ),
    ModelCatalogEntry("openai", "gpt-5", ("tools", "json", "vision", "reasoning"), 256_000, "high"),
    ModelCatalogEntry("openai", "gpt-5-mini", ("tools", "json", "vision"), 256_000, "low"),
    ModelCatalogEntry("openai", "gpt-5-nano", ("tools", "json"), 128_000, "low"),
    ModelCatalogEntry("openai", "o3-preview", ("reasoning", "tools"), 256_000, "high"),
    ModelCatalogEntry("openai", "o3-mini", ("reasoning", "tools"), 128_000, "low"),
    ModelCatalogEntry(
        "anthropic", "claude-opus-4-6", ("tools", "vision", "reasoning"), 200_000, "high"
    ),
    ModelCatalogEntry(
        "anthropic", "claude-sonnet-4-6", ("tools", "vision", "reasoning"), 200_000, "high"
    ),
    ModelCatalogEntry("groq", "llama-3.3-70b-versatile", ("tools", "json"), 128_000, "low"),
    ModelCatalogEntry("groq", "llama-3.3-8b-instant", ("tools", "json"), 128_000, "free"),
    ModelCatalogEntry("groq", "mixtral-8x7b-32768", ("tools", "json"), 32_768, "low"),
    ModelCatalogEntry("xai", "grok-4", ("tools", "json"), 256_000, "high"),
    ModelCatalogEntry("xai", "grok-4-mini", ("tools", "json"), 128_000, "low"),
    ModelCatalogEntry("ollama", "qwen3.5:8b", ("tools",), 128_000, "free"),
    ModelCatalogEntry("ollama", "qwen3.5:4b", ("tools",), 64_000, "free"),
    ModelCatalogEntry("ollama", "qwen2.5:1.5b", ("tools",), 32_768, "free"),
    ModelCatalogEntry("ollama", "qwen2.5:7b", ("tools",), 64_000, "free"),
    ModelCatalogEntry("ollama", "llama3.3", ("tools",), 128_000, "free"),
    ModelCatalogEntry("ollama", "llama3.2", ("tools",), 32_000, "free"),
    ModelCatalogEntry("ollama", "mistral", ("tools",), 32_000, "free"),
    ModelCatalogEntry("ollama", "deepseek-r1", ("reasoning", "tools"), 128_000, "free"),
)


def available_models_by_provider() -> Dict[str, List[str]]:
    providers: Dict[str, List[str]] = {}
    for entry in MODEL_CATALOG:
        providers.setdefault(entry.provider, []).append(entry.model_id)
    return providers
