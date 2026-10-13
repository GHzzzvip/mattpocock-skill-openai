---
name: codebase-design
description: Design or evaluate module interfaces when architectural boundaries, testability, or change locality are in question.
license: MIT
---

# Design useful interfaces

A module is an interface plus its implementation. The interface includes contracts, invariants, error behavior, and ordering constraints, not only type signatures. A deep module hides substantial complexity behind a small surface that callers can learn and test.

Consider three outcomes: capability gained by callers, concentration of related changes, and behavior observable through the interface. Apply the deletion test: would removing the module eliminate unnecessary ceremony, or scatter necessary complexity among callers?

Inspect actual dependencies and variation before adding abstractions. Prefer an interface that fits real callers and existing project vocabulary. Do not impose a universal naming vocabulary on a repository that already has clear terms.

For a tangled cluster, read [deepening guidance](references/deepening.md). For a consequential interface decision, compare a few materially different designs on caller complexity, testability, migration cost, and failure behavior. Delegation is optional; a single agent can compare alternatives.

Produce an interface proposal with an example call, its invariants, tradeoffs, and a migration/test approach. Implement it only when the user requested implementation.
