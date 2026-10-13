# Task format

Use one file per task in a local tracker, or one issue per task in an authorized remote tracker.

```markdown
# 01: Observable behavior delivered

Source spec: relative path or actual issue link
Status: ready-for-agent
Blocked by: None, or actual task identifiers

## What to build
Describe the complete behavior and relevant constraints.

## Acceptance criteria
- [ ] A concrete success scenario
- [ ] A meaningful error or regression scenario when applicable

## Verification
Public interface and observable evidence that establishes completion.
```

Write blockers first. Verify every reference exists and the graph has no cycles. For local tasks, update status and verification evidence as work completes. For remote tasks, use the platform's configured resolution workflow.
