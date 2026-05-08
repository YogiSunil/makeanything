# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This repo is the Tutorial 3 final-project deliverable for the "Mastering Claude AI" coursework. It is currently **documentation-driven**: there is no source code, build system, test runner, or package manifest yet. The deliverables are markdown artifacts plus screenshot evidence. Any code added should be a narrowly scoped proof of concept (POC) for the architecture described in `architecture.md`.

When the user asks for "the project" or "the planner," they mean **StudyFlow Coach** — the system proposed in `architecture.md`. It is a retrieval-backed assignment planner that combines three patterns: RAG, MCP, and Agent SDK.

## File Roles (and how they fit together)

These files are tightly coupled — edits to one usually require edits to the others:

- `proposal.md` — the "what & why" pitch (problem, users, MVP features, build plan). The high-level intent that `architecture.md` and `spec.md` refine.
- `architecture.md` — single-source-of-truth for the system design (scope, diagram, pattern fit, risks). New POC code must trace back to a component in section 4's mermaid diagram.
- `spec.md` — formal acceptance criteria. Defines Quality Gates **QG-1** (plan structure), **QG-2** (grounding), **QG-3** (evidence) and Given/When/Then ACs **AC-1**…**AC-5**. Treat these as the binding success contract; `poc-notes.md` §1 is a narrower restatement of QG-1/QG-2.
- `poc-notes.md` — narrative report for the *one* POC component being built (currently the "retrieval-backed assignment planner"). Section 3 ("Test-First Evidence") expects a red→green test cycle, so any POC code should follow test-first.
- `tutorial3-checklist.md` — the live execution tracker. Tick checkboxes here as work completes; this is the file used to judge submission readiness.
- `makeanything.md` — rubric tracker for 7 required workflow items (project memory, spec with teeth, test-first, complexity awareness, protocol integration, scoped rules, iterative refinement). Update the checkbox + evidence link any time an item's evidence changes.
- `CHANGELOG.md` — the *iterative refinement* evidence. Append a new dated section (What changed / Why / Result) at the top whenever a meaningful iteration completes; this file is what proves the rubric item, so don't squash entries.
- `evidence/screenshots/` — required screenshots with **fixed filenames**: `rag-progress.png`, `mcp-progress.png`, `agent-sdk-progress.png` (plus optional `certificate.png`). Do not rename these — graders look for these exact names.

## POC Scope Constraint

`tutorial3-checklist.md` Phase 3 explicitly says: "Keep scope narrow: one command, one output format, one test set." Resist building broader features. The POC's binding success criteria live in `spec.md` (QG-1, QG-2, AC-2, AC-3, AC-4) and are summarized in `poc-notes.md` §1:

- given an assignment prompt, return a checklist with ≥5 concrete tasks (QG-1 / AC-2)
- output includes citations to local files (QG-2 / AC-3)
- show fallback message when no relevant context is found (AC-4)

## Commit Style

Conventional-commit prefixes (`docs:`, `feat:`, `test:`, `chore:`) were used for the early scaffolding and retriever commits. The implementation phase (planner → reviewer → CLI) dropped the prefix — see `git log`. New commits should re-adopt the prefix where reasonable. Always land a `test:` commit with a failing assertion before the matching `feat:` commit (test-first cycle).

## How to Run

The POC is a Python package — `pyproject.toml` declares runtime deps (`fastapi`, `uvicorn`) and dev deps (`pytest`, `httpx`), and sets `pythonpath = ["src"]` so pytest finds the package without env setup.

- **Tests (any shell):** `pytest -q` — current baseline is **11 passed** (retriever, planner, reviewer/orchestrator flow, CLI smoke, web smoke).
- **CLI demo, PowerShell:** `$env:PYTHONPATH="src"; python -m studyflow.cli "Plan my final project" --docs "proposal.md::Build retrieval planner||spec.md::Return at least 5 tasks"`
- **CLI demo, bash:** `PYTHONPATH=src python -m studyflow.cli "Plan my final project" --docs "..."`
- **Web UI (FastAPI + uvicorn):** `$env:PYTHONPATH="src"; python -m uvicorn studyflow.app:app --reload` — serves a single-page studio at http://127.0.0.1:8000 (`GET /`) backed by `POST /api/plan`. Both routes are exercised by `tests/test_web.py`.

The CLI's `--docs` flag uses `source::text` entries separated by `||`; the web UI accepts the same `source::text` format, one per line. The reviewer rejects plans with <5 tasks or missing citations (when `used_fallback=False`).

## Cross-File Update Reflex

Several rubric items are duplicated by design — keep them in sync:

- Adding/finishing POC code → update `poc-notes.md` §3/§7, tick the relevant box in `tutorial3-checklist.md` Phase 3, and append a `CHANGELOG.md` iteration entry.
- Capturing a screenshot → tick the matching Phase 1 box in `tutorial3-checklist.md` *and* flip the "Submission Notes" / completion counts in `makeanything.md` and `README.md`.
- Changing scope or success criteria → edit `spec.md` first (it's the contract), then propagate to `architecture.md` §2/§5, `poc-notes.md` §1, and `proposal.md`.
