# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This repo is the Tutorial 3 final-project deliverable for the "Mastering Claude AI" coursework. It is currently **documentation-driven**: there is no source code, build system, test runner, or package manifest yet. The deliverables are markdown artifacts plus screenshot evidence. Any code added should be a narrowly scoped proof of concept (POC) for the architecture described in `architecture.md`.

When the user asks for "the project" or "the planner," they mean **StudyFlow Coach** — the system proposed in `architecture.md`. It is a retrieval-backed assignment planner that combines three patterns: RAG, MCP, and Agent SDK.

## File Roles (and how they fit together)

These four files are tightly coupled — edits to one usually require edits to the others:

- `architecture.md` — single-source-of-truth for the system design (scope, diagram, pattern fit, risks). New POC code must trace back to a component in section 4's mermaid diagram.
- `poc-notes.md` — narrative report for the *one* POC component being built (currently the "retrieval-backed assignment planner"). Section 3 ("Test-First Evidence") expects a red→green test cycle, so any POC code should follow test-first.
- `tutorial3-checklist.md` — the live execution tracker. Tick checkboxes here as work completes; this is the file used to judge submission readiness.
- `evidence/tutorial-3-screenshots/` — required screenshots with **fixed filenames**: `rag-progress.png`, `mcp-progress.png`, `agent-sdk-progress.png` (plus optional `certificate.png`). Do not rename these — graders look for these exact names.

## POC Scope Constraint

`tutorial3-checklist.md` Phase 3 explicitly says: "Keep scope narrow: one command, one output format, one test set." Resist building broader features. The POC's success criteria are defined in `poc-notes.md` §1:

- given an assignment prompt, return a checklist with ≥5 concrete tasks
- output includes citations to local files
- show fallback message when no relevant context is found

## Commit Style

Follow the suggested commit sequence in `README.md` and the per-phase suggestions in `tutorial3-checklist.md`. Conventional-commit prefixes are used: `docs:`, `feat:`, `test:`. Test commits should land before the corresponding `feat:` commit (test-first cycle).

## What is Missing

There is intentionally no `package.json`, `requirements.txt`, lint config, or test framework yet. If you add a POC, pick the lightest tooling that satisfies the test-first requirement and document the run command in `poc-notes.md` §7 ("Demo command/run steps") rather than inventing scripts the grader cannot find.
