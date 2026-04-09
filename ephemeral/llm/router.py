import logging
from typing import Any, AsyncIterator, Callable, Dict, List, Optional, Union

from .providers.anthropic_provider import AnthropicProvider
from .providers.base import BaseLLM
from .providers.google_provider import GoogleProvider
from .providers.ollama_provider import OllamaProvider
from .providers.openai_compatible import GroqProvider, XaiProvider
from .providers.openai_provider import OpenAIProvider
from .rate_limit import RateLimiter
from .registry import REGISTRY

logger = logging.getLogger(__name__)

class LLMRouter:
    def __init__(self, settings):
        self.settings = settings
        self.providers: Dict[str, BaseLLM] = {}

        self._init_providers()

    def _init_providers(self):
        # OpenAI
        if self.settings.openai_api_key:
            self.providers["openai"] = OpenAIProvider(
                api_key=self.settings.openai_api_key,
                rate_limiter=RateLimiter(60, 0.2)
            )

        # Anthropic
        if self.settings.anthropic_api_key:
            self.providers["anthropic"] = AnthropicProvider(
                api_key=self.settings.anthropic_api_key,
                rate_limiter=RateLimiter(40, 0.5)
            )

        # Google
        if self.settings.google_api_key:
            self.providers["google"] = GoogleProvider(
                api_key=self.settings.google_api_key,
                rate_limiter=RateLimiter(60, 0.2)
            )

        # Groq (OpenAI-compatible)
        if getattr(self.settings, "groq_api_key", None):
            self.providers["groq"] = GroqProvider(
                api_key=self.settings.groq_api_key,
                rate_limiter=RateLimiter(30, 0.5),
            )

        # xAI (OpenAI-compatible)
        if getattr(self.settings, "xai_api_key", None):
            self.providers["xai"] = XaiProvider(
                api_key=self.settings.xai_api_key,
                rate_limiter=RateLimiter(30, 0.5),
            )

        # Ollama (always available usually)
        ollama_base = getattr(self.settings, "ollama_host", None) or "http://localhost:11434"
        self.providers["ollama"] = OllamaProvider(
            base_url=ollama_base,
            rate_limiter=RateLimiter(100, 0.01),
        )

    async def chat(
        self,
        messages: List[Dict[str, str]],
        model: Optional[str] = None,
        tools: Optional[List[Dict[str, Any]]] = None,
        on_tool_call: Optional[Callable] = None,
        stream: bool = True,
        json_mode: bool = False,
        provider: Optional[str] = None
    ) -> Union[str, AsyncIterator[str]]:

        # Determine model and provider
        selected_model = model or self.settings.default_model
        selected_provider = provider

        if not selected_provider:
            selected_provider = REGISTRY.get_provider(selected_model)

        # Get client
        client = self.providers.get(selected_provider)
        if not client:
            # Fallback logic
            if "ollama" in self.providers:
                logger.warning(
                    "Provider %s not available (missing API key or not wired), falling back to Ollama",
                    selected_provider,
                )
                client = self.providers["ollama"]
                selected_model = getattr(self.settings, "ollama_model", None) or "llama3.3"
            else:
                raise ValueError(
                    f"Provider {selected_provider} not configured and no Ollama fallback available."
                )

        # Execute
        try:
            return await client.generate(
                messages=messages,
                model=selected_model,
                tools=tools,
                on_tool_call=on_tool_call,
                stream=stream,
                json_mode=json_mode
            )
        except Exception as e:
            logger.error(f"Error generation with {selected_provider}/{selected_model}: {e}")
            # Circuit breaker / fallback could go here
            if selected_provider != "ollama" and "ollama" in self.providers:
                logger.info("Falling back to Ollama due to error")
                fb_model = getattr(self.settings, "ollama_model", None) or "llama3.3"
                return await self.providers["ollama"].generate(
                    messages=messages,
                    model=fb_model,
                    tools=tools,
                    on_tool_call=on_tool_call,
                    stream=stream,
                    json_mode=json_mode,
                )
            raise

_router_instance: Optional[LLMRouter] = None


def get_router(settings: Any = None, *, force: bool = False) -> LLMRouter:
    """Return the shared router; use ``force=True`` after config changes."""
    global _router_instance
    from ..config import get_settings as _get_settings

    if force:
        s = settings if settings is not None else _get_settings()
        _router_instance = LLMRouter(s)
        return _router_instance
    if not _router_instance:
        if settings is None:
            raise RuntimeError("LLM Router not initialized and no settings provided")
        _router_instance = LLMRouter(settings)
    return _router_instance
