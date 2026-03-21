from __future__ import annotations

import re

import httpx
from rich.text import Text
from textual import work
from textual.events import Key
from textual.reactive import reactive
from textual.widgets import Input, Static

from sigma.config import get_settings, resolve_ollama_autocomplete_model
from sigma.core.engine import AutocompleteEngine


class SigmaLoader(Static):
    """Small status indicator (lives in the header — never beside the Input)."""

    frames = ["σ", "σ.", "σ..", "σ...", "σ..", "σ."]

    def on_mount(self) -> None:
        self.frame_index = 0
        self.update(Text("", end=""))
        self.set_interval(0.12, self.animate)

    def animate(self) -> None:
        if not self.has_class("active"):
            self.update(Text("", end=""))
            return
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.update(Text(self.frames[self.frame_index], style="bold #7aa2f7"))


class SigmaInput(Input):
    """
    Input with debounced Ollama-based ghost suggestions.
    Suggestions update the app label via watch_suggestion (same thread as Textual).
    """

    DEFAULT_CSS = """
    SigmaInput {
        border: none;
        height: 1;
        padding: 0;
        margin: 0;
        background: transparent;
        color: #e0e0e0;
    }
    SigmaInput:focus {
        border: none;
    }
    .ticker-highlight {
        color: #73daca;
        text-style: bold;
    }
    """

    BINDINGS = [
        ("tab", "accept_suggestion", "Accept suggestion"),
    ]

    suggestion = reactive("")

    def __init__(self, *args, **kwargs):
        # Compact mode is Textual's supported single-line Input (height 1, correct line rendering).
        kwargs.setdefault("compact", True)
        super().__init__(*args, **kwargs)
        self.debounce_timer = None
        self._slash_options: list[str] = []
        self._slash_index: int = 0

    def on_mount(self) -> None:
        self.border_title = None

    def action_accept_suggestion(self) -> None:
        if self._slash_options and self.value.strip().startswith("/"):
            pick = self._slash_options[self._slash_index]
            self.value = pick
            self.cursor_position = len(self.value)
            self._slash_options = []
            self._slash_index = 0
            self._sync_slash_panel()
            return
        if self.suggestion:
            self.value += self.suggestion
            self.suggestion = ""
            self.cursor_position = len(self.value)

    def on_key(self, event: Key) -> None:
        if not self.value.strip().startswith("/") or not self._slash_options:
            return
        if event.key == "down":
            event.stop()
            self._slash_index = (self._slash_index + 1) % len(self._slash_options)
            self._sync_slash_panel()
        elif event.key == "up":
            event.stop()
            self._slash_index = (self._slash_index - 1) % len(self._slash_options)
            self._sync_slash_panel()

    def _sync_slash_panel(self) -> None:
        try:
            panel = self.app.query_one("#slash-completions", Static)
        except Exception:
            return
        if not self.value.strip().startswith("/") or not self._slash_options:
            panel.styles.display = "none"
            panel.update("")
            return
        panel.styles.display = "block"
        t = Text()
        for i, opt in enumerate(self._slash_options[:12]):
            style = "bold #89b4fa" if i == self._slash_index else "#7f849c"
            prefix = "  "
            if i == self._slash_index:
                prefix = " ▸"
            t.append(f"{prefix} {opt}\n", style=style)
        t.append("Tab insert · Up/Down · ", style="dim #45475a")
        t.append("Enter", style="dim italic")
        t.append(" run", style="dim #45475a")
        panel.update(t)
        try:
            label = self.app.query_one("#suggestion-label")
            label.styles.display = "none"
        except Exception:
            pass

    def on_input_changed(self, event: Input.Changed) -> None:
        # Never let autocomplete / slash UI errors break typing (would leave Input unusable).
        try:
            self._on_input_changed_inner(event)
        except Exception:
            pass

    def _on_input_changed_inner(self, event: Input.Changed) -> None:
        self._check_tickers(event.value)

        if self.debounce_timer is not None:
            try:
                self.debounce_timer.stop()
            except (AttributeError, RuntimeError):
                pass
            self.debounce_timer = None

        v = event.value
        if v.strip().startswith("/"):
            self.suggestion = ""
            self._slash_options = AutocompleteEngine.get_suggestions(v.strip())
            self._slash_index = 0
            self._sync_slash_panel()
            return

        self._slash_options = []
        self._sync_slash_panel()

        if event.value.strip():
            self.debounce_timer = self.set_timer(0.45, self._fetch_suggestion)
        else:
            self.suggestion = ""

    def _check_tickers(self, value: str) -> None:
        ticker_pattern = r"\$[A-Z]{2,5}\b"
        matches = re.findall(ticker_pattern, value)
        if matches:
            pass

    def watch_suggestion(self, old: str, new: str) -> None:
        """Keep suggestion label in sync (must run on main Textual thread)."""
        try:
            label = self.app.query_one("#suggestion-label")
        except Exception:
            return
        if new:
            label.update(f"Suggestion: {new} (Tab)")
            label.styles.display = "block"
        else:
            label.styles.display = "none"

    @work(exclusive=True)
    async def _fetch_suggestion(self) -> None:
        if not self.value or len(self.value) < 3:
            return
        if self.value.lstrip().startswith("/"):
            self.suggestion = ""
            return

        settings = get_settings()
        model = resolve_ollama_autocomplete_model(settings)
        if not model:
            self.suggestion = ""
            return

        prompt = f"Complete this phrase in at most 6 words (no quotes): {self.value}"
        try:
            async with httpx.AsyncClient(timeout=4.0) as client:
                response = await client.post(
                    f"{settings.ollama_host.rstrip('/')}/api/generate",
                    json={
                        "model": model,
                        "prompt": prompt,
                        "stream": False,
                        "options": {"num_predict": 16, "temperature": 0.15, "stop": ["\n"]},
                    },
                )
            if response.status_code != 200:
                self.suggestion = ""
                return
            data = response.json()
            completion = (data.get("response") or "").strip()
            if not completion:
                self.suggestion = ""
                return
            lv = self.value.lower()
            cl = completion.lower()
            if cl.startswith(lv):
                self.suggestion = completion[len(self.value) :].lstrip()
            elif not cl.startswith(lv[:20]):
                self.suggestion = completion
            else:
                self.suggestion = ""
        except Exception:
            self.suggestion = ""


class TickerBadge(Static):
    """Shows detected tickers."""

    DEFAULT_CSS = """
    TickerBadge {
        background: #2b2d31;
        color: #73daca;
        padding: 0 1;
        margin: 0 1;
        display: none;
        height: 1;
    }
    TickerBadge.visible {
        display: block;
    }
    """

    def set_ticker(self, ticker: str) -> None:
        self.update(f"σ {ticker}")
        self.add_class("visible")

    def clear(self) -> None:
        self.remove_class("visible")
