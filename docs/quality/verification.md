# Foundation verification · 2026-11-15

This record lists what ran, where it ran and what has not run yet. Local checks used an Apple Silicon Mac running macOS 27.0.1. Hosted checks ran on GitHub Actions. A test result here describes the listed toolchain, ABI and runtime.

## Local checks

| Check | Result |
| --- | --- |
| Rust workspace | `cargo build --locked --workspace` passed with Rust 1.100.0. `scripts/test.sh` passed rustfmt, Clippy with warnings denied and three Rust tests. The workspace build and shared checks also passed from an isolated source copy. |
| ABI generation | UniFFI 0.31.2 generated Swift, its C header and Clang module map, and Kotlin from the compiled host library. Regenerating in a temporary directory produced an identical tree. The check rejected an edited binding even with its original byte count and timestamp. Regenerating repaired it. A separate Swift executable linked the host static archive and round-tripped both `Zoë 🌍` and an empty name through the generated binding. |
| Design system and resources | Generation and byte comparisons passed for both native token files and both English catalogs. Nine generator tests exercise invalid schemas, unresolved references, contrast, placeholder reordering, mismatched translations and edited or missing outputs. Apple `plutil` accepted the English strings resource. The tests read `tooling/codegen/fixtures/sources/`, not the checkout's own sources. |
| Architecture | Cargo dependency policy and required-document checks passed. In an isolated copy, the checker rejected a renamed, prohibited dev dependency and a missing contract document. |
| Product identity | Ran on 2026-11-15, after the identity moved into `apps/ios/Config/Identity.xcconfig` and `apps/android/identity.properties`. `scripts/test.sh` passed, with `scripts/init-project.sh --check` printing `foundation` and `--test` passing 21 unit tests. One of them derived a temporary copy of the checkout, required `derived` from the copy's own check and passed the copy's architecture check. Both apps carried `dev.foundation.mobile`, `Mobile Foundation`, version `0.1.0` and build `1`, read from the simulator and device `Info.plist` and from `aapt2 dump badging` on the debug APK. The iOS greeting test passed in light and dark on the iPhone 17 simulator running iOS 27.0, with the UI test bundle as `dev.foundation.mobile.uitests`. Two instrumentation tests passed in each appearance on the API 36 arm64 emulator. In a temporary copy derived as `Zoë's Proof` with `dev.example.derived`, the simulator app and the debug APK built, and each matched its identity file with the same commands the workflow uses. The greeting tests did not run under the sample identity locally. The [derived hosted run](#hosted-run) ran them under that identity on both platforms. |
| Schemas free of sample names | Ran on 2026-11-15, after the localization schema stopped naming a key and the typography role `greeting` became `heading`. `scripts/test.sh` passed, with nine generator tests passing on Python 3.9.6. `scripts/generate-design-tokens.sh --check` passed on the checkout. After the rename to `typographyHeading`, the simulator build and the unsigned device build of the iOS app succeeded, and the iOS greeting test passed in light and in dark on an iPhone 17 simulator running iOS 27.0, with the simulator set to each appearance before its run. The Android debug app and instrumentation APK assembled, and two instrumentation tests passed with night mode off and again with night mode on, on an API 36 arm64 emulator. In a scratch clone whose catalog held the single key `welcome_title`, generation, `--check` and `--test` passed, `git status --short` listed only the catalog and the two generated string files, and `git grep -i greeting` found nothing in the generator inputs and outputs. In the same clone an empty catalog and a token set without `heading` were each refused by `--check`, and with the catalog and `typography.json` both emptied `--test` still passed nine tests while `--check` failed. The working checkout was unchanged afterwards. |
| iOS compilation | The Xcode 27.1 / Swift 6.4 build in Swift 6 language mode linked the generated Swift and Rust archive for arm64 and x86_64 simulators and produced an unsigned arm64 Release build for iOS hardware. The x86_64 simulator build was verified by inspecting its Mach-O architecture. |
| iOS runtime | On an iPhone 17 simulator running iOS 27.0, XCTest launched the app in light and dark appearances, read **Hello, World!** through accessibility and verified that a background pixel actually changed between palettes. Xcode also packaged an additional locale in an isolated build through the synchronized App group. |
| Android compilation | Gradle 9.3.1 and AGP 9.1.0 assembled the debug app, instrumentation APK and unsigned Release APK with Temurin 17.0.21. `lintDebug` reported zero errors and six dependency-version warnings. |
| Android runtime | Two instrumentation tests passed in each appearance on an API 36 arm64 emulator. The tests exercise Unicode through Kotlin/JNA/Rust, read **Hello, World!** from Compose semantics, and compare the rendered text style with the generated size and foreground color. The saved screenshots provide independent pixel evidence for the background. |
| Android packaging | APK zip alignment passed `zipalign -c -P 16`. ELF load segments have 16 KiB alignment in the packaged Rust, JNA and Compose libraries for both ABIs. Local runtime verification used a 4 KiB-page emulator. |
| CI configuration | actionlint 1.7.12 passed for the GitHub Actions workflow as it stood on 2026-11-14. The jobs it configured ran in the [hosted run](#hosted-run) below. The `derived` input and the identity comparison steps added on 2026-11-15 were parsed as YAML only. actionlint was not run on them. They ran on hosted runners in the [derived hosted run](#hosted-run) below. |

Separate samples of the four saved screenshots matched the canonical background exactly on both platforms, `#F4F6FA` in light appearance and `#111824` in dark appearance. The files are under `build/verification/ios/` and `build/verification/android/` and are excluded from source control.

On a separate iOS 26.5 simulator the greeting appeared, but both the app and system Settings stayed light after requesting dark appearance. The dark-mode pixel check on that runtime did not pass. A fresh 26.5 simulator stalled during first-boot CoreLocation migration before app launch, so the retry was canceled. The iOS 27.0 result above includes both appearances. The hosted run below passed both appearances on iOS 26.5.

## Hosted run

[Hosted run 43593365100](https://github.com/ojiepermana/foundation-mobile/actions/runs/43593365100) ran the [workflow](../../.github/workflows/foundation.yml) on revision `65875793e37c708f31088fb65dca939d57cc2a50`, pushed to `main` on 2026-11-14. All three jobs passed.

| Job | Runner | Outcome | What ran |
| --- | --- | --- | --- |
| `foundation` | `ubuntu-24.04`, image 20261111.370.1 | Passed | `cargo build --locked --workspace` and `scripts/test.sh` passed with Rust 1.100.0 and Python 3.12. Three Rust tests and seven generator tests passed, along with the dependency policy and required document checks. |
| `ios` | `macos-26-arm64`, image 20261102.0473.1 | Passed | Xcode 26.5 built the app for the arm64 simulator and linked an unsigned Release build for iOS hardware. An iPhone 17 simulator running iOS 26.5 was shut down and booted again for each appearance. XCTest read **Hello, World!** through accessibility and checked that the background pixel was light in light appearance and dark in dark appearance. One test passed in each appearance. |
| `android` | `ubuntu-24.04`, image 20261111.370.1 | Passed | Gradle 9.3.1 assembled the debug app and the instrumentation APK with Temurin 17.0.21. On an API 36 x86_64 emulator (`google_apis` image, emulator 37.2.13.0), two instrumentation tests passed with night mode off and again with night mode on. They exercise Unicode through Kotlin/JNA/Rust and read the greeting from Compose semantics. |

[Hosted run 43701289339](https://github.com/ojiepermana/foundation-mobile/actions/runs/43701289339) ran the same workflow on revision `4a153fe4715bb410407b7fdb1652caf13734e9d8` on 2026-11-15. It was started by hand through `workflow_dispatch` with the `derived` input set. All three jobs passed.

| Job | Runner | Outcome | What ran |
| --- | --- | --- | --- |
| `foundation` | `ubuntu-24.04`, image 20261111.370.1 | Passed | `cargo build --locked --workspace` and `scripts/test.sh` passed. Three Rust tests, 21 derivation tests and seven generator tests passed. This job does not derive. |
| `ios` | `macos-26-arm64`, image 20261102.0473.1 | Passed | The derive step ran `scripts/init-project.sh --name "Zoë's Proof" --app-id dev.example.derived` and listed the two identity files, `README.md`, this record and the removed `graphify-out/`. Xcode 26.5 built the derived app for the arm64 simulator. The comparison step printed `Identity file: dev.example.derived, Zoë's Proof` and `Built app: dev.example.derived, Zoë's Proof`. The unsigned device build linked. On an iPhone 17 simulator running iOS 26.5, the greeting test passed once in light and once in dark appearance, with the UI test runner signed as `dev.example.derived.uitests.xctrunner`. |
| `android` | `ubuntu-24.04`, image 20261111.370.1 | Passed | The derive step ran the same command and listed the same paths. Gradle 9.3.1 assembled the derived debug app and instrumentation APK with Temurin 17.0.21. The comparison step printed `Identity file: dev.example.derived, Zoë's Proof` and `Built app: dev.example.derived, Zoë's Proof`. On an API 36 x86_64 emulator (`google_apis` image, emulator 37.2.13.0), two instrumentation tests passed with night mode off and again with night mode on. The app compile tasks were up to date, so the tests ran against the derived build. |

[Hosted run 43701281055](https://github.com/ojiepermana/foundation-mobile/actions/runs/43701281055) ran on the push of the same revision. All three jobs passed. In the `ios` and `android` jobs the derive step was skipped, and both comparison steps passed with `dev.foundation.mobile` and `Mobile Foundation`.

[Hosted run 43723923953](https://github.com/ojiepermana/foundation-mobile/actions/runs/43723923953) ran the same workflow on revision `b64055a6d5e2259e9fba401dbdd70deabaf0eac6`, pushed to `main` on 2026-11-15. It was the first hosted run after the localization schema stopped naming a key and the typography role `greeting` became `heading`. All three jobs passed.

| Job | Runner | Outcome | What ran |
| --- | --- | --- | --- |
| `foundation` | `ubuntu-24.04`, image 20261111.370.1 | Passed | `cargo build --locked --workspace` and `scripts/test.sh` passed with Rust 1.100.0 and Python 3.12. Three Rust tests, 50 derivation tests and nine generator tests passed. |
| `ios` | `macos-26-arm64`, image 20261102.0473.1 | Passed | Xcode 26.5 built the app for the arm64 simulator and linked the unsigned device build. The derive step was skipped, and the comparison step printed `Identity file: dev.foundation.mobile, Mobile Foundation` and `Built app: dev.foundation.mobile, Mobile Foundation`. On an iPhone 17 simulator running iOS 26.5, the greeting test passed once in light and once in dark appearance, with the simulator set to each appearance before its run. |
| `android` | `ubuntu-24.04`, image 20261111.370.1 | Passed | Gradle 9.3.1 assembled the debug app and the instrumentation APK with Temurin 17.0.21. The derive step was skipped, and the comparison step printed the same two lines. On an API 36 x86_64 emulator (`google_apis` image, emulator 37.2.13.0), two instrumentation tests passed with night mode off and again with night mode on. |

[Hosted run 43724499680](https://github.com/ojiepermana/foundation-mobile/actions/runs/43724499680) ran on the push of revision `3019db7e2a3a0a80027bf7afc9818df9b993b479` on 2026-11-15. That revision changed only the coordination log of scope 010 and the knowledge graph. All three jobs passed with the same test counts. Its `android` job ran on image 20261111.127.1.

The workflow runs on every push, so later revisions have their own runs. This record describes the five runs above.

## Runtimes exercised

| Target | Local | Hosted |
| --- | --- | --- |
| Shared checks | macOS 27.0.1 on Apple Silicon, Rust 1.100.0 | Ubuntu 24.04 on x86_64, Rust 1.100.0 |
| iOS simulator | iPhone 17, iOS 27.0, arm64, Xcode 27.1, light and dark | iPhone 17, iOS 26.5, arm64, Xcode 26.5, light and dark |
| Android emulator | API 36, arm64, 4 KiB pages, light and dark | API 36, x86_64, light and dark |

## Still unverified

This is the one list of targets that have not run. A target leaves this list when a local or hosted result above covers it.

- Physical devices on either platform.
- Signed distribution.
- The minimum supported OS versions.
- An Android runtime with 16 KiB pages. The packaging alignment passed locally, the local emulator used 4 KiB pages and the hosted run did not check the page size of its emulator.
- An x86_64 iOS simulator runtime. That build was compiled locally and has not run.
