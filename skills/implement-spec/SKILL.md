---
name: implement-spec
description: Implement a specification and dependency graph on an integration branch, coordinating independent tasks when supported.
license: MIT
---

# Implement a task graph

Read the spec and tasks. Validate blockers and completion criteria before scheduling. Track pending, active, complete, and blocked tasks; dispatch only the ready frontier. Record a starting revision and isolate existing user work.

Use an integration branch when the task's delivery calls for it. If authorized delegation and isolated worktrees are available, assign independent ready tasks to workers based on the current integration tip. Give each worker ownership, acceptance criteria, dependency artifacts, and allowed side effects. Pass file and commit pointers instead of copying whole transcripts. If delegation is unavailable, execute the same graph serially and report that choice.

Each task implements and verifies its behavior. Integrate one result at a time, resolve conflicts deliberately, and verify the combined behavior before unblocking dependents. Do not reset a worker's uncommitted work or delete unrelated worktrees.

Use available `tdd` and `code-review` skills when they fit, with direct implementation and review as fallbacks. Review the whole integrated diff against the spec, fix findings, and run required project checks.

Create or update remote PRs and close issues only as authorized by the requested workflow. Clean up only worktrees created for this run after confirming their work is preserved.

Done when every acceptance criterion is accounted for on the integration branch. Report checks, unresolved items, and the branch or authorized PR.
