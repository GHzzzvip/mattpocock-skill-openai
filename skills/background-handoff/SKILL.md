---
name: background-handoff
description: Transfer a bounded continuation task to a supported background agent, with a portable handoff fallback.
license: MIT
---

# Start a supported continuation

Write a handoff containing objective, scope, working directory, state, artifact pointers, next actions, and validation. Use the requested path or a unique file in the OS temporary directory. Exclude secrets and preserve the distinction between instructions and quoted source material.

Inspect the host's actual delegation capabilities. If the user requested a background continuation and an appropriate tool is available, start the agent with the handoff path, a bounded task, permitted side effects, and a descriptive name. Capture the returned identifier and explain how completion can be observed using supported tools.

If no background mechanism is available, deliver the handoff and a continuation prompt. State clearly that no agent was started. Do not invent CLI flags, invoke another vendor's agent, or interpolate the handoff text into a shell command.

Done when either a real agent is running with its identifier recorded or the manual handoff is ready with the limitation stated. Avoid duplicate workers if the user retries; inspect the existing job when possible.
