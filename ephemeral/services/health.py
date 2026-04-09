"""Aggregate connectivity and dependency health for doctor / status screens."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional

from ephemeral.config import Settings, detect_lean_installation, detect_ollama


@dataclass
class CheckResult:
    name: str
    ok: bool
    detail: str = ""


@dataclass
class ServiceHealthReport:
    """Structured output for CLI and TUI."""

    checks: List[CheckResult] = field(default_factory=list)
    router_backends: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "checks": [{"name": c.name, "ok": c.ok, "detail": c.detail} for c in self.checks],
            "router_backends": list(self.router_backends),
        }

    def all_critical_ok(self, *, require_llm: bool = True) -> bool:
        if not self.checks:
            return True
        critical = [c for c in self.checks if c.name.startswith("llm.") or c.name == "python"]
        if not critical:
            return all(c.ok for c in self.checks)
        return all(c.ok for c in critical)


def collect_service_health(
    settings: Settings,
    *,
    router_factory: Optional[Callable[[], Any]] = None,
) -> ServiceHealthReport:
    """Run lightweight checks without network except optional Ollama probe."""
    report = ServiceHealthReport()

    import sys

    report.checks.append(
        CheckResult(
            name="python.version",
            ok=sys.version_info >= (3, 11),
            detail=f"{sys.version_info.major}.{sys.version_info.minor}",
        )
    )

    ok_o, host = detect_ollama()
    report.checks.append(
        CheckResult(
            name="ollama.reachable",
            ok=ok_o,
            detail=host or "",
        )
    )

    lean_ok, lean_cli, lean_dir = detect_lean_installation()
    report.checks.append(
        CheckResult(
            name="lean.installed",
            ok=lean_ok,
            detail=f"cli={lean_cli or '—'} dir={lean_dir or '—'}",
        )
    )

    has_cloud = any(
        [
            settings.google_api_key,
            settings.openai_api_key,
            settings.anthropic_api_key,
            settings.groq_api_key,
            settings.xai_api_key,
        ]
    )
    report.checks.append(
        CheckResult(
            name="llm.cloud_key",
            ok=has_cloud or ok_o,
            detail="cloud or ollama required",
        )
    )

    if router_factory is not None:
        try:
            r = router_factory()
            report.router_backends = sorted(getattr(r, "providers", {}).keys())
        except Exception as e:
            report.checks.append(CheckResult(name="llm.router", ok=False, detail=str(e)))
    else:
        try:
            from ephemeral.llm import get_router

            r = get_router(settings, force=True)
            report.router_backends = sorted(r.providers.keys())
        except Exception as e:
            report.checks.append(CheckResult(name="llm.router", ok=False, detail=str(e)))

    return report
