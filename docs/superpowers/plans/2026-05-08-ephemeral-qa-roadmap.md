# Ephemeral QA Roadmap Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Move Ephemeral from a passing local v3.8 app to a more reliable product release by fixing configuration truth, stale QA artifacts, model metadata drift, and high-value workflow coverage.

**Architecture:** Keep the current Python CLI, bridge, and Ink UI boundaries. Focus first on correctness and user-visible trust: status must explain setup blockers, versions/model lists must have one source of truth, and tests must describe Ephemeral rather than old Sigma state.

**Tech Stack:** Python 3.11+, pydantic-settings, pytest, Ruff, TypeScript, React Ink, npm/tsc.

---

## Current QA Baseline

Verified on 2026-05-08 from `/Users/naitikgupta/Projects/ephemeral`:

- `uv run --extra dev pytest -q` -> `996 passed, 1 deselected`
- `npm --prefix ephemeral/ink_ui run typecheck` -> pass
- `npm --prefix ephemeral/ink_ui run smoke` -> pass
- `uv run ruff check .` -> pass
- `uv run python -m compileall ephemeral tests` -> pass
- `uv run ephemeral --version --no-ui` -> `ephemeral 3.8.0`
- `uv run ephemeral --status` -> provider `ollama`, model `qwen2.5:1.5b`, Ollama reachable, LEAN missing
- Ink bridge `status` -> `needs_setup: true`, `local_ready: false`, installed Ollama model list contains `gemma4:e4b`, active model unavailable
- Ink bridge `quote` for `AAPL` -> returns quote payload successfully

## Findings

1. Local status is confusing: the app can run, but `needs_setup` is true because the configured default model is not installed locally.
2. Version metadata is only partially centralized. Python uses `ephemeral/version.py`, but Ink and release scripts still hard-code `3.8.0`.
3. Test and verification output still says `SIGMA`, which weakens release confidence even though tests pass.
4. Model metadata is drift-prone. Available model IDs live in both `ephemeral/config.py` and `ephemeral/llm/registry.py`, and some registry entries do not match the available model list.
5. Bridge and CLI validation accepts arbitrary provider/model strings, then lets later status/routing fail indirectly.
6. The roadmap has some broad placeholder surfaces: generated validation payloads, template backtest code with TODO entry/exit logic, and app packaging placeholders.

## Task 1: Make Setup Status Actionable

**Files:**
- Modify: `ephemeral/ink_bridge.py`
- Modify: `ephemeral/cli_ui.py`
- Test: `tests/test_ink_bridge.py`
- Test: add or extend CLI status tests if an existing CLI status test exists

- [x] Add a status field that separates "keys missing", "local model missing", and "optional tools missing".
- [x] Update Ink status rendering to show the exact active local model and installed local model candidates.
- [x] Add a regression test where Ollama is reachable, the default model is absent, and `needs_setup` remains true with a useful reason.
- [x] Run `uv run --extra dev pytest tests/test_ink_bridge.py tests/test_setup_agent.py -q`.
- [x] Run `npm --prefix ephemeral/ink_ui run smoke`.

## Task 2: Centralize Release Version Across Python, Ink, and Scripts

**Files:**
- Modify: `ephemeral/version.py`
- Modify: `ephemeral/ink_ui/src/index.tsx`
- Modify: `scripts/build.sh`
- Modify: `scripts/create_app.py`
- Test: `tests/test_comprehensive.py`
- Test: add a small version consistency test for scripts and Ink source

- [x] Replace hard-coded Ink `APP_VERSION` with a value passed from the Python launcher or a checked-in generated JSON file.
- [x] Replace shell/script hard-coded versions with a read from `ephemeral/version.py` or a single release metadata file.
- [x] Add tests that fail if `3.8.0` is duplicated outside approved release metadata.
- [x] Run `uv run --extra dev pytest tests/test_comprehensive.py -q`.
- [x] Run `npm --prefix ephemeral/ink_ui run typecheck`.

## Task 3: Clean Up Stale Sigma QA Text

**Files:**
- Modify: `tests/test_comprehensive.py`
- Modify: `tests/verify_ui.py`
- Search: `rg -n "SIGMA|Sigma|sigma" tests ephemeral README.md CHANGELOG.md scripts`

- [x] Replace stale Sigma labels in executable test/verification output with Ephemeral.
- [x] Keep compatibility names only where they are intentionally testing legacy migration behavior.
- [x] Run `rg -n "SIGMA|Sigma|sigma" tests ephemeral README.md CHANGELOG.md scripts` and confirm remaining hits are intentional.
- [x] Run `uv run --extra dev pytest tests/test_comprehensive.py tests/verify_ui.py -q`.

## Task 4: Unify Model Catalog and Provider Routing

**Files:**
- Modify: `ephemeral/config.py`
- Modify: `ephemeral/llm/registry.py`
- Modify: `ephemeral/ink_bridge.py`
- Test: `tests/test_comprehensive.py`
- Test: add `tests/test_model_catalog.py`

- [x] Create one model catalog source that includes provider, model id, capabilities, context window, and display ordering.
- [x] Build `AVAILABLE_MODELS` and `REGISTRY` from that source.
- [x] Add tests that every available model resolves to the expected provider.
- [x] Add tests that deprecated or unsupported model IDs do not appear in the user-facing catalog.
- [x] Run `uv run --extra dev pytest tests/test_model_catalog.py tests/test_comprehensive.py -q`.

## Task 5: Validate Provider and Model Writes

**Files:**
- Modify: `ephemeral/config.py`
- Modify: `ephemeral/cli.py`
- Modify: `ephemeral/ink_bridge.py`
- Test: `tests/test_ink_bridge.py`
- Test: add CLI config tests if absent

- [x] Reject unknown providers in `save_setting` call paths before writing `~/.ephemeral/config.env`.
- [x] For cloud providers, warn or reject model IDs that do not map to the selected provider unless the user explicitly overrides.
- [x] For Ollama, allow arbitrary installed local models but show a clear warning if the selected model is not installed.
- [x] Add tests for invalid provider and mismatched model writes through both CLI and bridge paths.
- [x] Run `uv run --extra dev pytest tests/test_ink_bridge.py tests/test_comprehensive.py -q`.

## Task 6: Replace Placeholder Roadmap Surfaces With Explicit Product Choices

**Files:**
- Review: `ephemeral/validation/generated/payloads.py`
- Review: `ephemeral/tools/backtest.py`
- Review: `scripts/create_app.py`
- Modify only the files selected for the chosen scope

- [x] Decide whether generated validation payloads are real test fixtures or dead weight. If real, document generation and ownership. If not, remove them with tests adjusted.
- [x] Decide whether `ephemeral/tools/backtest.py` strategy template TODOs are meant for generated QuantConnect starter code. If yes, make the output text explicit that it is a starter template. If no, implement real entry/exit generation.
- [x] Replace packaging icon placeholders with a real asset or remove packaging claims from docs until supported.
- [x] Run `uv run --extra dev pytest -q`.
- [x] Run `uv run ruff check .`.

## Task 7: Add Product-Level Smoke Coverage

**Files:**
- Create or modify: `tests/test_cli_smoke.py`
- Modify: `ephemeral/ink_ui/package.json` only if adding a more deterministic UI smoke command

- [x] Add non-network CLI tests for `--version --no-ui`, `--list-models`, `tools`, invalid `--provider`, and invalid `--model` behavior.
- [x] Add bridge tests for `help`, `status`, `models`, `tools`, `set-provider`, `set-model`, and invalid payloads.
- [x] Keep network market-data tests either mocked or marked integration.
- [x] Run `uv run --extra dev pytest tests/test_cli_smoke.py tests/test_ink_bridge.py -q`.
- [x] Run full release gate: `uv run --extra dev pytest -q && npm --prefix ephemeral/ink_ui run typecheck && npm --prefix ephemeral/ink_ui run smoke && uv run ruff check .`.

## Recommended Order

1. Task 3, because it is low-risk and removes stale release noise.
2. Task 1, because current local setup status is the biggest user-facing confusion.
3. Task 5, because it prevents users from writing bad config state.
4. Task 4, because it removes model drift after validation rules are clear.
5. Task 2, because release metadata centralization touches multiple surfaces but is contained.
6. Task 7, because smoke coverage should lock the above in.
7. Task 6, because it needs product decisions before code churn.
