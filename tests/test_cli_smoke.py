from __future__ import annotations

import sys
from unittest.mock import patch

import pytest

from ephemeral import cli


def run_cli(args: list[str], tmp_path) -> int:
    with (
        patch.object(sys, "argv", ["ephemeral", *args]),
        patch("ephemeral.cli.is_first_run", return_value=False),
        patch("ephemeral.config.CONFIG_DIR", tmp_path),
        patch("ephemeral.config.CONFIG_FILE", tmp_path / "config.env"),
    ):
        return cli.main()


def test_version_no_ui_prints_plain_version(tmp_path, capsys) -> None:
    exit_code = run_cli(["--version", "--no-ui"], tmp_path)

    assert exit_code == 0
    assert capsys.readouterr().out.strip() == "ephemeral 3.8.0"


def test_list_models_smoke(tmp_path, capsys) -> None:
    exit_code = run_cli(["--list-models"], tmp_path)

    assert exit_code == 0
    output = capsys.readouterr().out
    assert "openai" in output
    assert "ollama" in output


def test_tools_smoke(tmp_path, capsys) -> None:
    exit_code = run_cli(["tools"], tmp_path)

    assert exit_code == 0
    assert "get_stock_quote" in capsys.readouterr().out


def test_invalid_provider_exits_before_writing_config(tmp_path) -> None:
    with pytest.raises(SystemExit) as exc:
        run_cli(["--provider", "not-real"], tmp_path)

    assert exc.value.code == 2
    assert not (tmp_path / "config.env").exists()
