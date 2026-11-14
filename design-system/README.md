# Design system

Edit the five JSON files in `tokens/` to change shared visual decisions. Each file contains primitive values and semantic aliases. The native apps use the generated semantic API.

Run these commands from the repository root.

```sh
scripts/generate-design-tokens.sh
scripts/generate-design-tokens.sh --check
scripts/generate-design-tokens.sh --test
```

The first command validates the token, configuration and locale sources, then writes both native token files and both platforms’ string resources. The second compares their UTF-8 bytes and reports drift. The third exercises failure cases in temporary directories. Python 3.9 or newer and pip are required. On first use the script downloads one hash-pinned schema-validator wheel to `build/tooling/`. Subsequent runs reuse that cache. [Validator release](https://pypi.org/project/fastjsonschema/2.21.2/)

The [schema](schemas/tokens.schema.json) describes the files as a single Draft 7 document keyed by filename stem. See the [conventions](../docs/design-system/token-conventions.md) and [platform mappings](../docs/design-system/platform-mapping.md) when extending it.
