# Repository structure

| Path | What belongs here |
| --- | --- |
| `apps/ios/` | Xcode project, SwiftUI app entry and presentation, native theme consumption and UI tests. Product identity lives in `Config/Identity.xcconfig`. |
| `apps/android/` | Gradle project, activity and packaging, Compose presentation/theme sources and instrumentation tests. Product identity lives in `identity.properties`. |
| `crates/core/` | Framework-independent Rust and unit tests. |
| `crates/mobile-ffi/` | Proc-macro exports, ABI configuration and feature-gated host binding generator entry point. |
| `bindings/{swift,kotlin}/` | Generated source snapshots used by native projects. |
| `design-system/` | Canonical semantic tokens, schema and authoring instructions. |
| `shared/` | Configuration definitions, localization catalogs, asset conventions and shared resource specifications. |
| `tooling/` | Build-host generation, validation and project derivation code. |
| `tests/contracts/` | Cargo integration tests for exported behavior. Platform runtime tests live with their apps. |
| `scripts/` | Public commands that resolve paths from the checkout. |
| `.github/workflows/` | Hosted verification of the same entry points. |
| `docs/` | Architecture, rules, design system, contracts and quality. `docs/scope/` lists what to build and its status. `docs/specs/` holds design and decision records. `docs/decisions/` holds the founding decision. |
| `target/`, `build/`, Android Gradle build directories | Local compilation, tools, packages and test evidence. Excluded from source control. |

Create a platform adapter directory when a feature needs an OS capability. Add fixtures when a test consumes them. [Service rules](../rules/service-rules.md) describe when a separate module or crate is justified.
