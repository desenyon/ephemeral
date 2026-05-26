import {useEffect, useState} from 'react';
import {useStdout} from 'ink';

export const useTerminalSize = () => {
	const {stdout} = useStdout();
	const [dimensions, setDimensions] = useState(() => ({
		width: stdout?.columns ?? process.stdout.columns ?? 120,
		height: stdout?.rows ?? process.stdout.rows ?? 40,
	}));

	useEffect(() => {
		const stream = stdout ?? process.stdout;
		const update = () => {
			setDimensions({
				width: stream?.columns ?? process.stdout.columns ?? 120,
				height: stream?.rows ?? process.stdout.rows ?? 40,
			});
		};

		update();
		stream?.on?.('resize', update);
		return () => {
			stream?.off?.('resize', update);
		};
	}, [stdout]);

	return dimensions;
};
