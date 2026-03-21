"""Rich presentation layer for the Sigma CLI — layout, themes, and diagnostics."""

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
    from sigma.config import Settings

SIGMA_THEME = Theme(
    {
        "sigma.brand": "bold #7aa2f7",
        "sigma.dim": "dim #565f89",
        "sigma.ok": "bold #9ece6a",
        "sigma.warn": "bold #e0af68",
        "sigma.err": "bold #f7768e",
        "sigma.accent": "bold #bb9af7",
        "sigma.muted": "#414868",
    }
)


def make_console() -> Console:
    return Console(theme=SIGMA_THEME, highlight=True, soft_wrap=True)


def sigma_logo_text(version: str) -> Text:
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
    t.append("σ", style="bold cyan")
    t.append("  Finance Research Agent", style="bold")
    return t


def print_banner(console: Console, version: str) -> None:
    console.print()
    console.print(Align.center(sigma_logo_text(version)))
    console.print()


def print_quick_start(console: Console) -> None:
    # Table header_style must use concrete styles — custom theme names are not resolved here (Rich 13+).
    grid = Table(
        title="[sigma.brand]Command palette[/sigma.brand]",
        box=box.ROUNDED,
        border_style="sigma.muted",
        show_header=True,
        header_style="bold #bb9af7",
        padding=(0, 1),
    )
    grid.add_column("Command", style="cyan", no_wrap=True)
    grid.add_column("What it does")
    rows = [
        ("sigma", "Launch the full-screen TUI"),
        ('sigma ask "…"', "One-shot LLM query with tools"),
        ("sigma quote AAPL MSFT", "Live-style quotes table"),
        ("sigma chart SPY --period 1y", "Export chart to ~/.sigma/charts"),
        ("sigma backtest AAPL -s sma_crossover", "Run a strategy backtest"),
        ("sigma compare AAPL MSFT GOOGL", "Side-by-side metrics"),
        ("sigma doctor", "Environment health check"),
        ("sigma --status", "Keys and provider (masked)"),
        ("sigma --setup", "Interactive setup wizard"),
    ]
    for cmd, desc in rows:
        grid.add_row(cmd, desc)
    console.print(Panel(grid, border_style="sigma.muted", box=box.DOUBLE))


def mask_secret(value: Optional[str], visible: int = 4) -> str:
    if not value:
        return "[sigma.err]—[/sigma.err]"
    if len(value) <= visible * 2:
        return "[sigma.ok]••••[/sigma.ok]"
    return f"[sigma.ok]{value[:visible]}…{value[-visible:]}[/sigma.ok]"


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
    console.print(Rule("[sigma.brand]Sigma doctor[/sigma.brand]", style="sigma.muted"))

    env = Table(box=box.SIMPLE, show_header=False, padding=(0, 2))
    env.add_column("Check", style="bold")
    env.add_column("Result")

    py_ok = sys.version_info >= (3, 11)
    env.add_row(
        "Python",
        f"[sigma.ok]{sys.version.split()[0]}[/sigma.ok]"
        if py_ok
        else f"[sigma.warn]{sys.version.split()[0]} (3.11+ recommended)[/sigma.warn]",
    )
    env.add_row("Platform", f"{platform.system()} {platform.release()}")

    critical = []
    for pkg in ("textual", "rich", "httpx", "pydantic", "pandas"):
        ok = module_available(pkg)
        env.add_row(
            f"import {pkg}",
            f"[sigma.ok]ok[/sigma.ok]" if ok else f"[sigma.err]missing[/sigma.err]",
        )
        if not ok:
            critical.append(pkg)

    ollama_bin = shutil.which("ollama")
    env.add_row(
        "ollama binary",
        f"[sigma.ok]{ollama_bin}[/sigma.ok]" if ollama_bin else "[sigma.dim]not in PATH[/sigma.dim]",
    )

    lean_bin = shutil.which("lean")
    env.add_row(
        "lean CLI",
        f"[sigma.ok]{lean_bin}[/sigma.ok]" if lean_bin else "[sigma.dim]not in PATH[/sigma.dim]",
    )

    console.print(env)
    console.print()

    keys = Table(title="API keys (presence only)", box=box.ROUNDED, border_style="sigma.muted")
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

    console.print()
    if critical:
        console.print(
            Panel(
                f"[sigma.err]Missing packages:[/sigma.err] {', '.join(critical)}\n"
                "Install: [bold]pip install sigma-terminal[all][/bold]",
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
        Text("Active provider", style="sigma.dim"),
        Text(pval, style="bold"),
    )
    top.add_row(
        Text("Default model", style="sigma.dim"),
        Text(settings.default_model, style="bold"),
    )
    top.add_row(
        Text("Ollama", style="sigma.dim"),
        Text(
            f"reachable at {ollama_host}" if ollama_up else "not reachable",
            style="sigma.ok" if ollama_up else "sigma.warn",
        ),
    )
    lean_detail = []
    if lean_cli:
        lean_detail.append(f"cli: {lean_cli}")
    if lean_dir:
        lean_detail.append(f"dir: {lean_dir}")
    lean_msg = " · ".join(lean_detail) if lean_detail else "lean CLI or project not found"
    top.add_row(
        Text("LEAN", style="sigma.dim"),
        Text(
            lean_msg,
            style="sigma.ok" if lean_ok else "sigma.dim",
        ),
    )

    console.print(
        Panel(
            top,
            title="[sigma.brand]Sigma status[/sigma.brand]",
            border_style="sigma.muted",
            box=box.ROUNDED,
        )
    )

    keys = Table(title="API keys", show_header=False, box=box.SIMPLE, padding=(0, 1))
    keys.add_column("Provider", style="bold")
    keys.add_column("Status")
    keys.add_row("Google", "[sigma.ok]set[/sigma.ok]" if settings.google_api_key else "[sigma.err]—[/sigma.err]")
    keys.add_row("OpenAI", "[sigma.ok]set[/sigma.ok]" if settings.openai_api_key else "[sigma.err]—[/sigma.err]")
    keys.add_row("Anthropic", "[sigma.ok]set[/sigma.ok]" if settings.anthropic_api_key else "[sigma.err]—[/sigma.err]")
    keys.add_row("Groq", "[sigma.ok]set[/sigma.ok]" if settings.groq_api_key else "[sigma.err]—[/sigma.err]")
    keys.add_row("xAI", "[sigma.ok]set[/sigma.ok]" if settings.xai_api_key else "[sigma.err]—[/sigma.err]")
    keys.add_row("Polygon", "[sigma.ok]set[/sigma.ok]" if settings.polygon_api_key else "[sigma.err]—[/sigma.err]")
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
            "*CLI:* `sigma --status` for the full Rich dashboard.",
        ]
    )
    return "\n".join(lines)


def print_help_footer(console: Console) -> None:
    console.print()
    console.print(
        Panel(
            Group(
                Rule("[sigma.dim]Keyboard · TUI[/sigma.dim]", style="sigma.muted"),
                Text("Ctrl+C  quit", style="sigma.dim"),
                Text("Ctrl+L  clear chat", style="sigma.dim"),
            ),
            border_style="sigma.muted",
            box=box.ROUNDED,
        )
    )
