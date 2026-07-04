from typing import Dict, List, Optional

from pydantic import BaseModel

from ephemeral.model_catalog import MODEL_CATALOG


class ModelInfo(BaseModel):
    provider: str
    model_id: str
    capabilities: List[str] = []  # "vision", "tools", "json", "reasoning"
    context_window: int = 4096
    cost_tier: str = "paid"  # "free", "low", "high"


class ModelRegistry:
    def __init__(self):
        self._models: Dict[str, ModelInfo] = {}

        for entry in MODEL_CATALOG:
            self.register(
                entry.model_id,
                entry.provider,
                list(entry.capabilities),
                entry.context_window,
                entry.cost_tier,
            )

    def register(
        self,
        model_id: str,
        provider: str,
        capabilities: List[str],
        context_window: int,
        cost_tier: str,
    ):
        self._models[model_id] = ModelInfo(
            provider=provider,
            model_id=model_id,
            capabilities=capabilities,
            context_window=context_window,
            cost_tier=cost_tier,
        )

    def get_provider(self, model_id: str) -> str:
        if model_id in self._models:
            return self._models[model_id].provider
        # Fallback heuristics
        if model_id.startswith("gpt"):
            return "openai"
        if model_id.startswith("o3"):
            return "openai"
        if model_id.startswith("claude"):
            return "anthropic"
        if model_id.startswith("gemini"):
            return "google"
        if model_id.startswith("grok"):
            return "xai"
        if model_id.startswith("mixtral-"):
            return "groq"
        return "ollama"

    def list_models(self) -> List[ModelInfo]:
        return list(self._models.values())

    def find_best_model(
        self, provider: Optional[str] = None, capability: Optional[str] = None
    ) -> Optional[str]:
        # Simple selection logic
        candidates = self._models.values()
        if provider:
            candidates = [m for m in candidates if m.provider == provider]
        if capability:
            candidates = [m for m in candidates if capability in m.capabilities]

        # Sort by "newest" implies preference order.
        # For now return first match.
        if candidates:
            return list(candidates)[0].model_id
        return None


REGISTRY = ModelRegistry()
