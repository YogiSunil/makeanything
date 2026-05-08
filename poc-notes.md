# Proof of Concept Notes

## 1. POC Goal

- Chosen component: Retrieval-backed assignment planner for StudyFlow Coach.
- Why this was selected: This validates the core value of the project quickly by proving that planning can be grounded in real assignment files instead of generic output.
- Success criteria:
	- given an assignment prompt, system returns a checklist with at least 5 concrete tasks
	- output includes source citations to local files
	- fallback message appears when no relevant context is found

## 2. What I Built

- Summary of implementation: Built a small pipeline that ingests local markdown instructions, retrieves top relevant chunks for a prompt, and generates a structured plan with citations.
- Files/components touched:
	- retriever module (chunking and scoring)
	- planner module (checklist generation)
	- CLI command for running a planning query
- External tools/services used:
	- local file retrieval for RAG context
	- optional live-doc lookup flow prepared via MCP integration path

## 3. Test-First Evidence

Each feature module landed via a red→green pair: a failing-test commit immediately before the implementing-feature commit. Verifiable in `git log`:

- Retriever
	- red: `c9f9420 test: add failing retriever relevance and empty-context tests` — asserts top-1 source for a relevant query and empty list when no terms overlap.
	- green: `ac63bb1 feat: implement retriever scoring for relevant context retrieval`.
	- follow-up: `edb0013 test: add failing retriever test for non-positive top_k` → `9335006 handle non-positive top_k in retriever`.
- Planner
	- red: `5c6a777 add failing planner tests for checklist citations and fallback` — asserts ≥5 checklist items, citations populated when retrieval is non-empty, and `used_fallback=True` when retrieval is empty.
	- green: `fdbf6c2 implement planner with checklist citations and fallback output`.
- Reviewer + orchestrator
	- red: `226fac9 add failing reviewer and orchestrator flow tests` — asserts reviewer flags missing citations when `used_fallback=False`, and `run_pipeline` returns a reviewed plan with ≥5 items.
	- green: `196fb02 implement reviewer rules and orchestrator pipeline`.
- CLI
	- red: `be2b515 add failing cli integration test for plan and review output` — asserts `main()` exits 0 and prints both "StudyFlow Plan" and "Review" headers.
	- green: `aa5a491 implement cli entrypoint for planning and review output`.

## 4. What Worked

- Retrieved chunks from assignment docs gave specific, actionable steps.
- Citation display made it easy to verify why each step was included.
- Test-first flow reduced regressions while refactoring planner formatting.

## 5. What Surprised Me

- Small formatting changes had a large effect on plan readability.
- Retrieval quality depended more on chunk boundaries than expected.

## 6. Risks Found During POC

- Risk: Overconfident plan output when retrieval returns weak matches.
- Impact: User may trust low-quality recommendations.
- Next mitigation step: Add relevance threshold and confidence indicator in output.

## 7. Evidence

- Screenshot/log reference 1: CLI run output showing a 5-step plan and review status `Valid: True`.
- Screenshot/log reference 2: test run output showing `9 passed`.
- Demo command/run steps:
	- set `PYTHONPATH=src`
	- run: `python -m studyflow.cli "Plan my final project" --docs "proposal.md::Build retrieval planner and capture evidence||spec.md::Return at least 5 tasks with fallback"`
	- run: `pytest -q`

Observed result summary:
	- CLI produced a structured 5-step checklist and passed reviewer validation.
	- Test suite currently reports 9 passing tests.

MCP decision log:
	- Confirmed API response-shape assumptions through live documentation workflow before finalizing field mapping strategy.
	- Kept MCP as an optional executor path in the MVP so planning remains deterministic when external tools are unavailable.

## 8. Next Steps

- Immediate next task: Connect planner output to milestone tracking for day-by-day execution.
- Improvements for full implementation:
	- add reviewer agent pass for rubric compliance
	- integrate live-doc tool call for API-specific tasks
	- export checklist as markdown for direct submission updates
