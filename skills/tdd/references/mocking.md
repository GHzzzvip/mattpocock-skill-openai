# Dependencies and doubles

Prefer real in-process behavior and disposable test services when practical. Control time, randomness, network responses, and other unstable dependencies to make failures interpretable.

Use a double at a meaningful dependency boundary when the real dependency is slow, unavailable, costly, or has unwanted effects. Model the contract that matters, including errors. Avoid mocking internal call structure merely to assert implementation details.

Inject a dependency where variation is real. Do not introduce a large abstraction only to satisfy a test framework. Pair contract-sensitive doubles with appropriate integration evidence when drift is a risk.

A passing test using a fake payment adapter proves the application's response to that fake, not that the live payment service accepts the request. State that boundary when reporting validation.
