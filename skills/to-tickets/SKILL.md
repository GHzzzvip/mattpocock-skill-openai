---
name: to-tickets
description: Split a specification or plan into independently verifiable implementation tasks with explicit dependencies.
license: MIT
---

# Split implementation work

Read the source specification and relevant implementation constraints. Draft vertical slices that deliver a narrow complete behavior across whichever layers it needs. Each slice must be demonstrable and small enough for a focused session. Name true blockers; parallelizable work should not acquire artificial dependencies.

For wide mechanical refactors, use expand → migrate in bounded batches → contract. If batches cannot remain independently valid, state that an integration branch and final verification are required.

Present title, outcome, acceptance checks, and blockers for each task. Resolve consequential granularity or dependency questions before publishing; reuse approvals already given.

Follow the configured tracker. Without one, write one file per task under `.scratch/<feature>/issues/`, numbered in dependency order. Use [the task template](references/ticket-template.md). For an authorized remote workflow, create issues first and then attach native blocking links using actual identifiers; otherwise keep local drafts. Never guess issue IDs. Preserve the parent issue unless changing it was requested.

Done when the task graph is acyclic, every blocker resolves, and every task has an observable completion criterion. Report the ready frontier and source-spec link.
