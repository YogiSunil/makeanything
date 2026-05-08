# Spec: StudyFlow Coach

## Product Goal

Build a retrieval-backed planning assistant that converts assignment prompts into actionable checklists with source-grounded context and risk notes.

## Scope

In scope:
- Parse assignment text and identify concrete deliverables.
- Generate ordered checklist steps.
- Include source-aware grounding notes for plan reliability.

Out of scope:
- LMS submission automation.
- Multi-user auth and collaboration.
- Full web dashboard.

## Quality Gates

### QG-1 Plan Structure Gate

How to verify:
- Run the planner flow on one assignment prompt.

Success criteria:
- Output contains at least 5 concrete next actions.
- Output is ordered and easy to execute.
- Output includes at least one risk note.

### QG-2 Grounding Gate

How to verify:
- Run the same prompt against local project/course docs.

Success criteria:
- Output includes explicit references to source context.
- Output avoids generic boilerplate recommendations.
- Empty/weak context triggers a fallback guidance message.

### QG-3 Evidence Gate

How to verify:
- Review Tutorial 3 artifact files and screenshot evidence folder.

Success criteria:
- `architecture.md` and `poc-notes.md` are complete.
- `proposal.md` clearly states problem, scope, and milestones.
- Screenshot evidence includes required module progress images.

## Acceptance Criteria

### AC-1 Requirement Extraction

Given a prompt with multiple requirements
When the planner processes the prompt
Then the response identifies key deliverables and deadlines in actionable language

### AC-2 Checklist Output

Given a valid assignment prompt
When the planner returns a plan
Then the response contains at least 5 numbered tasks with clear verbs

### AC-3 Grounded Recommendations

Given relevant local context exists
When a plan is generated
Then the plan includes source-grounded references and avoids unsupported claims

### AC-4 Fallback Behavior

Given weak or missing local context
When a plan is generated
Then the assistant returns a safe fallback response with next data-collection steps

### AC-5 Submission Readiness

Given all docs are complete
When the repository is reviewed
Then required files and evidence are present and linked for grading
