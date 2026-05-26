import React from 'react';
import {Box, Text} from 'ink';
import {APP_VERSION} from '../constants.js';
import type {ActionDefinition, DeskState} from '../types.js';
import {truncate} from '../formatters.js';

type Props = {
	busy: boolean;
	desk: DeskState;
	headerTone: string;
	selectedAction: ActionDefinition;
	shellStatus: string;
	topStatusLine: string;
};

export const Chrome = ({
	busy,
	desk,
	headerTone,
	selectedAction,
	shellStatus,
	topStatusLine,
}: Props) => (
	<Box justifyContent="space-between">
		<Box flexDirection="column">
			<Text>
				<Text color="yellow" bold>
					EPHEMERAL
				</Text>
				<Text color="gray"> RESEARCH DESK </Text>
				<Text color="cyanBright" bold>
					{desk.activeSymbol}
				</Text>
				<Text color="gray"> v{APP_VERSION}</Text>
			</Text>
			<Text color="gray">
				{selectedAction.group} / {selectedAction.label} / {topStatusLine}
			</Text>
		</Box>
		<Box flexDirection="column" alignItems="flex-end">
			<Text color={headerTone}>{busy ? 'RUNNING' : 'LIVE'} · {truncate(shellStatus, 44)}</Text>
			<Text color={desk.workspaceError ? 'red' : desk.workspaceLoading ? 'yellow' : 'green'}>
				{desk.workspaceError ? 'workspace degraded' : desk.workspaceLoading ? 'syncing workspace' : 'workspace ready'}
			</Text>
		</Box>
	</Box>
);
