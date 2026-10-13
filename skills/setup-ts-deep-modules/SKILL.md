---
name: setup-ts-deep-modules
description: Configure dependency-cruiser to enforce public package entry points in a TypeScript repository.
license: MIT
---

# Enforce package entry points

Inspect the package manager, package layout, dependency-cruiser version/config, and existing check command. Use the project's actual package root; do not create a new hierarchy merely because `src/` exists.

Adapt [the config template](assets/dependency-cruiser.config.cjs) to the real flat-package layout. Merge with existing rules and options. Preserve the capture-group backreferences that allow a package to reach its own internals while preventing imports into another package's internals. Root files are public entry points; nested implementation is private. Tests exercise public entry points and can use their own fixtures. Keep architectural layering separate from visibility rules.

Use the existing package manager for any required development dependency and connect the boundary check to the existing verification workflow. Avoid unrelated path aliases or tsconfig changes.

Prove enforcement in disposable fixtures or a safely restored local change: allowed imports pass, a cross-package deep import and a test-to-internal import fail, then the restored state passes. Record pre-existing violations separately. Add an example package only when needed or requested.

Document the convention near the packages with a conditional pointer from the applicable agent instructions. Done when the rules catch actual violations and the documented command invokes them.
