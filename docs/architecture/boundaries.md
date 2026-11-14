# Boundaries

| Layer | Inputs | Public surface and limits |
| --- | --- | --- |
| Native presentation | Native state, localized values, generated tokens and FFI APIs | Views render results, adapt to appearance and handle user events. Add a ViewModel when state or lifecycle needs one. |
| Native platform integration | OS APIs and app lifecycle | Swift owns Apple services and Kotlin owns Android services. Introduce a capability interface only when a shared use case needs one. |
| Shared Rust | Application inputs | Core functions own application behavior. The FFI crate maps exported shapes to the core. The core has no UI or UniFFI imports. |
| Design system | Canonical primitives and semantic aliases | Generated Swift/Kotlin values form the shared visual vocabulary. Native themes decide how to apply them. |
| Resources and tooling | Public schemas, locale catalogs, assets and crate metadata | Validation and generation run on the build host. Native artifacts are disposable derivatives of these inputs. |

A native SDK callback can update presentation directly. If it affects a shared decision, translate it at a documented capability boundary and let the core decide. Feature-specific adapters, ViewModels and services need an actual caller before introduction.
