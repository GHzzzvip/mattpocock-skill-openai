---
name: writing-for-agents
description: Write or improve skill instructions and agent-facing repository guidance with precise scope and conditional references.
license: MIT
---

# Write useful agent guidance

Identify the behavior the document should change and the tasks it applies to. Assume the agent can perform ordinary reasoning and coding; keep project-specific constraints, non-obvious conventions, useful procedures, and checkable outcomes.

For skills, keep name and description concise and discriminating. Describe the capability and its trigger; add an exclusion only for a likely routing collision. Keep required workflow and important constraints in `SKILL.md`, with substantial conditional detail in linked references. For metadata and discovery, read [skill mechanics](references/skill-mechanics.md).

For repository instructions, use contextual pointers: name the document and the condition for reading it. Avoid requiring an entire documentation stack before every small edit. Keep each rule in one authoritative place.

Use detailed sequences where order protects correctness; leave routine decisions flexible. Preserve existing user choices and permissions. Clarification should resolve actual uncertainty, not repeat consent for already-authorized work. State what completion looks like without forcing unnecessary artifacts or tests.

Remove stale guidance and instructions that do not change useful behavior. Verify local links and metadata, then try representative trigger and non-trigger requests when feasible. Report the change and limits of validation. Do not claim behavioral reliability based solely on a format check.
