# Anti-duplication

Locate the owner before adding a constant, rule, DTO, translation or asset. Search the Rust crates, canonical inputs and both apps. Review both native call sites when a shared requirement changes.

- Shared computations and validation belong in the core. A native view can decide how to present a validation result.
- Change FFI shapes in the annotated Rust export. Generate Kotlin and Swift in one operation.
- Shared visual decisions and shared translation values are generator inputs. Native typography, layout and resource lookup apply those definitions.
- A test may state an expected greeting literally. Application code displays the binding's return value.
- An OS-specific capability belongs in its own app. Promote shared behavior only once there is an identifiable contract and owner.

CI checks the Cargo graph and generated artifacts. Reviewers assess semantic duplication, including equivalent code written with different names or APIs.
