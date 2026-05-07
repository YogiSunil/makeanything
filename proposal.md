# Proposal: StudyFlow Coach

## Problem

Students working across multiple technical assignments lose time translating long instructions into actionable plans. Important requirements are easy to miss, and work becomes reactive instead of structured.

## Proposed Solution

StudyFlow Coach is a planning assistant that turns assignment prompts and project documents into an execution plan with milestones, checklist items, and evidence prompts.

The first release focuses on one core workflow:

1. User provides an assignment brief or prompt.
2. System retrieves relevant local project/course context.
3. System generates a clear, sequenced task plan.
4. System highlights required evidence and likely risks.

## Users

- Primary: students building AI engineering projects under deadlines.
- Secondary: mentors/TAs reviewing whether submissions align with rubrics.

## Why This Matters

The project reduces missed deliverables, improves planning quality, and creates reusable workflow artifacts (checklists, evidence notes, and milestone tracking) that directly support submission readiness.

## Core Features (MVP)

- Requirement extraction from assignment text.
- Retrieval-backed planning from local docs.
- Checklist generation with completion states.
- Risk and evidence prompts tied to rubric language.

## Architecture Direction

The project will use:

- RAG to ground plans in local files.
- MCP tool integration for live docs and verification tasks.
- Agent role split (planner, executor, reviewer) for complex requests.

## Quality Gates

1. Given an assignment prompt, the system returns at least 5 concrete next actions.
2. Output includes source references to local context used for planning.
3. Empty or weak context triggers a safe fallback recommendation.
4. Unit tests pass for parsing, retrieval ranking, and checklist formatting.

## Out of Scope (For This Iteration)

- LMS API integration and automatic submission.
- Team collaboration and user accounts.
- Full web dashboard UI.

## Success Criteria

By demo day, I can show a real assignment prompt processed into a grounded, actionable plan, then execute and track progress using the generated checklist.

## Build Plan

1. Implement retrieval and planning pipeline.
2. Add tests first for planner outputs and fallback behavior.
3. Add CLI command to run planning flow end-to-end.
4. Capture evidence and update architecture and POC notes.
