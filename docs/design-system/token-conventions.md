# Token conventions

A primitive names a value. A semantic role describes where to use it. For example, `colors.semantic.background.dark` references a primitive whose value is an opaque sRGB hex color. Use lower camel case for token names and uppercase `#RRGGBB` for colors. Names become native properties, so choose identifiers usable in Swift and Kotlin.

| Source | Primitives | Semantic aliases |
| --- | --- | --- |
| colors.json | Opaque colors | One primitive reference for each of `light` and `dark` |
| typography.json | Scales and numeric weights | A scale reference and a weight reference |
| spacing.json | Nonnegative layout units | Spacing by purpose |
| radius.json | Nonnegative layout units | Corner treatments by purpose |
| motion.json | Durations in milliseconds | Motion intent |

References are local to each group and point directly to primitives. Typography scales carry a size and line height in logical text units at the default user text setting. A scale name identifies its typographic intent. Platform adapters map that intent to native scaling behavior. The weight scale uses the nine conventional weights from 100 through 900.

Change the schema alongside a new token category or required role. Keep existing role names stable across both apps, or migrate their uses in the same change. Run generation and both platform builds when changing a consumed role. [Canonical token schema](../../design-system/schemas/tokens.schema.json)
