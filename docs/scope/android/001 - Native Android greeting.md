# 001 - Native Android greeting

**Phase** First working slice · **Status** `existing`

You can launch the app and read the string returned by the shared core. The screen follows the system appearance and respects native font scaling.

**Done when:** the app packages both supported CPU architectures, passes a Unicode name through the native binding, and displays the greeting with the shared text style in light and dark appearance. [App entry](../../../apps/android/app/src/main/kotlin/foundation/mobile/MainActivity.kt) · [Greeting screen](../../../apps/android/presentation/src/main/kotlin/foundation/presentation/GreetingScreen.kt) · [Device tests](../../../apps/android/app/src/androidTest/kotlin/foundation/mobile/GreetingTest.kt)

Both appearances passed on the API 36 arm64 emulator locally and on the API 36 x86_64 emulator in the hosted run. The minimum Android version, a runtime with 16 KiB memory pages and large text are planned in [002](002%20-%20Lowest%20supported%20Android%20and%20large%20text.md). Physical device coverage remains unverified. [Local results](../../quality/verification.md) · [Hosted run 43593365100](https://github.com/ojiepermana/foundation-mobile/actions/runs/43593365100)
