# Skill packaging

A skill directory contains `SKILL.md` with YAML `name` and `description`. Optional `agents/openai.yaml` configures UI and invocation policy. Use `references/` for conditional guidance, `scripts/` for repeatable execution, and `assets/` for templates used in output.

A Codex user can explicitly mention `$skill-name`; automatic selection depends on its description and policy. Preserve an existing explicit-only policy during migration. For new skills, automatic selection is the default unless the user requests explicit-only behavior. Invocation restrictions belong in `agents/openai.yaml`, not vendor-specific frontmatter.

Do not require a fictional universal Skill tool. Use the host's advertised skill loader or read the exposed entrypoint through available file tools. Optional sibling guidance must not make a standalone skill fail. Explicit-only sibling workflows should be recommended rather than implicitly launched.

Keep UI descriptions consistent with actual behavior. Validate YAML, names, references, resource availability, and representative trigger/non-trigger requests. Static validation alone does not demonstrate useful model behavior.
