---
name: improve-codebase-architecture
description: Survey an area of a codebase for concrete architectural friction and prioritize refactoring candidates.
license: MIT
---

# Survey architectural friction

Use the user-selected subsystem or infer a useful scope from recent changes. Read relevant domain terms and ADRs. Inspect areas where understanding or changing one behavior crosses many files, interfaces expose internal details, or tests miss caller interactions.

For each candidate, record concrete file evidence, the costly change or failure it causes, a proposed direction, expected benefit, and migration risk. Apply the deletion test: distinguish removable pass-through layers from modules that concentrate necessary complexity. Existing ADR conflicts need explicit reasoning.

Present a small ranked set of actionable candidates; include a before/after diagram when it clarifies the structure. If the user requests an HTML report, save a portable report in the requested destination or OS temporary directory, with inline styles and diagrams that do not require a CDN. Do not make HTML a prerequisite for a simple review.

After the user chooses a candidate, explore interface alternatives and test boundaries. Use available `codebase-design` or `domain-modeling` guidance if useful, or discuss those decisions directly. A survey alone does not authorize refactoring.

Done when the user can judge which candidate is worth pursuing and why. Distinguish strong evidence from speculative improvements.
