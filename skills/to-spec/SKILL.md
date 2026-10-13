---
name: to-spec
description: Synthesize an existing discussion or plan into a buildable feature specification with acceptance and testing criteria.
license: MIT
---

# Produce a specification

Use the existing discussion, relevant code, glossary, and ADRs. Separate agreed decisions from assumptions. Ask only about gaps that materially prevent a buildable spec; do not restart a broad interview.

Describe the user's problem, proposed behavior, acceptance criteria or user stories, implementation decisions, test boundaries, exclusions, and unresolved risks. Scale detail to the feature. Prefer stable contracts over speculative file layouts; include a prototype's decision-rich schema or state machine when it is clearer than prose.

For testing, identify public interfaces that cover critical behavior and explain what they miss. Honor agreed boundaries; seek input only for meaningful unresolved tradeoffs.

Use the project's spec template and destination. If none exists, write a local draft under `.scratch/<feature>/spec.md`. Publishing to an issue tracker requires the user's requested workflow to cover that action; otherwise provide the local artifact. Missing tracker setup does not block drafting. Read [spec structure](references/spec-template.md) when no template exists.

Done when another engineer can identify required behavior, acceptance checks, scope, and decisions still needed. Report the artifact and assumptions.
