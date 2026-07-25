"""Bridge to the OpenAI Codex CLI as an alternate Ephemeral backend.

Unlike Pi, Codex CLI has native MCP client support (`codex mcp` / `mcp_servers.*` config),
so Ephemeral's research tools are wired in via a one-off `-c mcp_servers.ephemeral.*`
override pointing at :mod:`ephemeral.mcp_server` — no extension/bridging layer needed.

Known limitation (verified against codex-cli 0.145.0): non-interactive `codex exec` runs
require a human to approve each MCP tool call, and there is no non-interactive escape hatch
for that gate short of `--dangerously-bypass-approvals-and-sandbox` (which also disables
all sandboxing and is deliberately not used here). In practice this means Ephemeral's tools
will show up to the model but calls to them get auto-declined in headless mode, and Codex
falls back to its own built-in tools (bash, web_search, ...) instead — still a useful,
correct answer, just not routed through Ephemeral's tool registry. `codex mcp add ephemeral`
(a one-time, explicit, user-approved step) registers the server globally so this improves
automatically if a future Codex release adds a non-interactive MCP approval mode.
"""

from __future__ import annotations

import asyncio
import json
import logging
import os
import shutil
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


class CodexHarnessError(Exception):
    """Raised when the `codex` CLI is unavailable or a turn fails to complete."""


def find_codex_binary() -> Optional[str]:
    return shutil.which("codex")


def codex_available() -> bool:
    return find_codex_binary() is not None


def _mcp_server_python() -> str:
    venv_python = REPO_ROOT / ".venv" / "bin" / "python"
    return str(venv_python) if venv_python.exists() else sys.executable


def _parse_event_stream(raw: str) -> Dict[str, Any]:
    """Reduce a `codex exec --json` event stream to a final answer + tool step log."""
    steps: List[Dict[str, Any]] = []
    final_text = ""
    error: Optional[str] = None

    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue

        if event.get("type") != "item.completed":
            continue
        item = event.get("item") or {}
        item_type = item.get("type")

        if item_type == "agent_message":
            final_text = item.get("text", final_text)
        elif item_type in ("mcp_tool_call", "command_execution", "web_search"):
            steps.append(
                {
                    "type": item_type,
                    "tool": item.get("tool") or item.get("server"),
                    "arguments": item.get("arguments"),
                    "failed": bool(item.get("error")),
                }
            )
        elif item_type == "error":
            # Codex emits informational notices (e.g. skill-budget trims) as
            # type "error" too — only treat it as fatal if no answer ever arrives.
            error = item.get("message") or "Codex CLI reported an error."

    if final_text:
        error = None
    return {"response": final_text, "steps": steps, "error": error}


async def run_codex_turn(
    query: str,
    *,
    model: Optional[str] = None,
    cwd: Optional[str] = None,
    timeout_seconds: float = 180.0,
    sandbox: str = "read-only",
) -> Dict[str, Any]:
    """Run one non-interactive turn through the OpenAI Codex CLI."""
    binary = find_codex_binary()
    if not binary:
        raise CodexHarnessError(
            "The `codex` CLI is not installed. Install it with `npm i -g @openai/codex` "
            "or see https://github.com/openai/codex, then retry."
        )

    args = [
        binary,
        "exec",
        "--json",
        "--skip-git-repo-check",
        "--sandbox",
        sandbox,
        "-c",
        f'mcp_servers.ephemeral.command="{_mcp_server_python()}"',
        "-c",
        'mcp_servers.ephemeral.args=["-m","ephemeral.mcp_server"]',
    ]
    if model:
        args += ["--model", model]
    args.append(query)

    process = await asyncio.create_subprocess_exec(
        *args,
        cwd=cwd or str(REPO_ROOT),
        env=dict(os.environ),
        stdin=asyncio.subprocess.DEVNULL,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    try:
        stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=timeout_seconds)
    except asyncio.TimeoutError as exc:
        process.kill()
        await process.wait()
        raise CodexHarnessError(f"Codex harness timed out after {timeout_seconds}s") from exc

    if process.returncode != 0 and not stdout:
        raise CodexHarnessError(
            f"Codex CLI exited with {process.returncode}: "
            f"{stderr.decode(errors='replace')[:2000]}"
        )

    result = _parse_event_stream(stdout.decode(errors="replace"))
    result["backend"] = "codex"
    result["provider"] = "openai"
    result["model"] = model
    return result
