# Ephemeral v4.0.0 Major Release Plan

> Generated from graphify analysis + QA roadmap + Research Desk plan on 2026-07-04.

**Goal:** Ship a coherent **v4.0.0** major release that merges origin's Research Desk (v3.9.0) with local QA/reliability work, closes 81 stale Palette bot PRs, and establishes a clean release baseline.

**Architecture:** Keep CLI → Ink bridge → Python backend boundaries. v4.0 is a product release, not a rewrite: Research Desk UI + unified model catalog + actionable setup status + release hygiene.

---

## Graphify Insights (what the codebase actually is)

| Layer | God nodes | Implication |
|-------|-----------|-------------|
| Core runtime | `LLMProvider`, `LLMRouter`, `Engine`, `IntentParser` | LLM routing is the spine — model catalog must be single-source-of-truth |
| Config | `Settings`, `ErrorCode`, `EphemeralError` | Setup/status clarity is high-leverage UX |
| Product | Research Desk layout, Ink bridge, workspace snapshots | v4.0 headline = terminal research desk, not palette tweaks |
| Noise | 398 communities, many generated validation payloads | Trim or document generated fixtures in a follow-up |

**Surprising bridge:** Design doc `Terminal Research Desk Layout` ↔ demo screenshot ↔ README Ink shell — product story is aligned; implementation lagged on `main` until v3.9 on origin.

---

## Phase 0 — Repo hygiene (this session)

- [x] Run graphify on corpus (108 files, 3877 nodes)
- [x] Close 81 stale Palette/Jules UX PRs (none fix runtime errors; tests already pass)
- [x] Fast-forward/merge `origin/main` (v3.9.0 Research Desk) into working tree
- [x] Reconcile local QA changes (model catalog, ink_bridge status, cli validation) on top

## Phase 1 — Merge & reconcile (v3.9 + local QA)

**Files in conflict risk:** `ink_bridge.py`, `config.py`, `ink_ui/src/index.tsx`, `cli.py`

- [x] Pull `origin/main` and resolve conflicts favoring: Research Desk UI structure + local model_catalog/status improvements
- [x] Ensure `ephemeral/research/workspace.py` and Ink component modules exist
- [x] Re-run full gate: `pytest -q`, `npm --prefix ephemeral/ink_ui run typecheck`, `ruff check .`

## Phase 2 — v4.0.0 version bump & release metadata

- [x] Bump `ephemeral/version.py` → `4.0.0`
- [x] Propagate version via launcher JSON / build scripts (no hard-coded duplicates)
- [x] Update `CHANGELOG.md` with v4.0.0 section (Research Desk + QA reliability)
- [x] Update `README.md` for v4.0 product story
- [x] Tag `v4.0.0` when user requests commit/push

## Phase 3 — Research Desk polish (from plan)

- [x] Hide "Enter to run" and pane shortcuts when the command dock is not focused
- [x] Dim inactive workspace headers; fix activity rail focus highlighting
- [x] Ctrl+R and periodic workspace refresh (90s)
- [x] Right rail focus border highlight

## Phase 4 — Reliability hardening (QA roadmap remainder)

- [x] Model catalog single source (`model_catalog.py`)
- [x] Provider/model validation on write paths
- [x] Actionable setup status (keys vs model vs optional tools)
- [x] CLI smoke tests (`test_cli_smoke.py`)
- [x] Document generated validation payload surface (`validation/generated/README.md`)
- [x] Integration test: workspace snapshot without network (`tests/test_ink_bridge.py`)

## Phase 5 — Release gate

```bash
uv run --extra dev pytest -q
npm --prefix ephemeral/ink_ui run typecheck
npm --prefix ephemeral/ink_ui run smoke
uv run ruff check .
uv run ephemeral --version --no-ui  # → 4.0.0
```

---

## Iteration loop

After each task: run affected tests → fix → next checkbox. No new Palette PRs — all UX goes into one v4.0 branch.

## Out of scope for v4.0

- Neo4j/graphify MCP integration
- New LLM providers beyond catalog
- macOS app packaging (placeholder cleanup only)
