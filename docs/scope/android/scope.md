# Android scope

The Android app owns its screen, appearance changes and native localization lookup. It uses the shared contract and theme. The [project scope](../index.md) sets the Tracer Bullet approach and Beta workflow.

## At a glance

| # | Feature | Phase | Status |
| --- | --- | --- | --- |
| 1 | Native Android greeting | First working slice | existing |

## First working slice

### 1. Native Android greeting · existing

You can launch the app and read the string returned by the shared core. The screen follows the system appearance and respects native font scaling.

**Done when:** the app packages both supported CPU architectures, passes a Unicode name through the native binding, and displays the greeting with the shared text style in light and dark appearance. [App entry](../../../apps/android/app/src/main/kotlin/foundation/mobile/MainActivity.kt) · [Greeting screen](../../../apps/android/presentation/src/main/kotlin/foundation/presentation/GreetingScreen.kt) · [Device tests](../../../apps/android/app/src/androidTest/kotlin/foundation/mobile/GreetingTest.kt)

Both appearances passed on the API 36 arm64 emulator. The x86_64 library was packaged. Runtime coverage on that architecture, a device with 16 KiB memory pages and the minimum Android version was still open in local verification. [Local results](../../quality/verification.md)
