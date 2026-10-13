# Codex rules adapter

Checked 2026-10-12 against [OpenAI Rules documentation](https://learn.chatgpt.com/docs/agent-configuration/rules). Verify the installed host before use; this interface is experimental.

Local Codex reads `.rules` files next to active configuration layers. User rules can live in `~/.codex/rules/`; project rules require the project configuration layer to be trusted. Managed Work environments use their own supported policy configuration.

An example for a user who explicitly requested blocking direct pushes:

```python
prefix_rule(
    pattern = ["git", "push"],
    decision = "forbidden",
    justification = "Direct pushes are disabled by the selected workflow.",
    match = ["git push origin main", "git push --force"],
    not_match = ["git status", "git -C repo push"],
)
```

Check without executing the candidate command:

```bash
codex execpolicy check --pretty --rules /path/to/git-guardrails.rules -- git push origin main
```

The `git -C` example deliberately exposes a prefix-matching gap. Additional forms need explicit treatment. These rules govern commands outside the sandbox; a matched test is not proof of complete prevention inside every tool, shell, or environment. Restart the relevant Codex process to reload local rule files.

For a broader policy, verify actual argument patterns and host capabilities rather than promising a complete destructive-command filter.
