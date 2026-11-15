# 004 - Shared settings, text and brand assets

**Phase** Foundation · **Status** `done`

You can change the public fallback locale and shared copy at their source. The brand rules identify where future artwork and its exports belong.

**Done when:** both apps receive the English greeting recipient from one catalog, invalid settings and translation placeholders are detected, and brand asset ownership is documented. [Configuration](../../../shared/config/README.md) · [Localization](../../../shared/localization/README.md) · [Assets](../../../shared/assets/README.md)

Only the English catalog has run inside an app. The core forms the sentence `Hello, {name}!` in English, so a second language would translate the recipient and nothing else. The index lists a second language under Deferred.

* [x] Verify on commit `58e3d2c570a0f5074357cd22eb228f5bf393e8a6`. `scripts/test.sh` regenerated both English catalogs from the shared catalog and matched the checked in copies. The generator tests rejected an open configuration schema, invalid resource keys and mismatched placeholders. Both apps read `greeting_recipient` from their generated catalog and displayed **Hello, World!** in [Hosted run 43593365100](https://github.com/ojiepermana/foundation-mobile/actions/runs/43593365100). The assets guide names `shared/assets/` as the owner of future artwork. [Verification record](../../quality/verification.md)
