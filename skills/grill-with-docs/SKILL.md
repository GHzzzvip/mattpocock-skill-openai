---
name: grill-with-docs
description: Clarify a project plan while recording agreed domain terminology and durable architecture decisions.
license: MIT
---

# Clarify and document

Read the relevant project glossary and decisions if present. Use available `grilling` and `domain-modeling` skills for their respective tasks; if absent, follow the workflow below directly.

Ask focused questions about material unresolved decisions. Investigate repository facts yourself and use concrete scenarios to expose ambiguity. Record settled domain terms in the existing glossary. Create a root `GLOSSARY.md` lazily when no glossary convention exists. Keep implementation plans out of the glossary.

Record an ADR only for a significant tradeoff whose rationale would otherwise be lost and whose reversal is costly. Follow the repository's ADR convention, defaulting to `docs/adr/`. Preserve user edits and distinguish proposed decisions from accepted ones.

Finish with the agreed plan, document paths, and any unresolved questions. Do not create a spec or start building solely because the interview is complete; honor the broader task the user actually requested.
