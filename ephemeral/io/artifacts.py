"""Write multi-file research artifacts under ~/.ephemeral/artifacts."""

from __future__ import annotations

import json
import zipfile
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional


@dataclass
class ArtifactBundle:
    """Named collection of text/json/markdown blobs."""

    name: str
    files: Dict[str, str] = field(default_factory=dict)
    meta: Dict[str, Any] = field(default_factory=dict)

    def add_text(self, path: str, content: str) -> None:
        self.files[path] = content

    def add_json(self, path: str, obj: Any) -> None:
        self.files[path] = json.dumps(obj, indent=2, default=str)


def write_artifact_bundle(
    bundle: ArtifactBundle,
    *,
    root: Optional[Path] = None,
    as_zip: bool = False,
) -> Path:
    """Persist bundle to ~/.ephemeral/artifacts/<timestamp>_<name>/ or .zip."""
    base = root or Path.home() / ".ephemeral" / "artifacts"
    base.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe = "".join(c if c.isalnum() or c in "-_" else "_" for c in bundle.name)[:80]
    target_dir = base / f"{stamp}_{safe}"
    if as_zip:
        zpath = base / f"{stamp}_{safe}.zip"
        with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as zf:
            manifest = {"name": bundle.name, "meta": bundle.meta, "files": list(bundle.files.keys())}
            zf.writestr("manifest.json", json.dumps(manifest, indent=2))
            for rel, content in bundle.files.items():
                zf.writestr(rel, content)
        return zpath

    target_dir.mkdir(parents=True, exist_ok=False)
    manifest = {"name": bundle.name, "meta": bundle.meta, "files": list(bundle.files.keys())}
    (target_dir / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    for rel, content in bundle.files.items():
        p = target_dir / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
    return target_dir
