"""Launch the Ink-based CLI frontend."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Iterable


def ink_ui_root() -> Path:
    return Path(__file__).resolve().parent / "ink_ui"


def ink_entrypoint() -> Path:
    return ink_ui_root() / "src" / "index.tsx"


def _tsx_binary() -> Path:
    suffix = ".cmd" if os.name == "nt" else ""
    return ink_ui_root() / "node_modules" / ".bin" / f"tsx{suffix}"


def ink_dependencies_ready() -> bool:
    return _tsx_binary().exists() and ink_entrypoint().exists()


def install_hint() -> str:
    ui_root = ink_ui_root()
    return (
        "curl -fsSL https://raw.githubusercontent.com/desenyon/ephemeral/main/scripts/install.sh | bash"
        f" (or `npm install --prefix {ui_root}` when running from a source checkout)"
    )


def launch_ink_ui(extra_args: Iterable[str] | None = None) -> int:
    node = shutil.which("node")
    if not node:
        print("Node.js is required for the Ink UI, but `node` was not found on PATH.", file=sys.stderr)
        return 1

    if not ink_dependencies_ready():
        print(
            "Ink UI dependencies are missing.\n"
            f"Run `{install_hint()}` and try again, or use `ephemeral --legacy-ui` for the Textual interface.",
            file=sys.stderr,
        )
        return 1

    cmd = [str(_tsx_binary()), str(ink_entrypoint())]
    if extra_args:
        cmd.extend(extra_args)

    env = os.environ.copy()
    env["EPHEMERAL_PYTHON_EXECUTABLE"] = sys.executable
    env["EPHEMERAL_PACKAGE_ROOT"] = str(Path(__file__).resolve().parent)
    env["EPHEMERAL_PROJECT_ROOT"] = str(Path(__file__).resolve().parent.parent)
    env.setdefault("FORCE_COLOR", "1")

    return subprocess.call(cmd, env=env)
