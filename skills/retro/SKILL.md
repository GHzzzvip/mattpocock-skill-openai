---
name: retro
description: Review a completed coding session and recommend evidence-based improvements to the agent working environment.
license: MIT
---

# Review the working environment

Read the specified session or available artifacts; default to the current session. If the original session is unavailable, state that the review is based on partial evidence.

Look for repeated friction in navigation, information access, tool usage, checks, or instructions. Trace each candidate to a concrete observed failure or cost. Inspect existing automation before proposing another check.

Route mechanical mistakes to deterministic checks where practical. Reserve written coding standards for judgment that automation cannot capture. Keep agent instructions as short contextual pointers rather than a history of every past failure.

Rank a few improvements by impact and effort. Explain the evidence, proposed change, and what future outcome would show improvement. Do not treat every one-off failure as a universal rule.

The output is recommendations unless implementation was requested. If improvements are in scope, make the smallest relevant changes and verify them. Avoid unrelated environment changes.
