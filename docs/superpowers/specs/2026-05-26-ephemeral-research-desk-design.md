# Ephemeral Research Desk Design

## Decision

Build the new version on top of the existing Ink UI and Python bridge. Do not restart the UI from scratch.

The current app already has the hardest reusable pieces: a persistent Python bridge worker, keyboard input handling, responsive terminal sizing, slash-command parsing, status hydration, a smoke-test path, and backend actions for quote, news, compare, chart, backtest, provider setup, and engine workflows. A full rewrite would mostly recreate these boundaries while increasing regression risk.

The right move is a modular rebuild: keep the launcher and bridge contract, split the large `ephemeral/ink_ui/src/index.tsx` file into focused TypeScript modules, and replace the current launcher-style shell with a denser Research Desk layout.

## Product Target

Ephemeral vNext should feel like a professional terminal-native research desk:

- Top market chrome with version, provider/model, local readiness, active symbol, session mode, and command state.
- Left rail for watchlist, workflow navigation, and recent activity.
- Center workspace for the selected research surface: overview, news, chart, comparison, backtest, portfolio, report, or raw payload.
- Right rail for context cards: quote snapshot, analyst/valuation style metrics, setup warnings, related articles, artifacts, and available actions.
- Bottom command dock that remains the primary control surface and supports slash commands, natural language, and action-specific prompts.

This should borrow the density and keyboard-first confidence of the supplied Fincept screenshots without cloning their brand or requiring a browser UI.

## Scope

The first implementation should ship one powerful terminal shell, not every possible finance terminal feature.

In scope:

- Research Desk layout with desktop and compact terminal breakpoints.
- Symbol context tracked across commands.
- Watchlist state in the UI process, seeded with common indexes and updated from quote/news commands.
- Backend workspace snapshot action that returns status, active symbol data, recent news, cached artifacts, and setup issues in one payload.
- Richer formatting for quote, news, compare, chart, backtest, portfolio, strategy, report, alert, status, and doctor payloads.
- Component/module split for the Ink frontend so future work is maintainable.
- Tests for bridge workspace snapshots, command parsing, layout helpers, and smoke rendering.

Out of scope for the first implementation:

- A browser or desktop UI.
- Real-time streaming market feeds.
- Broker integration or order entry.
- Custom terminal graphics beyond what Ink can render reliably.
- Replacing yfinance/optional providers with a new data platform.

## Architecture

Keep the existing process model:

```text
ephemeral CLI
  -> Ink React app
    -> persistent Python bridge process
      -> Engine, services, tools, config, artifacts
```

Add a higher-level workspace payload:

```text
Ink App
  requests: { action: "workspace", symbol, watchlist, recent_actions }

Bridge
  builds: status + quote bundle + news + artifacts + setup issues

Ink App
  renders: chrome + left rail + center workspace + right context rail + command dock
```

The bridge should remain action-oriented. The new `workspace` action is a read model for the UI, not a second engine. Existing actions still execute work; `workspace` lets the UI hydrate panels quickly and consistently.

## Frontend Units

Split `ephemeral/ink_ui/src/index.tsx` into small units while preserving behavior:

- `src/index.tsx`: render entrypoint only.
- `src/app.tsx`: top-level state orchestration.
- `src/types.ts`: shared TypeScript types.
- `src/actions.ts`: action definitions, slash command parsing, request building.
- `src/bridge.ts`: persistent bridge client.
- `src/formatters.tsx`: payload summary/detail renderers.
- `src/hooks/useTerminalSize.ts`: terminal sizing.
- `src/hooks/useRawMode.ts`: raw mode lifecycle.
- `src/components/KeyboardController.tsx`: keyboard map.
- `src/components/ResearchDesk.tsx`: full layout composition.
- `src/components/Chrome.tsx`: top status chrome.
- `src/components/LeftRail.tsx`: watchlist, workflows, activity.
- `src/components/Workspace.tsx`: center result and tab rendering.
- `src/components/RightRail.tsx`: contextual cards.
- `src/components/CommandDock.tsx`: prompt, hints, command state.

This is a controlled split, not a behavior rewrite. Each extraction should have typecheck/smoke coverage before visual changes land.

## Backend Units

Add backend support without disturbing existing actions:

- `ephemeral/research/workspace.py`: pure builders for workspace snapshots, watchlist quote summaries, artifact summaries, and setup issue summaries.
- `ephemeral/ink_bridge.py`: add `_workspace_payload()` and route `action == "workspace"`.
- `tests/test_ink_bridge.py`: cover valid workspace payloads, missing/invalid symbols, and no-network-safe fallbacks.
- Existing services continue to own data fetching and caching.

The workspace builder should prefer cached/local data when possible and return structured warnings rather than failing the whole shell if one panel cannot hydrate.

## Data Shape

The workspace action returns:

```json
{
  "active_symbol": "AAPL",
  "status": {},
  "watchlist": [
    {"symbol": "SPY", "price": 0, "change_percent": 0, "state": "ok"}
  ],
  "quote": {},
  "news": [],
  "artifacts": [],
  "setup_issues": [],
  "panel_warnings": []
}
```

Rules:

- `active_symbol` defaults to the first valid symbol from the request, then prior UI state, then `SPY`.
- Network failures produce `panel_warnings`; they do not crash the UI.
- The UI may render partial data.
- Secrets never cross the bridge.

## Interaction Model

Keep current shortcuts and add terminal-desk navigation:

- `Tab`: cycle left rail, workspace, right rail, command dock.
- `Left` / `Right`: move between major panes when the command dock is empty.
- `Up` / `Down`, `j` / `k`: move within the focused pane.
- `[` / `]`: page workspace content.
- `d`: toggle rendered/raw payload.
- `/`: start a slash command from any pane.
- `Esc`: clear prompt or return focus to command dock.
- `Enter`: run command.

The command dock remains the primary interaction surface. The desk panels should accelerate context and navigation, not compete with the prompt.

## Visual Direction

Use a dense professional terminal palette:

- Mostly black background.
- Orange/amber for active tabs and market-terminal accents.
- Cyan for data labels and secondary highlights.
- Green/red for market direction and health.
- Magenta sparingly for analyst/context rails.
- Gray borders and dividers.

Avoid a one-color theme. Avoid decorative gradients or large empty hero treatment. Every visible region should carry useful operational information.

## Testing And Verification

Minimum gates:

- `npm --prefix ephemeral/ink_ui run typecheck`
- `npm --prefix ephemeral/ink_ui run smoke`
- `uv run --extra dev pytest tests/test_ink_bridge.py tests/test_cli_smoke.py -q`
- `uv run --extra dev pytest -q` before calling the release complete

For frontend changes, use the existing Ink smoke path as the first regression gate. If browser-based screenshots are needed later, they should be for companion mockups only; the product remains terminal-native.

## Risks

- The current `index.tsx` file is large enough that layout changes without first splitting modules will be brittle.
- Market data calls can be slow or unavailable; workspace hydration must tolerate partial failures.
- Dense UI can become unreadable on small terminals; compact mode must be a first-class layout, not an afterthought.
- There is existing dirty work in this checkout. Implementation must avoid reverting unrelated changes and should commit only the files touched for this version.

## Success Criteria

- Launching `ephemeral` opens a Research Desk, not a command launcher.
- A user can type `/quote AAPL`, `/news AAPL`, `/compare AAPL MSFT`, `/backtest AAPL`, and see panels update around the active symbol.
- The UI still works on small terminals with a compact stacked layout.
- Backend status/setup problems appear as actionable context cards.
- The TypeScript UI is split into maintainable modules.
- Existing CLI, bridge, and setup tests remain passing.
