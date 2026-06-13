import React from 'react';
import {Box, Text} from 'ink';
import {actions} from '../actions.js';
import {pickGroupColor, truncate} from '../formatters.js';
import type {ActionDefinition, ActivityRow, DeskState, FocusPane} from '../types.js';

type Props = {
	activityRows: ActivityRow[];
	desk: DeskState;
	focusPane: FocusPane;
	height: number;
	selectedAction: ActionDefinition;
	width: number;
};

const formatQuoteRow = (row: any, width: number) => {
	const symbol = String(row?.symbol ?? '').padEnd(5);
	if (row?.state === 'error') {
		return `${symbol} data unavailable`;
	}
	const price = Number(row?.price ?? 0);
	const change = Number(row?.change_percent ?? 0);
	const sign = change >= 0 ? '+' : '';
	return truncate(`${symbol} ${price ? price.toFixed(2) : 'n/a'} ${sign}${change.toFixed(2)}%`, width);
};

export const LeftRail = ({
	activityRows,
	desk,
	focusPane,
	height,
	selectedAction,
	width,
}: Props) => {
	const rows: React.ReactNode[] = [];
	const watchlist = desk.workspace?.watchlist?.length ? desk.workspace.watchlist : desk.watchlist.map(symbol => ({symbol}));

	rows.push(
		<Text key="watch-title" color={focusPane === 'left' ? 'yellow' : 'gray'} bold>
			WATCHLIST
		</Text>,
	);
	for (const row of watchlist.slice(0, 6)) {
		const isActive = String(row?.symbol ?? '') === desk.activeSymbol;
		rows.push(
			<Text key={`watch-${row?.symbol}`} color={isActive ? 'cyanBright' : row?.state === 'error' ? 'red' : 'white'} bold={isActive} wrap="truncate-end">
				{isActive ? '>' : ' '} {formatQuoteRow(row, width - 3)}
			</Text>,
		);
	}
	rows.push(<Text key="gap-1"> </Text>);

	for (const group of ['Research', 'Build', 'Ops'] as const) {
		rows.push(
			<Text key={`group-${group}`} color={selectedAction.group === group ? pickGroupColor(group) : 'gray'} bold>
				{group.toUpperCase()}
			</Text>,
		);
		for (const action of actions.filter(item => item.group === group)) {
			const selected = action.id === selectedAction.id;
			rows.push(
				<Text key={`action-${action.id}`} color={selected ? pickGroupColor(group) : 'gray'} bold={selected} wrap="truncate-end">
					{selected ? '>' : ' '} {action.label}
				</Text>,
			);
		}
	}
	rows.push(<Text key="gap-2"> </Text>);
	rows.push(
		<Text key="recent-title" color={focusPane === 'left' ? 'cyanBright' : 'gray'} bold>
			ACTIVITY
		</Text>,
	);
	if (activityRows.length) {
		for (const row of activityRows.slice(0, 4)) {
			rows.push(
				<Text key={row.id} color={row.selected ? 'cyanBright' : row.error ? 'red' : 'gray'} bold={row.selected} wrap="truncate-end">
					{row.selected ? '>' : ' '} {truncate(row.label, Math.max(8, width - 11))} {row.timestamp}
				</Text>,
			);
		}
	} else {
		rows.push(<Text key="no-activity" color="gray">No runs yet</Text>);
	}

	return (
		<Box width={width} height={height} flexDirection="column" borderStyle="single" borderColor={focusPane === 'left' ? 'yellow' : 'gray'} paddingX={1}>
			{rows.slice(0, Math.max(1, height - 2))}
		</Box>
	);
};
