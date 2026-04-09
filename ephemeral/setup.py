"""Setup entry point and metadata (used by `ephemeral-setup` console script)."""

from __future__ import annotations

from .setup_agent import run_setup
from .version import VERSION

__version__ = VERSION

__all__ = ["__version__", "run_setup"]
