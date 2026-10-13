# Queue discovery and state transitions

Use the configured label mapping; the names below are roles, not necessarily literal label strings. Preserve category and unrelated labels when changing state.

## Show what needs attention

Collect open items in three buckets, oldest first within each bucket:

1. Untriaged: no triage state has been assigned, even if unrelated labels exist.
2. `needs-triage`: waiting for maintainer evaluation.
3. `needs-info` with a reporter reply after the latest triage request for information: ready for re-evaluation.

For the third bucket, compare comment author and timestamp with the latest triage information request. Unrelated activity, a bot update, or the maintainer's own comment is not a reporter reply. When history is unavailable or attribution is ambiguous, mark the item as uncertain instead of claiming a reply exists or silently excluding it. A partial reporter answer is still worth re-evaluation; it does not establish readiness for implementation.

Show counts and a linked title with a one-line reason for each item. Tag PRs and issues when mixed. Include external PRs only when discovery is enabled; use the project's definition of external. An explicitly named PR may be evaluated regardless of that filter. Listing alone does not authorize labels, comments, assignments, or closure. Let the user select work unless processing the queue was already requested.

## State machine

| Current state | Event or finding | Next state |
| --- | --- | --- |
| No triage state | Initial classification | `needs-triage` |
| `needs-triage` | Required facts missing | `needs-info` |
| `needs-triage` | Verified, sufficiently specified agent work | `ready-for-agent` |
| `needs-triage` | Human action or judgment required | `ready-for-human` |
| `needs-triage` | Rejected or already implemented | `wontfix`, with the reason distinguished |
| `needs-info` | Reporter supplies new information | `needs-triage` for re-evaluation |

Apply a transition only within existing authorization. For read-only requests, recommend it without mutating the tracker. Re-evaluation reuses prior notes and verifies new evidence; it may return to `needs-info` if gaps remain. Do not jump from “reporter replied” directly to `ready-for-agent` without checking the brief and evidence.

An explicit maintainer override can select another state. Flag unexplained conflicting states or unusual transitions rather than inventing the maintainer's intent. For PRs, `ready-for-agent` describes remaining work on the attached diff, while `ready-for-human` can mean ready for a human to merge. Neither label by itself authorizes merging.
