# Design system rules

1. Put shared visual values in `design-system/tokens/`. Reference semantic roles from presentation.
2. Update the Draft 7 schema and native mappings together when adding a new token shape.
3. Regenerate with `scripts/generate-design-tokens.sh` and include the native projections in the same change.
4. Run `scripts/generate-design-tokens.sh --check` to detect drift and `--test` when changing tooling. Verify the affected screen in both appearances and at larger text sizes.

Changes to public role names require migration of both consumers. Definitions and platform mapping belong in the [design system documentation](../design-system/token-conventions.md).
