import React from 'react';
import {Box, Text} from 'ink';
import {truncate} from '../formatters.js';
import type {DeskState, FocusPane} from '../types.js';

type Props = {
	desk: DeskState;
	focusPane: FocusPane;
	height: number;
	width: number;
};

const quoteLine = (quote: any) => {
	if (!quote || quote.state === 'error') {
		return 'quote unavailable';
	}
	const price = Number(quote.price ?? 0);
	const change = Number(quote.change_percent ?? 0);
	const sign = change >= 0 ? '+' : '';
	return `$${price.toFixed(2)} ${sign}${change.toFixed(2)}%`;
};

export const RightRail = ({desk, focusPane, height, width}: Props) => {
	const quote = desk.workspace?.quote;
	const setupIssues = desk.workspace?.setup_issues ?? [];
	const warnings = desk.workspace?.panel_warnings ?? [];
	const news = desk.workspace?.news ?? [];
	const artifacts = desk.workspace?.artifacts ?? [];
	const rows: React.ReactNode[] = [
		<Text key="context-title" color={focusPane === 'workspace' ? 'magentaBright' : 'gray'} bold>
			CONTEXT
		</Text>,
		<Text key="symbol" color="cyanBright" bold>
			{desk.activeSymbol} {quoteLine(quote)}
		</Text>,
		<Text key="source" color="gray">
			{desk.workspaceLoading ? 'hydrating panels' : desk.workspaceError ? desk.workspaceError : 'snapshot ready'}
		</Text>,
		<Text key="gap-1"> </Text>,
		<Text key="issues-title" color={setupIssues.length ? 'yellow' : 'green'} bold>
			SETUP
		</Text>,
	];

	if (setupIssues.length) {
		for (const issue of setupIssues.slice(0, 3)) {
			rows.push(
				<Text key={`issue-${issue.code ?? issue.message}`} color="yellow" wrap="truncate-end">
					{truncate(String(issue.message ?? issue.code ?? 'setup issue'), width - 3)}
				</Text>,
			);
		}
	} else {
		rows.push(<Text key="setup-ok" color="green">No required setup blockers</Text>);
	}

	rows.push(<Text key="gap-2"> </Text>);
	rows.push(<Text key="news-title" color="yellow" bold>NEWS</Text>);
	if (news.length) {
		for (const article of news.slice(0, 5)) {
			rows.push(
				<Text key={`news-${article.title ?? Math.random()}`} color="white" wrap="truncate-end">
					{truncate(String(article.title ?? 'Untitled'), width - 3)}
				</Text>,
			);
		}
	} else {
		rows.push(<Text key="news-empty" color="gray">No headlines loaded</Text>);
	}

	rows.push(<Text key="gap-3"> </Text>);
	rows.push(<Text key="artifacts-title" color="magentaBright" bold>ARTIFACTS</Text>);
	if (artifacts.length) {
		for (const artifact of artifacts.slice(0, 4)) {
			rows.push(
				<Text key={`artifact-${artifact.path ?? artifact.name}`} color="gray" wrap="truncate-end">
					{truncate(String(artifact.name ?? artifact.path), width - 3)}
				</Text>,
			);
		}
	} else {
		rows.push(<Text key="artifacts-empty" color="gray">No artifacts yet</Text>);
	}

	if (warnings.length) {
		rows.push(<Text key="gap-4"> </Text>);
		rows.push(<Text key="warnings-title" color="red" bold>WARNINGS</Text>);
		for (const warning of warnings.slice(0, 3)) {
			rows.push(<Text key={warning} color="red" wrap="truncate-end">{truncate(warning, width - 3)}</Text>);
		}
	}

	return (
		<Box width={width} height={height} flexDirection="column" borderStyle="single" borderColor={focusPane === 'right' ? 'magentaBright' : 'gray'} paddingX={1}>
			{rows.slice(0, Math.max(1, height - 2))}
		</Box>
	);
};
