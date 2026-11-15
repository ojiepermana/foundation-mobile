# Verify: A new project from the foundation · spec 0003 · updated 2026-11-15
_Steps derived from spec 0003 acceptance criteria. `/check verify` runs these; `/test` locks the durable ones._

Run the derivation steps in a scratch clone, never in your working checkout. A clone made with `git clone . /tmp/derive-proof` works, and its `origin` then is a local path, so pass `--foundation-url` there unless a step says otherwise.

## UI / manual

- [x] Install both debug apps on a simulator and an emulator → each home screen shows the label `Mobile Foundation`        → AC-1
- [ ] Open `apps/ios/MobileFoundation.xcodeproj` in Xcode → `Identity.xcconfig` shows in the file list next to `App.xcconfig`, and no target uses it as a base config        → AC-1
- [x] In a scratch clone derived as `Acme Notes` with `com.acme.notes`, install both debug apps beside the foundation apps → both pairs stay installed side by side, and the new pair shows the label `Acme Notes`        → AC-3
- [ ] Open the GitHub Actions page of the foundation repository → `Run workflow` offers a `derived` checkbox that is off by default        → AC-10
- [x] Read the README section `Start a project from this foundation` → it gives the clone at a tag, the branch, the remote rename, the command, the new `origin`, the graph rebuild, the `existing` scope rows, the first commit and the first results, then the ownership table, the later release merge and the foundation tag rule        → AC-11

## Commands

- [x] `cat apps/ios/Config/Identity.xcconfig apps/android/identity.properties` → four lines each, with `dev.foundation.mobile`, `Mobile Foundation`, `0.1.0` and `1`, and no comment        → AC-1
- [x] `git grep -n -E "dev\.foundation\.mobile|Mobile Foundation|MARKETING_VERSION|CURRENT_PROJECT_VERSION|app_name" -- apps ':!apps/ios/Config/Identity.xcconfig' ':!apps/android/identity.properties'` → no match        → AC-1
- [x] `grep -n uitests apps/ios/MobileFoundation.xcodeproj/project.pbxproj` → two lines, both `"$(APP_BUNDLE_IDENTIFIER).uitests"`        → AC-1
- [x] `scripts/test.sh` → exit `0`, and the output shows `foundation` and the unit tests of the command passing        → AC-2, AC-8, AC-9
- [x] `scripts/build-ios.sh simulator` then `scripts/build-ios.sh device` → both succeed        → AC-2
- [x] `scripts/build-ios.sh test "$SIMULATOR_UDID" light` and again with `dark` → one test passes in each appearance        → AC-2
- [x] `scripts/build-android.sh :app:assembleDebug :app:assembleDebugAndroidTest`, then `:app:connectedDebugAndroidTest` with `adb shell cmd uimode night no` and again with `yes` → two tests pass in each appearance        → AC-2
- [x] In a scratch clone: `scripts/init-project.sh --name "Acme Notes" --app-id com.acme.notes --foundation-url https://example.invalid/foundation` → exit `0`, five changed paths printed, and both identity files hold `Acme Notes`, `com.acme.notes`, `0.1.0` and `1`        → AC-3
- [x] In a fresh scratch clone, add `--ios-bundle-id com.acme.notes-ios --android-app-id com.acme.notes_droid --version 2.3.4` → each ID lands only in its own platform file and both files hold `2.3.4`        → AC-3
- [x] After the first derivation: `git status --porcelain` → only ` M README.md`, ` M apps/android/identity.properties`, ` M apps/ios/Config/Identity.xcconfig`, ` M docs/quality/verification.md` and ` D graphify-out/...` lines, and no rename        → AC-4
- [x] After the first derivation: `cat docs/quality/verification.md` → the empty record of the spec, with the product name, the foundation URL and the revision, nine unverified targets and no link to a hosted run        → AC-5
- [x] After the first derivation: `sed -n '1,4p' README.md` → line 1 is `# Acme Notes`, line 2 is blank, line 3 is the origin line with the URL, the revision and the date, line 4 is blank        → AC-6
- [x] In a fresh scratch clone, try each of these and expect exit `2`, one line on stderr and an unchanged `git status --porcelain`: `--app-id com.Acme.notes`, `--app-id dev.foundation.mobile`, `--name 'Acme $(HOME)'`, `--name ' Acme'`, `--version 1.0`, `--date 2026-13-40`, `--foundation-url /srv/git/foundation`, ``--foundation-ref 'main`x'``        → AC-7
- [x] In a fresh scratch clone: `touch notes.txt` then the command → exit `2`, the reason names uncommitted or untracked files        → AC-7
- [x] Run the command a second time in the derived and committed scratch clone → exit `2`, `checkout is already derived`        → AC-7
- [x] Copy the tracked files to a folder outside git and run the command without `--foundation-url` and `--foundation-ref` → exit `2`, both flags are named as required        → AC-7
- [x] In a scratch clone whose `origin` is a local path, run the command without `--foundation-url` → exit `2`, `no usable foundation URL; pass --foundation-url`        → AC-7
- [x] `scripts/init-project.sh --check` in the foundation → prints `foundation`, exit `0`. In the derived scratch clone → prints `derived`, exit `0`        → AC-8
- [x] In a scratch clone, change only `applicationId` in `apps/android/identity.properties`, then `--check` → exit `1`, the line names that file and key. Add a fifth line to `Identity.xcconfig` → exit `1`, the line names the file and the extra line        → AC-8
- [x] `scripts/init-project.sh --test` → every test passes, and `test_derivation_on_a_copy` reports `ok`, not `skipped`. `git status --porcelain` is the same before and after        → AC-9
- [x] `gh workflow run foundation.yml -f derived=true` then `gh run watch` → all three jobs pass, the two native logs show the derive step writing `Zoë's Proof` and `dev.example.derived`, and each comparison step prints matching `Identity file` and `Built app` lines        → AC-10
- [x] Open a run that a push started → the derive step is skipped in both native jobs and the comparison step passes with `dev.foundation.mobile` and `Mobile Foundation`        → AC-10
- [x] `grep -n "derived" docs/quality/verification.md` → the record names one hosted run with `derived` set, its link and its revision        → AC-10
- [x] `grep -c "actions/runs" docs/scope/index.md` → `0`        → AC-12
- [x] `grep -n "Identity.xcconfig\|init-project" docs/architecture/ownership-matrix.md docs/architecture/repository-structure.md docs/quality/architecture-compliance.md shared/config/README.md` → each file names the identity files or the command        → AC-12

### Value sourcing

One step per row of the spec's Value sourcing table. Each one changes the source and checks that the output follows.

- [x] Display name: derive with `--name "Zoë's Proof"` → both identity files, the README title and the record title carry exactly that text        → AC-3, AC-6
- [x] iOS application ID: derive once with `--app-id` alone and once with `--ios-bundle-id` too → `APP_BUNDLE_IDENTIFIER` follows the override when it is given, and `--app-id` when it is not        → AC-3
- [x] Android application ID: the same pair of runs with `--android-app-id` → `applicationId` follows the override when it is given        → AC-3
- [x] Version: derive without `--version` → `0.1.0`. Derive with `--version 2.3.4` → `2.3.4` in both files        → AC-3
- [x] Build: derive with any version → `CURRENT_PROJECT_VERSION` and `versionCode` are `1`        → AC-3
- [x] Foundation URL: with a `foundation` remote and an `origin` remote that differ → the origin line uses the `foundation` remote. With `origin` set to `https://user:token@host/owner/repo.git`, `ssh://git@host:22/owner/repo.git` and `git@host:owner/repo.git` → each is written as `https://host/owner/repo`. With `--foundation-url` → the flag wins        → AC-6, AC-7
- [x] Foundation ref: on a commit with the tags `foundation-v0.9.0` and `foundation-v0.10.0` → the origin line names `foundation-v0.10.0`. Without a tag → the full commit ID. With `--foundation-ref` → the flag wins        → AC-6
- [x] Date: derive without `--date` → today's local date. With `--date 2026-01-01` → that date in the origin line and the record title        → AC-6
- [x] README title: after derivation line 1 of `README.md` is `# ` followed by the `--name` value        → AC-6
- [x] Empty verification record: `diff <(sed -e "s/{name}/Acme Notes/" -e "s#{foundation_url}#<the URL>#" -e "s/{ref}/<the ref>/" -e "s/{date}/<the date>/" tooling/derive/verification-record.md) docs/quality/verification.md` in the derived clone → no difference        → AC-5
- [x] Default application ID for the check: set both identity files to `dev.foundation.mobile` in a derived clone → `--check` exits `1` and says the IDs are still the foundation default        → AC-8
- [x] Origin line for the check: move the origin line from line 3 to line 5 of `README.md` → `--check` exits `1` and names line 5        → AC-8
- [x] Derivation test values: `scripts/init-project.sh --test` → the copy is derived as `Zoë's Proof`, `dev.example.derived`, `https://example.invalid/foundation`, `foundation-v0.0.0` and `2026-01-01`, and its record equals the expected text        → AC-9
- [x] Android build: change `displayName`, `applicationId`, `versionName` and `versionCode` in a scratch clone's `identity.properties`, build, then `aapt2 dump badging` on the debug APK → all four values follow the file. Remove one key → the build stops with `identity.properties: missing key <key>`        → AC-1
- [x] iOS build: change the four values in a scratch clone's `Identity.xcconfig`, build for the simulator, then read `CFBundleIdentifier`, `CFBundleDisplayName`, `CFBundleShortVersionString` and `CFBundleVersion` with `/usr/libexec/PlistBuddy` → all four follow the file, and the UI test bundle ID is the app ID plus `.uitests`        → AC-1
- [x] CI identity comparison, expected values: in a scratch clone, write `displayName=Other Name` into `identity.properties` after building and run the comparison lines of the workflow by hand → the step fails        → AC-10
- [x] CI identity comparison, actual values: in a scratch clone, set `PRODUCT_BUNDLE_IDENTIFIER = dev.wrong.id` in `App.xcconfig`, build, and run the comparison lines by hand → the step fails        → AC-10

## Acceptance-criteria coverage

- AC-1 covered by the label check, the Xcode file list, the identity file listing, the `git grep`, the `uitests` grep and the two build rows under Value sourcing
- AC-2 covered by `scripts/test.sh`, the two iOS builds, the iOS greeting test and the Android build and instrumentation tests
- AC-3 covered by the side by side install, the first derivation, the override run and the name, ID, version and build rows
- AC-4 covered by the `git status --porcelain` step after derivation
- AC-5 covered by the record listing and the template `diff`
- AC-6 covered by the first four README lines and the URL, ref, date and title rows
- AC-7 covered by the eight input refusals, the untracked file, the second run, the run outside git and the local path remote
- AC-8 covered by `--check` in both states, the two hand made mismatches and the two check rows under Value sourcing
- AC-9 covered by `--test` and the derivation test values row
- AC-10 covered by the `derived` checkbox, the manual run, the push run, the record grep and the two comparison rows
- AC-11 covered by reading the README section
- AC-12 covered by the scope index grep and the document grep
