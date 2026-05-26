# Ephemeral Research Desk Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn Ephemeral's default Ink shell into a dense terminal-native Research Desk backed by real workspace snapshots.

**Architecture:** Keep the existing CLI launcher, Ink app, persistent Python bridge, and backend services. First add a backend `workspace` read model, then split the large Ink file into focused modules, then replace the current command-launcher layout with a professional research-desk layout that hydrates panels from bridge data.

**Tech Stack:** Python 3.11+, pytest, TypeScript, React 19, Ink 6, npm/tsc.

---

## File Structure

- Create: `ephemeral/research/workspace.py`
  - Pure backend builders for workspace snapshots, watchlist rows, artifact summaries, setup issue forwarding, and panel warnings.
- Modify: `ephemeral/ink_bridge.py`
  - Add `_workspace_payload()` and route `action == "workspace"` through the bridge server.
- Modify: `tests/test_ink_bridge.py`
  - Add non-network tests for workspace snapshots and bridge routing.
- Create: `ephemeral/ink_ui/src/types.ts`
  - Shared TypeScript types currently embedded in `index.tsx`.
- Create: `ephemeral/ink_ui/src/actions.ts`
  - Action definitions, slash command parsing, and action-to-bridge request mapping.
- Create: `ephemeral/ink_ui/src/bridge.ts`
  - Persistent Python bridge client.
- Create: `ephemeral/ink_ui/src/formatters.tsx`
  - Summary and detail rendering for bridge envelopes.
- Create: `ephemeral/ink_ui/src/hooks/useTerminalSize.ts`
  - Terminal resize hook.
- Create: `ephemeral/ink_ui/src/hooks/useRawMode.ts`
  - Ink raw-mode hook.
- Create: `ephemeral/ink_ui/src/components/KeyboardController.tsx`
  - Keyboard input controller.
- Create: `ephemeral/ink_ui/src/components/ResearchDesk.tsx`
  - Main shell layout composition.
- Create: `ephemeral/ink_ui/src/components/Chrome.tsx`
  - Top status chrome.
- Create: `ephemeral/ink_ui/src/components/LeftRail.tsx`
  - Watchlist, action groups, and activity.
- Create: `ephemeral/ink_ui/src/components/Workspace.tsx`
  - Center pane for selected output and tabs.
- Create: `ephemeral/ink_ui/src/components/RightRail.tsx`
  - Context cards for quote, setup issues, news, and artifacts.
- Create: `ephemeral/ink_ui/src/components/CommandDock.tsx`
  - Bottom prompt and shortcut hints.
- Modify: `ephemeral/ink_ui/src/index.tsx`
  - Reduce to the render entrypoint.
- Modify: `README.md`
  - Update the Ink shell section after implementation is verified.

---

### Task 1: Add Workspace Snapshot Backend

**Files:**
- Create: `ephemeral/research/workspace.py`
- Test: `tests/test_ink_bridge.py`

- [ ] **Step 1: Write failing workspace snapshot tests**

Add these tests to `tests/test_ink_bridge.py`:

```python
def test_workspace_payload_returns_partial_snapshot_without_network() -> None:
    with (
        patch("ephemeral.research.workspace.build_status", return_value={"provider": "ollama", "model": "qwen2.5:1.5b", "setup_issues": []}),
        patch("ephemeral.research.workspace.MarketDataService") as service_cls,
    ):
        service = service_cls.return_value
        service.get_quote.side_effect = RuntimeError("network unavailable")
        service.get_news_yf.side_effect = RuntimeError("network unavailable")

        from ephemeral.research.workspace import build_workspace_snapshot

        payload = build_workspace_snapshot({"symbol": "AAPL", "watchlist": ["SPY", "QQQ"]})

    assert payload["active_symbol"] == "AAPL"
    assert payload["status"]["provider"] == "ollama"
    assert payload["quote"]["symbol"] == "AAPL"
    assert payload["quote"]["state"] == "error"
    assert payload["watchlist"][0]["symbol"] == "SPY"
    assert payload["panel_warnings"]


def test_workspace_payload_defaults_to_spy() -> None:
    with (
        patch("ephemeral.research.workspace.build_status", return_value={"setup_issues": []}),
        patch("ephemeral.research.workspace.MarketDataService") as service_cls,
    ):
        service = service_cls.return_value
        service.get_quote.return_value = {"symbol": "SPY", "price": 500.0, "change_percent": 0.2}
        service.get_news_yf.return_value = []

        from ephemeral.research.workspace import build_workspace_snapshot

        payload = build_workspace_snapshot({})

    assert payload["active_symbol"] == "SPY"
    assert payload["quote"]["price"] == 500.0
```

- [ ] **Step 2: Run tests to verify failure**

Run:

```bash
uv run --extra dev pytest tests/test_ink_bridge.py::test_workspace_payload_returns_partial_snapshot_without_network tests/test_ink_bridge.py::test_workspace_payload_defaults_to_spy -q
```

Expected: FAIL with `ModuleNotFoundError: No module named 'ephemeral.research.workspace'`.

- [ ] **Step 3: Implement workspace snapshot builder**

Create `ephemeral/research/workspace.py`:

```python
"""Workspace read models for the Ink Research Desk."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List

from ephemeral.services.market_data import MarketDataService

DEFAULT_WATCHLIST = ["SPY", "QQQ", "DIA", "IWM"]


def _clean_symbol(value: Any) -> str:
    raw = str(value or "").strip().upper()
    return raw if raw.isalnum() and 1 <= len(raw) <= 12 else ""


def _symbols(values: Iterable[Any]) -> List[str]:
    out: List[str] = []
    for value in values:
        symbol = _clean_symbol(value)
        if symbol and symbol not in out:
            out.append(symbol)
    return out


def _safe_quote(service: MarketDataService, symbol: str, warnings: List[str]) -> Dict[str, Any]:
    try:
        quote = dict(service.get_quote(symbol))
        quote.setdefault("symbol", symbol)
        quote["state"] = "ok"
        return quote
    except Exception as exc:
        warnings.append(f"quote:{symbol}:{exc}")
        return {"symbol": symbol, "state": "error", "error": str(exc)}


def _safe_news(service: MarketDataService, symbol: str, warnings: List[str]) -> List[Dict[str, Any]]:
    try:
        return service.get_news_yf(symbol, limit=8)
    except Exception as exc:
        warnings.append(f"news:{symbol}:{exc}")
        return []


def _artifact_rows(root: Path | None = None, *, limit: int = 6) -> List[Dict[str, str]]:
    base = root or Path.home() / ".ephemeral" / "artifacts"
    if not base.exists():
        return []
    rows: List[Dict[str, str]] = []
    for path in sorted(base.iterdir(), key=lambda item: item.stat().st_mtime, reverse=True)[:limit]:
        rows.append({"name": path.name, "path": str(path)})
    return rows


def build_workspace_snapshot(
    payload: Dict[str, Any],
    *,
    build_status: Callable[[], Dict[str, Any]] | None = None,
    service: MarketDataService | None = None,
) -> Dict[str, Any]:
    warnings: List[str] = []
    status = build_status() if build_status else {}
    market_data = service or MarketDataService()
    requested = _clean_symbol(payload.get("symbol") or payload.get("active_symbol"))
    requested_watchlist = _symbols(payload.get("watchlist") or [])
    watchlist = requested_watchlist or DEFAULT_WATCHLIST
    active_symbol = requested or watchlist[0]

    return {
        "active_symbol": active_symbol,
        "status": status,
        "watchlist": [_safe_quote(market_data, symbol, warnings) for symbol in watchlist[:8]],
        "quote": _safe_quote(market_data, active_symbol, warnings),
        "news": _safe_news(market_data, active_symbol, warnings),
        "artifacts": _artifact_rows(),
        "setup_issues": status.get("setup_issues", []),
        "panel_warnings": warnings,
    }
```

- [ ] **Step 4: Run tests to verify pass**

Run:

```bash
uv run --extra dev pytest tests/test_ink_bridge.py::test_workspace_payload_returns_partial_snapshot_without_network tests/test_ink_bridge.py::test_workspace_payload_defaults_to_spy -q
```

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add ephemeral/research/workspace.py tests/test_ink_bridge.py
git commit -m "feat: add research desk workspace snapshot"
```

---

### Task 2: Route Workspace Through The Bridge

**Files:**
- Modify: `ephemeral/ink_bridge.py`
- Test: `tests/test_ink_bridge.py`

- [ ] **Step 1: Write failing bridge route test**

Add this test to `tests/test_ink_bridge.py`:

```python
def test_handle_request_routes_workspace_payload() -> None:
    with patch(
        "ephemeral.ink_bridge.build_workspace_snapshot",
        return_value={"active_symbol": "AAPL", "watchlist": [], "panel_warnings": []},
    ) as builder:
        result = asyncio.run(ink_bridge.handle_request({"action": "workspace", "symbol": "AAPL"}))

    assert result["ok"] is True
    assert result["action"] == "workspace"
    assert result["data"]["active_symbol"] == "AAPL"
    builder.assert_called_once()
```

- [ ] **Step 2: Run test to verify failure**

Run:

```bash
uv run --extra dev pytest tests/test_ink_bridge.py::test_handle_request_routes_workspace_payload -q
```

Expected: FAIL because `build_workspace_snapshot` is not imported or `workspace` is unknown.

- [ ] **Step 3: Implement bridge route**

In `ephemeral/ink_bridge.py`, add the import near the other project imports:

```python
from ephemeral.research.workspace import build_workspace_snapshot
```

Add this helper near the other payload helpers:

```python
def _workspace_payload(payload: Dict[str, Any]) -> Dict[str, Any]:
    return build_workspace_snapshot(payload, build_status=_status_payload)
```

Add this branch inside `handle_request` before `status`:

```python
    elif action == "workspace":
        data = _workspace_payload(payload)
```

- [ ] **Step 4: Run focused bridge tests**

Run:

```bash
uv run --extra dev pytest tests/test_ink_bridge.py -q
```

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add ephemeral/ink_bridge.py tests/test_ink_bridge.py
git commit -m "feat: expose research workspace bridge action"
```

---

### Task 3: Extract Current Ink Shell Without Visual Changes

**Files:**
- Create: `ephemeral/ink_ui/src/types.ts`
- Create: `ephemeral/ink_ui/src/actions.ts`
- Create: `ephemeral/ink_ui/src/bridge.ts`
- Create: `ephemeral/ink_ui/src/formatters.tsx`
- Create: `ephemeral/ink_ui/src/hooks/useTerminalSize.ts`
- Create: `ephemeral/ink_ui/src/hooks/useRawMode.ts`
- Create: `ephemeral/ink_ui/src/components/KeyboardController.tsx`
- Modify: `ephemeral/ink_ui/src/index.tsx`

- [ ] **Step 1: Extract types**

Move the existing type definitions from `index.tsx` into `types.ts`. Include the new workspace type:

```ts
export type ActionId =
	| 'help'
	| 'shortcuts'
	| 'keys'
	| 'ask'
	| 'quote'
	| 'news'
	| 'compare'
	| 'chart'
	| 'backtest'
	| 'portfolio'
	| 'strategy'
	| 'report'
	| 'alert'
	| 'status'
	| 'doctor'
	| 'models'
	| 'tools'
	| 'reload'
	| 'setup-help'
	| 'set-provider'
	| 'set-model'
	| 'set-key'
	| 'export'
	| 'legacy-ui';

export type FocusPane = 'left' | 'workspace' | 'right' | 'input';
export type DetailMode = 'rendered' | 'raw';
export type LayoutMode = 'desktop' | 'compact';

export type BridgeRequest = {
	action: ActionId | 'workspace';
	[key: string]: unknown;
};

export type BridgeEnvelope = {
	ok: boolean;
	id?: string;
	action?: string;
	data?: any;
	error?: string;
};

export type HistoryEntry = {
	id: string;
	label: string;
	input: string;
	body: string;
	result?: BridgeEnvelope;
	error?: string;
	createdAt: string;
};

export type ActionDefinition = {
	id: ActionId;
	label: string;
	description: string;
	hint: string;
	promptPlaceholder?: string;
	group: 'Research' | 'Build' | 'Ops';
};

export type WorkspaceSnapshot = {
	active_symbol: string;
	status: any;
	watchlist: any[];
	quote: any;
	news: any[];
	artifacts: any[];
	setup_issues: any[];
	panel_warnings: string[];
};
```

- [ ] **Step 2: Extract action definitions and request parsing**

Create `actions.ts` by mechanically moving the current `actions`, `parseSlashCommand`, and `requestForAction` declarations from `index.tsx`.

At the top of `actions.ts`, add:

```ts
import type {ActionDefinition, BridgeRequest} from './types.js';
```

Then paste the exact current declarations below that import and change `const` to `export const` for all three declarations. After extraction, `index.tsx` and later `app.tsx` must import `actions`, `parseSlashCommand`, and `requestForAction` from `./actions.js`. Command behavior must stay identical in this task.

- [ ] **Step 3: Extract bridge client**

Move `PersistentBridgeClient`, `getBridgeClient`, and `invokeBridge` into `bridge.ts`. Keep the current `pythonExecutable` and `projectRoot` calculation in this module:

```ts
import {spawn} from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import process from 'node:process';
import {fileURLToPath} from 'node:url';
import type {BridgeEnvelope, BridgeRequest} from './types.js';

export const sourceDir = path.dirname(fileURLToPath(import.meta.url));
export const defaultProjectRoot = path.resolve(sourceDir, '..', '..', '..');
export const bundledPython = path.resolve(defaultProjectRoot, '.venv', process.platform === 'win32' ? path.join('Scripts', 'python.exe') : path.join('bin', 'python'));
export const pythonExecutable = process.env.EPHEMERAL_PYTHON_EXECUTABLE ?? (fs.existsSync(bundledPython) ? bundledPython : 'python3');
export const projectRoot = process.env.EPHEMERAL_PROJECT_ROOT ?? defaultProjectRoot;
```

Below those constants, move the exact current `PendingBridgeRequest` type, `PersistentBridgeClient` class, `bridgeClient`, `bridgeCleanupRegistered`, `getBridgeClient`, and `invokeBridge` declarations from `index.tsx`. Export `invokeBridge`.

- [ ] **Step 4: Extract hooks and keyboard controller**

Move the existing `useTerminalSize` hook to `hooks/useTerminalSize.ts` and the existing `useRawMode` hook to `hooks/useRawMode.ts`. Move `InteractiveKeyboardController` to `components/KeyboardController.tsx`.

Keep the behavior identical except for renaming focus panes from `actions/history/output/input` to `left/workspace/right/input`.

- [ ] **Step 5: Extract formatters**

Move `truncate`, `previewValue`, `titleCase`, `formatStructuredBlock`, `summarizeEnvelope`, `detailBodyForEntry`, `wrapText`, and `viewportLines` into `formatters.tsx`.

- [ ] **Step 6: Reduce `index.tsx` to app entrypoint**

Leave `index.tsx` as:

```tsx
import React from 'react';
import {render} from 'ink';
import {App} from './app.js';

render(<App />);
```

Move the current top-level component into `app.tsx` with imports from the extracted modules.

- [ ] **Step 7: Verify no behavior regression**

Run:

```bash
npm --prefix ephemeral/ink_ui run typecheck
npm --prefix ephemeral/ink_ui run smoke
```

Expected: both pass.

- [ ] **Step 8: Commit**

```bash
git add ephemeral/ink_ui/src
git commit -m "refactor: split ink shell into focused modules"
```

---

### Task 4: Add Research Desk State And Workspace Hydration

**Files:**
- Modify: `ephemeral/ink_ui/src/app.tsx`
- Modify: `ephemeral/ink_ui/src/types.ts`
- Modify: `ephemeral/ink_ui/src/actions.ts`

- [ ] **Step 1: Add desk state types**

In `types.ts`, add:

```ts
export type DeskState = {
	activeSymbol: string;
	watchlist: string[];
	workspace: WorkspaceSnapshot | null;
	workspaceLoading: boolean;
	workspaceError: string | null;
};
```

- [ ] **Step 2: Hydrate workspace on startup**

In `app.tsx`, add state:

```ts
const [desk, setDesk] = useState<DeskState>({
	activeSymbol: 'SPY',
	watchlist: ['SPY', 'QQQ', 'DIA', 'IWM'],
	workspace: null,
	workspaceLoading: true,
	workspaceError: null,
});
```

Add a helper:

```ts
const refreshWorkspace = async (nextSymbol = desk.activeSymbol, nextWatchlist = desk.watchlist) => {
	setDesk(previous => ({...previous, workspaceLoading: true, workspaceError: null}));
	try {
		const result = await invokeBridge({action: 'workspace', symbol: nextSymbol, watchlist: nextWatchlist});
		setDesk(previous => ({
			...previous,
			activeSymbol: result.data?.active_symbol ?? nextSymbol,
			workspace: result.data,
			workspaceLoading: false,
		}));
	} catch (error) {
		setDesk(previous => ({
			...previous,
			workspaceLoading: false,
			workspaceError: error instanceof Error ? error.message : String(error),
		}));
	}
};
```

Call it from the startup `useEffect`.

- [ ] **Step 3: Update active symbol after market actions**

After a successful bridge request, derive a symbol:

```ts
const symbolFromResult = result.data?.symbol ?? result.data?.quote?.symbol ?? result.data?.quotes?.[0]?.symbol ?? result.data?.active_symbol;
if (typeof symbolFromResult === 'string' && symbolFromResult.trim()) {
	const nextSymbol = symbolFromResult.trim().toUpperCase();
	setDesk(previous => ({
		...previous,
		activeSymbol: nextSymbol,
		watchlist: previous.watchlist.includes(nextSymbol) ? previous.watchlist : [nextSymbol, ...previous.watchlist].slice(0, 8),
	}));
	void refreshWorkspace(nextSymbol);
}
```

- [ ] **Step 4: Verify**

Run:

```bash
npm --prefix ephemeral/ink_ui run typecheck
npm --prefix ephemeral/ink_ui run smoke
```

Expected: both pass.

- [ ] **Step 5: Commit**

```bash
git add ephemeral/ink_ui/src
git commit -m "feat: hydrate ink shell with workspace snapshots"
```

---

### Task 5: Build Research Desk Components

**Files:**
- Create: `ephemeral/ink_ui/src/components/ResearchDesk.tsx`
- Create: `ephemeral/ink_ui/src/components/Chrome.tsx`
- Create: `ephemeral/ink_ui/src/components/LeftRail.tsx`
- Create: `ephemeral/ink_ui/src/components/Workspace.tsx`
- Create: `ephemeral/ink_ui/src/components/RightRail.tsx`
- Create: `ephemeral/ink_ui/src/components/CommandDock.tsx`
- Modify: `ephemeral/ink_ui/src/app.tsx`

- [ ] **Step 1: Add component props**

In `ResearchDesk.tsx`, define:

```tsx
import React from 'react';
import {Box} from 'ink';
import type {ActionDefinition, DeskState, DetailMode, FocusPane, HistoryEntry, ShortcutHint} from '../types.js';
import {Chrome} from './Chrome.js';
import {LeftRail} from './LeftRail.js';
import {Workspace} from './Workspace.js';
import {RightRail} from './RightRail.js';
import {CommandDock} from './CommandDock.js';

type Props = {
	width: number;
	height: number;
	focusPane: FocusPane;
	selectedAction: ActionDefinition;
	history: HistoryEntry[];
	selectedEntry: HistoryEntry | null;
	desk: DeskState;
	busy: boolean;
	input: string;
	detailMode: DetailMode;
	shortcuts: ShortcutHint[];
	onInputChange: (value: string) => void;
};
```

- [ ] **Step 2: Implement desktop and compact layout**

In `ResearchDesk.tsx`, compute:

```tsx
const isDesktop = width >= 132 && height >= 28;
const leftWidth = isDesktop ? Math.max(24, Math.min(32, Math.floor(width * 0.18))) : width - 2;
const rightWidth = isDesktop ? Math.max(30, Math.min(42, Math.floor(width * 0.24))) : width - 2;
const centerWidth = isDesktop ? Math.max(48, width - leftWidth - rightWidth - 8) : width - 2;
const bodyHeight = Math.max(10, height - 8);
```

Render:

```tsx
return (
	<Box flexDirection="column" paddingX={1}>
		<Chrome desk={desk} selectedAction={selectedAction} busy={busy} />
		{isDesktop ? (
			<Box height={bodyHeight}>
				<LeftRail width={leftWidth} height={bodyHeight} focusPane={focusPane} desk={desk} history={history} selectedAction={selectedAction} />
				<Workspace width={centerWidth} height={bodyHeight} focusPane={focusPane} selectedEntry={selectedEntry} selectedAction={selectedAction} detailMode={detailMode} busy={busy} />
				<RightRail width={rightWidth} height={bodyHeight} focusPane={focusPane} desk={desk} />
			</Box>
		) : (
			<Box flexDirection="column">
				<Workspace width={centerWidth} height={Math.max(8, bodyHeight - 10)} focusPane={focusPane} selectedEntry={selectedEntry} selectedAction={selectedAction} detailMode={detailMode} busy={busy} />
				<LeftRail width={leftWidth} height={10} focusPane={focusPane} desk={desk} history={history.slice(0, 4)} selectedAction={selectedAction} />
			</Box>
		)}
		<CommandDock selectedAction={selectedAction} input={input} busy={busy} focusPane={focusPane} shortcuts={shortcuts} />
	</Box>
);
```

- [ ] **Step 3: Implement panels with real data**

Use these panel rules:

```tsx
// LeftRail
// Show active symbol, watchlist rows from desk.workspace?.watchlist, action groups, and recent history.

// Workspace
// If selectedEntry exists, render detailBodyForEntry(selectedEntry, detailMode).
// If not, render active symbol overview from desk.workspace?.quote, desk.workspace?.news, and selectedAction hint.

// RightRail
// Show quote card, setup issues, panel warnings, related news titles, artifacts.
```

Do not add decorative cards inside cards. Each rail is a bordered terminal region with compact labels and rows.

- [ ] **Step 4: Replace old layout in `app.tsx`**

Replace the current JSX layout with:

```tsx
return (
	<>
		{!smokeTest && process.stdin.isTTY ? (
			<KeyboardController
				busy={busy}
				focusPane={focusPane}
				historyLength={history.length}
				input={input}
				onRun={handleRun}
				outputViewportHeight={outputViewportHeight}
				setDetailMode={setDetailMode}
				setFocusPane={setFocusPane}
				setInput={setInput}
				setOutputScroll={setOutputScroll}
				setSelectedActionIndex={setSelectedActionIndex}
				setSelectedHistoryIndex={setSelectedHistoryIndex}
				exit={exit}
			/>
		) : null}
		<ResearchDesk
			width={terminalWidth}
			height={terminalHeight}
			focusPane={focusPane}
			selectedAction={selectedAction}
			history={history}
			selectedEntry={selectedEntry}
			desk={desk}
			busy={busy}
			input={input}
			detailMode={detailMode}
			shortcuts={composerShortcuts}
			onInputChange={setInput}
		/>
	</>
);
```

- [ ] **Step 5: Verify**

Run:

```bash
npm --prefix ephemeral/ink_ui run typecheck
npm --prefix ephemeral/ink_ui run smoke
```

Expected: both pass.

- [ ] **Step 6: Commit**

```bash
git add ephemeral/ink_ui/src
git commit -m "feat: build terminal research desk layout"
```

---

### Task 6: Polish Command And Pane Navigation

**Files:**
- Modify: `ephemeral/ink_ui/src/components/KeyboardController.tsx`
- Modify: `ephemeral/ink_ui/src/components/CommandDock.tsx`
- Modify: `ephemeral/ink_ui/src/actions.ts`

- [ ] **Step 1: Add slash bootstrap from any pane**

In `KeyboardController.tsx`, before printable-character handling:

```ts
if (value === '/' && !input.trim()) {
	setFocusPane('input');
	setInput('/');
	return;
}
```

- [ ] **Step 2: Update pane cycling**

Use pane order:

```ts
const nextPane = (pane: FocusPane): FocusPane => {
	if (pane === 'left') return 'workspace';
	if (pane === 'workspace') return 'right';
	if (pane === 'right') return 'input';
	return 'left';
};

const previousPane = (pane: FocusPane): FocusPane => {
	if (pane === 'input') return 'right';
	if (pane === 'right') return 'workspace';
	if (pane === 'workspace') return 'left';
	return 'left';
};
```

- [ ] **Step 3: Add command dock status language**

In `CommandDock.tsx`, show:

```tsx
<Text color={busy ? 'yellow' : 'green'}>{busy ? 'RUNNING' : 'READY'}</Text>
```

and keep the highlighted `Enter` hint from the current UI.

- [ ] **Step 4: Verify**

Run:

```bash
npm --prefix ephemeral/ink_ui run typecheck
npm --prefix ephemeral/ink_ui run smoke
```

Expected: both pass.

- [ ] **Step 5: Commit**

```bash
git add ephemeral/ink_ui/src
git commit -m "feat: refine research desk keyboard flow"
```

---

### Task 7: Document And Run Release Gates

**Files:**
- Modify: `README.md`
- Modify: `CHANGELOG.md` if it already has an unreleased section; otherwise leave it unchanged.

- [ ] **Step 1: Update README Ink shell section**

Replace the `The 3.8 Ink shell` section with a concise `Research Desk shell` section:

```markdown
## Research Desk shell

The default interface is a terminal-native research desk: top market chrome, left watchlist and workflow rail, center workspace, right context rail, and a bottom command dock.

- Use `/quote AAPL`, `/news AAPL`, `/compare AAPL MSFT`, and `/backtest AAPL` to drive market workflows directly.
- The active symbol updates surrounding panels as commands complete.
- Setup and provider problems appear as context cards instead of hidden failures.
- Compact terminals fall back to a stacked layout.
```

- [ ] **Step 2: Run focused gates**

Run:

```bash
uv run --extra dev pytest tests/test_ink_bridge.py tests/test_cli_smoke.py -q
npm --prefix ephemeral/ink_ui run typecheck
npm --prefix ephemeral/ink_ui run smoke
```

Expected: all pass.

- [ ] **Step 3: Run full gate**

Run:

```bash
uv run --extra dev pytest -q
uv run ruff check .
```

Expected: all pass.

- [ ] **Step 4: Commit**

```bash
git add README.md CHANGELOG.md
git commit -m "docs: describe research desk shell"
```

---

## Self-Review

- Spec coverage: the plan covers backend workspace snapshots, bridge routing, modular frontend split, dense Research Desk UI, keyboard flow, and verification.
- Placeholder scan: no `TBD`, `TODO`, or unspecified implementation steps are required for execution.
- Type consistency: `WorkspaceSnapshot`, `DeskState`, `FocusPane`, `BridgeRequest`, and bridge `workspace` action are introduced before use.
- Scope check: this remains one terminal-native product upgrade. Browser UI, streaming feeds, broker integration, and full market-data replacement stay out of scope.
