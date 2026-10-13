---
name: domain-modeling
description: Clarify project-specific domain terms and maintain glossaries or architecture decision records.
license: MIT
---

# Maintain domain language

Follow `GLOSSARY-MAP.md` when present; otherwise use the relevant existing glossary. Compare ambiguous terms with actual code and concrete business scenarios. Explain conflicts rather than silently choosing one meaning.

Record agreed definitions as they become useful. Use [the glossary format](references/GLOSSARY-FORMAT.md) when creating a glossary, adapting to existing conventions. Keep business concepts separate from implementation plans and general programming terminology.

For decisions with costly reversal, non-obvious rationale, and real alternatives, use [the ADR format](references/ADR-FORMAT.md). Record consequences and rejected alternatives only when they help a later reader. Create files lazily and distinguish proposals from agreed decisions.

Report the terminology or decision changes and any ambiguity that remains. Reading a glossary alone does not require this workflow.
