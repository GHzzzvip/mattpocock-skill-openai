---
name: loop-me
description: Design a recurring personal or team workflow as an implementable specification, without enabling automation.
license: MIT
---

# Specify a recurring workflow

Read existing `workflows/` and relevant `NOTES.md` in the user's workspace. Identify the recurring activity, desired outcome, trigger, inputs, outputs, and constraints. Ask focused questions about missing decisions and inspect available tools or artifacts directly.

Use schedules, AI steps, and human checkpoints only where the workflow requires them. Place a necessary review after useful preparatory work so the user sees a concrete result. Separate each checkpoint's brief from its detailed artifact.

Write one specification per workflow under `workflows/`, preserving existing conventions and user edits. Include failure handling, duplicate-run behavior, access requirements, and observable completion where relevant. Record known choices separately from unresolved assumptions.

Done when an implementer can identify the steps, decision points, required integrations, and success conditions. Designing a workflow does not authorize installing automations, scheduling future runs, or sending messages.
