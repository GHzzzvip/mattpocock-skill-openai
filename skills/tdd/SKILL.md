---
name: tdd
description: Develop a concrete behavior test-first using a failing test, minimal implementation, and behavior-preserving refactoring.
license: MIT
---

# Test-first development

Identify observable behavior and the public interface that exercises it. Use boundaries already agreed or established in nearby tests. Explain a new boundary's coverage tradeoff if it materially changes scope; do not gate routine test work on repeated confirmation.

Work one behavior at a time:

1. Write a test with an expected result grounded in the requirement or an independent worked example.
2. Run it and establish that it fails for the missing behavior, not an unrelated setup error.
3. Implement enough behavior to pass.
4. Refactor when it improves the change, keeping the tests green, then move to the next behavior.

Avoid writing a whole speculative test suite before implementation. Test behavior that survives internal refactors. Use [test examples](references/tests.md) for assertion design and [dependency guidance](references/mocking.md) when selecting doubles.

Prefer a boundary that exercises the real risk; a shallow test that cannot reproduce the failure is not evidence. Keep fixtures deterministic and avoid assertions that recompute the implementation. Match verification effort to the change; do not add tests for unrelated behavior.

Done when the requested behavior has observed red-to-green evidence and relevant regression checks pass. State any test boundary or environmental limitation.
