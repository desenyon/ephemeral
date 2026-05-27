import React from 'react';
import {Box, Text} from 'ink';
import type {ActionDefinition, FocusPane, ShortcutHint} from '../types.js';

type Props = {
	actionAccent: string;
	busy: boolean;
	focusPane: FocusPane;
	input: string;
	promptCursor: string;
	promptCursorColor: string;
	promptHint: string;
	selectedAction: ActionDefinition;
	shortcuts: ShortcutHint[];
};

export const CommandDock = ({
	actionAccent,
	busy,
	focusPane,
	input,
	promptCursor,
	promptCursorColor,
	promptHint,
	selectedAction,
	shortcuts,
}: Props) => (
	<Box flexDirection="column" borderStyle="single" borderColor={focusPane === 'input' ? actionAccent : 'gray'} paddingX={1}>
		<Box justifyContent="space-between">
			<Text color={focusPane === 'input' ? actionAccent : 'gray'} bold>
				{selectedAction.label}
			</Text>
			<Text color={busy ? 'yellow' : 'green'}>
				{busy ? 'RUNNING' : 'READY'}
				{!busy && focusPane === 'input' && (
					<>
						{' · '}
						<Text color="white" bold>Enter</Text>
						{' to run'}
					</>
				)}
			</Text>
		</Box>
		<Text>
			<Text color={focusPane === 'input' ? actionAccent : 'gray'}>{'> '}</Text>
			{input ? <Text>{input}</Text> : null}
			{focusPane === 'input' ? <Text color={promptCursorColor}>{promptCursor}</Text> : null}
			{!input ? <Text color="gray">{promptHint}</Text> : null}
		</Text>
		<Text color="gray">{selectedAction.description} · {selectedAction.hint}</Text>
		<Text color="gray">
			{shortcuts.map((shortcut, index) => (
				<React.Fragment key={`${shortcut.key}-${shortcut.description}`}>
					{index > 0 ? ' · ' : null}
					<Text color="white" bold>
						{shortcut.key}
					</Text>{' '}
					{shortcut.description}
				</React.Fragment>
			))}
		</Text>
	</Box>
);
