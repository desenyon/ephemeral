import ephemeral.tools.alpha_vantage  # noqa: F401
import ephemeral.tools.backtest  # noqa: F401
import ephemeral.tools.exa_search  # noqa: F401
import ephemeral.tools.local_backtest  # noqa: F401
import ephemeral.tools.polygon  # noqa: F401
from ephemeral.config import ErrorCode

from . import library as _library
from .adapter import register_legacy_tools
from .registry import TOOL_REGISTRY, filter_args_for_tool

_LIBRARY_EXPORTS = {name: getattr(_library, name) for name in dir(_library) if not name.startswith("_")}
globals().update(_LIBRARY_EXPORTS)
_get_polygon_key = _library._get_polygon_key
__all__ = sorted(
    list(_LIBRARY_EXPORTS)
    + ["TOOL_REGISTRY", "execute_tool", "filter_args_for_tool", "get_tools_for_llm", "_get_polygon_key"]
)

# Ensure legacy tools are registered
register_legacy_tools()


def execute_tool(name: str, args: dict):
    """Synchronous tool execution with stable error shape for CLI and tests."""
    tool = TOOL_REGISTRY.get_tool(name)
    if tool:
        try:
            return tool.func(**filter_args_for_tool(tool.func, args))
        except Exception as e:
            return {
                "error": str(e),
                "error_code": int(ErrorCode.REQUEST_FAILED),
            }
    return {
        "error": "Tool not found",
        "error_code": int(ErrorCode.UNKNOWN_ERROR),
    }

# Helpers
def get_tools_for_llm():
    return TOOL_REGISTRY.to_llm_format()
