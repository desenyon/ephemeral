import React from 'react';
import {Text} from 'ink';
import type {ActionDefinition, BridgeEnvelope, DetailMode, HistoryEntry, LineRow} from './types.js';

export const clamp = (value: number, minimum: number, maximum: number) =>
	Math.min(maximum, Math.max(minimum, value));

export const truncate = (value: string, max: number) =>
	value.length > max ? `${value.slice(0, max - 1)}…` : value;

export const previewValue = (value: unknown, max = 100) => {
	const raw = typeof value === 'string' ? value : JSON.stringify(value);
	return truncate((raw || '').replace(/\s+/g, ' ').trim(), max);
};

export const titleCase = (value: string) =>
	value
		.replace(/[_-]+/g, ' ')
		.replace(/\s+/g, ' ')
		.trim()
		.replace(/\b\w/g, character => character.toUpperCase());

const primitiveValue = (value: unknown) => {
	if (value === null || value === undefined || value === '') {
		return 'n/a';
	}
	if (typeof value === 'boolean') {
		return value ? 'yes' : 'no';
	}
	if (typeof value === 'number') {
		return Number.isInteger(value) ? value.toLocaleString() : value.toFixed(2);
	}
	return String(value);
};

const formatStructuredLines = (value: unknown, indent = 0): string[] => {
	const pad = ' '.repeat(indent);
	if (value === null || value === undefined || value === '') {
		return [`${pad}n/a`];
	}
	if (typeof value === 'string') {
		return value.split('\n').map(line => `${pad}${line}`);
	}
	if (typeof value === 'number' || typeof value === 'boolean') {
		return [`${pad}${primitiveValue(value)}`];
	}
	if (Array.isArray(value)) {
		if (!value.length) {
			return [`${pad}none`];
		}
		return value.flatMap(item => {
			if (item === null || item === undefined || typeof item !== 'object') {
				return [`${pad}- ${primitiveValue(item)}`];
			}

			const rows = Object.entries(item).filter(([, child]) => child !== undefined && child !== null && child !== '');
			if (!rows.length) {
				return [`${pad}- n/a`];
			}

			const [[firstKey, firstValue], ...rest] = rows;
			return [
				`${pad}- ${titleCase(firstKey)}: ${primitiveValue(firstValue)}`,
				...rest.flatMap(([childKey, childValue]) => {
					if (childValue === undefined || childValue === null || childValue === '') {
						return [];
					}
					if (typeof childValue === 'object') {
						return [`${pad}  ${titleCase(childKey)}`, ...formatStructuredLines(childValue, indent + 4)];
					}
					return [`${pad}  ${titleCase(childKey)}: ${primitiveValue(childValue)}`];
				}),
			];
		});
	}

	const rows = Object.entries(value as Record<string, unknown>).filter(([, child]) => child !== undefined && child !== null && child !== '');
	if (!rows.length) {
		return [`${pad}n/a`];
	}

	return rows.flatMap(([key, child]) => {
		if (typeof child === 'object') {
			return [`${pad}${titleCase(key)}`, ...formatStructuredLines(child, indent + 2)];
		}
		return [`${pad}${titleCase(key)}: ${primitiveValue(child)}`];
	});
};

export const formatStructuredBlock = (value: unknown) => formatStructuredLines(value).join('\n');
export const joinSections = (...sections: Array<string | undefined>) => sections.filter(Boolean).join('\n\n');
export const repeat = (character: string, count: number) => character.repeat(Math.max(0, count));

export const padRows = (rows: LineRow[], height: number) => {
	const padded = [...rows];
	while (padded.length < height) {
		padded.push({text: ''});
	}
	return padded.slice(0, height);
};

export const pickGroupColor = (group: ActionDefinition['group']) => {
	if (group === 'Research') return 'cyanBright';
	if (group === 'Build') return 'yellow';
	return 'green';
};

export const renderStyledLine = (line: string, accentColor = 'cyanBright'): React.ReactNode => {
	const trimmed = line.trim();
	if (!trimmed) {
		return <Text wrap="truncate-end">{' '}</Text>;
	}

	if (/^\[ok\]/i.test(trimmed)) {
		return (
			<Text wrap="truncate-end">
				<Text color="green" bold>
					[ok]
				</Text>
				<Text color="gray"> {trimmed.replace(/^\[ok\]\s*/i, '')}</Text>
			</Text>
		);
	}

	if (/^\[x\]/i.test(trimmed)) {
		return (
			<Text wrap="truncate-end">
				<Text color="red" bold>
					[x]
				</Text>
				<Text color="gray"> {trimmed.replace(/^\[x\]\s*/i, '')}</Text>
			</Text>
		);
	}

	if (/^\d+\.\s/.test(trimmed)) {
		const [, marker, rest] = trimmed.match(/^(\d+\.)\s+(.*)$/) ?? [];
		if (marker && rest) {
			return (
				<Text wrap="truncate-end">
					<Text color={accentColor} bold>
						{marker}
					</Text>
					<Text color="white"> {rest}</Text>
				</Text>
			);
		}
	}

	if (/^-\s/.test(trimmed)) {
		return (
			<Text wrap="truncate-end">
				<Text color={accentColor} bold>
					{'>'}
				</Text>
				<Text color="white"> {trimmed.replace(/^-\s*/, '')}</Text>
			</Text>
		);
	}

	if (/^[A-Z][A-Za-z ]+$/.test(trimmed) && trimmed.length < 28) {
		return (
			<Text color={accentColor} bold wrap="truncate-end">
				{trimmed}
			</Text>
		);
	}

	const keyValueMatch = line.match(/^(\s*[A-Za-z][A-Za-z0-9 /_-]{1,20})(\s{2,}|\s*:\s)(.+)$/);
	if (keyValueMatch) {
		const [, label, separator, value] = keyValueMatch;
		return (
			<Text wrap="truncate-end">
				<Text color="gray">{label.trimEnd()}</Text>
				<Text color="gray">{separator.includes(':') ? ': ' : '  '}</Text>
				<Text color="white">{value}</Text>
			</Text>
		);
	}

	const slashIndex = line.indexOf('/');
	if (slashIndex >= 0 && /\/[a-z]/i.test(line.slice(slashIndex))) {
		const match = line.match(/(.*?)(\/[A-Za-z0-9_-]+.*)/);
		if (match) {
			return (
				<Text wrap="truncate-end">
					<Text color="white">{match[1]}</Text>
					<Text color={accentColor} bold>
						{match[2]}
					</Text>
				</Text>
			);
		}
	}

	return <Text color="white" wrap="truncate-end">{line}</Text>;
};

export const wrapText = (input: string, width: number): string[] => {
	const lines = input.replace(/\t/g, '  ').split('\n');
	const output: string[] = [];
	const safeWidth = Math.max(12, width);

	for (const line of lines) {
		if (!line) {
			output.push('');
			continue;
		}

		let remaining = line;
		while (remaining.length > safeWidth) {
			const slice = remaining.slice(0, safeWidth);
			const breakAt = slice.lastIndexOf(' ');
			const boundary = breakAt > safeWidth * 0.55 ? breakAt : safeWidth;
			output.push(remaining.slice(0, boundary).trimEnd());
			remaining = remaining.slice(boundary).trimStart();
		}
		output.push(remaining);
	}

	return output;
};

export const viewportLines = (input: string, width: number, height: number, scrollOffset: number) => {
	const allLines = wrapText(input, width);
	const safeHeight = Math.max(1, height);
	const maxOffset = Math.max(0, allLines.length - safeHeight);
	const start = clamp(scrollOffset, 0, maxOffset);
	const visible = allLines.slice(start, start + safeHeight);
	const padded = [...visible];

	while (padded.length < safeHeight) {
		padded.push('');
	}

	return {
		lines: padded,
		total: allLines.length,
		offset: start,
		maxOffset,
	};
};

const renderToolCalls = (toolCalls: any[]) => {
	if (!toolCalls?.length) {
		return '';
	}

	return [
		'Tool calls',
		...toolCalls.map((toolCall, index) => {
			const name = toolCall?.name ?? `tool-${index + 1}`;
			const args = previewValue(toolCall?.args ?? {}, 78);
			const result = previewValue(toolCall?.result ?? {}, 110);
			return `${index + 1}. ${name}\n   args   ${args}\n   result ${result}`;
		}),
	].join('\n');
};

export const summarizeEnvelope = (result: BridgeEnvelope): string => {
	const action = result.action;
	const payload = result.data ?? {};

	switch (action) {
		case 'ask':
			return truncate(String(payload?.response ?? 'No response returned.'), 160);
		case 'status':
			return `Provider ${payload?.provider ?? 'n/a'}\nModel ${payload?.model ?? 'n/a'}\nState ${payload?.needs_setup ? 'setup needed' : 'ready'}`;
		case 'doctor':
			return `Doctor checks ${(payload?.checks ?? []).length}\nBackends ${(payload?.router_backends ?? []).join(', ') || 'none'}`;
		case 'quote':
			return (payload?.quotes ?? []).map((quote: any) => `${quote.symbol} ${quote.price}`).join('\n');
		case 'news':
			return (payload?.articles ?? []).slice(0, 3).map((article: any) => article.title ?? 'Untitled').join('\n');
		case 'compare':
			return `Best ${payload?.best_performer ?? 'n/a'}\nWorst ${payload?.worst_performer ?? 'n/a'}`;
		case 'chart':
			return `Chart saved to ${payload?.chart_path ?? 'n/a'}`;
		case 'backtest':
			return `Strategy ${payload?.result?.strategy ?? 'n/a'}\nReturn ${payload?.result?.performance?.total_return ?? 'n/a'}`;
		case 'export':
			return `Exported to ${payload?.path ?? 'unknown path'}`;
		case 'set-key':
			return `Saved key for ${payload?.provider ?? 'provider'}`;
		case 'set-provider':
		case 'set-model':
			return 'Updated configuration';
		default:
			return previewValue(payload, 160);
	}
};

export const detailBodyForEntry = (entry: HistoryEntry, detailMode: DetailMode): string => {
	if (entry.error) {
		return `Request failed\n\n${entry.error}`;
	}

	if (!entry.result) {
		return entry.body;
	}

	if (detailMode === 'raw') {
		return JSON.stringify(entry.result.data ?? {}, null, 2);
	}

	const action = entry.result.action;
	const payload = entry.result.data ?? {};

	switch (action) {
		case 'help':
			return joinSections(
				payload?.body ?? 'Ephemeral help',
				['Slash commands', ...((payload?.slash_commands ?? []) as string[])].join('\n'),
				['Tips', ...((payload?.tips ?? []) as string[]).map((tip: string) => `- ${tip}`)].join('\n'),
			);
		case 'shortcuts':
			return ((payload?.items ?? []) as any[]).map(item => `${item.key.padEnd(12)} ${item.action}`).join('\n');
		case 'keys':
			return joinSections(
				`Configured providers: ${payload?.configured ?? 0}`,
				((payload?.rows ?? []) as any[]).map(row => `${String(row.provider).padEnd(14)} ${row.status}`).join('\n'),
			);
		case 'status':
			return [
				`Provider      ${payload?.provider ?? 'n/a'}`,
				`Model         ${payload?.model ?? 'n/a'}`,
				`Setup         ${payload?.needs_setup ? 'required' : 'ready'}`,
				`Backends      ${(payload?.health?.router_backends ?? []).join(', ') || 'none'}`,
				payload?.ollama?.reachable ? `Ollama       ${payload?.ollama?.host ?? 'reachable'}` : `Ollama       unavailable`,
				payload?.ollama?.installed_models?.length ? `Installed    ${payload.ollama.installed_models.join(', ')}` : '',
				'',
				'Checks',
				...((payload?.health?.checks ?? []) as any[]).map(check => `${check.ok ? '[ok]' : '[x] '} ${check.name} ${check.detail ?? ''}`.trim()),
			]
				.filter(Boolean)
				.join('\n');
		case 'doctor':
			return [
				'Doctor',
				...((payload?.checks ?? []) as any[]).map(check => `${check.ok ? '[ok]' : '[x] '} ${check.name} ${check.detail ?? ''}`.trim()),
				'',
				`Router backends: ${(payload?.router_backends ?? []).join(', ') || 'none'}`,
			].join('\n');
		case 'ask':
			return joinSections(String(payload?.response ?? 'No response returned.').trim(), renderToolCalls(payload?.tool_calls ?? []));
		case 'quote':
			return ((payload?.quotes ?? []) as any[])
				.map(quote => {
					if (quote.error) {
						return `${quote.symbol ?? 'symbol'}\n  error   ${quote.error}`;
					}

					const change = Number(quote.change_percent ?? 0);
					const prefix = change >= 0 ? '+' : '';
					return `${quote.symbol}\n  price   $${Number(quote.price ?? 0).toFixed(2)}\n  move    ${prefix}${change.toFixed(2)}%\n  volume  ${Number(quote.volume ?? 0).toLocaleString()}`;
				})
				.join('\n\n');
		case 'news':
			return joinSections(
				`Source: ${payload?.source_used ?? 'unknown'}`,
				((payload?.articles ?? []) as any[])
					.slice(0, 10)
					.map(
						(article, index) =>
							`${index + 1}. ${article.title ?? 'Untitled'}\n   ${(article.source ?? article.publisher ?? 'unknown source').toString()}${article.url ? ` · ${article.url}` : ''}`,
					)
					.join('\n\n'),
			);
		case 'compare':
			return [
				`Period: ${payload?.period ?? 'n/a'}`,
				`Best:   ${payload?.best_performer ?? 'n/a'}`,
				`Worst:  ${payload?.worst_performer ?? 'n/a'}`,
				'',
				...((payload?.comparison ?? []) as any[]).map(
					row =>
						`${String(row.symbol ?? '').padEnd(6)} return ${String(Number(row.total_return ?? 0).toFixed(2)).padStart(7)}%  sharpe ${String(Number(row.sharpe ?? 0).toFixed(2)).padStart(5)}`,
				),
			].join('\n');
		case 'chart':
			return [
				`Chart path: ${payload?.chart_path ?? 'n/a'}`,
				payload?.symbol ? `Symbol:     ${payload.symbol}` : '',
				payload?.symbols ? `Symbols:    ${payload.symbols.join(', ')}` : '',
				`Period:     ${payload?.period ?? 'n/a'}`,
			]
				.filter(Boolean)
				.join('\n');
		case 'backtest':
			return formatStructuredBlock(payload?.result ?? payload);
		case 'portfolio':
		case 'strategy':
		case 'report':
		case 'alert':
			return formatStructuredBlock(payload?.engine_result ?? payload);
		case 'models':
			return [
				`Default provider ${payload?.default_provider ?? 'n/a'}`,
				`Default model    ${payload?.default_model ?? 'n/a'}`,
				'',
				...Object.entries(payload?.providers ?? {}).flatMap(([provider, models]) => [
					`${titleCase(provider)}`,
					...((models as string[]).map(model => `  - ${model}`) || ['  - none']),
					'',
				]),
			].join('\n');
		case 'tools':
			return ((payload?.tools ?? []) as string[]).map((tool, index) => `${index + 1}. ${tool}`).join('\n');
		case 'setup-help':
			return [
				'Setup',
				...((payload?.steps ?? []) as string[]).map((step, index) => `${index + 1}. ${step}`),
				'',
				payload?.docs_url ?? '',
			].join('\n');
		case 'reload':
			return joinSections('Router reloaded', formatStructuredBlock(payload?.status ?? payload));
		case 'export':
			return `Export complete\n\nPath: ${payload?.path ?? 'n/a'}\nCharacters: ${payload?.characters ?? 0}`;
		default:
			return entry.body || JSON.stringify(payload, null, 2);
	}
};
