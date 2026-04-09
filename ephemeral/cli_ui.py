"""Rich presentation layer for the Ephemeral CLI — layout, themes, and diagnostics."""

from __future__ import annotations

import importlib.util
import os
import platform
import shutil
import subprocess
import sys
import webbrowser
from pathlib import Path
from typing import TYPE_CHECKING, Optional

from rich import box
from rich.align import Align
from rich.console import Console, Group
from rich.panel import Panel
from rich.rule import Rule
from rich.table import Table
from rich.text import Text
from rich.theme import Theme

if TYPE_CHECKING:
    from ephemeral.config import Settings

from ephemeral.ink_launcher import ink_dependencies_ready, install_hint

EPHEMERAL_THEME = Theme(
    {
        "ephemeral.brand": "bold #7aa2f7",
        "ephemeral.dim": "dim #565f89",
        "ephemeral.ok": "bold #9ece6a",
        "ephemeral.warn": "bold #e0af68",
        "ephemeral.err": "bold #f7768e",
        "ephemeral.accent": "bold #bb9af7",
        "ephemeral.muted": "#414868",
    }
)


def make_console() -> Console:
    return Console(theme=EPHEMERAL_THEME, highlight=True, soft_wrap=True)


def ephemeral_logo_text(version: str) -> Text:
    """ASCII art logo as a Rich Text."""
    lines = [
        ("███████╗██╗ ██████╗ ███╗   ███╗ █████╗\n", "bold #3b82f6"),
        ("██╔════╝██║██╔════╝ ████╗ ████║██╔══██╗\n", "bold #60a5fa"),
        ("███████╗██║██║  ███╗██╔████╔██║███████║\n", "bold #93c5fd"),
        ("╚════██║██║██║   ██║██║╚██╔╝██║██╔══██║\n", "bold #60a5fa"),
        ("███████║██║╚██████╔╝██║ ╚═╝ ██║██║  ██║\n", "bold #3b82f6"),
        ("╚══════╝╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝\n", "bold #1d4ed8"),
    ]
    t = Text()
    for s, style in lines:
        t.append(s, style=style)
    t.append(f"v{version}  ", style="dim")
    t.append("E", style="bold cyan")
    t.append("  Terminal Research Agent", style="bold")
    return t


def print_banner(console: Console, version: str) -> None:
    console.print()
    console.print(Align.center(ephemeral_logo_text(version)))
    console.print()


def print_quick_start(console: Console) -> None:
    # Table header_style must use concrete styles — custom theme names are not resolved here (Rich 13+).
    grid = Table(
        title="[ephemeral.brand]Command palette[/ephemeral.brand]",
        box=box.ROUNDED,
        border_style="ephemeral.muted",
        show_header=True,
        header_style="bold #bb9af7",
        padding=(0, 1),
    )
    grid.add_column("Command", style="cyan", no_wrap=True)
    grid.add_column("What it does")
    rows = [
        ("ephemeral", "Launch the Ink interactive UI"),
        ("ephemeral --legacy-ui", "Launch the legacy Textual interface"),
        ('ephemeral ask "…"', "One-shot LLM query with tools"),
        ("ephemeral quote AAPL MSFT", "Live-style quotes table"),
        ("ephemeral chart SPY --period 1y", "Export chart to ~/.ephemeral/charts"),
        ("ephemeral backtest AAPL -s sma_crossover", "Run a strategy backtest"),
        ("ephemeral compare AAPL MSFT GOOGL", "Side-by-side metrics"),
        ("ephemeral doctor", "Environment health check"),
        ("ephemeral --status", "Keys and provider (masked)"),
        ("ephemeral --setup", "Interactive setup wizard"),
    ]
    for cmd, desc in rows:
        grid.add_row(cmd, desc)
    console.print(Panel(grid, border_style="ephemeral.muted", box=box.DOUBLE))


def mask_secret(value: Optional[str], visible: int = 4) -> str:
    if not value:
        return "[ephemeral.err]—[/ephemeral.err]"
    if len(value) <= visible * 2:
        return "[ephemeral.ok]••••[/ephemeral.ok]"
    return f"[ephemeral.ok]{value[:visible]}…{value[-visible:]}[/ephemeral.ok]"


def open_file_cross_platform(path: str) -> None:
    """Best-effort open of a file (image/HTML) in the user's default app."""
    p = Path(path).expanduser().resolve()
    if not p.is_file():
        return
    try:
        if platform.system() == "Darwin":
            subprocess.run(["open", str(p)], check=False)
        elif platform.system() == "Windows":
            os.startfile(str(p))  # type: ignore[attr-defined]
        else:
            webbrowser.open(p.as_uri())
    except Exception:
        try:
            webbrowser.open(p.as_uri())
        except Exception:
            pass


def module_available(name: str) -> bool:
    return importlib.util.find_spec(name) is not None


def run_doctor(console: Console, settings: "Settings") -> int:
    """Print a structured health report; returns 0 if nothing critical failed."""
    console.print(Rule("[ephemeral.brand]Ephemeral doctor[/ephemeral.brand]", style="ephemeral.muted"))

    env = Table(box=box.SIMPLE, show_header=False, padding=(0, 2))
    env.add_column("Check", style="bold")
    env.add_column("Result")

    py_ok = sys.version_info >= (3, 11)
    env.add_row(
        "Python",
        f"[ephemeral.ok]{sys.version.split()[0]}[/ephemeral.ok]"
        if py_ok
        else f"[ephemeral.warn]{sys.version.split()[0]} (3.11+ recommended)[/ephemeral.warn]",
    )
    env.add_row("Platform", f"{platform.system()} {platform.release()}")

    critical = []
    for pkg in ("textual", "rich", "httpx", "pydantic", "pandas"):
        ok = module_available(pkg)
        env.add_row(
            f"import {pkg}",
            "[ephemeral.ok]ok[/ephemeral.ok]" if ok else "[ephemeral.err]missing[/ephemeral.err]",
        )
        if not ok:
            critical.append(pkg)

    ollama_bin = shutil.which("ollama")
    env.add_row(
        "ollama binary",
        f"[ephemeral.ok]{ollama_bin}[/ephemeral.ok]" if ollama_bin else "[ephemeral.dim]not in PATH[/ephemeral.dim]",
    )

    lean_bin = shutil.which("lean")
    env.add_row(
        "lean CLI",
        f"[ephemeral.ok]{lean_bin}[/ephemeral.ok]" if lean_bin else "[ephemeral.dim]not in PATH[/ephemeral.dim]",
    )

    node_bin = shutil.which("node")
    env.add_row(
        "node",
        f"[ephemeral.ok]{node_bin}[/ephemeral.ok]" if node_bin else "[ephemeral.dim]not in PATH[/ephemeral.dim]",
    )
    env.add_row(
        "ink UI deps",
        "[ephemeral.ok]ready[/ephemeral.ok]"
        if ink_dependencies_ready()
        else f"[ephemeral.warn]missing[/ephemeral.warn] ({install_hint()})",
    )

    console.print(env)
    console.print()

    keys = Table(title="API keys (presence only)", box=box.ROUNDED, border_style="ephemeral.muted")
    keys.add_column("Provider")
    keys.add_column("Key")
    key_rows = [
        ("Google", settings.google_api_key),
        ("OpenAI", settings.openai_api_key),
        ("Anthropic", settings.anthropic_api_key),
        ("Groq", settings.groq_api_key),
        ("xAI", settings.xai_api_key),
        ("Polygon", settings.polygon_api_key),
        ("Alpha Vantage", settings.alpha_vantage_api_key),
        ("Exa", settings.exa_api_key),
    ]
    for label, val in key_rows:
        keys.add_row(label, mask_secret(val))
    console.print(keys)

    try:
        from ephemeral.llm import get_router

        router = get_router(settings, force=True)
        backends = ", ".join(sorted(router.providers.keys())) or "none"
        console.print()
        console.print(
            Panel(
                f"[bold]LLM router[/bold] (backends with credentials / Ollama): {backends}",
                border_style="ephemeral.muted",
            )
        )
    except Exception as e:
        console.print(Panel(f"[ephemeral.warn]Could not inspect LLM router:[/ephemeral.warn] {e}", border_style="yellow"))

    console.print()
    if critical:
        console.print(
            Panel(
                f"[ephemeral.err]Missing packages:[/ephemeral.err] {', '.join(critical)}\n"
                "Install: [bold]pip install ephemeral-terminal[all][/bold]",
                border_style="red",
            )
        )
        return 1
    if not py_ok:
        return 1
    return 0


def print_status_dashboard(
    console: Console,
    settings: "Settings",
    *,
    detect_ollama,
    detect_lean_installation,
) -> None:
    """Richer than a plain table: status + services."""
    ollama_up, ollama_host = detect_ollama()
    lean_ok, lean_cli, lean_dir = detect_lean_installation()

    prov = settings.default_provider
    pval = prov.value if hasattr(prov, "value") else str(prov)

    top = Table.grid(padding=(0, 2))
    top.add_row(
        Text("Active provider", style="ephemeral.dim"),
        Text(pval, style="bold"),
    )
    top.add_row(
        Text("Default model", style="ephemeral.dim"),
        Text(settings.default_model, style="bold"),
    )
    top.add_row(
        Text("Ollama", style="ephemeral.dim"),
        Text(
            f"reachable at {ollama_host}" if ollama_up else "not reachable",
            style="ephemeral.ok" if ollama_up else "ephemeral.warn",
        ),
    )
    lean_detail = []
    if lean_cli:
        lean_detail.append(f"cli: {lean_cli}")
    if lean_dir:
        lean_detail.append(f"dir: {lean_dir}")
    lean_msg = " · ".join(lean_detail) if lean_detail else "lean CLI or project not found"
    top.add_row(
        Text("LEAN", style="ephemeral.dim"),
        Text(
            lean_msg,
            style="ephemeral.ok" if lean_ok else "ephemeral.dim",
        ),
    )

    console.print(
        Panel(
            top,
            title="[ephemeral.brand]Ephemeral status[/ephemeral.brand]",
            border_style="ephemeral.muted",
            box=box.ROUNDED,
        )
    )

    keys = Table(title="API keys", show_header=False, box=box.SIMPLE, padding=(0, 1))
    keys.add_column("Provider", style="bold")
    keys.add_column("Status")
    keys.add_row("Google", "[ephemeral.ok]set[/ephemeral.ok]" if settings.google_api_key else "[ephemeral.err]—[/ephemeral.err]")
    keys.add_row("OpenAI", "[ephemeral.ok]set[/ephemeral.ok]" if settings.openai_api_key else "[ephemeral.err]—[/ephemeral.err]")
    keys.add_row("Anthropic", "[ephemeral.ok]set[/ephemeral.ok]" if settings.anthropic_api_key else "[ephemeral.err]—[/ephemeral.err]")
    keys.add_row("Groq", "[ephemeral.ok]set[/ephemeral.ok]" if settings.groq_api_key else "[ephemeral.err]—[/ephemeral.err]")
    keys.add_row("xAI", "[ephemeral.ok]set[/ephemeral.ok]" if settings.xai_api_key else "[ephemeral.err]—[/ephemeral.err]")
    keys.add_row("Polygon", "[ephemeral.ok]set[/ephemeral.ok]" if settings.polygon_api_key else "[ephemeral.err]—[/ephemeral.err]")
    console.print(keys)


def format_tui_status_markdown(
    settings: "Settings",
    *,
    detect_ollama,
    detect_lean_installation,
) -> str:
    """Plain Markdown for the TUI slash /status command (no Rich console)."""
    ollama_up, ollama_host = detect_ollama()
    lean_ok, lean_cli, lean_dir = detect_lean_installation()

    prov = settings.default_provider
    pval = prov.value if hasattr(prov, "value") else str(prov)

    ollama_line = (
        f"reachable at `{ollama_host}`"
        if ollama_up
        else "**not reachable** — start `ollama serve`"
    )
    lean_bits = []
    if lean_cli:
        lean_bits.append(f"CLI `{lean_cli}`")
    if lean_dir:
        lean_bits.append(f"dir `{lean_dir}`")
    lean_line = " · ".join(lean_bits) if lean_bits else "not detected"

    lines = [
        "## Status",
        "",
        f"- **Provider:** `{pval}`",
        f"- **Default model:** `{settings.default_model}`",
        f"- **Ollama:** {ollama_line}",
        f"- **LEAN:** {lean_line}",
        "",
        "### API keys (set / not set)",
        "",
        "| Provider | Status |",
        "| --- | --- |",
    ]
    keys = [
        ("Google", settings.google_api_key),
        ("OpenAI", settings.openai_api_key),
        ("Anthropic", settings.anthropic_api_key),
        ("Groq", settings.groq_api_key),
        ("xAI", settings.xai_api_key),
        ("Polygon", getattr(settings, "polygon_api_key", None)),
        ("Alpha Vantage", getattr(settings, "alpha_vantage_api_key", None)),
        ("Exa", getattr(settings, "exa_api_key", None)),
    ]
    for label, val in keys:
        lines.append(f"| {label} | {'set' if val else '—'} |")
    lines.extend(
        [
            "",
            "*CLI:* `ephemeral --status` for the full Rich dashboard.",
        ]
    )
    return "\n".join(lines)


def print_help_footer(console: Console) -> None:
    console.print()
    console.print(
        Panel(
            Group(
                Rule("[ephemeral.dim]Keyboard · TUI[/ephemeral.dim]", style="ephemeral.muted"),
                Text("Ctrl+C  quit", style="ephemeral.dim"),
                Text("Ctrl+L  clear chat", style="ephemeral.dim"),
            ),
            border_style="ephemeral.muted",
            box=box.ROUNDED,
        )
    )
