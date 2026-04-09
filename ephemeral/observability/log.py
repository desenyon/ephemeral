"""Central logging configuration for CLI and long-running tools."""

from __future__ import annotations

import logging
import os
import sys
from pathlib import Path
from typing import Optional

_CONFIGURED = False


def configure_ephemeral_logging(
    *,
    level: int = logging.INFO,
    log_file: Optional[Path] = None,
    force: bool = False,
) -> None:
    """Idempotent basicConfig with optional file handler under ~/.ephemeral/logs."""
    global _CONFIGURED
    if _CONFIGURED and not force:
        return

    fmt = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"
    handlers: list[logging.Handler] = [logging.StreamHandler(sys.stderr)]

    if log_file is None:
        log_dir = Path(os.path.expanduser("~/.ephemeral/logs"))
        log_dir.mkdir(parents=True, exist_ok=True)
        log_file = log_dir / "ephemeral.log"

    try:
        fh = logging.FileHandler(log_file, encoding="utf-8")
        fh.setFormatter(logging.Formatter(fmt, datefmt))
        handlers.append(fh)
    except OSError:
        pass

    logging.basicConfig(level=level, format=fmt, datefmt=datefmt, handlers=handlers, force=True)
    _CONFIGURED = True


def get_logger(name: str) -> logging.Logger:
    if not _CONFIGURED:
        configure_ephemeral_logging()
    return logging.getLogger(name)
