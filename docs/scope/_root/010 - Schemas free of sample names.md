# 010 - Schemas free of sample names

**Phase** Foundation · **Status** `done` · from spec 0003

You can replace the greeting with your first feature without editing a foundation schema. Today the localization schema requires a key named `greeting_recipient`, and the token schema requires a typography role named `greeting`. A product that removes the sample fails `scripts/generate-design-tokens.sh` and the generator tests that load the live catalog.

**Done when:** the localization schema asks for at least one key and names none, the typography role carries a name for its purpose, both native themes and the generator tests follow, and a catalog and a token set with no greeting name pass `scripts/generate-design-tokens.sh --check`. [Localization schema](../../../shared/specifications/localization.schema.json) · [Token schema](../../../design-system/schemas/tokens.schema.json) · [Spec 0003](../../specs/_root/0003-new-project-from-foundation/index.md) · [Spec 0004](../../specs/_root/0004-schemas-free-of-sample-names/index.md)

* [x] Design it (spec): `/architect schemas free of sample names`
* [x] Build it: `/develop schemas free of sample names`
   * [x] The one key rule in the localization schema and the `heading` role through both apps (Build plan 1, 2 · AC-1 to AC-4)
   * [x] Generator tests on their own source tree, after the milestone above (Build plan 3 · AC-5, AC-6)
   * [x] The document updates and the verification record, after both milestones above (Build plan 4, 5 · AC-4, AC-6, AC-7)
* [x] Verify it: `/check verify schemas free of sample names`
* [x] Test it: `/test schemas free of sample names`
