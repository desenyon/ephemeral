"""External agent-harness backends (Pi, Codex CLI) that complement Ephemeral's own LLMRouter.

Each module here shells out to a separate agentic CLI, gives it access to Ephemeral's
real research tools via the MCP server in :mod:`ephemeral.mcp_server`, and normalizes
its output into the same ``{"response": str, "steps": [...]}`` shape so callers (the
Ink bridge, the multi-agent race pane) can treat every backend interchangeably.
"""
