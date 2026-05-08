# Final Project

This repository contains the final project deliverables and implementation work.

## What This Project Is About

StudyFlow Coach is a small AI-assisted planning tool for school assignments.
It takes one assignment prompt and turns it into a practical checklist that is:

- specific and actionable
- grounded in local project documents
- transparent through source citations
- safe with fallback behavior when context is weak

The project demonstrates three Tutorial 3 patterns in one MVP:

- RAG-style retrieval from local markdown notes
- MCP-aware architecture for optional external tool execution
- Agent-style pipeline roles (planner plus reviewer)

## How It Works

The current MVP runs as a command-line pipeline:

1. You provide a prompt and local context documents.
2. The retriever ranks the most relevant text chunks from those documents.
3. The planner generates at least 5 checklist steps with citations.
4. The reviewer validates structure and flags any quality issues.
5. The CLI prints the final plan and review result.

If retrieval confidence is low, the pipeline returns a safe fallback response instead of low-quality guidance.

## Tutorial 3 Deliverables

- [x] Complete required module: RAG with Claude
- [x] Complete required module: MCP Integration
- [x] Complete required module: Agent SDK
- [x] Capture screenshot evidence for each required module
- [x] Write architecture proposal in architecture.md
- [x] Build one proof of concept component
- [x] Document proof of concept in poc-notes.md
- [x] Add, commit, and push changes to GitHub

## Files

- tutorial3-checklist.md: Step-by-step checklist for Tutorial 3
- architecture.md: One-page architecture proposal with system diagram
- poc-notes.md: Brief proof-of-concept report
- evidence/screenshots/: Screenshot evidence

## Certification and Module Evidence Screenshots

### RAG Module (100%)

![RAG Module Progress](evidence/screenshots/rag-progress.png)

### MCP Integration Module (100%)

![MCP Module Progress](evidence/screenshots/mcp-progress.png)

### Agent SDK / End Course Module (100%)

![Agent SDK Module Progress](evidence/screenshots/agent-sdk-progress.png)

### Specialization Certificate

![Mastering Claude AI Certificate](evidence/screenshots/certificate.png)

## Current Status

- Completed: proposal.md, architecture.md, poc-notes.md, checklist setup, and Tutorial 3 screenshot evidence.
- Remaining: submit final GitHub link via Gradescope.

## MVP Contract (Locked)

Input:
- One assignment prompt from the user.

Output:
- At least 5 actionable checklist steps.
- Source citations to local markdown context.
- At least one risk note.
- Fallback response when context is weak.

Implementation boundaries:
- One CLI command for end-to-end planning flow.
- One output format for consistency and testability.
- One test suite proving retrieval, planning, and fallback behavior.

## Run and Verify

Run planner flow (current scaffold command):

```bash
PYTHONPATH=src python -m studyflow.cli "Plan my final project" --docs "proposal.md::Build retrieval planner and capture evidence||spec.md::Return at least 5 tasks with fallback"
```

Run tests:

```bash
pytest -q
```

Latest observed test result: 9 passed.

## MCP in This Build

- Design role: MCP is represented as the executor/tool path in the architecture (`Context7` + browser verification).
- Development role: live-doc and verification decisions were validated during implementation workflow and captured in companion evidence under the wiredup project.
- MVP behavior: current CLI keeps local retrieval-first execution and leaves MCP calls as an optional extension path, which keeps the core flow stable even when external tools are unavailable.

## Suggested Commit Sequence

1. `docs: add tutorial 3 checklist and architecture draft`
2. `feat: add poc component with tests`
3. `docs: add poc notes and module screenshot evidence`
