---
name: ask-matt
description: Choose a skill or engineering workflow from this collection when the user asks which one fits their task.
license: MIT
---

# Choose a workflow

Use the user's goal, current artifacts, and unresolved decisions to recommend the smallest useful next step. Read a candidate's entrypoint before describing its detailed behavior. Recommend explicit-only skills to the user; do not activate them on their behalf.

- Unclear feature: `grill-with-docs`; informal discussion with no saved artifacts: `grill-me`.
- Settled discussion needing a specification: `to-spec`. A larger specification needing independent slices: `to-tickets`.
- Concrete implementation: `implement`; a whole task graph: `implement-spec`.
- Test-first behavior: `tdd`. Difficult failure: `diagnosing-bugs`. Review of changes: `code-review`. PR description: `pr`.
- Large effort with unresolved decisions across sessions: `wayfinder`. Architectural friction: `improve-codebase-architecture`.
- Runnable design experiment: `prototype`. Evidence gathering: `research`. Shared terminology: `domain-modeling`. Interface design: `codebase-design`.
- Session retrospective: `retro`. Repository workflow configuration: `setup-matt-pocock-skills`.
- Portable context: `handoff`; a running continuation agent: `background-handoff` when available.
- Learning workspace: `teach`. Questions for someone else: `to-questionnaire`. Re-explanation: `wait-what`.
- Skill or agent-instruction writing: `writing-for-agents`. Manual setup procedure: `wizard`.
- Experimental workflow design: `loop-me`; long-running coordination: `chief-of-staff`.
- Writing material: `writing-fragments`; article development: `writing-shape` or `writing-beats`.
- Optional setup: `setup-ts-deep-modules`, `setup-pre-commit`, `git-guardrails`; specialized tasks: `scaffold-exercises`, `migrate-to-shoehorn`.

For a typical substantial feature, suggest clarification → spec → tickets → implementation → review. Small changes need only the relevant steps. Explain why the recommended step fits and what artifact it produces. Missing optional siblings are not blockers: describe the equivalent work directly.

For context transitions, read [session boundaries](references/session-boundaries.md). Do not prescribe a fixed token threshold or assume commands exist in every host.
