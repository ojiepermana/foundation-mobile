# Configuration

`foundation.json` contains public build-time configuration used by shared tooling. Its v1 schema fixes the bundle development locale to `en`. The generator uses this setting to select the required catalog and to place Android defaults in unqualified `res/values`. The iOS project uses the same development region. Change the catalog, schema and native development region together for a fallback migration.

| Kind | Ownership and consumption |
| --- | --- |
| Shared build settings | Put cross-platform public values in the versioned shared schema and generate only the outputs required by a consumer. |
| Native build settings | Keep deployment targets, bundle and application IDs, entitlements and manifest entries in Xcode or Gradle. Product identity lives in `apps/ios/Config/Identity.xcconfig` and `apps/android/identity.properties`. |
| Environments | If environments become necessary, define their names and public override fields in the shared schema. Resolve them at build time and validate the resulting configuration for each environment. |
| Runtime settings and future feature flags | Add a definition through an approved design that specifies typing, defaults, ownership, compatibility and the runtime consumer. |
| Signing and other secrets | Provision through the native credential store or CI secret store. Only public settings belong here. |

Validate with `scripts/generate-design-tokens.sh --check`. Unknown keys and unsupported schema versions fail the build check. For an incompatible change, version the schema, update the reader and migrate every checked-in config in the same change. [Configuration schema](../specifications/config.schema.json)
