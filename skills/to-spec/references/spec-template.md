# Specification structure

Follow an existing project template first. For a new local spec, include these parts at a depth proportional to the task:

- **Problem:** actor, current behavior, and the concrete cost or limitation.
- **Desired behavior:** what changes for the user, including meaningful error and edge cases.
- **Acceptance criteria:** observable examples or user stories that distinguish success from failure.
- **Decisions:** contracts, state transitions, data changes, relevant architecture choices, and rationale already settled.
- **Verification:** public interfaces under test, representative scenarios, checks to run, and important blind spots.
- **Out of scope:** nearby work deliberately excluded.
- **Open questions:** unresolved decisions and their impact. Mark the artifact as a draft if they block implementation.

Link source discussions, prototypes, and ADRs. Do not invent requirements to fill sections or declare an exhaustive user-story count.
