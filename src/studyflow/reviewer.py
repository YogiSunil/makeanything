from __future__ import annotations

from dataclasses import dataclass

from studyflow.planner import PlanResult


@dataclass
class ReviewResult:
    is_valid: bool
    issues: list[str]


def review_plan(plan: PlanResult) -> ReviewResult:
    issues: list[str] = []

    if len(plan.checklist) < 5:
        issues.append("Checklist must include at least 5 tasks.")

    if not plan.used_fallback and not plan.citations:
        issues.append("Citations are required when fallback mode is not used.")

    return ReviewResult(is_valid=len(issues) == 0, issues=issues)
