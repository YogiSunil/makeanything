from __future__ import annotations

from dataclasses import dataclass

from studyflow.planner import PlanResult, build_plan
from studyflow.retriever import retrieve
from studyflow.reviewer import ReviewResult, review_plan


@dataclass
class PipelineResult:
    plan: PlanResult
    review: ReviewResult


def run_pipeline(prompt: str, docs: dict[str, str]) -> PipelineResult:
    retrieved = retrieve(prompt, docs, top_k=3)
    plan = build_plan(prompt, retrieved)
    review = review_plan(plan)
    return PipelineResult(plan=plan, review=review)
