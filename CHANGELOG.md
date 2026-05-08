# Changelog

## 2026-05-08 - Iteration 4 (Implementation MVP)

What changed:
- Added Python package skeleton (`pyproject.toml`, `src/studyflow/`).
- Implemented retriever, planner, reviewer, orchestrator, and CLI end-to-end with explicit red→green commit pairs per module.
- Added test suite covering retrieval, planning, reviewer rules, orchestrator flow, and CLI smoke (9 tests passing).
- Synced `poc-notes.md`, `README.md`, `makeanything.md`, and `tutorial3-checklist.md` with real run output and module-based CLI command.

Why:
- Move beyond documentation-only deliverables so success criteria can be verified by running `pytest -q` and the CLI demo, not just by reading prose.

Result:
- POC satisfies QG-1 (≥5-task checklist), QG-2 (citations + fallback), and the makeanything test-first rubric item with auditable git history.

## 2026-05-08 - Iteration 3 (Rubric Alignment)

What changed:
- Added `spec.md` with quality gates and acceptance criteria.
- Added `makeanything.md` requirements tracker with evidence links.
- Refined completion status in project docs to separate done work from pending screenshots.

Why:
- Increase rubric clarity and make grading artifacts easier to validate.

Result:
- Project now shows explicit coverage for spec quality, scoped rules, and iterative refinement evidence.

## 2026-05-07 - Iteration 2 (Architecture and POC Consolidation)

What changed:
- Expanded `architecture.md` into a complete one-page proposal with diagram and risks.
- Replaced placeholder sections in `poc-notes.md` with concrete component scope and outcomes.
- Updated Tutorial 3 checklist with phase-by-phase execution tracking.

Why:
- Move from template-only documentation to submission-quality narrative.

Result:
- Deliverables became coherent and traceable from proposal to architecture to POC.

## 2026-05-06 - Iteration 1 (Initial Deliverables Scaffold)

What changed:
- Created base files: `proposal.md`, `architecture.md`, `poc-notes.md`, `tutorial3-checklist.md`.
- Created evidence folder structure for required module screenshots.

Why:
- Establish minimum required structure early to avoid last-minute file gaps.

Result:
- Repo had all required deliverable filenames and a clear path for incremental completion.
