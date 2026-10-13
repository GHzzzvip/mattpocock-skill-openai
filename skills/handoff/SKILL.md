---
name: handoff
description: Write a portable handoff artifact so another session, agent, or colleague can continue the current task.
license: MIT
---

# Hand off context

Capture the objective, user constraints, current state, completed work, next actions, blockers, and checks already run. Include the working directory and branch/revision when relevant. Reference existing specs, issues, diffs, and notes instead of copying them.

Tailor the artifact to the next session's focus. Distinguish user decisions from agent assumptions and suggestions. Include relevant available skills by name, without assuming the receiving host exposes the same tools.

Use the requested destination; otherwise write a uniquely named Markdown file in the OS temporary directory. Exclude secrets and unnecessary personal information. Explain that temporary storage may be cleaned up if long-term retention matters.

Done when a fresh reader can locate the evidence and take the next action without reconstructing the conversation. Report the path and a short continuation prompt. Writing a handoff does not start a new process or end the current task unless requested.
