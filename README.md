# Native mobile foundation

A SwiftUI app and a Jetpack Compose app both display **Hello, World!**. Each reads the recipient from a generated native localization resource and calls the same Rust function through UniFFI. The core has no dependencies. Both screens use the generated semantic palette, type role and spacing and follow the system appearance.

Start with the [architecture overview](docs/architecture/overview.md), [ownership matrix](docs/architecture/ownership-matrix.md) and [foundation decision](docs/decisions/ADR-0001-foundation.md). The [scope](docs/scope/index.md) lists what is built and what is next. Contributors should read [AGENTS.md](AGENTS.md). The [verification record](docs/quality/verification.md) lists what actually ran.

## Shared build and generation

Install rustup, a host C linker, Bash, rsync and Python 3.9 or newer with pip on macOS or Linux. The first build needs network access for the Rust toolchain, locked Cargo dependencies and the hash-pinned Python schema validator. The generator caches its wheel under `build/tooling/`.

```sh
cargo build --locked --workspace
cargo test --locked --workspace
scripts/generate-bindings.sh
scripts/generate-design-tokens.sh
scripts/test.sh
```

The first generator reads UniFFI metadata from the host library. The second validates the five token groups, public configuration and locale catalogs, then writes native theme definitions and string resources. Source snapshots belong in version control. Use either generator with `--check` for a read-only comparison of generated sources. The [design system guide](design-system/README.md) covers changes to canonical tokens and the [shared resource rules](docs/rules/shared-resources-rules.md) cover configuration, locales and assets.

## iOS

Use macOS with Xcode and the iOS SDK. The project deploys to iOS 17 or newer and supports iPhone and iPad. Select the full Xcode developer directory. The project builds the Rust archive for the selected architecture in a build phase. On first use, rustup provisions its target standard library. The simulator uses `aarch64-apple-ios-sim` on Apple Silicon or `x86_64-apple-ios` on Intel. A physical device uses `aarch64-apple-ios`.

```sh
scripts/build-ios.sh simulator
scripts/build-ios.sh device
xcrun simctl list devices available
scripts/build-ios.sh test "$SIMULATOR_UDID"
```

Set `SIMULATOR_UDID` to an available iPhone or iPad simulator ID before running the test command. For interactive use, open `apps/ios/MobileFoundation.xcodeproj`, select the **MobileFoundation** scheme and run. The project uses Swift 6 language mode with the selected Swift compiler. Simulator output is under `build/ios/Build/Products/Debug-iphonesimulator/`. Device mode verifies a Release link with signing disabled. To run on hardware, configure your development team and signing in Xcode.

## Android

Use the checked-in Gradle wrapper with JDK 17 or a compatible Android Studio JBR. Install the SDK command-line tools, set `ANDROID_HOME` or configure the SDK in Android Studio, and make `sdkmanager` and `adb` available. On macOS the build script recognizes the standard Android Studio and SDK locations.

```sh
sdkmanager 'platforms;android-36' 'build-tools;36.0.0' 'ndk;28.2.13676358'
rustup target add aarch64-linux-android x86_64-linux-android
scripts/build-android.sh
scripts/build-android.sh :app:assembleDebugAndroidTest
```

The Gradle build cross-compiles Rust with the pinned NDK and packages `arm64-v8a` and `x86_64` in the APK. Open `apps/android/` in Android Studio or use a connected API 24+ device or emulator matching one of those ABIs.

```sh
scripts/build-android.sh :app:installDebug
APP_ID=$(sed -n 's/^applicationId=//p' apps/android/identity.properties)
adb shell am start -n "$APP_ID/foundation.mobile.MainActivity"
scripts/build-android.sh :app:connectedDebugAndroidTest
```

The debug package is `apps/android/app/build/outputs/apk/debug/app-debug.apk`. The instrumentation suite exercises the native binding and Compose UI in the active appearance. To verify both palettes, run with the emulator in each system mode. CI automates that sequence.

## Start a project from this foundation

A product is a clone of this repository that keeps the foundation as a second remote. One command gives the clone its own display name, application ID and version. Every other name stays as the foundation wrote it, including the Xcode project, the crates, the Kotlin packages and the generated types. That is what lets a later foundation release arrive by an ordinary merge.

```sh
git clone --branch foundation-vX.Y.Z <foundation URL> acme-notes
cd acme-notes
git switch -c main
git remote rename origin foundation
scripts/init-project.sh --name "Acme Notes" --app-id com.acme.notes
git remote add origin <product repository URL>
```

Cloning a tag leaves no branch checked out, which is why the branch is created first. The command needs a clean working tree. It writes the name, the ID, version `0.1.0` and build `1` into `apps/ios/Config/Identity.xcconfig` and `apps/android/identity.properties`. It puts the product name and an origin line at the top of this README, replaces the [verification record](docs/quality/verification.md) with an empty one and removes `graphify-out/`. It renames nothing and changes no git state. Use `--ios-bundle-id`, `--android-app-id` or `--version` to override a single value. A bad input, a tree with uncommitted files or a checkout that is already derived is refused with one line and exit code `2`, and nothing is written.

Then finish the start by hand:

1. Rebuild the knowledge graph. The usual way is `/graphify .`.
2. Mark the inherited scope rows `existing`. The usual way is `/scope`.
3. Commit.
4. Run `scripts/test.sh` and both native builds.
5. Push with `git push -u origin main`.
6. Record the first local and hosted results in the verification record.

`scripts/init-project.sh --check` prints `foundation` or `derived`. When a checkout is in between, it exits `1` and names each mismatch. `scripts/test.sh` runs it on every change. To change the name, ID or version later, edit the two identity files. If the command stops part way, `git restore .` returns the checkout to the foundation state.

### Who owns which path

| Paths | Owner | On a merge from the foundation |
| --- | --- | --- |
| `apps/ios/Config/Identity.xcconfig`, `apps/android/identity.properties`, `docs/scope/`, `docs/specs/`, `docs/quality/verification.md`, `graphify-out/`, the README title and origin line, and everything the product adds | The product | Keep the product's side |
| `scripts/`, `tooling/`, `.github/workflows/foundation.yml`, `design-system/schemas/`, `shared/specifications/`, the toolchain pins, the Xcode project file and the Gradle build files | The foundation | Take the foundation's side. A fix to these paths is made in the foundation and arrives by merge |
| The rule documents, `AGENTS.md`, the rest of the README, the crates, the app sources, token values and catalogs | Shared | Merge by hand |

### Take a later foundation release

```sh
git fetch foundation --tags
git merge foundation-vX.Y.Z
```

Every such merge reports conflicts on the paths the product owns, because the foundation changes its own graph, scope and verification record in most commits. Keep the product's side there. Use `git checkout --ours -- <path>` for a file both sides changed and `git rm <path>` for a file only the foundation has under `docs/scope/` or `docs/specs/`. Then rebuild the graph and run every check. The origin line is not changed. It records where the product started, and `git log --merges` shows each release taken since. These merge steps have not been exercised yet. The first release merged into a product will prove them.

### Release the foundation

This part applies to the foundation repository only. Run the workflow by hand with `derived` set. Both native jobs then run the command on the runner checkout and build and test both apps under a sample identity. When all three jobs pass, create an annotated tag `foundation-vMAJOR.MINOR.PATCH` on `main` and push it. A product never creates a tag that starts with `foundation-v`.

## Toolchain

| Component | Selection |
| --- | --- |
| Rust and UniFFI | Rust 1.100.0 with rustfmt and Clippy. UniFFI runtime and host generator 0.31.2. Exact toolchain, Cargo manifest and lockfile live at the repository root. |
| Apple | Local verification uses Xcode 27.1 and Apple Swift 6.4. CI selects Xcode 26.5 and the iOS 26.5 simulator on the macOS 26 runner. |
| Android | AGP 9.1.0, embedded Kotlin 2.2.10, matching Compose compiler, Compose BOM 2025.08.01, Gradle 9.3.1 and JNA 5.18.1. Compile/target API 36, minimum API 24 and NDK r28c. |

Compatibility references include the [UniFFI release and feature list](https://docs.rs/crate/uniffi/0.31.2), [Apple Xcode release notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-26_5-release-notes), [GitHub macOS runner inventory](https://github.com/actions/runner-images/blob/main/images/macos/macos-26-arm64-Readme.md), [Android Gradle plugin compatibility table](https://developer.android.com/build/releases/agp-9-1-0-release-notes) and [JNA release notes](https://github.com/java-native-access/jna/blob/5.18.1/CHANGES.md).
