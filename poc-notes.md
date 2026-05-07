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

- Tests written before implementation:
	- returns checklist format with numbered actions
	- includes at least one source citation when context exists
	- returns safe fallback on empty context
- Initial failing behavior:
	- planner returned generic advice without citations
	- empty-context case raised an exception
- Implementation changes that made tests pass:
	- added citation requirement in planner formatter
	- added empty-context guard and fallback response
	- improved retriever relevance scoring with keyword weighting

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

- Screenshot/log reference 1: terminal run showing prompt, checklist output, and citations.
- Screenshot/log reference 2: failing-to-passing test run showing red/green cycle.
- Demo command/run steps:
	- run tests
	- run planner command with a Tutorial 3 prompt
	- run planner command with a Wiredup prompt

## 8. Next Steps

- Immediate next task: Connect planner output to milestone tracking for day-by-day execution.
- Improvements for full implementation:
	- add reviewer agent pass for rubric compliance
	- integrate live-doc tool call for API-specific tasks
	- export checklist as markdown for direct submission updates
