# Architecture compliance

Run `scripts/test.sh` from a checkout on macOS or Linux. The script stops on the first failed command. Run either native build separately or use the GitHub Actions jobs. The [verification record](verification.md) distinguishes local results from the configured CI matrix.

| Automated check | Evidence and failure condition |
| --- | --- |
| Rust format and lint | rustfmt checks workspace formatting. Clippy checks all targets and features with warnings denied, including the host generator. |
| Core and FFI contracts | Locked Cargo tests cover the formatter's handling of ordinary, empty and whitespace input and the exported Unicode string contract. |
| Cargo dependencies and governance | `tooling/validation/check-architecture.py` reads Cargo metadata. An unknown member, moved member, unapproved direct dependency or substituting an external crate for the workspace core fails. It checks every required architecture, rules, design, contracts, planning, decision and governance document for presence. |
| UniFFI generated files | `scripts/generate-bindings.sh --check` builds a host library and matching CLI, regenerates Swift, its header/module map and Kotlin in a temporary directory and diffs the whole binding tree. |
| Tokens, configuration and localization | `scripts/generate-design-tokens.sh --check` validates canonical data and compares expected native outputs. `--test` exercises failure and regeneration cases. |
| iOS linkage and UI | The macOS CI job builds a simulator app and unsigned device app, then uses XCTest on a simulator to read the greeting and sample the rendered background in light and dark mode. |
| Android linkage and UI | The Linux CI job packages both enabled ABIs, compiles instrumentation tests and runs them on an x86_64 emulator in both appearances. The tests call Rust with Unicode and check the displayed greeting’s text color and size against the generated theme. |

A new dependency or material change to the architecture needs an ADR and a corresponding policy update. For generated drift, change the source, run the generator without `--check`, and review the entire diff. CI can detect drift or a missing document. It cannot decide whether two algorithms have the same meaning, whether a document is accurate, or whether a boundary serves a real use case.

Reviewers trace a changed behavior from its owner into each affected client. Review API compatibility, accessibility, translation context and approval of new services or framework dependencies. On physical hardware, verify capabilities that a simulator cannot exercise when a future feature depends on them.
