# Service and module rules

The greeting is a pure function. There are no application services to start, stop or register.

Before proposing a service, name its single responsibility, the existing module that might own it, its caller, and the reason extraction pays for itself. Document the owner, public operations and data, permitted dependencies, structured errors, lifecycle, concurrency, cancellation and tests. If the change introduces a crate or changes an ownership boundary, record the trade-off in a spec under `docs/specs/`.

A service may call another service through its public interface. Keep private state and internal storage with the owning module. Draw the dependency edges and reject cycles before adding the crate. Keep a capability beside its first caller when a separate service would only forward the call.
