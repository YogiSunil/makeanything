from __future__ import annotations

from dataclasses import dataclass

from studyflow.retriever import RetrievedResult


@dataclass
class PlanResult:
    checklist: list[str]
    citations: list[str]
    used_fallback: bool


def build_plan(prompt: str, retrieved: list[RetrievedResult]) -> PlanResult:
    if not retrieved:
        fallback_steps = [
            "Define the assignment goal and expected final deliverables.",
            "Break the work into implementation and evidence milestones.",
            "Identify one small proof-of-concept to build first.",
            "Run validation checks and capture supporting evidence.",
            "Review rubric requirements and patch any missing artifacts.",
        ]
        return PlanResult(checklist=fallback_steps, citations=[], used_fallback=True)

    checklist = [
        "Extract required deliverables from the assignment prompt.",
        "Map each deliverable to one concrete implementation task.",
        "Implement the smallest working component first.",
        "Capture evidence and update checklist status.",
        "Run final validation and prepare submission artifacts.",
    ]

    citations = [item.source for item in retrieved]
    return PlanResult(checklist=checklist, citations=citations, used_fallback=False)
