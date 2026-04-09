"""Lightweight research session state machine (offline / orchestration)."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable, Dict, List


class ResearchPhase(str, Enum):
    INTAKE = "intake"
    DATA_GATHER = "data_gather"
    ANALYSIS = "analysis"
    SYNTHESIS = "synthesis"
    REVIEW = "review"
    EXPORT = "export"


@dataclass
class ResearchSession:
    """Tracks phases, notes, and artifacts for a single research thread."""

    topic: str
    phase: ResearchPhase = ResearchPhase.INTAKE
    notes: List[str] = field(default_factory=list)
    artifacts: Dict[str, Any] = field(default_factory=dict)
    checklist: Dict[str, bool] = field(default_factory=dict)

    def advance(self, new_phase: ResearchPhase) -> None:
        self.phase = new_phase

    def log(self, line: str) -> None:
        self.notes.append(line)

    def set_artifact(self, name: str, value: Any) -> None:
        self.artifacts[name] = value

    def ensure_checklist(self, items: List[str]) -> None:
        for it in items:
            self.checklist.setdefault(it, False)

    def check(self, item: str) -> None:
        if item in self.checklist:
            self.checklist[item] = True

    def completion_ratio(self) -> float:
        if not self.checklist:
            return 0.0
        done = sum(1 for v in self.checklist.values() if v)
        return done / max(1, len(self.checklist))

    def default_equity_checklist(self) -> None:
        self.ensure_checklist(
            [
                "Quote & liquidity",
                "Key metrics / valuation",
                "Catalysts & risks",
                "News / sentiment scan",
                "Peer comparison",
                "Thesis & price target (if applicable)",
            ]
        )

    def run_phase(
        self,
        phase: ResearchPhase,
        fn: Callable[["ResearchSession"], None],
    ) -> None:
        self.advance(phase)
        fn(self)
