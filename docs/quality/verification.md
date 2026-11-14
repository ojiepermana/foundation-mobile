# Foundation verification · 2026-11-14

Local checks used an Apple Silicon Mac running macOS 27.0.1. A test result here describes the listed toolchain, ABI and runtime.

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
| CI configuration | actionlint 1.7.12 passed for the GitHub Actions workflow. The hosted jobs have not been executed as part of this verification. |

Separate samples of the four saved screenshots matched the canonical background exactly on both platforms, `#F4F6FA` in light appearance and `#111824` in dark appearance. The files are under `build/verification/ios/` and `build/verification/android/` and are excluded from source control.

On a separate iOS 26.5 simulator the greeting appeared, but both the app and system Settings stayed light after requesting dark appearance. The dark-mode pixel check on that runtime did not pass. A fresh 26.5 simulator stalled during first-boot CoreLocation migration before app launch, so the retry was canceled. The iOS 27.0 result above includes both appearances.

Physical devices, signed distribution, the minimum supported OS versions and a 16 KiB-page Android runtime were not exercised. The Android x86_64 library was cross-compiled and packaged locally. The CI emulator job is configured to exercise that ABI.
