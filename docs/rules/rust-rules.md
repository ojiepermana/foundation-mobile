# Rust

Implement shared algorithms in `crates/core`. Exercise edge values at the core function. Keep exports thin and test the public contract when type conversion can affect native callers. The greeting accepts the caller's complete Unicode string, including whitespace and an empty name.

Pin the compiler in `rust-toolchain.toml` and dependencies in `Cargo.lock`. Use `--locked` for builds and tests. Keep the UniFFI generator feature restricted to host tooling. Enabling CLI features in a production cross-build would pull in the generator dependencies.

After a signature or UniFFI upgrade, regenerate both languages and run both apps. [FFI conventions](../contracts/ffi-conventions.md) cover new types, errors and ownership. [Dependency rules](../architecture/dependency-rules.md) govern manifest changes.
