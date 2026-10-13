---
name: setup-matt-pocock-skills
description: Configure a repository issue tracker, triage labels, and domain-document locations for this engineering skill collection.
license: MIT
---

# Configure project conventions

Inspect repository instructions, remotes, existing tracker documentation, glossary layout, and triage conventions. Reuse configured choices. Ask only for unresolved choices that matter, such as a tracker preference when no convention exists.

Write concise project-specific references under the existing docs convention, defaulting to `docs/agents/`: `issue-tracker.md`, `domain.md`, and `triage-labels.md` only if triage is used. For the tracker, record read/write operations, parent-child and blocker relationships, and how work is closed. Support local Markdown without a remote service.

Read [setup reference](references/setup.md) for the local tracker and default roles. Existing labels take precedence. A remote origin identifies a candidate tracker, not permission to create labels or issues; perform those changes only when covered by the user's setup request.

Add short conditional pointers to the applicable `AGENTS.md`. If that file is a symlink or delegates to another instruction file, update its authoritative target rather than duplicating instructions. Preserve surrounding content and existing layouts. Create a root `AGENTS.md` only when none exists and setup requires one.

Use one glossary by default; add multiple domain contexts only when business boundaries justify them. Create glossary/ADR files when there is actual content to record.

Done when the project conventions are discoverable and internally consistent. Report the files and any remote changes actually made.
