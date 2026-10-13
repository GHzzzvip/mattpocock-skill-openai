---
name: git-guardrails
description: Configure Codex execution rules for specified Git commands when the user requests Git command restrictions.
license: MIT
---

# Configure Git command restrictions

Inspect the installed Codex version and the user's requested scope and policy. Read [rules guidance](references/codex-rules.md) and verify the current host's supported execution-policy interface before editing configuration.

Specify the exact command families the user wants blocked or prompted. Preview the rules and their scope when not already established. Preserve existing rule files and approval settings. Prefer a separate named rules file; never replace unrelated configuration or weaken a stronger existing restriction.

These execution rules govern commands outside the sandbox. They are not a universal Git sandbox and may not constrain tools running through another execution path. Flags such as `git -C`, absolute executable paths, aliases, shell wrappers, and other tools can change matching. Test realistic variants with the installed policy checker and document uncovered cases. Do not claim the old vendor-specific hook can be copied into Codex unchanged.

Use policy-check or dry-run commands, not destructive Git operations, to verify matches and non-matches. If the host cannot enforce the requested policy, report the gap and offer a documented alternative without silently applying weaker protection.

Done when the intended rules are saved in a supported location, their match behavior is verified, and limitations are stated. This skill does not perform the blocked Git operations to prove a rule works.
