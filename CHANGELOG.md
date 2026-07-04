# Changelog

All notable changes to Ephemeral are recorded here.

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
