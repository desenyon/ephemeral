import React from 'react';
import {useInput} from 'ink';
import {actions} from '../actions.js';
import type {DetailMode, FocusPane} from '../types.js';

type KeyboardControllerProps = {
	busy: boolean;
	focusPane: FocusPane;
	historyLength: number;
	input: string;
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
	useInput((value, key) => {
		if (key.ctrl && value === 'c') {
			exit();
			return;
		}

		if (key.tab) {
			setFocusPane(previous => {
				if (previous === 'actions') return 'history';
				if (previous === 'history') return 'output';
				if (previous === 'output') return 'input';
				return 'actions';
			});
			return;
		}

		if (key.leftArrow) {
			if (focusPane === 'input' && input.length > 0) {
				return;
			}
			setFocusPane(previous => {
				if (previous === 'input') return 'output';
				if (previous === 'output') return 'history';
				if (previous === 'history') return 'actions';
				return 'actions';
			});
			return;
		}

		if (key.rightArrow) {
			if (focusPane === 'input' && input.length > 0) {
				return;
			}
			setFocusPane(previous => {
				if (previous === 'actions') return 'history';
				if (previous === 'history') return 'output';
				if (previous === 'output') return 'input';
				return 'input';
			});
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

		if (key.downArrow && focusPane === 'input' && !input.trim()) {
			setSelectedActionIndex(previous => (previous + 1) % actions.length);
			return;
		}

		if (key.upArrow && focusPane === 'input' && !input.trim()) {
			setSelectedActionIndex(previous => (previous - 1 + actions.length) % actions.length);
			return;
		}

		if ((value === 'j' || key.downArrow) && focusPane !== 'input') {
			if (focusPane === 'actions') {
				setSelectedActionIndex(previous => (previous + 1) % actions.length);
				return;
			}
			if (focusPane === 'history') {
				setSelectedHistoryIndex(previous => Math.min(Math.max(historyLength - 1, 0), previous + 1));
				return;
			}
			if (focusPane === 'output') {
				setOutputScroll(previous => previous + Math.max(1, Math.floor(outputViewportHeight / 3)));
				return;
			}
		}

		if ((value === 'k' || key.upArrow) && focusPane !== 'input') {
			if (focusPane === 'actions') {
				setSelectedActionIndex(previous => (previous - 1 + actions.length) % actions.length);
				return;
			}
			if (focusPane === 'history') {
				setSelectedHistoryIndex(previous => Math.max(0, previous - 1));
				return;
			}
			if (focusPane === 'output') {
				setOutputScroll(previous => Math.max(0, previous - Math.max(1, Math.floor(outputViewportHeight / 3))));
				return;
			}
		}

		if (value === '[') {
			setOutputScroll(previous => Math.max(0, previous - Math.max(1, outputViewportHeight - 2)));
			return;
		}

		if (value === ']') {
			setOutputScroll(previous => previous + Math.max(1, outputViewportHeight - 2));
			return;
		}

		if (value.toLowerCase() === 'd' && !input.trim()) {
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
