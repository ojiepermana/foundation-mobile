# Working in the mobile foundation

## Before editing

Inspect the checkout and read the [ownership matrix](docs/architecture/ownership-matrix.md). Locate the existing owner, public contract, callers and tests. Search both apps and the shared sources for an existing implementation. Use the [dependency rules](docs/architecture/dependency-rules.md) to identify permitted edges and the [quality checks](docs/quality/architecture-compliance.md) to choose verification.

## During implementation

- Put shared behavior in `crates/core`. Change a mobile API at the [UniFFI boundary](docs/contracts/ffi-conventions.md). Keep both native clients on the same contract.
- Implement presentation and OS integration in the owning app. Follow the [iOS](docs/rules/ios-rules.md) or [Android](docs/rules/android-rules.md) rules for native behavior and accessibility.
- Change shared visual values in [tokens](design-system/README.md). Change shared copy, configuration and brand sources under [shared resources](docs/rules/shared-resources-rules.md). Regenerate their native outputs. Never hand-edit generated files.
- Check the [service rules](docs/rules/service-rules.md) before allocating a new responsibility. Add a plan for a new capability and an ADR for a material ownership, contract or dependency decision. Update the affected architecture documents in the same change.

## Before handoff

Run `scripts/test.sh` and the [build and device checks](README.md) for each affected platform. For a contract change, verify both clients. Include exact commands, target/toolchain, observed result and any unverified target in the handoff.
