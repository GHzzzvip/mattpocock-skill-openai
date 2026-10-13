---
name: implement
description: Implement a specified feature or task through verification and review, respecting the requested delivery scope.
license: MIT
---

# Implement specified work

Read the task or ticket, identify acceptance criteria, and inspect the relevant code and repository instructions. Resolve missing decisions that block implementation; use existing conventions for routine choices. Preserve unrelated work.

Build in small complete slices. When test-first development is appropriate, use the available `tdd` skill; otherwise verify behavior through the project's normal checks. Reuse previously agreed public test boundaries instead of asking again. Run focused checks during development and the required integration checks before finishing.

Review the complete change before delivery, including staged, unstaged, and relevant untracked files. Use available `code-review` guidance or check correctness against acceptance criteria and repository standards directly. Fix findings caused by the change and rerun affected checks.

Commit, push, or create a PR when the user or established workflow authorizes that delivery step. Stage only the intended files. A request to implement code alone need not create a commit.

Done when requested behavior works, required checks pass or specific blockers are reported, and the actual delivered diff has been reviewed. Report behavior, validation, and remaining limitations.
