import React from 'react';
import {Box} from 'ink';
import type {ActionDefinition, ActivityRow, DeskState, FocusPane, LineRow, ShortcutHint} from '../types.js';
import {Chrome} from './Chrome.js';
import {CommandDock} from './CommandDock.js';
import {LeftRail} from './LeftRail.js';
import {RightRail} from './RightRail.js';
import {Workspace} from './Workspace.js';

type Props = {
	actionAccent: string;
	activityRows: ActivityRow[];
	bodyHeight: number;
	busy: boolean;
	desk: DeskState;
	focusPane: FocusPane;
	headerTone: string;
	input: string;
	promptCursor: string;
	promptCursorColor: string;
	promptHint: string;
	selectedAction: ActionDefinition;
	shellStatus: string;
	shortcuts: ShortcutHint[];
	terminalHeight: number;
	terminalWidth: number;
	topStatusLine: string;
	workspaceRows: LineRow[];
};

export const ResearchDesk = ({
	actionAccent,
	activityRows,
	bodyHeight,
	busy,
	desk,
	focusPane,
	headerTone,
	input,
	promptCursor,
	promptCursorColor,
	promptHint,
	selectedAction,
	shellStatus,
	shortcuts,
	terminalHeight,
	terminalWidth,
	topStatusLine,
	workspaceRows,
}: Props) => {
	const isDesktop = terminalWidth >= 118 && terminalHeight >= 24;
	const leftWidth = isDesktop ? Math.max(25, Math.min(32, Math.floor(terminalWidth * 0.22))) : terminalWidth - 2;
	const rightWidth = isDesktop ? Math.max(30, Math.min(40, Math.floor(terminalWidth * 0.27))) : terminalWidth - 2;
	const centerWidth = isDesktop ? Math.max(42, terminalWidth - leftWidth - rightWidth - 6) : terminalWidth - 2;
	const shellBodyHeight = Math.max(10, bodyHeight);

	return (
		<Box flexDirection="column" paddingX={1}>
			<Chrome
				busy={busy}
				desk={desk}
				headerTone={headerTone}
				selectedAction={selectedAction}
				shellStatus={shellStatus}
				topStatusLine={topStatusLine}
			/>
			{isDesktop ? (
				<Box height={shellBodyHeight}>
					<LeftRail
						activityRows={activityRows}
						desk={desk}
						focusPane={focusPane}
						height={shellBodyHeight}
						selectedAction={selectedAction}
						width={leftWidth}
					/>
					<Box width={1} />
					<Workspace
						actionAccent={actionAccent}
						focusPane={focusPane}
						height={shellBodyHeight}
						selectedAction={selectedAction}
						width={centerWidth}
						workspaceRows={workspaceRows}
					/>
					<Box width={1} />
					<RightRail
						desk={desk}
						focusPane={focusPane}
						height={shellBodyHeight}
						width={rightWidth}
					/>
				</Box>
			) : (
				<Box flexDirection="column">
					<Workspace
						actionAccent={actionAccent}
						focusPane={focusPane}
						height={Math.max(8, shellBodyHeight - 8)}
						selectedAction={selectedAction}
						width={centerWidth}
						workspaceRows={workspaceRows}
					/>
					<LeftRail
						activityRows={activityRows}
						desk={desk}
						focusPane={focusPane}
						height={8}
						selectedAction={selectedAction}
						width={leftWidth}
					/>
				</Box>
			)}
			<CommandDock
				actionAccent={actionAccent}
				busy={busy}
				focusPane={focusPane}
				input={input}
				promptCursor={promptCursor}
				promptCursorColor={promptCursorColor}
				promptHint={promptHint}
				selectedAction={selectedAction}
				shortcuts={shortcuts}
			/>
		</Box>
	);
};
