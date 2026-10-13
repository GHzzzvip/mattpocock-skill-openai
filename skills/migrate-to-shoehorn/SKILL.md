---
name: migrate-to-shoehorn
description: Replace selected TypeScript test fixture assertions with appropriate @total-typescript/shoehorn helpers.
license: MIT
---

# Migrate test fixtures

Inspect the requested tests, current package version, and package manager. Determine why each assertion exists before replacing it. Keep production code unchanged and preserve literal assertions such as `as const` when they express useful types.

Use `fromPartial` for intentionally incomplete valid fixtures and `fromAny` only for intentionally invalid input in negative tests. Check the installed library's signatures and inference at each call site; a mechanical replacement can weaken the test's meaning. Prefer ordinary typed fixtures when no escape hatch is needed.

Add the library as a development dependency if necessary using the project's package manager. Migrate only relevant test files and retain required imports and fixture intent. Do not replace unrelated casts across the repository.

Run the affected tests and type checker. Done when the selected fixtures express the same intended behavior and compile against the actual library version. Report migration coverage and assertions intentionally retained.
