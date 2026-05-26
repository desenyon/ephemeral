import type {ActionDefinition, BridgeRequest} from './types.js';

export const actions: ActionDefinition[] = [
	{
		id: 'ask',
		label: 'Ask',
		description: 'LLM research with tool use',
		hint: 'Ask for catalysts, thesis work, risk analysis, or quick synthesis.',
		promptPlaceholder: 'Why is NVDA moving and what changes the thesis?',
		group: 'Research',
	},
	{
		id: 'quote',
		label: 'Quote',
		description: 'Live quote snapshots',
		hint: 'Enter one or more tickers separated by spaces.',
		promptPlaceholder: 'AAPL MSFT NVDA',
		group: 'Research',
	},
	{
		id: 'news',
		label: 'News',
		description: 'Headline digest and catalysts',
		hint: 'Ticker and optional limit, like `AAPL 12`.',
		promptPlaceholder: 'TSLA 8',
		group: 'Research',
	},
	{
		id: 'compare',
		label: 'Compare',
		description: 'Relative performance and quality',
		hint: 'Compare multiple tickers side by side.',
		promptPlaceholder: 'META GOOGL AMZN',
		group: 'Research',
	},
	{
		id: 'chart',
		label: 'Chart',
		description: 'Generate a chart artifact',
		hint: 'Symbol and optional period, like `QQQ 1y`.',
		promptPlaceholder: 'SPY 6mo',
		group: 'Research',
	},
	{
		id: 'backtest',
		label: 'Backtest',
		description: 'Run a built-in strategy',
		hint: 'Ticker, strategy, period. Example: `AAPL sma_crossover 2y`.',
		promptPlaceholder: 'IWM breakout 3y',
		group: 'Research',
	},
	{
		id: 'portfolio',
		label: 'Portfolio',
		description: 'Portfolio construction workflow',
		hint: 'Describe a basket, objective, or optimization need.',
		promptPlaceholder: 'Build a lower-vol growth portfolio with MSFT NVDA TSM ASML',
		group: 'Build',
	},
	{
		id: 'strategy',
		label: 'Strategy',
		description: 'Generate research-driven trade ideas',
		hint: 'Ask for a strategy concept, regime fit, or implementation direction.',
		promptPlaceholder: 'Strategy ideas for GLD in a falling real-yield regime',
		group: 'Build',
	},
	{
		id: 'report',
		label: 'Report',
		description: 'Produce a memo artifact bundle',
		hint: 'Describe the company or thesis you want turned into a report.',
		promptPlaceholder: 'Create an AI infrastructure memo for AMD',
		group: 'Build',
	},
	{
		id: 'alert',
		label: 'Alert',
		description: 'Draft watch levels and triggers',
		hint: 'Describe the name or setup you want monitored.',
		promptPlaceholder: 'Draft pullback and breakout levels for PLTR',
		group: 'Build',
	},
	{
		id: 'status',
		label: 'Status',
		description: 'Provider and routing state',
		hint: 'Refresh provider, model, and health information.',
		group: 'Ops',
	},
	{
		id: 'doctor',
		label: 'Doctor',
		description: 'Dependency and install health',
		hint: 'Check Python, Node, Ollama, and registered backends.',
		group: 'Ops',
	},
	{
		id: 'models',
		label: 'Models',
		description: 'Provider model catalog',
		hint: 'Inspect bundled model suggestions by provider.',
		group: 'Ops',
	},
	{
		id: 'tools',
		label: 'Tools',
		description: 'Registered tool inventory',
		hint: 'List all callable tools available to the model.',
		group: 'Ops',
	},
	{
		id: 'keys',
		label: 'Keys',
		description: 'Key presence overview',
		hint: 'See which providers are configured without exposing secrets.',
		group: 'Ops',
	},
	{
		id: 'shortcuts',
		label: 'Shortcuts',
		description: 'Keyboard map',
		hint: 'Show navigation and control shortcuts.',
		group: 'Ops',
	},
	{
		id: 'setup-help',
		label: 'Setup',
		description: 'Configuration guidance',
		hint: 'Get setup steps for providers, keys, and local models.',
		group: 'Ops',
	},
	{
		id: 'set-provider',
		label: 'Provider',
		description: 'Set the default provider',
		hint: 'Enter a provider id like `openai`, `google`, or `ollama`.',
		promptPlaceholder: 'openai',
		group: 'Ops',
	},
	{
		id: 'set-model',
		label: 'Model',
		description: 'Set the default model',
		hint: 'Enter the exact model id you want persisted.',
		promptPlaceholder: 'gpt-5.4',
		group: 'Ops',
	},
	{
		id: 'set-key',
		label: 'API Key',
		description: 'Persist a provider key',
		hint: 'Enter `provider key`.',
		promptPlaceholder: 'openai sk-...',
		group: 'Ops',
	},
	{
		id: 'reload',
		label: 'Reload',
		description: 'Reload the router from config',
		hint: 'Refresh the in-process routing state after config changes.',
		group: 'Ops',
	},
	{
		id: 'export',
		label: 'Export',
		description: 'Save the current session',
		hint: 'Write a markdown export to `~/.ephemeral/exports`.',
		group: 'Ops',
	},
	{
		id: 'legacy-ui',
		label: 'Legacy UI',
		description: 'Open the Textual shell',
		hint: 'Switch to the older Textual interface.',
		group: 'Ops',
	},
	{
		id: 'help',
		label: 'Help',
		description: 'Show slash commands and tips',
		hint: 'Display the built-in command map.',
		group: 'Ops',
	},
];

export const parseSlashCommand = (raw: string): BridgeRequest | null => {
	const trimmed = raw.trim();
	if (!trimmed.startsWith('/')) {
		return null;
	}

	const [command, ...rest] = trimmed.slice(1).split(/\s+/);
	const joined = rest.join(' ');
	switch (command) {
		case 'help':
			return {action: 'help'};
		case 'shortcuts':
			return {action: 'shortcuts'};
		case 'keys':
			return {action: 'keys'};
		case 'ask':
			return {action: 'ask', query: joined};
		case 'quote':
			return {action: 'quote', symbols: rest};
		case 'news':
		case 'digest': {
			const maybeLimit = Number(rest.at(-1));
			return {
				action: 'news',
				symbol: rest[0] ?? '',
				limit: Number.isFinite(maybeLimit) ? maybeLimit : 10,
				query: '',
			};
		}
		case 'compare':
			return {action: 'compare', symbols: rest};
		case 'chart':
			return {action: 'chart', symbol: rest[0] ?? '', period: rest[1] ?? '6mo'};
		case 'backtest':
			return {
				action: 'backtest',
				symbol: rest[0] ?? '',
				strategy: rest[1] ?? 'sma_crossover',
				period: rest[2] ?? '1y',
			};
		case 'portfolio':
			return {action: 'portfolio', query: joined || 'Build a resilient growth portfolio with MSFT NVDA TSM ASML'};
		case 'strategy':
			return {action: 'strategy', query: joined || 'Generate strategy ideas for GLD in a falling real-yield regime'};
		case 'report':
			return {action: 'report', query: joined || 'Create an AI infrastructure memo for AMD'};
		case 'alert':
		case 'watchlist':
			return {action: 'alert', query: joined || 'Draft pullback and breakout levels for PLTR'};
		case 'status':
			return {action: 'status'};
		case 'doctor':
			return {action: 'doctor'};
		case 'models':
			return {action: 'models'};
		case 'tools':
			return {action: 'tools'};
		case 'provider':
			return rest.length > 0 ? {action: 'set-provider', provider: rest[0] ?? ''} : {action: 'status'};
		case 'model':
			return rest.length > 0 ? {action: 'set-model', model: joined} : {action: 'models'};
		case 'setkey':
			return {action: 'set-key', provider: rest[0] ?? '', key: rest.slice(1).join(' ')};
		case 'reload':
			return {action: 'reload'};
		case 'setup-help':
		case 'preset':
			return {action: 'setup-help'};
		case 'export':
			return {action: 'export'};
		case 'legacy':
			return {action: 'legacy-ui'};
		default:
			return {action: 'ask', query: trimmed.slice(1)};
	}
};

export const requestForAction = (
	selectedAction: ActionDefinition,
	rawInput: string,
): BridgeRequest => {
	const input = rawInput.trim();
	switch (selectedAction.id) {
		case 'help':
		case 'shortcuts':
		case 'keys':
		case 'status':
		case 'doctor':
		case 'models':
		case 'tools':
		case 'reload':
		case 'setup-help':
		case 'export':
		case 'legacy-ui':
			return {action: selectedAction.id};
		case 'ask':
			return {action: 'ask', query: input};
		case 'quote':
			return {action: 'quote', symbols: input.split(/[,\s]+/).filter(Boolean)};
		case 'news': {
			const parts = input.split(/[,\s]+/).filter(Boolean);
			const maybeLimit = Number(parts.at(-1));
			return {
				action: 'news',
				symbol: parts[0] ?? '',
				limit: Number.isFinite(maybeLimit) ? maybeLimit : 10,
				query: '',
			};
		}
		case 'compare':
			return {action: 'compare', symbols: input.split(/[,\s]+/).filter(Boolean)};
		case 'chart': {
			const parts = input.split(/[,\s]+/).filter(Boolean);
			return {action: 'chart', symbol: parts[0] ?? '', period: parts[1] ?? '6mo'};
		}
		case 'backtest': {
			const parts = input.split(/[,\s]+/).filter(Boolean);
			return {
				action: 'backtest',
				symbol: parts[0] ?? '',
				strategy: parts[1] ?? 'sma_crossover',
				period: parts[2] ?? '1y',
			};
		}
		case 'portfolio':
		case 'strategy':
		case 'report':
		case 'alert':
			return {action: selectedAction.id, query: input};
		case 'set-provider':
			return {action: 'set-provider', provider: input};
		case 'set-model':
			return {action: 'set-model', model: input};
		case 'set-key': {
			const [provider, ...rest] = input.split(/\s+/);
			return {action: 'set-key', provider: provider ?? '', key: rest.join(' ')};
		}
	}
};
