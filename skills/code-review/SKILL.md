---
name: code-review
description: Review committed or working-tree changes for correctness, requirement coverage, and repository standards.
license: MIT
---

# Review a concrete change

Establish the review target from the request and repository state. For a named branch/base, resolve it to a SHA and use the merge-base with `HEAD` for the committed diff. For current work, include staged and unstaged changes plus relevant untracked files; an empty committed diff does not mean there is nothing to review. Read files in context, not only changed lines. Ask if the intended base remains ambiguous.

Identify the requirement source from the user, referenced issue/spec, or matching local artifact. If none exists, state that requirement coverage cannot be fully assessed and still review correctness. Missing tracker configuration is not a blocker.

Keep two independent lenses:

- **Standards and correctness:** applicable repository guidance, concrete bugs, regressions, maintainability risks. Use [review heuristics](references/review-heuristics.md) for design concerns; heuristics are not hard violations.
- **Requirements:** missing or partial behavior, incorrect implementation, and unrequested scope. Trace findings to actual requirements.

Use independent reviewers only when delegation is available, authorized, and useful; otherwise perform separate passes yourself. Both passes must inspect the same captured change, including working-tree artifacts where relevant.

Report actionable findings with severity, file/line, triggering scenario, consequence, and supporting evidence. Distinguish confirmed defects from uncertainty. Keep the two lenses identifiable; avoid duplicate findings and cosmetic issues already handled by tooling.

Review is read-only unless fixes were requested. Finish with coverage and verification limits, including an explicit statement when no actionable findings were found.
