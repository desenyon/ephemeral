import {useEffect} from 'react';
import {useStdin} from 'ink';
import {smokeTest} from '../constants.js';

export const useRawMode = () => {
	const stdinControls = useStdin();

	useEffect(() => {
		const supportCheck = stdinControls?.isRawModeSupported;
		const supported = typeof supportCheck === 'boolean' ? supportCheck : true;

		if (smokeTest || !supported || typeof stdinControls?.setRawMode !== 'function') {
			return;
		}

		stdinControls.setRawMode(true);
		return () => {
			stdinControls.setRawMode(false);
		};
	}, [stdinControls]);
};
