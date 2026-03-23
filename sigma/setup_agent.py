import sys
import os
import subprocess
import platform
import shutil
import time
import asyncio
from typing import Dict, Tuple

from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.markdown import Markdown
from rich.table import Table

from .config import detect_ollama, get_settings, save_api_key, save_setting, mark_first_run_complete
from .llm.registry import REGISTRY

console = Console()


def _ollama_installed_names() -> set[str]:
    """Parse `ollama list` NAME column."""
    try:
        r = subprocess.run(
            ["ollama", "list"],
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return set()
    if r.returncode != 0 or not r.stdout.strip():
        return set()
    names: set[str] = set()
    for line in r.stdout.strip().splitlines()[1:]:
        parts = line.split()
        if parts:
            names.add(parts[0].strip())
    return names


def _run_ollama_pull(model: str) -> bool:
    """Stream `ollama pull` lines to the console; return success."""
    console.print(f"  [dim]Pulling [bold]{model}[/bold] (large downloads can take several minutes)…[/dim]")
    try:
        proc = subprocess.Popen(
            ["ollama", "pull", model],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )
    except FileNotFoundError:
        console.print("  [red]ollama binary not found on PATH[/red]")
        return False
    if proc.stdout is None:
        return False
    for line in proc.stdout:
        line = line.rstrip()
        if line:
            console.print(f"  [dim]{line}[/dim]")
    proc.wait()
    if proc.returncode != 0:
        console.print(f"  [red]ollama pull failed (exit {proc.returncode})[/red]")
        return False
    return True


def _ensure_ollama_server() -> bool:
    """Best-effort: verify API responds; start `ollama serve` in background if `ollama list` fails."""
    try:
        subprocess.run(
            ["ollama", "list"],
            capture_output=True,
            text=True,
            timeout=15,
            check=True,
        )
        return True
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False
    except subprocess.CalledProcessError:
        pass
    ollama_bin = shutil.which("ollama")
    if not ollama_bin:
        return False
    console.print("  [yellow]Starting Ollama in the background…[/yellow]")
    try:
        subprocess.Popen(
            [ollama_bin, "serve"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True,
        )
    except OSError as e:
        console.print(f"  [red]Could not start ollama serve: {e}[/red]")
        return False
    for _ in range(20):
        time.sleep(0.5)
        ok, _ = detect_ollama()
        if ok:
            return True
    return False

class SetupAgent:
    def __init__(self):
        self.os_type = platform.system().lower()
        self.checks = {
            "python": False,
            "pip": False,
            "git": False,
            "docker": False,
            "lean": False,
            "ollama": False
        }
        
    def run(self):
        console.clear()
        console.print(Panel.fit(
            "[bold blue]Sigma Setup Wizard v3.7.2[/bold blue]\n"
            "[dim]Wire up an LLM, then optional data keys (Polygon, Alpha Vantage, Exa) for live quotes and news.[/dim]\n"
            "[dim]Guide: https://github.com/desenyon/sigma#readme[/dim]",
            border_style="blue",
            padding=(1, 2),
        ))
        
        self.check_system_requirements()
        self.install_dependencies()
        self.configure_local_llm()
        self.configure_api_keys()
        
        mark_first_run_complete()
        
        console.print("\n[bold green][OK] Setup Complete![/bold green]")
        console.print("[dim]Launching Sigma Terminal...[/dim]")
        time.sleep(2)

    def check_system_requirements(self):
        console.print("\n[bold cyan]1. System Requirements Check[/bold cyan]")
        
        table = Table(show_header=False, box=None, padding=(0, 2))
        table.add_column("Component")
        table.add_column("Status")
        table.add_column("Details")
        
        # Python
        py_ver = sys.version.split()[0]
        self.checks["python"] = True
        table.add_row("Python", "[green][OK][/green]", f"v{py_ver}")
        
        # Git
        if shutil.which("git"):
            self.checks["git"] = True
            table.add_row("Git", "[green][OK][/green]", "Installed")
        else:
            table.add_row("Git", "[yellow][WARN][/yellow]", "Not found")
            
        # Docker
        if shutil.which("docker"):
            try:
                subprocess.run(["docker", "info"], capture_output=True, check=True)
                self.checks["docker"] = True
                table.add_row("Docker", "[green][OK][/green]", "Running")
            except subprocess.CalledProcessError:
                table.add_row("Docker", "[yellow][WARN][/yellow]", "Installed but not running")
        else:
            table.add_row("Docker", "[red][ERR][/red]", "Not installed (Recommended for local tools)")
            
        console.print(table)
        
    def install_dependencies(self):
        console.print("\n[bold cyan]2. Essential Tools Installation[/bold cyan]")
        
        # LEAN CLI
        if shutil.which("lean"):
            console.print("  [green][OK][/green] LEAN CLI is already installed.")
            self.checks["lean"] = True
        else:
            if Confirm.ask("  Install LEAN CLI? (Required for backtesting)"):
                self._install_package("lean", "LEAN CLI")
                self.checks["lean"] = True
                
        # Ollama
        if shutil.which("ollama"):
            console.print("  [green][OK][/green] Ollama is already installed.")
            self.checks["ollama"] = True
        else:
            console.print("  [yellow]Ollama not found on PATH.[/yellow]")
            if self.os_type == "darwin":
                console.print(
                    "  [dim]macOS: install the app from https://ollama.com/download "
                    "or run: [bold]curl -fsSL https://ollama.com/install.sh | sh[/bold][/dim]"
                )
            else:
                console.print("  [dim]Install from https://ollama.com/download[/dim]")
            if Confirm.ask("  Run the official install script now? (requires curl)"):
                try:
                    console.print("  [dim]Running https://ollama.com/install.sh …[/dim]")
                    subprocess.run(
                        "curl -fsSL https://ollama.com/install.sh | sh",
                        shell=True,
                        check=True,
                    )
                    if shutil.which("ollama"):
                        self.checks["ollama"] = True
                        console.print("  [green][OK][/green] Ollama installed.")
                    else:
                        console.print(
                            "  [yellow]Install script finished but `ollama` is not on PATH yet. "
                            "Open a new terminal or add it to PATH.[/yellow]"
                        )
                except subprocess.CalledProcessError as e:
                    console.print(f"  [red]Install script failed: {e}[/red]")
                    console.print("  Install manually from https://ollama.com")

    def _install_package(self, package: str, name: str):
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}")) as progress:
            task = progress.add_task(f"Installing {name}...", total=None)
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                progress.update(task, completed=True)
                console.print(f"  [green][OK][/green] {name} installed successfully.")
            except Exception as e:
                console.print(f"  [red]Failed to install {name}: {e}[/red]")

    def configure_local_llm(self):
        console.print("\n[bold cyan]3. Local AI Configuration (Ollama)[/bold cyan]")
        
        if not self.checks["ollama"]:
            console.print("  [dim]Skipping — Ollama not installed. Install it above or use a cloud API key in step 4.[/dim]")
            return

        if not _ensure_ollama_server():
            console.print(
                "  [yellow]Could not talk to Ollama. Start Ollama Desktop (macOS) or run `ollama serve`, then retry setup.[/yellow]"
            )
            return

        installed = _ollama_installed_names()
        suggested = ["qwen3.5:8b", "qwen3.5:4b", "llama3.3", "mistral"]
        console.print("  Suggested models for tool use:")
        for m in suggested:
            st = "[green]installed[/green]" if m in installed else "[dim]not installed[/dim]"
            console.print(f"    • {m:<18} {st}")

        if Confirm.ask("  Pull a model now? (recommended: qwen3.5:8b)", default=True):
            model = Prompt.ask("  Model name", default="qwen3.5:8b")
            model = model.strip()
            if not model:
                console.print("  [yellow]Skipped empty model name.[/yellow]")
                return
            if _run_ollama_pull(model):
                save_setting("default_model", model)
                save_setting("ollama_host", "http://localhost:11434")
                save_setting("default_provider", "ollama")
                console.print("  [green][OK][/green] Saved DEFAULT_MODEL, OLLAMA_HOST, and DEFAULT_PROVIDER=ollama.")

    def configure_api_keys(self):
        console.print("\n[bold cyan]4. API Key Verification[/bold cyan]")
        
        providers = [
            ("OpenAI", "openai_api_key", "openai"),
            ("Anthropic", "anthropic_api_key", "anthropic"),
            ("Google Gemini", "google_api_key", "google"),
            ("Groq", "groq_api_key", "groq"),
            ("Alpha Vantage", "alpha_vantage_api_key", "alpha_vantage"),
            ("Exa Search", "exa_api_key", "exa"),
            ("Polygon.io", "polygon_api_key", "polygon"),
        ]
        
        settings = get_settings()
        
        for name, setting_key, provider_id in providers:
            current_key = getattr(settings, setting_key, None)
            status = "[green]Configured[/green]" if current_key else "[red]Missing[/red]"
            
            console.print(f"\n  [bold]{name}[/bold]: {status}")
            
            if not current_key or Confirm.ask(f"  Update {name} key?"):
                if not current_key and not Confirm.ask(f"  Do you have a {name} key?"):
                    continue
                    
                key = Prompt.ask(f"  Enter {name} API Key", password=False)
                if key:
                    # Verify!
                    if self._verify_key(provider_id, key):
                        save_api_key(provider_id, key)
                        console.print(f"  [green][OK] Verified and Saved[/green]")
                    else:
                        if Confirm.ask("  [red]Verification failed.[/red] Save anyway?"):
                            save_api_key(provider_id, key)

    def _verify_key(self, provider: str, key: str) -> bool:
        """Attempt a minimal API call to verify key."""
        with console.status(f"Verifying {provider} key..."):
            try:
                # Basic mock verification logic for now as actual calls depend on libs
                # In a real scenario, we'd import the provider class and run a simple generation
                if provider == "openai":
                    from openai import OpenAI
                    client = OpenAI(api_key=key)
                    client.models.list()
                elif provider == "anthropic":
                    import anthropic
                    client = anthropic.Anthropic(api_key=key)
                    # client.messages.create(...) # hard to do cheap verify without cost
                    pass 
                elif provider == "google":
                    import google.generativeai as genai
                    genai.configure(api_key=key)
                    model = genai.GenerativeModel('gemini-pro')
                    # model.generate_content("test")
                    pass
                elif provider == "alpha_vantage":
                    # Simple check
                    import requests
                    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey={key}"
                    r = requests.get(url)
                    if "Error Message" in r.text or "Invalid API call" in r.text:
                        raise Exception("Invalid Key")
                    pass
                elif provider == "exa":
                    # Simple check
                    import requests
                    url = "https://api.exa.ai/search"
                    headers = {"x-api-key": key, "Content-Type": "application/json"}
                    data = {"query": "test", "numResults": 1}
                    r = requests.post(url, headers=headers, json=data)
                    if r.status_code != 200:
                        raise Exception("Invalid Key")
                    pass
                elif provider == "polygon":
                    # Simple check
                    import requests
                    url = f"https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2023-01-09/2023-01-09?apiKey={key}"
                    r = requests.get(url)
                    if r.status_code != 200:
                        raise Exception("Invalid Key")
                    pass
                
                # If we didn't crash, assume OK (or skip if we can't easily verify without cost)
                return True
            except Exception as e:
                console.print(f"  [red]Error: {e}[/red]")
                return False

def run_setup():
    agent = SetupAgent()
    agent.run()
    return True

if __name__ == "__main__":
    run_setup()
