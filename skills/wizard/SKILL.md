---
name: wizard
description: Create an interactive shell guide for setup steps requiring human credentials, browser interaction, or manual judgment.
license: MIT
---

# Guide a manual procedure

Inspect configuration names and existing setup instructions without printing secret values. Identify steps the agent can complete and steps that genuinely require the human. For each manual step, establish the source of input, destination, whether it is secret, and observable success.

Verify unfamiliar service URLs and instructions against current official documentation. Generate a focused script from [the wizard template](assets/template.sh), adapting the stages and helpers to the target environment. Keep actual credentials out of the script. Use hidden input and report variable names rather than values.

Persist secrets only to the user-selected destination with restrictive permissions. Verify dotenv encoding against the project's loader; shell quoting is not automatically dotenv quoting. For multiline or unusual values use the target's supported encoding or secret store. Check the exact repository before writing CI secrets. Explain irreversible stages and require the relevant authorization before executing them.

Validate generated syntax with `bash -n` and shellcheck if available. Exercise non-interactive helpers with disposable fixtures where changed; do not run the real interactive procedure on the user's behalf. A reusable procedure may belong in `scripts/`; a one-off can live in the OS temp directory.

Done when each input reaches its intended destination, failure and retry behavior are clear, and the user has the script path and run command. Do not claim setup completed merely because the guide was generated.
