# Architecture

Both apps resolve a name using the platform localization system. A SwiftUI view or Compose screen calls the generated `hello(name)` binding and displays its return value. The generated code transfers a UTF-8 string into Rust, invokes the export and lifts its result into a native string. The sole formatter is `foundation_core::hello`. There is no application server or runtime configuration service.

```text
SwiftUI → generated Swift → C ABI ┐
                                  ├→ mobile-ffi → foundation-core
Compose → generated Kotlin → JNA ┘

token JSON  → generator → Swift and Compose theme inputs
locale JSON → generator → native localization resources
```

The two arrows from JSON describe build-time generation. Color selection, font scaling, layout and accessibility run natively. An app can use its platform's navigation, gestures and controls without coordinating a shared renderer.

For a new capability, follow the [extension procedure](../plans/README.md). The [ownership matrix](ownership-matrix.md) identifies the source to change for each responsibility. The [foundation decision](../decisions/ADR-0001-foundation.md) records the trade-offs.
