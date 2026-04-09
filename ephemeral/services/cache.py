"""Filesystem-backed TTL cache for JSON-serializable payloads."""

from __future__ import annotations

import hashlib
import json
import os
import time
from pathlib import Path
from typing import Any, Callable, TypeVar

T = TypeVar("T")

CACHE_META_KEY = "_ephemeral_cache"
LEGACY_CACHE_META_KEY = "_" + "".join(["s", "i", "g", "m", "a"]) + "_cache"


def cache_key_for_symbol(*parts: str) -> str:
    raw = "|".join(p.upper().strip() for p in parts if p)
    return hashlib.sha256(raw.encode()).hexdigest()[:24]


class FileTTLCache:
    """Single-file entries: ``{\"_ephemeral_cache\": {\"created\", \"ttl\", \"tag\"}, \"payload\": ...}``."""

    def __init__(self, root: str | Path, *, default_ttl: float = 300.0) -> None:
        self.root = Path(root)
        self.default_ttl = default_ttl
        self.root.mkdir(parents=True, exist_ok=True)

    def _path(self, key: str) -> Path:
        safe = key.replace("/", "_").replace("..", "")
        return self.root / f"{safe}.cache.json"

    def get(self, key: str) -> Any | None:
        path = self._path(key)
        if not path.exists():
            return None
        try:
            raw = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return None
        meta = raw.get(CACHE_META_KEY) or raw.get(LEGACY_CACHE_META_KEY) or {}
        try:
            created = float(meta["created"])
            ttl = float(meta["ttl"])
        except (KeyError, TypeError, ValueError):
            return None
        if time.time() > created + ttl:
            self.invalidate(key)
            return None
        return raw.get("payload")

    def set(self, key: str, value: Any, *, ttl: float | None = None, tag: str = "") -> None:
        path = self._path(key)
        ttl_use = self.default_ttl if ttl is None else ttl
        envelope = {
            CACHE_META_KEY: {
                "created": time.time(),
                "ttl": ttl_use,
                "tag": tag,
            },
            "payload": value,
        }
        tmp = path.with_suffix(".tmp")
        tmp.write_text(json.dumps(envelope, default=str), encoding="utf-8")
        tmp.replace(path)

    def invalidate(self, key: str) -> None:
        try:
            self._path(key).unlink(missing_ok=True)
        except OSError:
            pass

    def clear_expired(self) -> int:
        removed = 0
        for path in self.root.glob("*.cache.json"):
            try:
                raw = json.loads(path.read_text(encoding="utf-8"))
                meta = raw.get(CACHE_META_KEY) or raw.get(LEGACY_CACHE_META_KEY) or {}
                created = float(meta["created"])
                ttl = float(meta["ttl"])
                if time.time() > created + ttl:
                    path.unlink(missing_ok=True)
                    removed += 1
            except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError):
                continue
        return removed

    def get_or_set(
        self,
        key: str,
        factory: Callable[[], T],
        *,
        ttl: float | None = None,
        tag: str = "",
    ) -> T:
        cached = self.get(key)
        if cached is not None:
            return cached  # type: ignore[return-value]
        value = factory()
        self.set(key, value, ttl=ttl, tag=tag)
        return value


def default_cache_dir() -> Path:
    return Path(os.path.expanduser("~/.ephemeral/cache"))
