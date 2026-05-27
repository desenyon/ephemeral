import React, {useEffect, useMemo, useState} from 'react';
import {Text, useApp} from 'ink';
import {spawn} from 'node:child_process';
import process from 'node:process';
import {actions, parseSlashCommand, requestForAction} from './actions.js';
import {invokeBridge, projectRoot, pythonExecutable} from './bridge.js';
import {APP_VERSION, animationFrames, smokeTest} from './constants.js';
import {KeyboardController} from './components/KeyboardController.js';
import {ResearchDesk} from './components/ResearchDesk.js';
import {useRawMode} from './hooks/useRawMode.js';
import {useTerminalSize} from './hooks/useTerminalSize.js';
import {
	clamp,
	detailBodyForEntry,
	padRows,
	pickGroupColor,
	renderStyledLine,
	repeat,
	summarizeEnvelope,
	truncate,
	viewportLines,
} from './formatters.js';
import type {ActivityRow, BridgeRequest, DeskState, DetailMode, FocusPane, HistoryEntry, LayoutMode, LineRow, ShortcutHint} from './types.js';

const buildExportHistory = (history: HistoryEntry[]) =>
	history
		.slice()
		.reverse()
		.map(entry => ({
			label: entry.label,
			input: entry.input,
			body: entry.body,
			error: entry.error ?? '',
		}));

const Divider = ({width}: {width: number}) => <Text color="gray">{repeat('-', Math.max(8, width))}</Text>;

export const App = () => {
	const {exit} = useApp();
	useRawMode();

	const {width: terminalWidth, height: terminalHeight} = useTerminalSize();
	const [frameIndex, setFrameIndex] = useState(0);
	const [selectedActionIndex, setSelectedActionIndex] = useState(0);
	const [selectedHistoryIndex, setSelectedHistoryIndex] = useState(0);
	const [focusPane, setFocusPane] = useState<FocusPane>('input');
	const [detailMode, setDetailMode] = useState<DetailMode>('rendered');
	const [input, setInput] = useState('');
	const [busy, setBusy] = useState(false);
	const [history, setHistory] = useState<HistoryEntry[]>([]);
	const [statusSnapshot, setStatusSnapshot] = useState<any>(null);
	const [outputScroll, setOutputScroll] = useState(0);
	const [pendingLabel, setPendingLabel] = useState<string | null>(null);
	const [statusLoading, setStatusLoading] = useState(true);
	const [desk, setDesk] = useState<DeskState>({
		activeSymbol: 'SPY',
		watchlist: ['SPY', 'QQQ', 'DIA', 'IWM'],
		workspace: null,
		workspaceLoading: true,
		workspaceError: null,
	});

	const selectedAction = actions[selectedActionIndex]!;
	const selectedEntry = history[selectedHistoryIndex] ?? null;

	useEffect(() => {
		if (smokeTest) {
			return;
		}

		const timer = setInterval(() => {
			setFrameIndex(previous => (previous + 1) % animationFrames.length);
		}, 220);
		return () => clearInterval(timer);
	}, []);

	const pushEntry = (entry: HistoryEntry) => {
		setHistory(previous => [entry, ...previous].slice(0, 18));
		setSelectedHistoryIndex(0);
		setOutputScroll(0);
	};

	const refreshWorkspace = async (
		nextSymbol = desk.activeSymbol,
		nextWatchlist = desk.watchlist,
	) => {
		setDesk(previous => ({...previous, workspaceLoading: true, workspaceError: null}));
		try {
			const result = await invokeBridge({
				action: 'workspace',
				symbol: nextSymbol,
				watchlist: nextWatchlist,
			});
			setDesk(previous => ({
				...previous,
				activeSymbol: result.data?.active_symbol ?? nextSymbol,
				workspace: result.data,
				workspaceLoading: false,
			}));
			setStatusSnapshot(result.data?.status ?? null);
		} catch (error) {
			setDesk(previous => ({
				...previous,
				workspaceLoading: false,
				workspaceError: error instanceof Error ? error.message : String(error),
			}));
		}
	};

	const runRequest = async (request: BridgeRequest, sourceLabel: string, currentInput: string) => {
		const effectiveRequest = request.action === 'export' ? {...request, history: buildExportHistory(history)} : request;
		setBusy(true);
		setPendingLabel(sourceLabel);

		try {
			if (effectiveRequest.action === 'legacy-ui') {
				exit();
				const child = spawn(pythonExecutable, ['-m', 'ephemeral.cli', '--legacy-ui'], {
					cwd: projectRoot,
					env: process.env,
					stdio: 'inherit',
				});
				child.on('close', code => process.exit(code ?? 0));
				return;
			}

			const result = await invokeBridge(effectiveRequest);
			pushEntry({
				id: `${Date.now()}-${Math.random()}`,
				label: sourceLabel,
				input: currentInput.trim(),
				body: summarizeEnvelope(result),
				result,
				createdAt: new Date().toLocaleTimeString(),
			});

			if (
				effectiveRequest.action === 'status' ||
				effectiveRequest.action === 'doctor' ||
				effectiveRequest.action === 'reload' ||
				effectiveRequest.action === 'set-provider' ||
				effectiveRequest.action === 'set-model'
			) {
				setStatusSnapshot(result.data);
			}

			const symbolFromResult =
				result.data?.symbol ??
				result.data?.quote?.symbol ??
				result.data?.quotes?.[0]?.symbol ??
				result.data?.active_symbol;
			if (typeof symbolFromResult === 'string' && symbolFromResult.trim()) {
				const nextSymbol = symbolFromResult.trim().toUpperCase();
				const nextWatchlist = desk.watchlist.includes(nextSymbol)
					? desk.watchlist
					: [nextSymbol, ...desk.watchlist].slice(0, 8);
				setDesk(previous => ({
					...previous,
					activeSymbol: nextSymbol,
					watchlist: nextWatchlist,
				}));
				void refreshWorkspace(nextSymbol, nextWatchlist);
			}

			if (smokeTest) {
				process.exit(0);
			}
		} catch (error) {
			const errorMessage = error instanceof Error ? error.message : String(error);
			pushEntry({
				id: `${Date.now()}-${Math.random()}`,
				label: sourceLabel,
				input: currentInput.trim(),
				body: errorMessage,
				error: errorMessage,
				createdAt: new Date().toLocaleTimeString(),
			});
			if (smokeTest) {
				console.error(`Smoke test failed: ${errorMessage}`);
				process.exit(1);
			}
		} finally {
			setBusy(false);
			setPendingLabel(null);
		}
	};

	const handleRun = (currentInput: string) => {
		const slashRequest = parseSlashCommand(currentInput);
		const request = slashRequest ?? requestForAction(selectedAction, currentInput);
		const sourceLabel = slashRequest ? `Command ${currentInput.trim()}` : selectedAction.label;
		void runRequest(request, sourceLabel, currentInput);
		setInput('');
		setFocusPane('workspace');
	};

	useEffect(() => {
		if (smokeTest) {
			return;
		}

		setStatusLoading(true);
		void refreshWorkspace()
			.catch(() => undefined)
			.finally(() => {
				setStatusLoading(false);
			});
	}, []);

	const layoutMode: LayoutMode = terminalWidth >= 120 && terminalHeight >= 24 ? 'desktop' : 'stacked';
	const sidebarWidth = layoutMode === 'desktop' ? clamp(Math.floor(terminalWidth * 0.24), 26, 30) : terminalWidth - 2;
	const mainWidth = layoutMode === 'desktop' ? Math.max(terminalWidth - sidebarWidth - 5, 60) : terminalWidth - 2;
	const bodyHeight = clamp(terminalHeight - (layoutMode === 'desktop' ? 9 : 14), 10, 40);
	const outputViewportHeight = Math.max(6, bodyHeight - 5);
	const outputViewportWidth = Math.max(32, mainWidth - 2);
	const activityVisible = layoutMode === 'desktop' ? 5 : 4;

	const metrics = useMemo(() => {
		const snapshot = statusSnapshot?.status ?? statusSnapshot ?? {};
		const routerBackends = (snapshot.health?.router_backends ?? snapshot.router_backends ?? []) as string[];
		return {
			provider: snapshot.provider ?? 'n/a',
			model: snapshot.model ?? 'n/a',
			backends: String(routerBackends.length || 0),
			state: snapshot.needs_setup ? 'setup' : 'ready',
			installedModels: snapshot.ollama?.installed_models ?? [],
			host: snapshot.ollama?.host ?? 'n/a',
			localReady: Boolean(snapshot.local_ready ?? snapshot.ollama?.current_model_available),
		};
	}, [statusSnapshot]);

	const activityRows: ActivityRow[] = useMemo(() => {
		if (history.length === 0) {
			return [];
		}
		return history.slice(0, activityVisible).map((entry, index) => ({
			id: entry.id,
			label: truncate(entry.label, 24),
			timestamp: entry.error ? 'error' : entry.createdAt,
			selected: index === selectedHistoryIndex,
			error: Boolean(entry.error),
		}));
	}, [activityVisible, history, selectedHistoryIndex]);

	const selectedBody = selectedEntry
		? detailBodyForEntry(selectedEntry, detailMode)
		: busy && pendingLabel
			? [
					`${pendingLabel} is running.`,
					'',
					'The request is executing in the background while the shell stays interactive.',
					'Recent runs stay in the sidebar and the prompt becomes available again as soon as the job completes.',
				].join('\n')
			: [
					'Ephemeral turns one command into market context, tools, and execution.',
					'Use the left rail to move between workflows, keep the workspace focused on one result, and let the composer drive the session.',
					'',
					'Best starting points',
					'- Ask for a catalyst read, thesis update, or risk check',
					'- Compare a basket, open live news, or chart a setup',
					'- Draft a portfolio, memo, strategy, or alert without leaving the shell',
					'',
					'Fast paths',
					'- /status for routing health and local model readiness',
					`- ${selectedAction.promptPlaceholder ?? selectedAction.hint}`,
				].join('\n');
	const viewport = viewportLines(selectedBody, outputViewportWidth, outputViewportHeight, outputScroll);

	const workspaceStatus = selectedEntry ? selectedEntry.label : pendingLabel ?? selectedAction.label;
	const workspaceSubtitle = selectedEntry?.input
		? `input · ${truncate(selectedEntry.input, Math.max(28, outputViewportWidth - 10))}`
		: detailMode === 'raw'
			? 'raw payload'
			: selectedAction.description;

	const promptCursor = focusPane === 'input' ? '▏' : '';
	const promptCursorColor = frameIndex % 2 === 0 ? 'cyanBright' : 'blue';
	const promptStatus = busy ? 'running' : 'ready';
	const promptHint = input.trim()
		? selectedAction.hint
		: selectedAction.promptPlaceholder ?? 'Use natural language or slash commands like /quote AAPL';
	const shellStatus = busy ? `running ${pendingLabel ?? 'request'}` : statusLoading ? 'syncing state' : `${metrics.provider} · ${metrics.model}`;
	const dividerWidth = Math.min(terminalWidth - 8, 72);
	const headerTone = busy ? 'yellow' : statusLoading ? 'blue' : 'green';
	const actionAccent = pickGroupColor(selectedAction.group);
	const topStatusLine = `${selectedAction.group} · ${selectedAction.label} · ${metrics.localReady ? 'local ready' : 'setup path'}`;
	const composerShortcuts = useMemo<ShortcutHint[]>(() => {
		const hints: ShortcutHint[] = [{key: 'Tab', description: 'switch pane'}];

		if (focusPane === 'input') {
			if (input.trim()) {
				hints.push({key: 'Esc', description: 'clear input'});
			} else {
				hints.push({key: 'Up/Down', description: 'choose action'});
			}
		}

		if (focusPane === 'left') {
			hints.push({key: 'Up/Down', description: 'navigate'});
		}

		if (focusPane === 'right') {
			hints.push({key: 'Up/Down', description: 'navigate'});
			hints.push({key: 'Ctrl+L', description: 'clear history'});
		}

		if (focusPane === 'workspace') {
			hints.push({key: 'Up/Down', description: 'scroll'});
			hints.push({key: '[ ]', description: 'page'});
		}

		if (focusPane !== 'input') {
			hints.push({key: 'd', description: 'toggle raw output'});
		}
		return hints;
	}, [focusPane, input]);

	const sidebarRows = useMemo(() => {
		const rows: LineRow[] = [
			{text: 'NAVIGATOR', color: focusPane === 'left' ? actionAccent : 'gray', bold: true},
			{text: `${metrics.provider} · ${truncate(String(metrics.model), 20)}`, color: 'gray'},
			{text: ''},
		];

		for (const group of ['Research', 'Build', 'Ops'] as const) {
			rows.push({
				text: group.toUpperCase(),
				color: selectedAction.group === group ? pickGroupColor(group) : 'gray',
				bold: true,
			});
			for (const action of actions.filter(item => item.group === group)) {
				const selected = action.id === selectedAction.id;
				rows.push({
					text: `${selected ? '>' : ' '} ${action.label}`,
					color: selected ? (focusPane === 'left' ? pickGroupColor(group) : 'white') : 'gray',
					bold: selected,
				});
			}
			rows.push({text: ''});
		}

		rows.push({text: 'RECENT', color: focusPane === 'right' ? 'cyanBright' : 'gray', bold: true});
		if (activityRows.length) {
			for (const row of activityRows) {
				rows.push({
					text: `${row.selected ? '>' : ' '} ${truncate(row.label, 16)} · ${row.timestamp}`,
					color: row.selected ? (focusPane === 'right' ? 'cyanBright' : 'white') : row.error ? 'red' : 'gray',
					bold: row.selected,
				});
			}
		} else {
			rows.push({text: 'No runs yet', color: 'gray'});
		}

		rows.push({text: ''});
		rows.push({text: `${metrics.localReady ? 'Local ready' : 'Local warming'} · ${metrics.state}`, color: metrics.localReady ? 'green' : 'yellow'});
		if (metrics.host !== 'n/a') {
			rows.push({text: truncate(metrics.host, sidebarWidth - 1), color: 'gray'});
		}
		rows.push({text: `Focus ${focusPane} · ${selectedEntry ? detailMode : 'workspace'}`, color: 'gray'});
		return padRows(rows, bodyHeight);
	}, [actionAccent, activityRows, bodyHeight, focusPane, metrics.host, metrics.localReady, metrics.model, metrics.provider, metrics.state, selectedAction.group, selectedAction.id, selectedEntry, detailMode, sidebarWidth]);

	const workspaceRows = useMemo(
		() =>
			padRows(
				[
					{text: workspaceStatus, color: focusPane === 'workspace' ? 'cyanBright' : 'gray', bold: true},
					{text: workspaceSubtitle, color: 'gray'},
					{text: ''},
					...viewport.lines.map(line => ({text: line || ' '})),
					{text: ''},
					{
						text: '',
						node: viewport.total > viewport.lines.length ? (
							<Text wrap="truncate-end">
								<Text color="white" bold>[ ]</Text>
								<Text color="gray"> page {viewport.offset + 1}-{Math.min(viewport.offset + viewport.lines.length, viewport.total)} of {viewport.total} · {detailMode}</Text>
							</Text>
						) : (
							<Text color="gray" wrap="truncate-end">{detailMode} view · {busy ? 'request running' : 'ready for next command'}</Text>
						),
					},
				],
				bodyHeight,
			),
		[bodyHeight, busy, detailMode, focusPane, viewport.lines, viewport.offset, viewport.total, workspaceStatus, workspaceSubtitle],
	);

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
				actionAccent={actionAccent}
				activityRows={activityRows}
				bodyHeight={bodyHeight}
				busy={busy}
				desk={desk}
				focusPane={focusPane}
				headerTone={headerTone}
				input={input}
				promptCursor={promptCursor}
				promptCursorColor={promptCursorColor}
				promptHint={promptHint}
				selectedAction={selectedAction}
				shellStatus={shellStatus}
				shortcuts={composerShortcuts}
				terminalHeight={terminalHeight}
				terminalWidth={terminalWidth}
				topStatusLine={topStatusLine}
				workspaceRows={workspaceRows}
			/>
		</>
	);

};
