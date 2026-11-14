# 002 - Lowest supported Android and large text

**Phase** Verification · **Status** `planned`

You can trust the declared minimum version, the 16 KiB page packaging and the font scaling claim, because all three have run. The app declares API 24 as its minimum, and the greeting has only run on API 36 with 4 KiB pages. No test changes the font scale.

**Done when:** the greeting tests pass on an API 24 emulator and on a 16 KiB page emulator in light and dark appearance, the greeting stays whole at the largest font scale, and the result names each runtime. [Build settings](../../../apps/android/app/build.gradle.kts) · [Device tests](../../../apps/android/app/src/androidTest/kotlin/foundation/mobile/GreetingTest.kt)

* [ ] Add the runs with `/develop lowest supported Android and large text`.
