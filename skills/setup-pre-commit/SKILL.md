---
name: setup-pre-commit
description: Configure requested commit-time checks using the repository existing hook and formatting conventions.
license: MIT
---

# Configure commit-time checks

Inspect the package manager, hook framework, formatter, lint-staged configuration, and check scripts. Extend the existing setup where possible. Use Husky and lint-staged for a compatible JavaScript repository when that is the requested or chosen approach; verify commands against the installed versions.

Merge configuration rather than replacing hooks, `prepare` scripts, or formatting preferences. Add dependencies only as needed. Limit staged formatting to supported files and choose checks with acceptable latency. Reuse actual typecheck/test scripts; document missing checks instead of adding broken commands.

Verify the hook's syntax and run its checks against disposable or task-owned changes. A verification command must not accidentally reformat, stage, or commit the user's unrelated work. Do not create a commit solely as a smoke test.

Done when the intended hook is executable, invokes the expected checks, preserves prior behavior, and has demonstrated pass/fail behavior where feasible. Report the checks, files changed, and any validation limits.
