from __future__ import annotations

from studyflow.planner import build_plan
from studyflow.retriever import RetrievedResult


def test_build_plan_returns_minimum_five_tasks_and_citations():
    retrieved = [
        RetrievedResult(
            source="assignment.md",
            score=3,
            text="Complete architecture proposal, build POC component, and capture evidence.",
        )
    ]

    result = build_plan("plan my tutorial deliverables", retrieved)

    assert len(result.checklist) >= 5
    assert result.citations == ["assignment.md"]
    assert result.used_fallback is False


def test_build_plan_uses_fallback_when_context_is_empty():
    result = build_plan("plan my tutorial deliverables", [])

    assert len(result.checklist) >= 5
    assert result.used_fallback is True
    assert result.citations == []
