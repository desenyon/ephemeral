from unittest.mock import call, patch

from ephemeral import setup_agent


def test_preferred_ollama_model_prefers_known_tooling_models() -> None:
    model = setup_agent._preferred_ollama_model({"mistral", "qwen2.5:1.5b", "llama3.3"})
    assert model == "qwen2.5:1.5b"


def test_preferred_ollama_model_falls_back_to_sorted_first_entry() -> None:
    model = setup_agent._preferred_ollama_model({"zed", "alpha"})
    assert model == "alpha"


def test_bind_ollama_model_persists_all_runtime_settings() -> None:
    with patch("ephemeral.setup_agent.save_setting") as save_setting:
        setup_agent._bind_ollama_model("qwen2.5:1.5b")

    assert save_setting.call_args_list == [
        call("default_model", "qwen2.5:1.5b"),
        call("ollama_model", "qwen2.5:1.5b"),
        call("ollama_host", "http://localhost:11434"),
        call("default_provider", "ollama"),
    ]
