---
name: wayfinder
description: Map unresolved decisions for a large multi-session effort before converting it into implementation work.
license: MIT
---

# Map a large decision space

Establish the destination and exclusions. Reuse an existing map or create one in the configured tracker; without a tracker, use local files. Planning is the default: do not turn a decision map into an implementation campaign without the user's request.

The map indexes decisions, while individual decision tickets hold detail. Read [map format and ticket types](references/map-format.md) when creating or updating them. Ticket a precise question even if blocked. Keep questions that cannot yet be stated precisely in “Not yet specified”; keep excluded work separate.

Create real ticket identifiers before wiring links and blocking edges. Use readable linked titles. When resuming, inspect the map and ready frontier, then load only the relevant ticket detail. The ready frontier excludes completed, blocked, and already-claimed tickets. Resume this run's own claim when appropriate; an explicit ticket selection does not override another worker's claim. Before beginning work, follow the ownership and claim procedure in [map format](references/map-format.md). Claim work only within the requested authorization; when ownership cannot be established safely, report the coordination gap instead of starting a duplicate worker.

Resolve a focused decision with research, a prototype, or discussion. Record its evidence and answer, update the map pointer, and expose newly precise questions. Preserve concurrent edits by rereading before updates. Do not delete historical tickets merely because a decision changed; mark them superseded or out of scope with rationale.

Work to the user's requested scope rather than a fixed token count or one-ticket limit. Finish with settled decisions, remaining frontier, and whether the effort is ready for a specification. Remote publication and closure follow existing authorization.
