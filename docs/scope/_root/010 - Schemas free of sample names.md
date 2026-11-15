# 010 - Schemas free of sample names

**Phase** Foundation · **Status** `planned` · needs a decision · from spec 0003

You can replace the greeting with your first feature without editing a foundation schema. Today the localization schema requires a key named `greeting_recipient`, and the token schema requires a typography role named `greeting`. A product that removes the sample fails `scripts/generate-design-tokens.sh` and the generator tests that load the live catalog.

**Done when:** the localization schema asks for at least one key and names none, the typography role carries a name for its purpose, both native themes and the generator tests follow, and a catalog and a token set with no greeting name pass `scripts/generate-design-tokens.sh --check`. [Localization schema](../../../shared/specifications/localization.schema.json) · [Token schema](../../../design-system/schemas/tokens.schema.json) · [Spec 0003](../../specs/_root/0003-new-project-from-foundation.md)

* [ ] Design it (spec): `/architect schemas free of sample names`
