"""OS-keychain-backed secret storage for BYOK API keys.

Ephemeral historically stored API keys as plaintext in ``~/.ephemeral/config.env``.
This module adds an OS keychain (macOS Keychain / Secure Storage on Windows / Secret
Service on Linux) as the preferred store, via the ``keyring`` package, with the
plaintext file remaining as an automatic fallback when no OS keychain backend is
available (e.g. headless Linux without a Secret Service daemon).

Disabled under pytest and via ``EPHEMERAL_DISABLE_KEYRING`` so automated test runs
never touch a real OS keychain or trigger interactive OS permission prompts.
"""

from __future__ import annotations

import logging
import os
from typing import List, Optional

logger = logging.getLogger(__name__)

SERVICE_NAME = "ephemeral"

_keyring_available: Optional[bool] = None


def _disabled_by_env() -> bool:
    return bool(
        os.environ.get("PYTEST_CURRENT_TEST") or os.environ.get("EPHEMERAL_DISABLE_KEYRING")
    )


def _keyring_backend_ok() -> bool:
    """Probe once whether a usable, non-interactive keychain backend is present."""
    global _keyring_available
    if _disabled_by_env():
        return False
    if _keyring_available is not None:
        return _keyring_available
    try:
        import keyring
        from keyring.backends.fail import Keyring as FailBackend

        backend = keyring.get_keyring()
        _keyring_available = not isinstance(backend, FailBackend)
    except Exception as exc:
        logger.debug("Keychain backend unavailable: %s", exc)
        _keyring_available = False
    return _keyring_available


def set_secret(env_key: str, value: str) -> bool:
    """Store a secret in the OS keychain. Returns True on success."""
    if not _keyring_backend_ok():
        return False
    try:
        import keyring

        keyring.set_password(SERVICE_NAME, env_key, value)
        return True
    except Exception as exc:
        logger.warning("Keychain write failed for %s, falling back to file: %s", env_key, exc)
        return False


def get_secret(env_key: str) -> Optional[str]:
    """Read a secret from the OS keychain, or None if unavailable/not set."""
    if not _keyring_backend_ok():
        return None
    try:
        import keyring

        return keyring.get_password(SERVICE_NAME, env_key)
    except Exception as exc:
        logger.debug("Keychain read failed for %s: %s", env_key, exc)
        return None


def delete_secret(env_key: str) -> None:
    if not _keyring_backend_ok():
        return
    try:
        import keyring
        from keyring.errors import PasswordDeleteError

        try:
            keyring.delete_password(SERVICE_NAME, env_key)
        except PasswordDeleteError:
            pass
    except Exception as exc:
        logger.debug("Keychain delete failed for %s: %s", env_key, exc)


def hydrate_environment(env_keys: List[str]) -> None:
    """Populate ``os.environ`` from the OS keychain for keys not already set.

    Lets Settings' normal env/.env loading pick up keychain-backed secrets
    transparently, without any change to how Settings resolves values.
    """
    if not _keyring_backend_ok():
        return
    for env_key in env_keys:
        if os.environ.get(env_key):
            continue
        value = get_secret(env_key)
        if value:
            os.environ[env_key] = value


def backend_label() -> str:
    """Human-readable description of the active secret storage backend."""
    if _keyring_backend_ok():
        try:
            import keyring

            return str(keyring.get_keyring())
        except Exception:
            return "OS keychain"
    return "plaintext file (~/.ephemeral/config.env)"
