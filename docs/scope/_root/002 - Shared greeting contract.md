# 002 - Shared greeting contract

**Phase** Foundation · **Status** `done`

Both native apps call the same greeting function through generated bindings, the code that carries values between languages.

**Done when:** each app can pass a name and display the returned string, including Unicode text, with one implementation of the greeting. [Core](../../../crates/core/src/lib.rs) · [Mobile export](../../../crates/mobile-ffi/src/lib.rs) · [Contract conventions](../../contracts/ffi-conventions.md)

The contract carries one string in and one string out. The conventions also describe records, typed errors, async calls and native callbacks, and none of those has a caller or a test yet. The index lists that work under Deferred.

* [x] Verify on commit `58e3d2c570a0f5074357cd22eb228f5bf393e8a6`. `scripts/test.sh` passed the contract test `exported_contract_preserves_unicode` on macOS 27.0.1. Both apps pass the catalog recipient to `hello` and displayed **Hello, World!** in [Hosted run 43593365100](https://github.com/ojiepermana/foundation-mobile/actions/runs/43593365100) on `65875793e37c708f31088fb65dca939d57cc2a50`, and no app, core or binding source has changed since. The Android test called `hello("Zoë 🌍")` on the emulator. On iOS the Unicode round trip ran through the generated Swift binding in a host executable. Neither screen has shown a Unicode name. [Verification record](../../quality/verification.md)
