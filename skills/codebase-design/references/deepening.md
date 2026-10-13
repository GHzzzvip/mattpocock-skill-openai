# Deepen a cluster

Map the cluster's callers, behaviors, and dependencies. Distinguish local computation, stable internal dependencies, replaceable infrastructure, and external systems. The useful public interface often corresponds to a caller's complete behavior rather than an internal helper.

Consider what a caller must learn: parameter shape, state ordering, required configuration, errors, and performance constraints. Compare proposed interfaces using actual call examples and failure scenarios.

Move complexity behind the interface only when it reduces repeated knowledge or concentrates future changes. Keep dependency injection focused on real variation. A wider interface can be justified when it represents genuinely different caller needs.

During migration, preserve observable behavior, route callers through the new contract, and retire redundant tests only after replacement coverage exercises their meaningful requirements. Avoid deleting coverage solely because its old module disappeared.
