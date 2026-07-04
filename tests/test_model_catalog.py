from ephemeral.config import AVAILABLE_MODELS
from ephemeral.llm.registry import REGISTRY
from ephemeral.model_catalog import MODEL_CATALOG


def test_available_models_all_resolve_to_their_provider() -> None:
    for provider, models in AVAILABLE_MODELS.items():
        for model in models:
            assert REGISTRY.get_provider(model) == provider


def test_registry_is_built_from_model_catalog() -> None:
    catalog_ids = {entry.model_id for entry in MODEL_CATALOG}
    registry_ids = {entry.model_id for entry in REGISTRY.list_models()}

    assert registry_ids == catalog_ids


def test_deprecated_models_are_not_user_facing_or_registered() -> None:
    deprecated = {
        "gemini-2.0-flash",
        "gemini-1.5-pro",
        "gemini-3-flash-preview",
        "gemini-3-pro-preview",
        "gemini-3-pro-image-preview",
        "gpt-4o",
        "gpt-4o-mini",
        "o1",
        "o1-mini",
        "claude-3-opus-20240229",
        "claude-sonnet-4-20250514",
        "claude-opus-4-20250514",
        "grok-3",
        "grok-3-mini",
    }
    user_facing = {model for models in AVAILABLE_MODELS.values() for model in models}
    registered = {entry.model_id for entry in REGISTRY.list_models()}

    assert deprecated.isdisjoint(user_facing)
    assert deprecated.isdisjoint(registered)
