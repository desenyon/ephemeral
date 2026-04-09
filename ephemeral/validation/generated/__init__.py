"""Generated validation payloads namespace (lazy attribute access)."""

from __future__ import annotations

from importlib import import_module
from typing import Any


def __getattr__(name: str) -> Any:
    mod = import_module("ephemeral.validation.generated.payloads")
    return getattr(mod, name)
