import {spawn} from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import process from 'node:process';
import {fileURLToPath} from 'node:url';
import type {BridgeEnvelope, BridgeRequest} from './types.js';

const sourceDir = path.dirname(fileURLToPath(import.meta.url));
const defaultProjectRoot = path.resolve(sourceDir, '..', '..', '..');
const bundledPython = path.resolve(
	defaultProjectRoot,
	'.venv',
	process.platform === 'win32' ? path.join('Scripts', 'python.exe') : path.join('bin', 'python'),
);

export const pythonExecutable =
	process.env.EPHEMERAL_PYTHON_EXECUTABLE ?? (fs.existsSync(bundledPython) ? bundledPython : 'python3');
export const projectRoot = process.env.EPHEMERAL_PROJECT_ROOT ?? defaultProjectRoot;

type PendingBridgeRequest = {
	resolve: (result: BridgeEnvelope) => void;
	reject: (error: Error) => void;
};

class PersistentBridgeClient {
	private child = spawn(pythonExecutable, ['-m', 'ephemeral.ink_bridge', '--server'], {
		cwd: projectRoot,
		env: process.env,
		stdio: ['pipe', 'pipe', 'pipe'],
	});

	private buffer = '';
	private stderr = '';
	private nextId = 0;
	private closed = false;
	private pending = new Map<string, PendingBridgeRequest>();

	constructor() {
		this.child.stdout.on('data', chunk => {
			this.buffer += String(chunk);
			this.flushBuffer();
		});

		this.child.stderr.on('data', chunk => {
			this.stderr += String(chunk);
		});

		this.child.on('error', error => {
			this.failAll(error.message);
		});

		this.child.on('close', code => {
			this.closed = true;
			if (bridgeClient === this) {
				bridgeClient = null;
			}
			this.failAll(this.stderr.trim() || `Bridge exited with code ${code ?? 'unknown'}`);
		});
	}

	isClosed() {
		return this.closed;
	}

	request(request: BridgeRequest): Promise<BridgeEnvelope> {
		if (this.closed || this.child.stdin.destroyed) {
			return Promise.reject(new Error('Bridge is not available.'));
		}

		const id = `bridge-${++this.nextId}`;
		return new Promise((resolve, reject) => {
			this.pending.set(id, {resolve, reject});
			this.child.stdin.write(`${JSON.stringify({id, payload: request})}\n`, error => {
				if (!error) {
					return;
				}
				this.pending.delete(id);
				reject(error);
			});
		});
	}

	close() {
		if (this.closed) {
			return;
		}

		this.closed = true;
		this.child.kill();
	}

	private flushBuffer() {
		let newlineIndex = this.buffer.indexOf('\n');
		while (newlineIndex >= 0) {
			const line = this.buffer.slice(0, newlineIndex).trim();
			this.buffer = this.buffer.slice(newlineIndex + 1);
			if (line) {
				this.resolvePacket(line);
			}
			newlineIndex = this.buffer.indexOf('\n');
		}
	}

	private resolvePacket(line: string) {
		let packet: BridgeEnvelope;
		try {
			packet = JSON.parse(line) as BridgeEnvelope;
		} catch {
			this.failAll(`Invalid bridge response: ${line}\n${this.stderr}`);
			return;
		}

		const packetId = packet.id;
		if (!packetId) {
			return;
		}

		const pending = this.pending.get(packetId);
		if (!pending) {
			return;
		}
		this.pending.delete(packetId);

		if (!packet.ok) {
			pending.reject(new Error(packet.error ?? 'Bridge request failed.'));
			return;
		}

		pending.resolve(packet);
	}

	private failAll(message: string) {
		if (bridgeClient === this) {
			bridgeClient = null;
		}

		for (const [id, pending] of this.pending.entries()) {
			this.pending.delete(id);
			pending.reject(new Error(message));
		}
	}
}

let bridgeClient: PersistentBridgeClient | null = null;
let bridgeCleanupRegistered = false;

const getBridgeClient = () => {
	if (!bridgeClient || bridgeClient.isClosed()) {
		bridgeClient = new PersistentBridgeClient();
	}

	if (!bridgeCleanupRegistered) {
		bridgeCleanupRegistered = true;
		process.on('exit', () => {
			bridgeClient?.close();
		});
	}

	return bridgeClient;
};

export const invokeBridge = async (request: BridgeRequest): Promise<BridgeEnvelope> =>
	getBridgeClient().request(request);
