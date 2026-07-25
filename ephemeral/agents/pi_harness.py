"""Bridge to the Pi coding-agent harness (https://pi.dev) as an alternate Ephemeral backend.

Ephemeral's own :class:`~ephemeral.llm.router.LLMRouter` calls providers directly
in-process. This module instead shells out to the `pi` CLI so a turn runs through Pi's
own minimal agent loop (read/write/edit/bash + Pi's 15+ provider list), with Ephemeral's
research tools (quote, news, compare, chart, backtest, ...) available to it through the
project-local ``.pi/extensions/ephemeral-tools.ts`` extension — an MCP client wired to
:mod:`ephemeral.mcp_server`, auto-discovered by Pi when run from the repo root.
"""

from __future__ import annotations

import asyncio
import json
import logging
import os
import shutil
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


class PiHarnessError(Exception):
    """Raised when the `pi` CLI is unavailable or a turn fails to complete."""


def find_pi_binary() -> Optional[str]:
    """Locate the `pi` CLI: PATH first, then the ink_ui-local npm install."""
    on_path = shutil.which("pi")
    if on_path:
        return on_path
    local = REPO_ROOT / "ephemeral" / "ink_ui" / "node_modules" / ".bin" / "pi"
    if local.exists():
        return str(local)
    return None


def pi_available() -> bool:
    return find_pi_binary() is not None


def _parse_event_stream(raw: str) -> Dict[str, Any]:
    """Reduce a `pi --mode json` event stream to a final answer + tool step log."""
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

        etype = event.get("type")
        if etype == "tool_execution_end":
            steps.append(
                {
                    "tool": event.get("toolName"),
                    "args": event.get("args"),
                    "is_error": bool(event.get("isError")),
                }
            )
        elif etype == "agent_end":
            for message in reversed(event.get("messages") or []):
                if message.get("role") != "assistant":
                    continue
                # Pi reports provider-side failures (bad model, no model access, etc.)
                # as an assistant message with empty content and stopReason "error"
                # rather than a non-zero process exit — surface it explicitly.
                if message.get("stopReason") == "error":
                    error = message.get("errorMessage") or "Pi harness reported an error."
                    break
                content = message.get("content")
                if isinstance(content, str):
                    final_text = content
                elif isinstance(content, list):
                    final_text = "".join(
                        block.get("text", "")
                        for block in content
                        if isinstance(block, dict) and block.get("type") == "text"
                    )
                break

    return {"response": final_text, "steps": steps, "error": error}


async def run_pi_turn(
    query: str,
    *,
    provider: Optional[str] = None,
    model: Optional[str] = None,
    api_key: Optional[str] = None,
    cwd: Optional[str] = None,
    timeout_seconds: float = 120.0,
) -> Dict[str, Any]:
    """Run one non-interactive turn through the Pi coding-agent harness."""
    binary = find_pi_binary()
    if not binary:
        raise PiHarnessError(
            "The `pi` CLI is not installed. Install it with "
            "`npm i -g @earendil-works/pi-coding-agent` or run `npm install` inside "
            "ephemeral/ink_ui, then retry."
        )

    # --approve trusts project-local files (.pi/extensions/ephemeral-tools.ts) for this
    # run. Without it, headless --print runs never load project-local extensions (they
    # require project trust, which has no one to prompt outside the TUI) and the model
    # silently falls back to Pi's builtin bash/read/write/edit tools instead of
    # Ephemeral's research tools.
    args = [binary, "--print", "--mode", "json", "--no-session", "--approve"]
    if provider:
        args += ["--provider", provider]
    if model:
        args += ["--model", model]
    if api_key:
        args += ["--api-key", api_key]
    args.append(query)

    process = await asyncio.create_subprocess_exec(
        *args,
        cwd=cwd or str(REPO_ROOT),
        env=dict(os.environ),
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    try:
        stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=timeout_seconds)
    except asyncio.TimeoutError as exc:
        process.kill()
        await process.wait()
        raise PiHarnessError(f"Pi harness timed out after {timeout_seconds}s") from exc

    if process.returncode != 0:
        raise PiHarnessError(
            f"Pi harness exited with {process.returncode}: "
            f"{stderr.decode(errors='replace')[:2000]}"
        )

    result = _parse_event_stream(stdout.decode(errors="replace"))
    result["backend"] = "pi"
    result["provider"] = provider
    result["model"] = model
    return result
