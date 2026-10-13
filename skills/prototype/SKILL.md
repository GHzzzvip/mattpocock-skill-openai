---
name: prototype
description: Build a disposable runnable experiment to answer a specific logic, state-model, or UI design question.
license: MIT
---

# Answer a design question

Name the question and the observation that would settle it. Choose the smallest runnable experiment:

- Logic or state: an isolated harness or shareable HTML demo exposing transitions and current state.
- UI: materially different visual or interaction variants within the project's routing conventions.

Keep the prototype clearly labeled and separate from production behavior. Use in-memory data or disposable fixtures unless persistence is the experiment. Add only enough robustness to run and evaluate the question. Follow applicable UI-design guidance when available.

Exercise the scenarios that discriminate between alternatives and record what was learned, including inconclusive results. Preserve the experiment at a documented path; use a separate branch only when the project workflow calls for it. Do not automatically commit, push, modify production code, or delete the evidence.

Done when the experiment is runnable and the answer or remaining uncertainty is explicit. Report how to run it, observations, and which decisions should carry forward.
