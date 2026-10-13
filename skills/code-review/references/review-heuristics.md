# Design review heuristics

Use these as prompts to investigate a concrete cost, not mandatory findings. Repository standards and intended behavior govern the verdict.

- Unclear names can hide a mistaken domain assumption.
- Repeated logic can drift when one behavior changes.
- Data that always travels together may have an unexpressed invariant.
- One logical change touching many unrelated locations may indicate misplaced responsibility.
- Repeated type switches can make a new case easy to miss.
- Speculative parameters, hooks, and abstractions increase callers' burden without required capability.
- Chains through internal objects can couple callers to hidden structure.
- Pass-through layers may add indirection without concentrating useful complexity.

For each potential finding, identify the changed location, a realistic scenario, and the consequence. Cosmetic preference alone is not a bug. Distinguish enforced standards from discretionary suggestions and avoid reporting the same defect under two labels.
