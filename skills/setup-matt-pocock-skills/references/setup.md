# Project setup choices

## Local tracker

A lightweight layout is `.scratch/<feature>/spec.md` and `.scratch/<feature>/issues/NN-title.md`. Store title, status, source spec, blockers, acceptance checks, and verification evidence in each task. Number blockers before dependents and preserve stable file links.

For a decision map, use `.scratch/<effort>/map.md` and a separate decision-ticket directory. Track ticket type, blockers, status, and resolution. Decision tickets are planning artifacts, not automatically ready implementation tasks.

## Remote tracker

Record the actual project/repository and supported tools. Describe how to fetch full issues and comments, create tasks, link parents and blockers, apply labels, and resolve work. Verify unfamiliar CLI/API behavior against the available tool or current official documentation. Do not encode credentials in docs.

## Triage vocabulary

Map the categories `bug` and `enhancement` and states `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix` to the project's actual labels. Normally one category and one state apply. External PR discovery is off unless the user enables it.

## Domain documents

Reuse existing locations. A single root `GLOSSARY.md` and `docs/adr/` works when the domain is cohesive. A `GLOSSARY-MAP.md` can route to separate business contexts when needed; a monorepo alone does not require multiple glossaries.
