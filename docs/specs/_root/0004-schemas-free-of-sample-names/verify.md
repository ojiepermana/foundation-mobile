# Verify: Schemas free of sample names · spec 0004 · updated 2026-11-15
_Steps derived from spec 0004 acceptance criteria. `/check verify` runs these; `/test` locks the durable ones._

Run every step that removes or breaks the sample in a scratch clone, never in your working checkout. A clone holds committed work only. Make it like this:

```sh
SCRATCH=$(mktemp -d)
git clone --branch "$(git branch --show-current)" . "$SCRATCH/f010-proof"
mkdir -p "$SCRATCH/f010-proof/build" && cp -R build/tooling "$SCRATCH/f010-proof/build/"
```

Run `git checkout -- .` in the clone after each clone step, so every step starts from the committed state. Run `git status --short` in your working checkout before the first clone step and keep the output for the last AC-6 step. Remove the clone at the end with `rm -rf "$SCRATCH"`.

## UI / manual

- [x] Launch the iOS debug app on a simulator in light and in dark appearance → the screen shows `Hello, World!` in the same large semibold style as before the rename        → AC-3, AC-4
- [x] Launch the Android debug app on an emulator in light and in dark mode → the screen shows `Hello, World!` in the same large style as before the rename        → AC-3, AC-4

## Commands

- [x] `cat shared/specifications/localization.schema.json` → equals the schema given in spec 0004, with `"minProperties": 1` and no `required` and no `properties` member        → AC-1
- [x] In the clone: `echo '{}' > shared/localization/en.json`, then `scripts/generate-design-tokens.sh --check` → exit `1`, `en.json: data must contain at least 1 properties`        → AC-1
- [x] `git grep -n -i greeting -- design-system` → no match        → AC-2
- [x] In the clone: `sed 's/"heading"/"display"/' design-system/tokens/typography.json > t.json && mv t.json design-system/tokens/typography.json`, then `scripts/generate-design-tokens.sh --check` → exit `1`, `tokens: data.typography.semantic must contain ['heading'] properties`        → AC-2
- [x] `git grep -n typographyGreeting -- ':!docs/specs' ':!docs/scope' ':!graphify-out'` → no match        → AC-3
- [x] `git grep -n typographyHeading -- apps` → five lines: the two generated files, `GreetingScreen.swift`, `FoundationTheme.kt` and `GreetingTest.kt`        → AC-3
- [x] `scripts/generate-design-tokens.sh --check` → exit `0`, `Validated tokens, configuration and localizations (4 generated files).`        → AC-3
- [x] `scripts/test.sh` → exit `0`, nine generator tests pass        → AC-4
- [x] `scripts/build-ios.sh simulator`, `scripts/build-ios.sh device`, then `scripts/build-ios.sh test <udid> light` and again with `dark`, with the UDID of a simulator from `xcrun simctl list devices available` → both builds succeed, one test passes in each appearance        → AC-4
- [x] `scripts/build-android.sh :app:assembleDebug :app:assembleDebugAndroidTest`, then `:app:connectedDebugAndroidTest` with `adb shell cmd uimode night no` and again with `yes` → two tests pass in each appearance        → AC-4
- [x] `git grep -l greeting_recipient -- shared apps` → seven files: the catalog, the localization README, the two generated string files, `MobileFoundationApp.swift`, `MainActivity.kt` and `GreetingTest.kt`        → AC-4
- [x] `git grep -n -i greeting -- tooling/codegen` → no match        → AC-5
- [x] `grep -n "generate.ROOT" tooling/codegen/test_generation.py` → one line, `schema = generate.load(generate.ROOT / LOCALIZATION_SCHEMA)`        → AC-5
- [x] In the clone: `echo '{}' > shared/localization/en.json`, `echo '{}' > design-system/tokens/typography.json`, then `scripts/generate-design-tokens.sh --test` and `--check` → `--test` passes nine tests, `--check` exits `1`        → AC-5
- [x] `scripts/generate-design-tokens.sh --test` → `test_sources_without_a_sample_name_generate_and_check ... ok`        → AC-6
- [x] In the clone: `printf '{\n  "welcome_title": "Welcome"\n}\n' > shared/localization/en.json`, then `scripts/generate-design-tokens.sh`, `scripts/generate-design-tokens.sh --check` and `scripts/generate-design-tokens.sh --test` → all three exit `0`, and `git status --short` lists the catalog and the two generated string files only        → AC-6
- [x] In the clone, before `git checkout -- .`: `git grep -n -i greeting -- design-system shared/specifications shared/localization/en.json shared/config tooling/codegen scripts/generate-design-tokens.sh apps/ios/DesignSystem apps/ios/App/Resources apps/android/designsystem apps/android/app/src/main/res` → no match        → AC-6
- [x] `git status --short` in the working checkout after the last clone step → the same output as before the first clone step        → AC-6
- [x] `grep -n typographyHeading docs/design-system/platform-mapping.md`, ``grep -n '`heading` and `body` for typography' docs/design-system/token-conventions.md``, `grep -n "names none" shared/localization/README.md`, `grep -n "fixtures/sources" docs/quality/architecture-compliance.md` → one match in each file        → AC-7
- [x] `grep -n "Nine generator tests" docs/quality/verification.md` and `grep -n "Schemas free of sample names" docs/quality/verification.md` → one match each, both in the `Local checks` table        → AC-7

### Value sourcing

One step per row of the spec's Value sourcing table. Each one changes the source and checks that the output follows.

- [x] Typography property name: in the clone, rename the role `body` to `copy` in `typography.json` and the schema, run `scripts/generate-design-tokens.sh` → both generated token files carry `typographyCopy` in place of `typographyBody`        → AC-3
- [x] Font, size, line height and weight of `typographyHeading`: in the clone, set the `headline` scale to 34 and 42 and point `heading` at `regular`, then generate → Kotlin shows `34.sp`, `42.sp` and `FontWeight(400)`, Swift shows `.system(.title, weight: .regular)`        → AC-3
- [x] Catalog keys: the AC-6 clone step → `Localizable.strings` and `foundation_strings.xml` carry `welcome_title` and no other key        → AC-6
- [x] Lowest number of keys: the AC-1 clone step with `{}` is refused, and `test_localization_schema_asks_for_one_key_and_names_none` accepts `{"a": "Text"}`        → AC-1
- [x] Required typography roles: the AC-2 clone step without `heading` is refused, and `test_schema_rejects_invalid_token_shapes` refuses a fixture without `heading` and one without `body`        → AC-2
- [x] Test token groups, configuration and catalog: the AC-5 clone step with the checkout's `en.json` and `typography.json` emptied → `--test` still passes nine tests        → AC-5
- [x] Test schemas: in the clone, add `"required": ["welcome_title"]` back into the localization schema, then `scripts/generate-design-tokens.sh --test` → `test_localization_schema_asks_for_one_key_and_names_none` fails        → AC-5
- [x] Output paths inside the temporary copy: `scripts/generate-design-tokens.sh --test` passes and `git status --short` in the working checkout is unchanged afterwards        → AC-5
- [x] Android theme: `grep -n typographyHeading apps/android/designsystem/src/main/kotlin/foundation/designsystem/FoundationTheme.kt` → the Material slot `headlineLarge` reads it        → AC-3
- [x] iOS screen: `grep -n typographyHeading apps/ios/Presentation/GreetingScreen.swift` → the greeting text uses it as its font        → AC-3
- [x] Android greeting test: `grep -n typographyHeading apps/android/app/src/androidTest/kotlin/foundation/mobile/GreetingTest.kt` → the expected font size comes from it, and the instrumentation tests pass        → AC-3, AC-4
- [x] Recipient passed to `hello`: both apps still read `greeting_recipient` and show `Hello, World!`        → AC-4

## Acceptance-criteria coverage

- AC-1 covered by the schema listing, the empty catalog clone step and the lowest number of keys row
- AC-2 covered by the `design-system` grep, the missing `heading` clone step and the required roles row
- AC-3 covered by the two app launches, the `typographyGreeting` and `typographyHeading` greps, `--check` and the property, font, theme, screen and test rows
- AC-4 covered by `scripts/test.sh`, the iOS builds and tests, the Android builds and tests, the `greeting_recipient` grep and the recipient row
- AC-5 covered by the `tooling/codegen` grep, the `generate.ROOT` grep, the emptied sources clone step and the test source rows
- AC-6 covered by the named test, the `welcome_title` clone step, the clone grep, the unchanged working checkout and the catalog keys row
- AC-7 covered by the four document greps and the two verification record greps
