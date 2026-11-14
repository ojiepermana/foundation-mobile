# 002 - Shared greeting contract

**Phase** Foundation · **Status** `existing`

Both native apps call the same greeting function through generated bindings, the code that carries values between languages.

**Done when:** each app can pass a name and display the returned string, including Unicode text, with one implementation of the greeting. [Core](../../../crates/core/src/lib.rs) · [Mobile export](../../../crates/mobile-ffi/src/lib.rs) · [Contract conventions](../../contracts/ffi-conventions.md)
