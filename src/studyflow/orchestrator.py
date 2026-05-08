from __future__ import annotations

from dataclasses import dataclass

from studyflow.planner import PlanResult, build_plan
from studyflow.retriever import confidence_for, retrieve
from studyflow.reviewer import ReviewResult, review_plan


@dataclass
class PipelineResult:
    plan: PlanResult
    review: ReviewResult
    confidence: float
    weak_context: bool


def run_pipeline(prompt: str, docs: dict[str, str]) -> PipelineResult:
    retrieved = retrieve(prompt, docs, top_k=3)
    plan = build_plan(prompt, retrieved)
    review = review_plan(plan)
    confidence = confidence_for(prompt, retrieved)
    weak_context = plan.used_fallback or confidence < 0.2
    return PipelineResult(
        plan=plan,
        review=review,
        confidence=confidence,
        weak_context=weak_context,
    )
