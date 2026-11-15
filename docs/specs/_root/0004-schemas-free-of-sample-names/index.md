# 0004. Schemas free of sample names: one key of any name, a `heading` role, generator tests on their own sources

**Date**: 2026-11-15
**Status**: In Progress

## Summary

This spec removes the two sample names that the foundation schemas (the files that say what a valid catalog and a valid token set look like) still require. The localization schema will ask for at least one key and name none. The typography role `greeting` becomes `heading`, a name for where the text is used, and both apps follow. The generator tests stop reading the checkout's own catalog and tokens and read a small source tree of their own, so they pass in a product that has replaced the greeting.

## Requirements

**User stories**:

- As the maintainer of a product, I want to replace the greeting with my first feature by editing the catalog, the token values and the app sources only, so that I never edit a path the foundation owns.
- As the maintainer of the foundation, I want the generator tests to pass whatever a product puts in its catalog and tokens, so that a foundation release still merges cleanly after the sample is gone.
- As a contributor to either app, I want the large text style to be named for its use, so that I can use it on a screen that greets nobody.

**Acceptance criteria** (the contract, each criterion is IDed and independently checkable):

- **AC-1**: `shared/specifications/localization.schema.json` holds `"minProperties": 1` and has no `required` member and no `properties` member, so it names no key. The key pattern and the value rule stay as they are. With an empty default catalog (`{}`), `scripts/generate-design-tokens.sh --check` exits `1` and prints `en.json: data must contain at least 1 properties`. A catalog whose only key is any name that fits the key pattern is accepted.
- **AC-2**: The typography role is named `heading` in `design-system/tokens/typography.json`, with the same scale (`headline`) and weight (`semibold`) the role `greeting` had. `design-system/schemas/tokens.schema.json` requires `heading` and `body`. No tracked file under `design-system/` contains the word `greeting` in any letter case. A token set without `heading` is rejected with `tokens: data.typography.semantic must contain ['heading'] properties`.
- **AC-3**: Both generated token files carry `typographyHeading` with unchanged values: `static let typographyHeading: Font = .system(.title, weight: .semibold)` in Swift, and `val typographyHeading = TextStyle(` with `32.sp`, `40.sp` and `FontWeight(600)` in Kotlin. `apps/ios/Presentation/GreetingScreen.swift`, `FoundationTheme.kt` and `GreetingTest.kt` read `FoundationTokens.typographyHeading`. `typographyGreeting` appears in no tracked file outside `docs/specs/`, `docs/scope/` and `graphify-out/`. `scripts/generate-design-tokens.sh --check` exits `0`.
- **AC-4**: The sample app behaves as before. `scripts/test.sh` exits `0`, both apps build, and the greeting tests pass in light and dark appearance on both platforms. The key `greeting_recipient` stays in `shared/localization/en.json`, in both generated string files and in both app entry points.
- **AC-5**: No test under `tooling/codegen/` reads `design-system/tokens/`, `shared/config/` or `shared/localization/` of the checkout. The tests read `tooling/codegen/fixtures/sources/` and the checkout's schemas. With the checkout's own `en.json` and `typography.json` each replaced by `{}`, `scripts/generate-design-tokens.sh --test` still passes. No tracked file under `tooling/codegen/` contains the word `greeting` in any letter case.
- **AC-6**: A catalog and a token set with no greeting name pass. The test `test_sources_without_a_sample_name_generate_and_check` proves it on every run of `--test`. In a scratch clone whose `shared/localization/en.json` is replaced by a catalog with the single key `welcome_title`, `scripts/generate-design-tokens.sh` writes the outputs, `--check` exits `0`, `--test` passes, and `git grep -i greeting` finds nothing in the generator inputs and outputs listed under Verification matrix. The working checkout is unchanged afterwards.
- **AC-7**: The documents follow, with the texts given in the Build plan: the platform mapping names `typographyHeading`, the token conventions list the required roles and the naming rule, the localization README says that the schema names no key and that `greeting_recipient` is sample content, the quality checks table names the fixture tree, and the verification record states what ran.

## Decision

**Chosen option**: Option 1: Fix the two schemas in place, rename the role to `heading`, and give the generator tests their own source tree.

The localization schema asks for one key of any name through `minProperties`, the required typography role is renamed from `greeting` to `heading` in one change across the source, both generated files and their three readers, and every generator test reads `tooling/codegen/fixtures/sources/` in place of the checkout's catalog and tokens.

## Rationale

Reasoning and options: see [rationale.md](rationale.md).

## Feature design

**Owner and contract**. Nothing changes owner. The ownership matrix rows stay as they are: `design-system/tokens/` and `design-system/schemas/` own the visual values and roles, `shared/` owns the catalogs, and `tooling/` owns generation and schema checks. The public contract that changes is one generated property name, `FoundationTokens.typographyGreeting`, which becomes `FoundationTokens.typographyHeading` on both platforms. The type names `FoundationTokens` and `FoundationTheme` and the file `foundation_strings.xml` are names spec `0003` keeps, and they do not change. No dependency edge is added.

**Data model sketch**:

There is no database. The model is two schemas, one renamed role and one fixture tree (a small set of files that only the tests read).

The localization schema, in full, after the change:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Shared strings for one locale",
  "type": "object",
  "minProperties": 1,
  "propertyNames": { "pattern": "^[a-z][a-z0-9]*(_[a-z0-9]+)*$" },
  "additionalProperties": { "type": "string", "minLength": 1 }
}
```

The token schema changes on one line. Under `typography.semantic`, `"required": ["greeting", "body"]` becomes `"required": ["heading", "body"]`. Every other required name in that schema stays.

The typography source changes on one line. In `design-system/tokens/typography.json`, `"greeting": { "scale": "headline", "weight": "semibold" }` becomes `"heading": { "scale": "headline", "weight": "semibold" }`. No alias for the old name is kept.

| Role | Meaning | Swift, generated | Kotlin, generated | Read by |
| --- | --- | --- | --- | --- |
| `heading` | The most prominent line of text on a screen | `static let typographyHeading: Font = .system(.title, weight: .semibold)` | `val typographyHeading = TextStyle(fontSize = 32.sp, lineHeight = 40.sp, fontWeight = FontWeight(600))`, written over five lines as today | iOS `GreetingScreen.swift`, Android `FoundationTheme.kt` (the Material slot `headlineLarge`) and `GreetingTest.kt` |
| `body` | Running text | `typographyBody`, unchanged | `typographyBody`, unchanged | Nothing yet |

The generator sorts roles by name, so `typographyBody` still comes first and `typographyHeading` takes the line `typographyGreeting` had. Each generated file changes on exactly one line.

What stays as sample content, on purpose: the key `greeting_recipient` in `shared/localization/en.json`, the two generated string files, `MobileFoundationApp.swift`, `MainActivity.kt`, `GreetingTest.kt`, the screens named `GreetingScreen`, and the accessibility identifier `greeting`. A product replaces these together when its first feature arrives. No schema and no generator test names any of them after this change.

The fixture tree, `tooling/codegen/fixtures/sources/`. It mirrors the layout the generator reads, and its names and values differ from the checkout's own on purpose, so a test cannot pass by reading the wrong tree. Seven files, each ending with one newline:

```text
tooling/codegen/fixtures/sources/design-system/tokens/colors.json
{
  "primitives": { "paper": "#FFFFFF", "coal": "#000000" },
  "semantic": {
    "brand":         { "light": "coal", "dark": "paper" },
    "primary":       { "light": "coal", "dark": "paper" },
    "secondary":     { "light": "coal", "dark": "paper" },
    "background":    { "light": "paper", "dark": "coal" },
    "surface":       { "light": "paper", "dark": "coal" },
    "textPrimary":   { "light": "coal", "dark": "paper" },
    "textSecondary": { "light": "coal", "dark": "paper" },
    "border":        { "light": "coal", "dark": "paper" },
    "success":       { "light": "coal", "dark": "paper" },
    "warning":       { "light": "coal", "dark": "paper" },
    "error":         { "light": "coal", "dark": "paper" }
  }
}

tooling/codegen/fixtures/sources/design-system/tokens/typography.json
{
  "primitives": {
    "scale": {
      "headline": { "size": 30, "lineHeight": 36 },
      "reading": { "size": 15, "lineHeight": 22 }
    },
    "weight": { "regular": 400, "bold": 700 }
  },
  "semantic": {
    "heading": { "scale": "headline", "weight": "bold" },
    "body": { "scale": "reading", "weight": "regular" }
  }
}

tooling/codegen/fixtures/sources/design-system/tokens/spacing.json
{
  "primitives": { "near": 8, "far": 20 },
  "semantic": { "content": "near", "page": "far" }
}

tooling/codegen/fixtures/sources/design-system/tokens/radius.json
{
  "primitives": { "round": 10 },
  "semantic": { "surface": "round" }
}

tooling/codegen/fixtures/sources/design-system/tokens/motion.json
{
  "primitives": { "brisk": 120 },
  "semantic": { "feedback": "brisk" }
}

tooling/codegen/fixtures/sources/shared/config/foundation.json
{
  "schemaVersion": 1,
  "defaultLocale": "en"
}

tooling/codegen/fixtures/sources/shared/localization/en.json
{
  "welcome_title": "Welcome"
}
```

The scale names `headline` and `reading` are kept in the fixture because the generator maps exactly those two names to SwiftUI text styles.

**State transitions**: none.

**API surface**:

The surface is the existing command. Its forms, flags and output paths do not change. `tooling/codegen/generate.py`, `tokens.py` and `resources.py` are not edited.

| Form | What changes | Exit |
| --- | --- | --- |
| `scripts/generate-design-tokens.sh` | Accepts any catalog with at least one valid key. Writes `typographyHeading` | `0` written · `1` invalid source |
| `scripts/generate-design-tokens.sh --check` | The same two rules. An empty catalog and a token set without `heading` are refused with the messages in AC-1 and AC-2 | `0` clean · `1` invalid or drifted |
| `scripts/generate-design-tokens.sh --test` | Runs nine tests in place of seven. None reads the checkout's catalog, configuration or tokens | `0` passed · `1` failed |

The tests in `tooling/codegen/test_generation.py` after the change. The module gains these four names, written exactly so:

```python
FIXTURE = Path(__file__).resolve().parent / "fixtures/sources"
TOKEN_SCHEMA = "design-system/schemas/tokens.schema.json"
LOCALIZATION_SCHEMA = "shared/specifications/localization.schema.json"


def token_groups():
    return {path.stem: generate.load(path) for path in (FIXTURE / "design-system/tokens").glob("*.json")}
```

The two schema constants are relative strings, because `generate.check_schema` joins them to the checkout root itself. The only line in the module that names `generate.ROOT` is `schema = generate.load(generate.ROOT / LOCALIZATION_SCHEMA)` in the new localization test. Both tests that copy the fixture tree wrap their body in `TemporaryDirectory()` and `redirect_stdout(StringIO())`, as `test_stale_edited_and_missing_files` does today, so the generator's own output stays out of the test report.

| Test | Sources | What it asserts |
| --- | --- | --- |
| `test_alias_and_text_contrast` | Fixture colors | Unchanged assertions: an unknown primitive and a failed text contrast are refused |
| `test_schema_rejects_invalid_token_shapes` | Fixture tokens | The fixture passes the token schema. A color value `red` is refused. Removing `spacing.semantic.page`, `typography.semantic.heading` or `typography.semantic.body` is refused, each with `tokens:` |
| `test_typography_uses_native_mapping_from_neutral_scales` | Fixture tokens | The Swift output holds `static let typographyHeading: Font = .system(.title, weight: .bold)`. The Kotlin output holds `val typographyHeading = TextStyle(`, `fontSize = 30.sp` and `lineHeight = 36.sp`. Adding `appleStyle` to the `headline` scale is refused with `tokens:`. The test no longer edits a scale before rendering |
| `test_schema_requires_closed_configuration_and_valid_resource_keys` | Literals | Unchanged, except that the catalog literal becomes `{"welcome_title": "Welcome", "Upper": "invalid"}` |
| `test_localization_schema_asks_for_one_key_and_names_none` (new) | The checkout's localization schema, literals | The schema has `minProperties` equal to `1` and has neither `required` nor `properties`. `{}` is refused with `localization: data must contain at least 1 properties`. `{"a": "Text"}` and `{"welcome_title": "Welcome", "second_key": "More"}` are accepted |
| `test_placeholders_reorder_and_literals_escape` | Literals | Unchanged |
| `test_placeholder_key_and_locale_mismatch` | Literals | Unchanged |
| `test_stale_edited_and_missing_files` | A temporary copy of the fixture tree | Unchanged flow. The copy is made with `shutil.copytree(FIXTURE, root, dirs_exist_ok=True)`, and the added `fr.json` holds `{"welcome_title": "Bienvenue"}` |
| `test_sources_without_a_sample_name_generate_and_check` (new) | A temporary copy of the fixture tree | `generate.generate(root, check=False)` then `generate.generate(root, check=True)` both succeed. The Android `values/foundation_strings.xml` in the copy holds `<string name="welcome_title" formatted="false">"Welcome"</string>`. Both generated token files in the copy hold `typographyHeading`. Its first two calls repeat the start of the test above on purpose, so the proof has a name of its own in the test report |

**Value sourcing**:

| Action | Value produced / displayed | Source |
| --- | --- | --- |
| generate | Typography property name on both platforms | `typography` plus the role name with its first letter in upper case, from the keys of `typography.semantic` in `design-system/tokens/typography.json` (the existing `tokens.property_name`) |
| generate | Font, size, line height and weight of `typographyHeading` | The scale and weight the role `heading` refers to in the same file: `headline` (32, 40, SwiftUI `.title`) and `semibold` (600) |
| generate | Keys in `Localizable.strings` and `foundation_strings.xml` | The keys of each catalog under `shared/localization/` |
| check | Lowest number of keys in a catalog | `minProperties` in `shared/specifications/localization.schema.json` |
| check | Required typography roles | `required` under `typography.semantic` in `design-system/schemas/tokens.schema.json` |
| test | Token groups, configuration and catalog | `tooling/codegen/fixtures/sources/`, read through `FIXTURE` |
| test | Schemas | The checkout's three schema files, read through `generate.ROOT` as today |
| test | Output paths inside the temporary copy | `tokens.SWIFT_PATH`, `tokens.KOTLIN_PATH`, `resources.IOS_RESOURCES` and `resources.ANDROID_RESOURCES`, as today |
| Android theme | Text style of the Material slot `headlineLarge` | `FoundationTokens.typographyHeading` |
| iOS screen | Font of the greeting text | `FoundationTokens.typographyHeading` |
| Android greeting test | Expected font size | `FoundationTokens.typographyHeading.fontSize` |
| Both apps | Recipient passed to `hello` | The key `greeting_recipient`, unchanged |

**Key invariants**:

- A schema names a role or a key only for where it is used. It never names the screen or the sample that uses it today.
- The localization schema names no key at all. A catalog is valid with any one key that fits the pattern.
- A generator test reads the fixture tree and the schemas, never the checkout's own catalog, configuration or tokens. `--check` is the one proof that the checkout's own sources are valid.
- The fixture tree satisfies the schemas. When a schema gains a required name, the fixture gains it in the same change, and a failing `--test` is the signal that it did not.
- A consumed role is renamed in one change with every reader on both platforms. No alias is kept.

**Security model**: nothing new. The generator reads and writes inside the checkout, the tests inside a temporary folder that they remove. No network beyond the existing download of the pinned validator wheel on first use, and no secret.

**Configuration required**: none.

**Critical test scenarios** (each maps to an acceptance criterion in ## Requirements):

- Happy path: the checkout as it stands after the change passes `--check` and `--test`, and both apps show `Hello, World!` in the heading style in both appearances, verifies **AC-3**, **AC-4**
- A catalog with one key of another name: the fixture catalog `welcome_title` generates and checks cleanly in a temporary folder, verifies **AC-1**, **AC-6**
- Empty catalog: `{}` is refused with the at least one key message, verifies **AC-1**
- Missing role: a token set without `heading`, and one without `body`, are each refused, verifies **AC-2**
- A product without the sample: in a scratch clone the catalog loses `greeting_recipient`, and the generator, its check and its tests all pass, verifies **AC-6**
- Broken checkout sources: with the checkout's catalog and typography file emptied in a scratch clone, `--check` fails and `--test` passes, verifies **AC-5**
- Drift detection still works: an edited output and a missing output are reported, and a removed locale takes its outputs with it, on the fixture copy, verifies **AC-5**

## Verification matrix

`/develop` turns these rows into `verify.md` in this folder, as spec `0003` has. Every step that removes or breaks the sample runs in a scratch clone, never in the working checkout. A clone holds committed work only, so commit steps 1 to 4 first. Then make the clone:

```sh
SCRATCH=$(mktemp -d)
git clone --branch "$(git branch --show-current)" . "$SCRATCH/f010-proof"
mkdir -p "$SCRATCH/f010-proof/build" && cp -R build/tooling "$SCRATCH/f010-proof/build/"
```

The third line copies the pinned validator wheel so the clone does not download it again. `build/tooling/` exists in the working checkout once `scripts/test.sh` or the generator has run there. Without the copy the clone downloads the wheel on first use, which also works. Run `git checkout -- .` in the clone after each clone row, so every row starts from the committed state. Run `git status --short` in the working checkout before the first clone row and keep the output for the last AC-6 row. Remove the clone at the end with `rm -rf "$SCRATCH"`.

| AC | Command | Expected |
| --- | --- | --- |
| AC-1 | `cat shared/specifications/localization.schema.json` | Equals the schema given in this spec |
| AC-1 | In the clone: `echo '{}' > shared/localization/en.json`, then `scripts/generate-design-tokens.sh --check` | Exit `1`, `en.json: data must contain at least 1 properties` |
| AC-2 | `git grep -n -i greeting -- design-system` | No match |
| AC-2 | In the clone: `sed 's/"heading"/"display"/' design-system/tokens/typography.json > t.json && mv t.json design-system/tokens/typography.json`, then `scripts/generate-design-tokens.sh --check` | Exit `1`, `tokens: data.typography.semantic must contain ['heading'] properties` |
| AC-3 | `git grep -n typographyGreeting -- ':!docs/specs' ':!docs/scope' ':!graphify-out'` | No match |
| AC-3 | `git grep -n typographyHeading -- apps` | Five lines: the two generated files, `GreetingScreen.swift`, `FoundationTheme.kt` and `GreetingTest.kt` |
| AC-3 | `scripts/generate-design-tokens.sh --check` | Exit `0`, `Validated tokens, configuration and localizations (4 generated files).` |
| AC-4 | `scripts/test.sh` | Exit `0`, nine generator tests pass |
| AC-4 | `scripts/build-ios.sh simulator`, `scripts/build-ios.sh device`, then `scripts/build-ios.sh test <udid> light` and again with `dark`, with the UDID of a simulator from `xcrun simctl list devices available` | Both builds succeed, one test passes in each appearance |
| AC-4 | `scripts/build-android.sh :app:assembleDebug :app:assembleDebugAndroidTest`, then `:app:connectedDebugAndroidTest` with `adb shell cmd uimode night no` and again with `yes` | Two tests pass in each appearance |
| AC-4 | `git grep -l greeting_recipient -- shared apps` | Seven files: the catalog, the localization README, the two generated string files, `MobileFoundationApp.swift`, `MainActivity.kt` and `GreetingTest.kt` |
| AC-5 | `git grep -n -i greeting -- tooling/codegen` | No match |
| AC-5 | `grep -n "generate.ROOT" tooling/codegen/test_generation.py` | One line, `schema = generate.load(generate.ROOT / LOCALIZATION_SCHEMA)` |
| AC-5 | In the clone: `echo '{}' > shared/localization/en.json`, `echo '{}' > design-system/tokens/typography.json`, then `scripts/generate-design-tokens.sh --test` and `--check` | `--test` passes nine tests. `--check` exits `1` |
| AC-6 | `scripts/generate-design-tokens.sh --test` | `test_sources_without_a_sample_name_generate_and_check ... ok` |
| AC-6 | In the clone: `printf '{\n  "welcome_title": "Welcome"\n}\n' > shared/localization/en.json`, then `scripts/generate-design-tokens.sh`, `scripts/generate-design-tokens.sh --check` and `scripts/generate-design-tokens.sh --test` | All three exit `0`. `git status --short` lists the catalog and the two generated string files only |
| AC-6 | In the clone, before `git checkout -- .`: `git grep -n -i greeting -- design-system shared/specifications shared/localization/en.json shared/config tooling/codegen scripts/generate-design-tokens.sh apps/ios/DesignSystem apps/ios/App/Resources apps/android/designsystem apps/android/app/src/main/res` | No match |
| AC-6 | `git status --short` in the working checkout after the last clone row | The same output as before the first clone row |
| AC-7 | `grep -n typographyHeading docs/design-system/platform-mapping.md`, ``grep -n '`heading` and `body` for typography' docs/design-system/token-conventions.md``, `grep -n "names none" shared/localization/README.md`, `grep -n "fixtures/sources" docs/quality/architecture-compliance.md` | One match in each file |
| AC-7 | `grep -n "Nine generator tests" docs/quality/verification.md` and `grep -n "Schemas free of sample names" docs/quality/verification.md` | One match each, both in the `Local checks` table |

## Build plan

Ordered as one thin thread first (the renamed role travels from its source through the generator into both running apps), then the tests that guard it, then the written record.

1. In `shared/specifications/localization.schema.json`, replace the line `"required": ["greeting_recipient"],` with `"minProperties": 1,`. Run `scripts/generate-design-tokens.sh --check`, satisfies **AC-1**
2. Rename the role along its whole path in one commit. In `design-system/schemas/tokens.schema.json` change the required typography roles to `["heading", "body"]`. In `design-system/tokens/typography.json` rename the key `greeting` to `heading`. Run `scripts/generate-design-tokens.sh`, which rewrites `apps/ios/DesignSystem/Generated/FoundationTokens.swift` and `apps/android/designsystem/src/main/kotlin/foundation/designsystem/FoundationTokens.kt` (never edit these two by hand). Change `typographyGreeting` to `typographyHeading` in `apps/ios/Presentation/GreetingScreen.swift`, in `apps/android/designsystem/src/main/kotlin/foundation/designsystem/FoundationTheme.kt` and in `apps/android/app/src/androidTest/kotlin/foundation/mobile/GreetingTest.kt`. Build both apps and run the greeting tests in both appearances, satisfies **AC-2**, **AC-3**, **AC-4**
3. Add the seven fixture files under `tooling/codegen/fixtures/sources/` with the contents given above, and change `tooling/codegen/test_generation.py` to the nine tests in the table above. Run `scripts/generate-design-tokens.sh --test`, satisfies **AC-5**, **AC-6**
4. Update the documents with the texts below, satisfies **AC-7**
5. Run `scripts/test.sh` and the scratch clone rows of the Verification matrix, then record the results in `docs/quality/verification.md` as described below, satisfies **AC-4**, **AC-6**, **AC-7**

Texts for step 4:

- `docs/design-system/platform-mapping.md`: in the last paragraph, change `` `typographyGreeting` and `spacingPage` `` to `` `typographyHeading` and `spacingPage` ``. Nothing else changes.
- `docs/design-system/token-conventions.md`: add this paragraph before the last paragraph (the one that starts `Change the schema alongside`).

  ```markdown
  The schema requires a fixed set of roles so both apps can rely on them: the eleven color roles, `heading` and `body` for typography, `page` and `content` for spacing, `surface` for radius and `feedback` for motion. Each one is named for where it is used. `heading` is the most prominent line of text on a screen, and `body` is running text. Name a new role the same way, never after the screen or the sample that uses it first.
  ```

- `shared/localization/README.md`: replace the first paragraph with this one.

  ```markdown
  Each UTF-8 JSON object maps stable lower snake case keys to strings. A catalog needs at least one key. The schema names none, so the keys are yours to choose. The sample catalog has one key, `greeting_recipient`, which names the recipient passed to the Rust greeting. Its English translation is the canonical terminology for this example. Both applications render the exact string returned from Rust. Replace that key together with the greeting screen when your first feature arrives.
  ```

- `docs/quality/architecture-compliance.md`: in the row `Tokens, configuration and localization`, append this sentence to the second cell.

  ```markdown
  The tests read their own source tree under `tooling/codegen/fixtures/sources/`, so they pass whatever the tokens and catalogs of the checkout hold.
  ```

Text for step 5, in `docs/quality/verification.md`:

- In the row `Design system and resources`, change `Seven generator tests` to `Nine generator tests`, and append: `` The tests read `tooling/codegen/fixtures/sources/`, not the checkout's own sources. ``
- Add a row after `Product identity` in the `Local checks` table, in that row's style: the first cell is `Schemas free of sample names`, the second cell is one paragraph that starts with `Ran on <date>`. It states the date, that `scripts/test.sh` passed, that both apps built and passed the greeting tests in both appearances after the rename to `typographyHeading`, and that in a scratch clone a catalog with the single key `welcome_title` passed generation, `--check` and `--test`. State only what ran. A target that did not run goes to the `Still unverified` list in that file's own words.
- Leave the `Hosted run` rows as they are. They describe past runs, and `seven generator tests` was true for them.

The commit rule in `AGENTS.md` applies to every step as usual: the knowledge graph is updated with the change. `graphify-out/` still holds the old property name until then, which is why the AC-3 search leaves that folder out.

**Parallel sessions**. Steps 1 and 2 touch different files and can run side by side. Step 4 touches only documents that no other step touches, so it can run beside any of them. Step 3 needs steps 1 and 2 merged first, because its tests assert the changed schemas. Step 5 needs all of them. The whole build is about twenty small files, so one developer session in the order above is the simpler plan, and the split is offered only if a second session is already waiting.

## Consequences

**Positive**:

- A product replaces the greeting by editing the catalog, the token values and the app sources. It never edits `design-system/schemas/`, `shared/specifications/` or `tooling/`, the paths spec `0003` gives to the foundation.
- The generator tests pass in every product, whatever its catalog and tokens hold. A foundation release still merges after the sample is gone.
- The large text style has a name that fits any screen.
- An empty catalog is still refused, so both apps always get a string resource file with content.
- One more test proves, on every push, that sources with no greeting name generate and check cleanly.

**Negative / tradeoffs**:

- `typographyGreeting` is gone with no alias. A product derived before this release renames its uses when it merges the release. The compiler names each place, and the generated files are rewritten by the generator.
- Seven fixture files are a second, smaller set of sources to keep valid. A new required name in a schema must be added to the fixture in the same change.
- The generator tests no longer exercise the checkout's own tokens. Only `--check` covers them. That is the same coverage in practice, since every test that read them asserted generator behavior, not token values.
- The token schema still requires seventeen role names. A product that wants no `heading` or no `feedback` role still has to keep it. This spec removes the sample name, not the idea of required roles.
- The sample itself keeps its names (`greeting_recipient`, `GreetingScreen`, `GreetingTest`). A product that replaces the greeting renames those in its own app sources.

**Neutral**:

- No owner, dependency or command changes, so the ownership matrix, the dependency rules and the README are not edited.
- The rendered greeting is unchanged: the same font, size, weight and color in both apps.
- `tooling/codegen/generate.py`, `tokens.py` and `resources.py` are not edited.
- `/develop` moves this spec to `In Progress` and `Accepted` with scope row `010`.

## Follow-up

- [ ] The generator maps the scale names `headline` and `reading` to SwiftUI text styles in `tooling/codegen/tokens.py`. A product that adds a third scale has to edit that file, which the foundation owns. Decide whether the SwiftUI style moves into the token source when the first product needs a new scale.
- [ ] Foundation owned files outside the schemas still name the sample in prose: the empty verification record in `tooling/derive/verification-record.md` (`the greeting test`), a fixture string in `tooling/derive/test_init_project.py` and one step name in `.github/workflows/foundation.yml`. None of them fails when the greeting is replaced. Reword them when the first product replaces the greeting.
- [ ] Decide whether the token schema should require fewer roles once a product shows which ones it does not use.
