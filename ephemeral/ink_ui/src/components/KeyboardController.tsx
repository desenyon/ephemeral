import React from 'react';
import {useInput} from 'ink';
import {actions} from '../actions.js';
import type {DetailMode, FocusPane} from '../types.js';

type KeyboardControllerProps = {
	busy: boolean;
	focusPane: FocusPane;
	historyLength: number;
	input: string;
	onRefreshWorkspace?: () => void;
	onRun: (currentInput: string) => void;
	outputViewportHeight: number;
	setDetailMode: React.Dispatch<React.SetStateAction<DetailMode>>;
	setFocusPane: React.Dispatch<React.SetStateAction<FocusPane>>;
	setInput: React.Dispatch<React.SetStateAction<string>>;
	setOutputScroll: React.Dispatch<React.SetStateAction<number>>;
	setSelectedActionIndex: React.Dispatch<React.SetStateAction<number>>;
	setSelectedHistoryIndex: React.Dispatch<React.SetStateAction<number>>;
	exit: () => void;
};

export const KeyboardController = ({
	busy,
	focusPane,
	historyLength,
	input,
	onRefreshWorkspace,
	onRun,
	outputViewportHeight,
	setDetailMode,
	setFocusPane,
	setInput,
	setOutputScroll,
	setSelectedActionIndex,
	setSelectedHistoryIndex,
	exit,
}: KeyboardControllerProps) => {
	const nextPane = (pane: FocusPane): FocusPane => {
		if (pane === 'left') return 'workspace';
		if (pane === 'workspace') return 'right';
		if (pane === 'right') return 'input';
		return 'left';
	};

	const previousPane = (pane: FocusPane): FocusPane => {
		if (pane === 'input') return 'right';
		if (pane === 'right') return 'workspace';
		if (pane === 'workspace') return 'left';
		return 'left';
	};

	useInput((value, key) => {
		if (key.ctrl && value === 'c') {
			exit();
			return;
		}

		if (key.tab) {
			setFocusPane(previous => nextPane(previous));
			return;
		}

		if (key.leftArrow) {
			if (focusPane === 'input' && input.length > 0) {
				return;
			}
			setFocusPane(previous => previousPane(previous));
			return;
		}

		if (key.rightArrow) {
			if (focusPane === 'input' && input.length > 0) {
				return;
			}
			setFocusPane(previous => nextPane(previous));
			return;
		}

		if (key.ctrl && value === 'r' && onRefreshWorkspace) {
			onRefreshWorkspace();
			return;
		}

		if (key.ctrl && value === 'l') {
			setSelectedHistoryIndex(0);
			setOutputScroll(0);
			return;
		}

		if (key.escape) {
			setInput('');
			setFocusPane('input');
			return;
		}

		if (value === '/' && !input.trim()) {
			setFocusPane('input');
			setInput('/');
			return;
		}

		if (key.downArrow && focusPane === 'input' && !input.trim()) {
			setSelectedActionIndex(previous => (previous + 1) % actions.length);
			return;
		}

		if (key.upArrow && focusPane === 'input' && !input.trim()) {
			setSelectedActionIndex(previous => (previous - 1 + actions.length) % actions.length);
			return;
		}

		if ((value === 'j' || key.downArrow) && focusPane !== 'input') {
			if (focusPane === 'left') {
				setSelectedActionIndex(previous => (previous + 1) % actions.length);
				return;
			}
			if (focusPane === 'workspace') {
				setOutputScroll(previous => previous + Math.max(1, Math.floor(outputViewportHeight / 3)));
				return;
			}
			if (focusPane === 'right') {
				setSelectedHistoryIndex(previous => Math.min(Math.max(historyLength - 1, 0), previous + 1));
				return;
			}
		}

		if ((value === 'k' || key.upArrow) && focusPane !== 'input') {
			if (focusPane === 'left') {
				setSelectedActionIndex(previous => (previous - 1 + actions.length) % actions.length);
				return;
			}
			if (focusPane === 'workspace') {
				setOutputScroll(previous => Math.max(0, previous - Math.max(1, Math.floor(outputViewportHeight / 3))));
				return;
			}
			if (focusPane === 'right') {
				setSelectedHistoryIndex(previous => Math.max(0, previous - 1));
				return;
			}
		}

		if (value === '[' && focusPane === 'workspace') {
			setOutputScroll(previous => Math.max(0, previous - Math.max(1, outputViewportHeight - 2)));
			return;
		}

		if (value === ']' && focusPane === 'workspace') {
			setOutputScroll(previous => previous + Math.max(1, outputViewportHeight - 2));
			return;
		}

		if (value.toLowerCase() === 'd' && focusPane !== 'input') {
			setDetailMode(previous => (previous === 'rendered' ? 'raw' : 'rendered'));
			return;
		}

		if (key.return) {
			if (busy) {
				return;
			}
			onRun(input);
			return;
		}

		if (key.backspace || key.delete) {
			setFocusPane('input');
			setInput(previous => previous.slice(0, -1));
			return;
		}

		if (!key.ctrl && !key.meta && value && !/[\r\n\t]/.test(value)) {
			setFocusPane('input');
			setInput(previous => previous + value);
		}
	});

	return null;
};
