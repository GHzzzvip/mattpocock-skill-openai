# Decision map

The map is a compact index with Destination, Notes, Decisions so far, Not yet specified, and Out of scope. Each settled decision points to its ticket for the full answer and evidence.

A ticket contains a precise question, type, blockers, status, owner when used, and resolution. Types describe how to resolve it:

- `research`: evidence from primary sources.
- `prototype`: a runnable experiment and its verdict.
- `grilling`: a choice requiring user preferences or domain judgment.
- `task`: an explicitly scoped prerequisite action that unlocks a decision.

Keep live tickets discoverable through the tracker or a local index. The ready frontier contains uncompleted, unclaimed tickets whose blockers are resolved. Exclude work active in another session even when it has no blockers. Flag dependency cycles.

## Ownership and claims

Before starting, reread the ticket's status, blockers, and ownership. Use the tracker's assignment or claim mechanism within existing authorization, then verify ownership. Record a session or run identifier when multiple sessions share the same human assignee; assignment to that human alone does not distinguish their concurrent sessions. A run may resume its own claim, but must not take over another run's claim merely because the ticket was explicitly selected or looks stale.

For local tickets, record status, owner/run identifier, and claimed-at time using the workspace convention. Use an atomic exclusive claim operation or an existing lock mechanism when concurrent workers are possible; a Markdown read followed by a write is not a lock. Recheck status and dependencies after obtaining the claim. If a competing claim wins, leave it intact and choose another ready ticket, or report the conflict when the user selected that ticket. If the tracker or filesystem offers no reliable claim mechanism, serialize work through a single coordinator rather than implying collision protection.

On completion, persist the resolution before releasing this run's claim. On a deliberate handoff or blocked exit, record the verified state and transfer or release only this run's ownership according to the project convention. Do not silently clear someone else's claim; recovery requires evidence that the worker stopped and an authorized handoff or takeover. Read-only planning can recommend a ticket without claiming or resolving it.

For remote trackers, create tickets before wiring links with real IDs. For local files, use stable relative paths. Do not use guessed IDs or empty placeholder links.

Closing a decision ticket means its question has an answer or has explicitly become out of scope. It does not mean a product feature was implemented. When the route to the destination is clear, hand the linked decisions into a build specification if implementation is requested.
