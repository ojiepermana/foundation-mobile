# 003 - Shared visual definitions

**Phase** Foundation · **Status** `done`

The apps share named values for color, type, spacing, corners and motion. Each platform renders them using its own native controls.

**Done when:** one set of source values generates both themes, both screens use the shared colors, type and spacing, and light and dark text meet the documented contrast threshold. [Design sources](../../../design-system/README.md) · [Accessibility](../../design-system/accessibility.md)

Color, type and page spacing reach both screens. Corner and motion values are generated for both apps, but no screen uses them, so they stay unproven until a first component needs them.

* [x] Verify on commit `58e3d2c570a0f5074357cd22eb228f5bf393e8a6`. `scripts/test.sh` regenerated both token files and matched the checked in copies, and the contrast test passed. Both screens read color, type and page spacing from `FoundationTokens`. In [Hosted run 43593365100](https://github.com/ojiepermana/foundation-mobile/actions/runs/43593365100) the iOS test sampled a light and a dark background, and the Android test matched the rendered text size and color to the generated values in both appearances. [Verification record](../../quality/verification.md)
