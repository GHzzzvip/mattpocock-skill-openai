---
name: scaffold-exercises
description: Create course exercise folders and meaningful problem, solution, or explainer stubs from a supplied plan.
license: MIT
---

# Scaffold course exercises

Read the plan and inspect neighboring exercises and available lint commands. Follow established numbering and variants. Without a convention, use `exercises/XX-section/XX.YY-exercise/` and appropriate `problem/`, `solution/`, or `explainer/` folders.

Create non-empty `readme.md` files with the exercise objective and a useful starting instruction. Include code entrypoints only when the exercise requires code. Keep student TODOs in problem material, and distinguish reference solutions from unexplained placeholders.

Preserve existing exercises. For moves, update affected links and numbering. Use the course's actual validator; run `ai-hero-cli` only if the repository already provides it. Otherwise check the generated structure and links directly without installing an unrelated CLI.

Done when the requested exercises exist, are navigable, and pass available validation. Commit only when the user or established workflow includes committing this work; do not stage unrelated files.
