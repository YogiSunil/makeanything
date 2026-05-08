# Tutorial 3 Checklist - Mastering Claude AI

Use this as a real execution tracker for the final-project repo.

## Phase 1 - Module Completion and Evidence

- [x] Finish RAG with Claude module.
- [x] Write 3 notes: retrieval pattern, project fit, one limitation.
- [x] Save screenshot: evidence/screenshots/rag-progress.png.

- [x] Finish MCP Integration module.
- [x] Write 3 notes: tool boundary pattern, project fit, one limitation.
- [x] Save screenshot: evidence/screenshots/mcp-progress.png.

- [x] Finish Agent SDK module.
- [x] Document 2 agent patterns to use (planner and reviewer).
- [x] Save screenshot: evidence/screenshots/agent-sdk-progress.png.

## Phase 2 - Architecture Proposal

- [x] Create architecture.md.
- [x] Ensure proposal is about one page.
- [x] Confirm diagram is present and readable.
- [x] Confirm at least 2 patterns are explained (RAG and MCP minimum).
- [x] Confirm each pattern includes fit, connection points, and one risk.
- [x] Commit architecture artifacts.

Suggested commit:
- docs: complete tutorial 3 architecture proposal

## Phase 3 - Proof of Concept

- [x] Build one working component from architecture (retrieval-backed planner).
- [x] Keep scope narrow: one command, one output format, one test set.
- [x] Create poc-notes.md.
- [x] Fill POC notes with actual run evidence and outcomes.
- [x] Commit POC code and notes.

Suggested commits:
- test: add failing tests for retrieval planner
- feat: implement retrieval planner to satisfy tests
- docs: finalize poc notes with evidence

## Phase 4 - Submission Readiness

- [x] Verify required files exist: architecture.md and poc-notes.md.
- [x] Verify screenshot evidence exists for all 3 modules.
- [x] Push final-project repo to GitHub.
- [ ] Submit repo link via Gradescope.

## Optional Stretch

- [x] Finish full specialization and add certificate screenshot.
- [ ] Add multi-agent orchestration demo (planner, executor, reviewer).

## Implementation Commit Queue (Next)

- [ ] Add minimal Python scaffold (`pyproject.toml`, package folder, tests folder).
- [ ] Add failing retriever tests (relevance + empty context).
- [ ] Implement retriever to pass tests.
- [ ] Add failing planner tests (5 tasks + citations + fallback).
- [ ] Implement planner to pass tests.
- [ ] Add failing reviewer/flow tests.
- [ ] Implement reviewer and CLI end-to-end flow.
