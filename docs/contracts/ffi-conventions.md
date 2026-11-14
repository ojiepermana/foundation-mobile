# Mobile contract

The public contract is `hello(name: String) -> String` in `crates/mobile-ffi`. It delegates to the core, accepts empty and Unicode input, and returns an owned string. It has no error channel or external side effects. The formatter emits the English greeting specified by the foundation contract. The name supplied by the native example is localizable.

UniFFI derives the native functions, buffer handling and contract checks from the Rust export. The binding generator and runtime use the same pinned package. Ship the generated source together with a library built from the same revision. Never expose raw pointers to native views or hand-maintain declarations for the generated C ABI.

## Extending the contract

| Topic | Convention for a future contract |
| --- | --- |
| Inputs and results | Use explicit application records and enums when a scalar no longer expresses the use case. Map private core, persistence and backend transport shapes at the adapter. Keep future OpenAPI models behind that boundary. |
| Optionality | Use `Option<T>` for meaningful absence. Document the difference between absence, empty collections and empty text. Use fixed-width integer types across the ABI. |
| Errors | Export a typed UniFFI error with stable variants or an explicit machine-readable code. Describe retryability and which failures callers can act on. Translate user-facing messages in the native presentation layer. |
| Compatibility | Review removed/renamed APIs, record fields, integer widths, optionality and enum variants as source- or ABI-affecting changes. Version a breaking contract and coordinate regeneration, both app updates and release together. |
| Async and cancellation | Specify execution context, completion, error mapping and what cancellation stops before introducing an async export. Define behavior of partial work and callbacks after cancellation. Keep blocking work off the UI thread. |
| Resources | For future UniFFI objects, document who retains a handle, when it is released and which calls are thread-safe. Keep native resource handles in the owning platform adapter when possible. |
| Native capabilities | Define only the operations the core requires. State callback threading, errors, permissions and teardown before adding a UniFFI callback interface. |

Check edge cases in Rust and pass representative values through both generated languages. A Rust-only test cannot prove header import, binary linkage, symbol lookup or native rendering.
