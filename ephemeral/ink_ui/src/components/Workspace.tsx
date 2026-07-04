import React from 'react';
import {Box, Text} from 'ink';
import {renderStyledLine} from '../formatters.js';
import type {ActionDefinition, FocusPane, LineRow} from '../types.js';

type Props = {
	actionAccent: string;
	focusPane: FocusPane;
	height: number;
	selectedAction: ActionDefinition;
	width: number;
	workspaceRows: LineRow[];
};

export const Workspace = ({
	actionAccent,
	focusPane,
	height,
	selectedAction,
	width,
	workspaceRows,
}: Props) => (
	<Box width={width} height={height} flexDirection="column" borderStyle="single" borderColor={focusPane === 'workspace' ? 'cyanBright' : 'gray'} paddingX={1}>
		<Box justifyContent="space-between">
			<Text color={focusPane === 'workspace' ? 'yellow' : 'gray'} bold={focusPane === 'workspace'}>
				{selectedAction.label.toUpperCase()}
			</Text>
			<Text color="gray">workspace</Text>
		</Box>
		{workspaceRows.slice(0, Math.max(1, height - 3)).map((row, index) => (
			<Box key={`workspace-${index}`} height={1}>
				{row.node ? (
					row.node
				) : row.color || row.bold ? (
					<Text color={row.color} bold={row.bold} wrap="truncate-end">
						{row.text || ' '}
					</Text>
				) : (
					renderStyledLine(row.text, actionAccent)
				)}
			</Box>
		))}
	</Box>
);
