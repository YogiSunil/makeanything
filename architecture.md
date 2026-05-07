# Architecture Proposal: StudyFlow Coach

## 1. Project Overview

- Project name: StudyFlow Coach
- Problem statement: Students lose time switching between assignment docs, checklists, and tool outputs, which causes missed requirements and rushed submissions.
- Target users: Students managing multiple AI engineering assignments and project deliverables.
- Success outcome: A user can enter an assignment brief and receive a grounded action plan, progress checklist, and next-step recommendations in one place.

## 2. Scope

In scope:
- Parse assignment prompts and extract required deliverables.
- Retrieve project-relevant context from local course notes and project docs.
- Use tool integrations for live documentation checks and browser verification evidence.
- Generate a weekly execution plan with milestone tracking.

Out of scope:
- Full LMS integration (Canvas/Gradescope API automation).
- Multi-user authentication and shared team workspaces.

## 3. Chosen Patterns

This design uses all three Tutorial 3 patterns:

- [x] RAG
- [x] MCP
- [x] Agent SDK

## 4. System Diagram

```mermaid
flowchart TD
        U[Student User] --> UI[CLI Assistant]
        UI --> P[Planner Agent]
        P --> R[Retriever]
        R --> KB[(Local Course Docs and Project Files)]
        P --> T[MCP Tool Router]
        T --> C7[Context7 Live Docs]
        T --> BR[Browser Verification Tool]
        P --> E[Executor Agent]
        E --> Q[Task Queue and Checklist State]
        E --> RV[Reviewer Agent]
        RV --> UI
```

## 5. Pattern Details

### Pattern A: RAG

- Why this pattern fits: Assignment instructions are long and change often; retrieval reduces missed requirements by grounding outputs in local source files.
- Connected data/services: Local markdown files, project README/spec files, and saved module notes.
- One anticipated risk: Irrelevant chunks can be ranked highly and pollute answers.
- Mitigation: Add metadata filters (course/week/tag) and return top-k sources with citation display.

### Pattern B: MCP

- Why this pattern fits: Live docs and browser checks reduce API guesswork and improve evidence quality.
- Connected data/services: Context7 for version-aware docs and browser tool for visual verification screenshots.
- One anticipated risk: External tool downtime or rate limits can block workflow.
- Mitigation: Implement graceful fallback to cached notes plus retry and timeout handling.

### Pattern C: Agent SDK

- Why this pattern fits: Splitting work into planner, executor, and reviewer roles improves reliability on multi-step assignment tasks.
- Connected data/services: Planner consumes retrieved context, executor performs tool calls, reviewer checks rubric alignment.
- One anticipated risk: Extra orchestration can increase latency.
- Mitigation: Use a lightweight mode for small tasks and full multi-agent mode only for complex requests.

## 6. Request Flow

1. User submits an assignment prompt or asks for next actions.
2. Planner agent classifies the request (quick task vs. multi-step task).
3. Retriever fetches relevant local context and prior notes.
4. Executor optionally calls MCP tools for live docs or verification.
5. Reviewer checks output against rubric items and missing requirements.
6. System returns final checklist, timeline, and evidence suggestions.

## 7. Risks and Constraints

- Risk 1: Hallucinated API usage when live docs are unavailable.
- Risk 2: Over-scoped plans that are hard to finish before deadlines.
- Constraint 1: Project must remain demoable on a local machine with minimal setup.

## 8. Validation Plan

- Unit tests:
    - requirement extraction logic
    - checklist state transitions
    - source citation formatting
- Integration tests:
    - retriever plus planner output generation
    - MCP tool call success and fallback behavior
- Manual demo checklist:
    - one Tutorial 3 prompt run
    - one Wiredup prompt run
    - one hallucination comparison scenario

## 9. Milestones

- Milestone 1: Complete module notes and screenshot evidence.
- Milestone 2: Finish architecture proposal and diagram.
- Milestone 3: Build one working POC component (retrieval plus planning output).
- Milestone 4: Polish docs, run tests, and submit repo link.
