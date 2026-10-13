---
name: to-questionnaire
description: Draft a questionnaire for another person whose knowledge is needed to resolve a decision.
license: MIT
---

# Ask the person who knows

Establish the recipient's role, context, and the decisions or facts the user needs back. Reuse information already supplied; ask only for consequential missing context. Do not interview the user for subject knowledge they have explicitly said they lack.

Write questions that cover the knowledge gap, ordered by importance and grouped by theme where useful. Each question should address one idea, with an answer space and a short rationale only when necessary. Allow partial answers and explicit uncertainty.

Include purpose, recipient, relevant context, how answers will be used, and any supplied deadline or effort expectation. Do not invent names or deadlines. End with an invitation to add missing considerations.

Save to the requested destination, defaulting to `to-questionnaire-<topic>.md` in the workspace. The outcome is a draft artifact; sending it requires a request to contact the recipient.

Done when every decision the user needs is covered and a recipient unfamiliar with the conversation can answer. Report the file path.
