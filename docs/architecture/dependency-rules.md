# Dependency rules

1. The Cargo workspace contains `mobile-ffi → foundation-core`. Core currently uses only the Rust standard library. The FFI crate depends directly on the local core and the pinned UniFFI crate. Cargo checks cycles, and the repository validator checks member location and direct dependencies, including optional, target, build and dev dependencies.
2. Proc-macro exports define the cross-language API. The `bindgen` Cargo feature enables host CLI dependencies. Build both mobile libraries with default features. Link the Apple static archive and package an Android shared object for each enabled ABI.
3. App sources depend on their own platform SDK, generated bindings, native theme and resources. The two app trees do not import one another. The core does not call into platform UI.
4. Token and resource generators consume neutral sources and emit platform artifacts. A generator must never recover canonical values from native output. Platform builds consume the source snapshots under version control.
5. Propose new dependency edges with an owning module, a use case and a test. Update the policy check with the architecture decision when an edge changes. Review transitive dependency and binary-size effects when changing libraries.

See [architecture compliance](../quality/architecture-compliance.md) for what CI inspects.
