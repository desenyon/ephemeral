import type React from 'react';

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

export type FocusPane = 'actions' | 'history' | 'output' | 'input';
export type DetailMode = 'rendered' | 'raw';
export type LayoutMode = 'desktop' | 'stacked';

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

export type ActivityRow = {
	id: string;
	label: string;
	timestamp: string;
	selected: boolean;
	error?: boolean;
};

export type LineRow = {
	text: string;
	color?: string;
	bold?: boolean;
	node?: React.ReactNode;
};

export type ShortcutHint = {
	key: string;
	description: string;
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
