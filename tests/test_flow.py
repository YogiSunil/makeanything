from __future__ import annotations

from studyflow.orchestrator import run_pipeline
from studyflow.reviewer import review_plan
from studyflow.planner import PlanResult


def test_reviewer_accepts_valid_plan():
    plan = PlanResult(
        checklist=[
            "Extract required deliverables.",
            "Map deliverables to concrete tasks.",
            "Implement the smallest working component first.",
            "Capture evidence and update checklist status.",
            "Run final validation and prepare submission artifacts.",
        ],
        citations=["proposal.md"],
        used_fallback=False,
    )

    result = review_plan(plan)
    assert result.is_valid is True
    assert result.issues == []


def test_reviewer_flags_missing_citations_when_not_fallback():
    plan = PlanResult(
        checklist=[
            "Task one.",
            "Task two.",
            "Task three.",
            "Task four.",
            "Task five.",
        ],
        citations=[],
        used_fallback=False,
    )

    result = review_plan(plan)
    assert result.is_valid is False
    assert "citations are required" in " ".join(result.issues).lower()


def test_orchestrator_returns_reviewed_plan():
    docs = {
        "assignment.md": "Build architecture proposal, implement proof of concept, and capture evidence."
    }

    result = run_pipeline("plan final project", docs)

    assert len(result.plan.checklist) >= 5
    assert result.review.is_valid is True
