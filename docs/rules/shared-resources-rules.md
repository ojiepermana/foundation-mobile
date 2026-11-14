# Shared resource ownership

The shared resources owner maintains canonical [build configuration](../../shared/config/README.md), [localization](../../shared/localization/README.md) and [brand assets](../../shared/assets/README.md). Use the Draft 7 schemas in `shared/specifications/` for the implemented JSON formats. Native platform settings and operating-system artwork belong with the relevant app.

Keep generated native strings under the resource generator’s ownership. Include source and regenerated changes together. Run `scripts/generate-design-tokens.sh --check` to validate configuration shape, keys, placeholders and generated files. Changes to source formats must account for both native consumers. Treat incompatible changes as migrations with a documented rollout.
