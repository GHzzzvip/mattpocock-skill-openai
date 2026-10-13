---
name: pr
description: Write or revise a pull-request title and description grounded in the final diff and verification evidence.
license: MIT
metadata:
  credits:
    skill: show-me
    author: Dex Horthy
    organisation: Humanlayer
    url: https://github.com/humanlayer/skills/blob/main/plugins/show-me/skills/show-me/SKILL.md
---

# Describe a pull request

Read the final change, originating requirement, and available validation. Follow the repository's PR template. Lead with the concrete problem and resulting behavior; use a before/after example when helpful.

Scale detail to the change. Include relevant tests or observations, remaining limitations, and material rollout or rollback concerns. Use a small diagram or diff sketch only when it explains the change better than prose. Separate tests actually run from suggested checks; never invent screenshots, results, or guarantees.

Write for a reviewer who did not see the conversation. Explain consequential tradeoffs and omit abandoned approaches unless they clarify a decision. Describe the final scope, not a sequence of chat turns.

Drafting a description does not itself publish or merge a PR. When publication is authorized, use a structured body argument or a file-based CLI input to preserve newlines and avoid shell expansion.

Done when the title and body match the actual change and a reviewer can assess its behavior and validation. Attribution for the upstream visual-summary inspiration is in [credits](references/CREDITS.md).
