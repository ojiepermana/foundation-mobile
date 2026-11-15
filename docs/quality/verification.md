# Foundation verification · 2026-11-14

This record lists what ran, where it ran and what has not run yet. Local checks used an Apple Silicon Mac running macOS 27.0.1. Hosted checks ran on GitHub Actions. A test result here describes the listed toolchain, ABI and runtime.

## Local checks

| Check | Result |
| --- | --- |
| Rust workspace | `cargo build --locked --workspace` passed with Rust 1.100.0. `scripts/test.sh` passed rustfmt, Clippy with warnings denied and three Rust tests. The workspace build and shared checks also passed from an isolated source copy. |
| ABI generation | UniFFI 0.31.2 generated Swift, its C header and Clang module map, and Kotlin from the compiled host library. Regenerating in a temporary directory produced an identical tree. The check rejected an edited binding even with its original byte count and timestamp. Regenerating repaired it. A separate Swift executable linked the host static archive and round-tripped both `Zoë 🌍` and an empty name through the generated binding. |
| Design system and resources | Generation and byte comparisons passed for both native token files and both English catalogs. Seven generator tests exercise invalid schemas, unresolved references, contrast, placeholder reordering, mismatched translations and edited or missing outputs. Apple `plutil` accepted the English strings resource. |
| Architecture | Cargo dependency policy and required-document checks passed. In an isolated copy, the checker rejected a renamed, prohibited dev dependency and a missing contract document. |
| iOS compilation | The Xcode 27.1 / Swift 6.4 build in Swift 6 language mode linked the generated Swift and Rust archive for arm64 and x86_64 simulators and produced an unsigned arm64 Release build for iOS hardware. The x86_64 simulator build was verified by inspecting its Mach-O architecture. |
| iOS runtime | On an iPhone 17 simulator running iOS 27.0, XCTest launched the app in light and dark appearances, read **Hello, World!** through accessibility and verified that a background pixel actually changed between palettes. Xcode also packaged an additional locale in an isolated build through the synchronized App group. |
| Android compilation | Gradle 9.3.1 and AGP 9.1.0 assembled the debug app, instrumentation APK and unsigned Release APK with Temurin 17.0.21. `lintDebug` reported zero errors and six dependency-version warnings. |
| Android runtime | Two instrumentation tests passed in each appearance on an API 36 arm64 emulator. The tests exercise Unicode through Kotlin/JNA/Rust, read **Hello, World!** from Compose semantics, and compare the rendered text style with the generated size and foreground color. The saved screenshots provide independent pixel evidence for the background. |
| Android packaging | APK zip alignment passed `zipalign -c -P 16`. ELF load segments have 16 KiB alignment in the packaged Rust, JNA and Compose libraries for both ABIs. Local runtime verification used a 4 KiB-page emulator. |
| CI configuration | actionlint 1.7.12 passed for the GitHub Actions workflow. The jobs it configures ran in the [hosted run](#hosted-run) below. |

Separate samples of the four saved screenshots matched the canonical background exactly on both platforms, `#F4F6FA` in light appearance and `#111824` in dark appearance. The files are under `build/verification/ios/` and `build/verification/android/` and are excluded from source control.

On a separate iOS 26.5 simulator the greeting appeared, but both the app and system Settings stayed light after requesting dark appearance. The dark-mode pixel check on that runtime did not pass. A fresh 26.5 simulator stalled during first-boot CoreLocation migration before app launch, so the retry was canceled. The iOS 27.0 result above includes both appearances. The hosted run below passed both appearances on iOS 26.5.

## Hosted run

[Hosted run 43593365100](https://github.com/ojiepermana/foundation-mobile/actions/runs/43593365100) ran the [workflow](../../.github/workflows/foundation.yml) on revision `65875793e37c708f31088fb65dca939d57cc2a50`, pushed to `main` on 2026-11-14. All three jobs passed.

| Job | Runner | Outcome | What ran |
| --- | --- | --- | --- |
| `foundation` | `ubuntu-24.04`, image 20261111.370.1 | Passed | `cargo build --locked --workspace` and `scripts/test.sh` passed with Rust 1.100.0 and Python 3.12. Three Rust tests and seven generator tests passed, along with the dependency policy and required document checks. |
| `ios` | `macos-26-arm64`, image 20261102.0473.1 | Passed | Xcode 26.5 built the app for the arm64 simulator and linked an unsigned Release build for iOS hardware. An iPhone 17 simulator running iOS 26.5 was shut down and booted again for each appearance. XCTest read **Hello, World!** through accessibility and checked that the background pixel was light in light appearance and dark in dark appearance. One test passed in each appearance. |
| `android` | `ubuntu-24.04`, image 20261111.370.1 | Passed | Gradle 9.3.1 assembled the debug app and the instrumentation APK with Temurin 17.0.21. On an API 36 x86_64 emulator (`google_apis` image, emulator 37.2.13.0), two instrumentation tests passed with night mode off and again with night mode on. They exercise Unicode through Kotlin/JNA/Rust and read the greeting from Compose semantics. |

The workflow runs on every push, so later revisions have their own runs. This record describes the run above.

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
