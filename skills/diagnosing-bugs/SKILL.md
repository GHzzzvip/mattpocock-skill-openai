---
name: diagnosing-bugs
description: Diagnose reproducible or intermittent bugs and performance regressions using a targeted feedback loop.
license: MIT
---

# Diagnose with evidence

Identify the exact symptom and establish an executable signal for it: a failing test, request replay, CLI fixture, browser scenario, or timing harness. Inspect code as needed to build this signal, but distinguish hypotheses from observations. For intermittent bugs, measure failure rates across controlled repetitions.

Minimize inputs and moving parts while preserving the observed failure. Make the loop fast and deterministic where possible. Use representative original inputs again before declaring a fix complete.

Form falsifiable hypotheses, ranked by evidence. Change one variable per probe and map instrumentation to the prediction it tests. For performance, measure a baseline before optimizing. Avoid broad logging that cannot distinguish causes; remove temporary instrumentation after use.

When the correct test boundary exists, turn the reproducer into a regression test, observe it fail before the fix, then observe it pass. If it cannot represent the real failure, document the missing boundary rather than claiming coverage. If no reproducible signal is possible, report attempts and the precise access or artifact needed; continue independent useful diagnosis without inventing certainty.

For unavoidable manual reproduction, adapt [the manual loop template](assets/hitl-loop.template.sh). Redact secrets from captured artifacts and outputs.

Done when the original scenario is verified, relevant regressions are checked, diagnostic changes are cleaned up, and the cause is explained. Separate a verified fix from a plausible unverified mitigation.
