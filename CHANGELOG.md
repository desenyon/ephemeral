# Changelog

All notable changes to Ephemeral are recorded here.

## 4.1.0

Released: 2026-07-25

### Providers and keys

- Added NVIDIA NIM as a provider (`nim`), an OpenAI-compatible endpoint alongside Groq and xAI, with bundled free-tier hosted models in the model catalog.
- BYOK key storage now prefers the OS keychain (macOS Keychain / Windows Credential Manager / Linux Secret Service via `keyring`), falling back to the existing plaintext `~/.ephemeral/config.env` when no keychain backend is available. Existing plaintext keys keep working; new/updated keys migrate to the keychain automatically.
- The setup wizard now covers every provider, including xAI (previously missing from the wizard) and NIM.

### Multi-harness backends

- Added an MCP server (`ephemeral/mcp_server.py`) exposing Ephemeral's full tool registry (quote, news, compare, chart, backtest, ...) over the Model Context Protocol, so external agent runtimes can call Ephemeral's real research tools instead of reimplementing them.
- Added a [Pi](https://pi.dev) coding-agent harness backend (`ephemeral/agents/pi_harness.py`) with a project-local MCP-client extension (`.pi/extensions/ephemeral-tools.ts`), letting a turn run through Pi's own agent loop with Ephemeral's tools wired in.
- Added an OpenAI Codex CLI backend (`ephemeral/agents/codex_agent.py`) for delegating turns to Codex's non-interactive `exec` mode.
- Added `/race`: fires one question at the native provider, Pi, and Codex simultaneously and shows all three answers side by side with timing and tool-call counts.

### Strategy authoring

- Added `/strategize` (and `ephemeral strategize "<description>"`): describe a strategy in English and the model writes it (`write_strategy`), backtests it (`run_custom_backtest`) against live data, and returns a performance/risk summary plus an equity-curve chart artifact — a full closed loop in one turn.
- Custom strategies are saved under `~/.ephemeral/custom_strategies/` and reuse the same simulation and metrics engine as the built-in strategies.

## 4.0.0

Released: 2026-07-04

### Major release

- Merged Research Desk (v3.9) with reliability and setup-trust improvements from the QA roadmap.
- Unified model catalog: single source of truth for provider routing, Ink model lists, and CLI validation.
- Actionable setup status separates missing keys, unavailable local models, and optional tool gaps.
- Provider and model writes are validated before persisting to `~/.ephemeral/config.env`.
- Release version is centralized: Python launcher passes `EPHEMERAL_VERSION` to Ink; build scripts read `version.py`.
- Closed 81 stale Palette bot PRs; absorbed focus-hierarchy UX into CommandDock and workspace chrome.

### UI

- Hide "Enter to run" and pane shortcuts when the command dock is not focused.
- Dim inactive workspace headers; fix activity rail focus highlighting.

## 3.9.0

Released: 2026-05-26

### UI

- Upgraded the default Ink shell into a terminal-native Research Desk with market chrome, watchlist rail, workspace pane, context rail, and command dock.
- Added workspace hydration so active symbols, watchlist quotes, setup issues, news, artifacts, and panel warnings can render from one bridge snapshot.
- Split the Ink frontend into focused modules for actions, bridge access, formatting, hooks, keyboard handling, and Research Desk components.

### Bridge

- Added a `workspace` bridge action for partial, failure-tolerant Research Desk snapshots.

## 3.8.0

Released: 2026-04-09

### UI

- Rebuilt the Ink shell around a cleaner workspace, navigator sidebar, and prompt dock.
- Fixed inconsistent prompt focus and cursor behavior so typing always returns to the input surface.
- Added direct action switching from the empty composer so the shell feels live before any request runs.
- Reduced layout bloat and raised the stacked-layout fallback threshold to keep content inside the frame on smaller terminals.
- Improved rendered output formatting for status, help, ask/tool responses, and operational views.

### Setup and routing

- Optimized the Ink bridge so lightweight actions do not eagerly import heavy workflow modules.
- Replaced per-request bridge spawning with a persistent worker and cached status surfaces for dramatically faster warm interactions.
- Added richer Ollama status details, including installed-model visibility and active-model availability.
- Updated setup to reuse already-installed Ollama models instead of assuming a fresh pull is required.
- Persisted `OLLAMA_MODEL` alongside the default provider and model to keep runtime routing aligned.

### Release hygiene

- Centralized version metadata in `ephemeral/version.py`.
- Bumped package, script, and verification references to `3.8.0`.
- Replaced the PyPI release publish path with a GitHub-hosted one-line installer script.
- Rewrote the README around the new `3.8.0` product story and command surface.
- Added setup regression tests in `tests/test_setup_agent.py`.
