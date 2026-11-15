# 0003. A new project from the foundation: product identity in two files, one init command, updates by merge

**Date**: 2026-11-15
**Status**: Accepted

## Summary

This spec decides how the foundation becomes a new product. You clone the foundation, keep it as a second git remote (a named link to another repository), and run one command that gives the copy its own display name, application ID and version. Every other name stays as the foundation wrote it, so later foundation releases arrive by an ordinary merge. The command also empties the inherited verification record and removes the inherited knowledge graph, and the shared checks prove on every push that the command still works.

## Requirements

**User stories**:

- As the maintainer, I want one command that turns a clone of the foundation into a named product, so that I do not hunt for names by hand.
- As the maintainer of several products, I want foundation releases to arrive by merge, so that a fix is written once.
- As a contributor to a product, I want the verification record to list only what ran in this repository, so that I can trust it.
- As the maintainer of the foundation, I want every push to prove the command still works, so that it has not rotted when the next product starts.

**Acceptance criteria** (the contract, each criterion is IDed and independently checkable):

- **AC-1**: In the foundation, both apps carry the same default identity: application ID `dev.foundation.mobile`, display name `Mobile Foundation`, version `0.1.0`, build `1`. iOS reads all four values from `apps/ios/Config/Identity.xcconfig`. Android reads all four from `apps/android/identity.properties`. No other tracked file under `apps/` states the application ID, the display name or the app version, and the iOS UI test bundle ID is derived from the app ID.
- **AC-2**: With the default identity, `scripts/test.sh` passes, both apps build, and the greeting tests pass in both appearances on both platforms.
- **AC-3**: On a clean foundation checkout, `scripts/init-project.sh --name "Acme Notes" --app-id com.acme.notes` writes that name and ID, version `0.1.0` and build `1` into both identity files. `--ios-bundle-id`, `--android-app-id` and `--version` override single values.
- **AC-4**: After that command, `git status --porcelain` lists changes in exactly these paths: the two identity files, `README.md`, `docs/quality/verification.md` and the removed `graphify-out/` files. No crate, package, type, target, scheme or file is renamed.
- **AC-5**: After that command, `docs/quality/verification.md` is the empty record given in this spec. It names the product, the foundation URL and the foundation revision, lists every target as unverified, and holds no link to a hosted run.
- **AC-6**: After that command, `README.md` has the product name as its title on line 1, and the origin line as line 3 with one blank line after it. The origin line names the foundation URL, the revision and the date.
- **AC-7**: The command refuses, changes nothing and exits `2` with a one line reason in each of these cases: a name, ID, version, URL, ref or date that breaks its rule; a resulting application ID equal to the foundation default; a working tree with uncommitted or untracked files; a checkout that is already derived or is mixed; a run outside git without `--foundation-url` and `--foundation-ref`; no usable foundation URL.
- **AC-8**: `scripts/init-project.sh --check` prints `foundation` or `derived` and exits `0` when the checkout is fully in one of those two states. In any mixed state it exits `1` and names each mismatch. `scripts/test.sh` runs it.
- **AC-9**: `scripts/init-project.sh --test` runs the unit tests. One of them copies the files git lists to a temporary folder, runs the copy's own command there with sample values, requires the copy's `--check` to print `derived` and the copy's `check-architecture.py` to pass, and removes the copy. `scripts/test.sh` runs `--test`, so the `foundation` CI job proves the command on every push.
- **AC-10**: The workflow accepts a manual run with the input `derived`. With that input set, the `ios` and `android` jobs run the command on the runner checkout first, then build and test both apps under the sample identity. In every run, each native job compares the application ID and the display name of the built app with the identity file and fails on a difference. One run with `derived` set has passed and is named in the verification record.
- **AC-11**: `README.md` has a section that gives the full path: clone at a tag, create a branch, rename the remote, run the command, point `origin` at the product repository, rebuild the graph, mark inherited scope rows `existing`, make the first commit, record the first local and hosted results. It also says which paths a product owns, which the foundation owns, how to take a later foundation release, and how the foundation is tagged.
- **AC-12**: `docs/scope/index.md` no longer links a hosted run. The ownership matrix, the repository structure, the quality checks table and `shared/config/README.md` name the identity files or the command, with the texts given in the Build plan.

## Decision

**Chosen option**: Option 1: Clone and merge, product identity in two files, one init command.

A product is a clone of the foundation that changes only its display name, application ID and version through `scripts/init-project.sh`, keeps every other name, starts with an empty verification record, and takes later foundation releases by merging a `foundation-v` tag.

## Feature design

**Data model sketch**:

There is no database. The model is two identity files, one origin line and two repository states.

| Value | iOS (`apps/ios/Config/Identity.xcconfig`) | Android (`apps/android/identity.properties`) | Default | Rule |
| --- | --- | --- | --- | --- |
| Application ID | `APP_BUNDLE_IDENTIFIER` | `applicationId` | `dev.foundation.mobile` | `^[a-z][a-z0-9]*(\.[a-z][a-z0-9]*)+$` for `--app-id` |
| Display name | `APP_DISPLAY_NAME` | `displayName` | `Mobile Foundation` | See the name rule below |
| Version | `MARKETING_VERSION` | `versionName` | `0.1.0` | `^\d+\.\d+\.\d+$` |
| Build | `CURRENT_PROJECT_VERSION` | `versionCode` | `1` | `^[1-9]\d*$` |

Rules for the other inputs. Every pattern in this spec is compiled with `re.ASCII`, so `\d` means the digits 0 to 9 only.

| Input | Rule |
| --- | --- |
| `--ios-bundle-id` | `^[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)+$` |
| `--android-app-id` | `^[A-Za-z][A-Za-z0-9_]*(\.[A-Za-z][A-Za-z0-9_]*)+$` |
| Display name | 1 to 30 code points. Each one is a letter (`str.isalpha()`), a digit 0 to 9, a space, `.`, `-` or the apostrophe U+0027. No space at the start or the end, and no two spaces in a row |
| Foundation URL, after it is normalized | `^https://[A-Za-z0-9.-]+(/[A-Za-z0-9._~-]+)+$` |
| Foundation ref | `^[A-Za-z0-9._/-]{1,100}$` |
| Date | `^\d{4}-\d{2}-\d{2}$`, and `date.fromisoformat` accepts it |

File contents in the foundation, in full:

```text
apps/ios/Config/Identity.xcconfig
APP_BUNDLE_IDENTIFIER = dev.foundation.mobile
APP_DISPLAY_NAME = Mobile Foundation
MARKETING_VERSION = 0.1.0
CURRENT_PROJECT_VERSION = 1

apps/android/identity.properties
applicationId=dev.foundation.mobile
displayName=Mobile Foundation
versionName=0.1.0
versionCode=1
```

Each file holds exactly these four lines, in this order, and ends with one newline. The xcconfig form is `KEY = value`. The properties form is `key=value`. Neither file carries a comment. Both are UTF-8. `--check` reports a missing file, a missing key, an extra line or a comment as a mismatch that names the file and the key.

How each build reads its file:

- **iOS.** `Project.xcconfig` starts with `#include "Identity.xcconfig"` and loses its own `CURRENT_PROJECT_VERSION` and `MARKETING_VERSION` lines. `App.xcconfig` sets `PRODUCT_BUNDLE_IDENTIFIER = $(APP_BUNDLE_IDENTIFIER)` and `INFOPLIST_KEY_CFBundleDisplayName = $(APP_DISPLAY_NAME)`. The UI test target has no base config file and inherits project level settings, so its two lines in `project.pbxproj` become `PRODUCT_BUNDLE_IDENTIFIER = "$(APP_BUNDLE_IDENTIFIER).uitests";`. So that the file shows in Xcode, add one file reference to `project.pbxproj`: `FA0000000000000000000007 /* Identity.xcconfig */` with `lastKnownFileType = text.xcconfig; name = Identity.xcconfig; path = Config/Identity.xcconfig; sourceTree = "<group>";`, listed in the children of the main group `AB0000000000000000000005` after `App.xcconfig`. Add no build file, and do not make it a base config of any target.
- **Android.** `app/build.gradle.kts` loads `rootProject.file("identity.properties")` with a UTF-8 reader and takes `applicationId`, `versionName` and `versionCode` from it. `namespace` stays `foundation.mobile` (it names the code package, not the product). The display name reaches the manifest as a manifest placeholder (a build time value the manifest refers to): `manifestPlaceholders["appLabel"]` and `android:label="${appLabel}"`. The `app_name` string leaves `res/values/app.xml`. A missing key stops the build with a message that names the file and the key.

Names the foundation keeps, which no product changes: the Xcode project, targets and scheme (`MobileFoundation`, `MobileFoundationUITests`), `rootProject.name`, the crates (`foundation-core`, `mobile-ffi`), the UniFFI namespace `mobile_ffi`, the Kotlin packages (`foundation.mobile`, `foundation.designsystem`, `foundation.presentation`), the generated types (`FoundationTokens`, `FoundationTheme`), `foundation_strings.xml`, `shared/config/foundation.json`, the workflow file and the test variable `TEST_RUNNER_FOUNDATION_APPEARANCE`.

The origin line. The command replaces line 1 of `README.md` with the title and inserts two new lines after line 2: the origin line as line 3 and a blank line as line 4. The old line 3 (the opening paragraph) becomes line 5.

```markdown
Started from the [mobile foundation](<foundation URL>) at `<ref>` on <YYYY-MM-DD>.
```

`--check` treats the origin line as present only when line 3 matches the pattern below and line 4 is blank. A line that starts with `Started from the [mobile foundation]` anywhere else, or a line 3 that starts that way and does not match, is a mismatch.

```text
^Started from the \[mobile foundation\]\((https://[^\s()]+)\) at `([^`\s]+)` on (\d{4}-\d{2}-\d{2})\.$
```

The empty verification record. The command keeps this text as `tooling/derive/verification-record.md`, with one final newline, and fills the placeholders `{name}`, `{foundation_url}`, `{ref}` and `{date}` with `str.replace`:

```markdown
# {name} verification · {date}

This record lists what ran, where it ran and what has not run yet. Nothing has run in this repository yet. This project started from the [mobile foundation]({foundation_url}) at `{ref}`. The foundation's own results live in that repository. They are not results for this project.

## Local checks

None yet. Add a row for each check after it runs here.

## Hosted run

None yet. Record the first hosted run here with its link, its revision and each job outcome.

## Still unverified

This is the one list of targets that have not run. A target leaves this list when a local or hosted result above covers it.

- The shared checks in `scripts/test.sh`.
- The iOS simulator build, the unsigned device link and the greeting test in light and dark appearance.
- The Android debug build and the instrumentation tests in light and dark appearance.
- All three hosted jobs.
- Physical devices on either platform.
- Signed distribution.
- The minimum supported OS versions.
- An Android runtime with 16 KiB pages.
- An x86_64 iOS simulator runtime.
```

**State transitions**:

```text
foundation  --init succeeds-->  derived
foundation  --init refused-->   foundation   (nothing written)
derived     --init-->           refused      (exit 2, nothing written)
mixed       --init-->           refused      (exit 2, nothing written)
mixed       --git restore .-->  foundation   (the way back after a failed write)
```

| State | Application IDs in the two identity files | Origin line in `README.md` |
| --- | --- | --- |
| `foundation` | Both are the default | Absent |
| `derived` | Neither is the default | Present and valid |
| mixed | Anything else | Anything else |

In both good states the check also requires both identity files to have the exact form above and every value to match its rule.

**API surface**:

The surface is one command, `scripts/init-project.sh`. It resolves the repository from its own location, as the other scripts do, and passes its arguments to `tooling/derive/init_project.py`.

| Form | Key inputs | What it does | Exit |
| --- | --- | --- | --- |
| `--name N --app-id ID` | `--name` (required), `--app-id` (required), `--ios-bundle-id`, `--android-app-id`, `--version`, `--foundation-url`, `--foundation-ref`, `--date` (all optional) | Checks every input and the state first. Then writes both identity files, the README title and origin line and the empty verification record, and removes `graphify-out/`. Prints each path it changed. | `0` done · `2` refused, nothing written |
| `--check` | None | Prints `foundation` or `derived`. In a mixed state prints one line per mismatch. | `0` one clean state · `1` mixed |
| `--test` | None | Runs the unit tests under `tooling/derive/`, including the derivation case in AC-9. | `0` passed · `1` failed |

Details the build must honor:

- **In git or not.** The checkout counts as in git only when `git -C <root> rev-parse --show-toplevel` equals the resolved repository root. In git, any output from `git status --porcelain` (tracked or untracked, ignored files left out) makes the tree dirty. Outside git the dirty test is skipped, and `--foundation-url` and `--foundation-ref` are both required.
- **Refusals.** Each one prints a single line that names the input and the rule, and exits `2`. Examples: `--app-id: expected reverse DNS in lowercase, such as com.acme.notes`, `--app-id: must differ from the foundation default dev.foundation.mobile` (also used when an override equals the default), `checkout is mixed; run scripts/init-project.sh --check`, `no usable foundation URL; pass --foundation-url`.
- **Writing.** Nothing is written until every check has passed. All new contents are built in memory. Each file is then written through a temporary file in the same folder and moved into place with `os.replace`, in this order: the two identity files, `README.md`, the verification record. `graphify-out/` is removed last. If a step fails, the command prints the paths it already changed and `git restore .` as the way back.
- **The derivation test.** It copies exactly the files that `git ls-files -z --cached --others --exclude-standard` lists and that exist, using a Python file copy, into a temporary folder. It then runs `<copy>/scripts/init-project.sh` with the sample values, `<copy>/scripts/init-project.sh --check` and `python3 <copy>/tooling/validation/check-architecture.py`, each with the copy as the working directory, and removes the copy in a `finally` block. It never runs the original script against the copy. It is skipped, with the reason printed, when the checkout is not in git or is already `derived`.
- **Sample values.** `--name "Zoë's Proof" --app-id dev.example.derived`, and in the derivation test also `--foundation-url https://example.invalid/foundation --foundation-ref foundation-v0.0.0 --date 2026-01-01`. The name carries a letter outside ASCII and an apostrophe on purpose. If the Android build rejects or alters the apostrophe, remove the apostrophe from the name rule in the same change. Do not add escaping.
- **Unit tests and git.** Tests that need a repository create one in a temporary folder and run git with `GIT_CONFIG_GLOBAL=/dev/null`, `GIT_CONFIG_NOSYSTEM=1`, the four author and committer name and email variables set, and `-c commit.gpgsign=false`. No test touches the real checkout.

**Value sourcing**:

| Action | Value produced / displayed | Source |
| --- | --- | --- |
| init | Display name | `--name` |
| init | iOS application ID | `--ios-bundle-id`, else `--app-id` |
| init | Android application ID | `--android-app-id`, else `--app-id` |
| init | Version | `--version`, else `0.1.0` |
| init | Build | Always `1` |
| init | Foundation URL | `--foundation-url`, else `git remote get-url foundation`, else `git remote get-url origin`. Accepted forms: `https://`, `http://` (written as `https://`), `ssh://` (user and port dropped) and `user@host:path`. A user name or token, a trailing `.git` and a trailing `/` are removed. Any other form, or no remote, is a refusal |
| init | Foundation ref | `--foundation-ref`, else the `foundation-v*` tag that points exactly at `HEAD` (the highest version when several do), else the full `HEAD` commit ID |
| init | Date | `--date`, else today's local date |
| init | README title | `--name` |
| init | Empty verification record | `tooling/derive/verification-record.md`, filled with the name, URL, ref and date above |
| check | Default application ID | A constant in `tooling/derive/init_project.py`, `dev.foundation.mobile` |
| check | Origin line | Line 3 of `README.md`, matched with the pattern above |
| derivation test | Name, ID, URL, ref and date | The sample values listed under API surface |
| Android build | `applicationId`, `versionName`, `versionCode`, app label | `apps/android/identity.properties` |
| iOS build | Bundle ID, display name, version, build, UI test bundle ID | `apps/ios/Config/Identity.xcconfig` |
| CI identity comparison | Expected ID and display name | The identity file of that platform, read by the workflow step |
| CI identity comparison | Actual ID and display name | iOS: `CFBundleIdentifier` and `CFBundleDisplayName` in `build/ios/Build/Products/Debug-iphonesimulator/MobileFoundation.app/Info.plist`, read with `/usr/libexec/PlistBuddy`. Android: `package: name` and `application-label` from `aapt2 dump badging` on `apps/android/app/build/outputs/apk/debug/app-debug.apk`, with `aapt2` taken from `build-tools/36.0.0` in the SDK |

**Key invariants**:

- A checkout is `foundation` or `derived`, never in between. `--check` in `scripts/test.sh` enforces it.
- An identity value is stated in exactly one file per platform. The CI identity comparison catches a value written anywhere else once the identity differs from the default, which the manual run with `derived` set guarantees. Between those runs it rests on review.
- The command renames nothing. The list of paths in AC-4 is the whole write set.
- The command never runs on a derived or mixed checkout, so it cannot erase a product's verification record.
- The command never changes git state. It reads with `git status`, `git remote get-url`, `git describe`, `git tag` and `git rev-parse` only. Branches, remotes, commits and tags are the maintainer's steps.
- Foundation tags match `foundation-v*`. A product never creates a tag with that prefix.

**Security model**:

- The command reads and writes only inside the checkout. The derivation test adds one temporary folder that it removes.
- It uses no network and no secret.
- A remote URL can carry a user name or a token. The command removes that part before the URL is written into `README.md` or the verification record, and the URL rule rejects anything that is left over.
- Input is checked against the rules above before any write, so a name cannot inject a build setting (`$(`), a comment (`//`) or a second line into an identity file, and a URL or ref cannot break the Markdown link.
- Signing teams, keystores and store credentials are not identity in this spec. They stay out of the repository (R12).

**Configuration required**: none. No environment variable and no credential.

**Critical test scenarios** (each maps to an acceptance criterion in ## Requirements):

- Happy path: on a clean foundation tree, the command with a name and an ID writes both identity files, the README title, origin line and blank line, and the empty record, and `--check` then prints `derived`, verifies **AC-3**, **AC-5**, **AC-6**, **AC-8**
- Write set: after the command, the changed paths are exactly the five in AC-4, verifies **AC-4**
- Overrides: `--ios-bundle-id` and `--android-app-id` reach only their own platform file, verifies **AC-3**
- Refusals: an ID with an upper case letter, an ID equal to the default, a name with `$(`, a name with a leading space, a date of `2026-13-40`, a dirty tree, an untracked file, a derived checkout, a mixed checkout, and a tree outside git without the two foundation values each exit `2` and leave every file byte for byte unchanged, verifies **AC-7**
- Remote forms: `https://user:token@host/owner/repo.git`, `ssh://git@host:22/owner/repo.git` and `git@host:owner/repo.git` are each written as `https://host/owner/repo`, and a local path is refused, verifies **AC-6**, **AC-7**
- Mixed state: one identity file changed by hand, an extra line in an identity file, and an origin line on line 5 each make `--check` exit `1` and name the mismatch, verifies **AC-8**
- Derivation on a copy: the copy ends `derived` and passes `check-architecture.py`, and the real checkout is unchanged afterwards, verifies **AC-9**
- Native builds: both apps build, pass the greeting tests and pass the identity comparison with the default identity, and again under the sample identity in a manual hosted run, verifies **AC-1**, **AC-2**, **AC-10**

## Build plan

Ordered as one thin thread first (the identity value travels from its file through each build into the running app), then the command along that thread, then the proofs and the written path.

1. Move the iOS identity into `apps/ios/Config/Identity.xcconfig` and change `Project.xcconfig`, `App.xcconfig` and `project.pbxproj` as described. Build for the simulator and run the greeting test, satisfies **AC-1**, **AC-2**
2. Move the Android identity into `apps/android/identity.properties`, load it in `app/build.gradle.kts`, switch the manifest label to the placeholder and remove `app_name`. Build, install and run the instrumentation tests, satisfies **AC-1**, **AC-2**
3. Change the Android run command in `README.md` to read the ID from the identity file: `APP_ID=$(sed -n 's/^applicationId=//p' apps/android/identity.properties)` then `adb shell am start -n "$APP_ID/foundation.mobile.MainActivity"`, satisfies **AC-1**
4. Add `scripts/init-project.sh` and `tooling/derive/init_project.py` with the first form (input checks, both identity files) and `--check`, satisfies **AC-3**, **AC-8**
5. Add the README title and origin line, `tooling/derive/verification-record.md` and the record reset, the removal of `graphify-out/`, the safe write order and every refusal, satisfies **AC-4**, **AC-5**, **AC-6**, **AC-7**
6. Add `tooling/derive/test_init_project.py` covering the test scenarios above, including the derivation case, and the `--test` form, satisfies **AC-3** to **AC-9**
7. In `scripts/test.sh`, add `scripts/init-project.sh --check` and then `scripts/init-project.sh --test` directly after the `check-architecture.py` line, satisfies **AC-8**, **AC-9**
8. In the workflow, add the boolean input `derived` (default `false`) under `workflow_dispatch`. In the `ios` and `android` jobs add a step before the first build, with `if: ${{ inputs.derived }}`, that runs the command with the sample name and ID when `scripts/init-project.sh --check` prints `foundation`, and otherwise prints that the proof is for the foundation repository only. In both jobs add a step after the build, with no condition, that makes the identity comparison described under Value sourcing and fails on a difference, satisfies **AC-10**
9. Write the README section `Start a project from this foundation` with the content below, satisfies **AC-11**
10. Update the documents with the texts below, satisfies **AC-12**
11. Run the workflow once by hand with `derived` set. Record that run, and the local results for steps 1, 2 and 7, in `docs/quality/verification.md`, satisfies **AC-2**, **AC-10**

Texts for step 10:

- `docs/scope/index.md`: replace the sentence that starts `All three hosted jobs passed` and its link with `The [verification record](../quality/verification.md) lists what ran, local and hosted.`
- `docs/architecture/ownership-matrix.md`: add the row below after the two app rows, and change the first cell of the tooling row to `Resource generation, schema checks, compliance and project derivation`.

  ```markdown
  | Product identity: display name, application IDs and app version | `apps/ios/Config/Identity.xcconfig` and `apps/android/identity.properties` | The Xcode and Gradle builds, `scripts/init-project.sh` |
  ```

- `docs/architecture/repository-structure.md`: append ``Product identity lives in `Config/Identity.xcconfig`.`` to the `apps/ios/` row and ``Product identity lives in `identity.properties`.`` to the `apps/android/` row, and change the `tooling/` row to `Build-host generation, validation and project derivation code.`
- `docs/quality/architecture-compliance.md`: add this row after the Cargo dependencies row.

  ```markdown
  | Project identity state | `scripts/init-project.sh --check` reads both identity files and the README origin line and fails when the checkout is neither the foundation nor fully derived. `--test` runs the command on a temporary copy and exercises every refusal. Each native CI job compares the built app's ID and display name with its identity file. |
  ```

- `shared/config/README.md`: append ``Product identity lives in `apps/ios/Config/Identity.xcconfig` and `apps/android/identity.properties`.`` to the Native build settings row.
- `docs/specs/_root/0001-ownership-development-rules.md`: in rule R1 change `The matrix lists ten` to `The matrix lists eleven`. Nothing else in that spec changes.

Content of the README section (step 9). Write it in the README's own voice, with these parts in this order:

- **Start a product.**
  ```sh
  git clone --branch foundation-vX.Y.Z <foundation URL> acme-notes
  cd acme-notes
  git switch -c main
  git remote rename origin foundation
  scripts/init-project.sh --name "Acme Notes" --app-id com.acme.notes
  git remote add origin <product repository URL>
  ```
  Then: rebuild the knowledge graph (usual way: `/graphify .`), mark the inherited scope rows `existing` (usual way: `/scope`), commit, run `scripts/test.sh` and both native builds, push with `git push -u origin main`, and record the first local and hosted results in the verification record. Say that cloning a tag leaves no branch checked out, which is why the branch is created first.
- **Who owns which path after that.**

  | Paths | Owner | On a merge from the foundation |
  | --- | --- | --- |
  | `apps/ios/Config/Identity.xcconfig`, `apps/android/identity.properties`, `docs/scope/`, `docs/specs/`, `docs/quality/verification.md`, `graphify-out/`, the README title and origin line, and everything the product adds | The product | Keep the product's side |
  | `scripts/`, `tooling/`, `.github/workflows/foundation.yml`, `design-system/schemas/`, `shared/specifications/`, the toolchain pins, the Xcode project file and the Gradle build files | The foundation | Take the foundation's side. A fix to these paths is made in the foundation and arrives by merge |
  | The rule documents, `AGENTS.md`, the rest of the README, the crates, the app sources, token values and catalogs | Shared | Merge by hand |

- **Take a later foundation release.** `git fetch foundation --tags`, then `git merge foundation-vX.Y.Z`. Say plainly that every such merge reports conflicts on the product owned paths, because the foundation changes its own graph, scope and verification record in most commits. Keep the product's side there (`git checkout --ours -- <path>` for a file both sides changed, `git rm <path>` for a file only the foundation has under `docs/scope/` or `docs/specs/`), then rebuild the graph and run every check. The origin line is not changed.
- **Release the foundation** (foundation repository only). Run the workflow by hand with `derived` set. When all three jobs pass, create an annotated tag `foundation-vMAJOR.MINOR.PATCH` on `main` and push it. A product never creates a tag that starts with `foundation-v`.

## Consequences

**Positive**:

- Two products built from the foundation install side by side, and each ships under its own name and ID from the first commit.
- A foundation fix reaches every product by one merge.
- A checkout that is half derived fails `scripts/test.sh`, in the foundation and in a product alike.
- A product's verification record starts empty and lists only what ran in that repository.
- The identity mismatch between the two apps is gone, and each value has one home per platform.
- Every native run now proves that the built app carries the identity the file states.

**Negative / tradeoffs**:

- Foundation names stay in product code. The Xcode project, the scheme and the app bundle are named `MobileFoundation`, and types and packages keep the `Foundation` prefix. Users see only the display name.
- A product carries the foundation's commit history and its `foundation-v` tags.
- A command and its unit tests are kept for a job that runs once per product.
- The Linux proof does not build anything. A change that breaks a derived native build can sit on `main` until the next manual run with `derived` set.
- Three steps rest on the person: rebuilding the graph, marking inherited rows `existing`, and recording the first results. `--check` does not see them.
- Every merge of a foundation release reports conflicts on the paths a product owns. They are resolved the same way each time, by hand, until the sync command exists.
- Later foundation scope rows and specs do not flow into products. The reason behind a new foundation rule is read in the foundation repository.
- Display names are limited to letters, digits, space, period, hyphen and apostrophe until a product needs more.
- The Android application ID changes from `foundation.mobile` to `dev.foundation.mobile`. A device that has the old debug build keeps it as a separate app until it is removed.

**Neutral**:

- The ownership matrix grows to eleven rows, and spec `0001` is amended in the same change, as its premise note asks.
- The iOS version moves from `1.0` to `0.1.0` to match Android. Whether the two must always match is a release decision, not this one.
- The Cargo workspace version is not an app version and is left alone.
- `/develop` moves this spec to `In Progress` and `Accepted` with scope row `009`. Creating the first tag, `foundation-v0.1.0`, is the maintainer's step after that.

## Follow-up

- [ ] Build the command that takes a foundation release (fetch, merge, apply the ownership table) when the first release is merged into a product. Until then the README steps are the path, and they are unproven until that first merge.
- [ ] Write how a change proven in a product returns to the foundation (needed by every product, already exercised by a real caller, free of product nouns, touches foundation owned paths only) once a product closes a Deferred item.
- [ ] Record where `/graphify` and `/scope` come from, with a way to do each step by hand. The written path depends on both. Spec `0002` already lists this for the second contributor.
- [ ] Decide where dependency update bots run. A bot in every product changes foundation owned files and will conflict with merges. Running it in the foundation only is the likely answer.
- [ ] Two foundation schemas still require sample names (`greeting_recipient` in the localization schema, the `greeting` role in the token schema). A product that replaces the greeting hits both. This deserves its own scope row.
- [ ] Decide in the release path spec whether the iOS and Android versions must match, and add that test to `--check` if they must.
- [ ] Allow a localized display name when a product needs one. It would move from the identity files to the catalogs.
- [ ] Revisit keeping `MobileFoundation` as the Xcode project and scheme name if it confuses contributors to a product in practice.
