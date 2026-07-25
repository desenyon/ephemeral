"""MCP server exposing Ephemeral's research tool registry to external agent harnesses.

Ephemeral's own :class:`~ephemeral.llm.router.LLMRouter` calls tools directly in-process.
This module exposes the same :data:`~ephemeral.tools.registry.TOOL_REGISTRY` (quote, news,
compare, chart, backtest, ...) over the Model Context Protocol, so an external agent runtime —
the Pi coding-agent harness, the OpenAI Codex CLI, or any other MCP client — can call
Ephemeral's real research tools natively instead of re-implementing them.

Run standalone for manual testing:

    python -m ephemeral.mcp_server

Point an MCP client's config at this command (stdio transport) to wire it in.
"""

from __future__ import annotations

import asyncio
import json
import logging

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool

import ephemeral.tools  # noqa: F401 — populates TOOL_REGISTRY as a side effect of import
from ephemeral.tools.registry import TOOL_REGISTRY

logger = logging.getLogger(__name__)

SERVER_NAME = "ephemeral-research-desk"


def build_server() -> Server:
    """Construct an MCP server backed by the live tool registry.

    A fresh :class:`Server` is built (rather than a module-level singleton) so tests
    can spin up isolated instances against a registry snapshot.
    """
    server: Server = Server(SERVER_NAME)

    @server.list_tools()
    async def list_tools() -> list[Tool]:
        return [
            Tool(
                name=tool.name,
                description=tool.description,
                inputSchema=tool.input_schema,
            )
            for tool in TOOL_REGISTRY.list_tools()
        ]

    @server.call_tool()
    async def call_tool(name: str, arguments: dict) -> list[TextContent]:
        try:
            result = await TOOL_REGISTRY.execute(name, arguments or {})
        except Exception as exc:  # noqa: BLE001 - surfaced to the calling agent, not raised
            result = {"error": str(exc)}
        return [TextContent(type="text", text=json.dumps(result, default=str))]

    return server


async def serve_stdio() -> None:
    server = build_server()
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options(),
        )


def main() -> None:
    logging.basicConfig(level=logging.WARNING)
    asyncio.run(serve_stdio())


if __name__ == "__main__":
    main()
