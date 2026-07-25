/**
 * Ephemeral Tools Extension
 *
 * Wires Ephemeral's research tool registry (quote, news, compare, chart, backtest, ...)
 * into the Pi coding-agent harness as native tools. Pi has no built-in MCP support
 * (by design — see docs/usage.md), so this extension is a small MCP *client*: it spawns
 * `python -m ephemeral.mcp_server` (see ephemeral/mcp_server.py) over stdio, lists its
 * tools once at session start, and registers each one with `pi.registerTool()` so the
 * model can call Ephemeral's real market-data and backtest tools directly.
 *
 * Auto-discovered from `.pi/extensions/` when Pi is run from the repo root (see
 * ephemeral/agents/pi_harness.py, which sets cwd accordingly).
 */

import { spawn } from "node:child_process";
import { existsSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const REPO_ROOT = join(dirname(fileURLToPath(import.meta.url)), "..", "..");

function findPython(): string {
	// Prefer the project's own uv-managed virtualenv so the tool registry (yfinance,
	// pandas, etc.) resolves the same way it does for the rest of Ephemeral.
	const venvPython = join(REPO_ROOT, ".venv", "bin", "python");
	if (existsSync(venvPython)) return venvPython;
	return process.env.EPHEMERAL_PYTHON ?? "python3";
}

export default function ephemeralToolsExtension(pi: ExtensionAPI) {
	let client: Client | undefined;
	const registered = new Set<string>();

	async function connect(): Promise<Client> {
		if (client) return client;

		const transport = new StdioClientTransport({
			command: findPython(),
			args: ["-m", "ephemeral.mcp_server"],
			cwd: REPO_ROOT,
		});

		const c = new Client({ name: "ephemeral-pi-extension", version: "1.0.0" });
		await c.connect(transport);
		client = c;
		return c;
	}

	pi.on("session_start", async (_event, ctx) => {
		try {
			const c = await connect();
			const { tools } = await c.listTools();

			for (const tool of tools) {
				if (registered.has(tool.name)) continue;
				registered.add(tool.name);

				pi.registerTool({
					name: tool.name,
					label: tool.name,
					description: tool.description ?? `Ephemeral research tool: ${tool.name}`,
					// Ephemeral's registry already emits JSON-Schema-shaped objects
					// (type/properties/required), which is exactly what `parameters`
					// expects at runtime — no typebox compilation needed here.
					parameters: (tool.inputSchema ?? { type: "object", properties: {} }) as any,
					async execute(_toolCallId, params) {
						const result = await c.callTool({ name: tool.name, arguments: params as any });
						const text = Array.isArray(result.content)
							? result.content
									.filter((b: any) => b.type === "text")
									.map((b: any) => b.text)
									.join("\n")
							: JSON.stringify(result);
						return { content: [{ type: "text", text }], details: { tool: tool.name } };
					},
				});
			}

			ctx.ui.notify(`Ephemeral: ${tools.length} research tools connected`, "info");
		} catch (err) {
			ctx.ui.notify(`Ephemeral tools unavailable: ${(err as Error).message}`, "warning");
		}
	});

	// The MCP child process (ephemeral.mcp_server) keeps its stdin open waiting for more
	// requests, which in turn keeps Node's event loop alive — without this, `pi --print`
	// never exits after a one-shot turn even though the turn itself completed correctly.
	// Closing here is safe for interactive sessions too: the next tool call lazily
	// reconnects via `connect()`.
	async function disconnect() {
		if (!client) return;
		const closing = client;
		client = undefined;
		registered.clear();
		try {
			await closing.close();
		} catch {
			// best-effort
		}
	}

	pi.on("agent_settled", disconnect);
	pi.on("session_shutdown", disconnect);
}
