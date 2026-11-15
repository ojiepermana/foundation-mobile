# 0004. Rationale. Schemas free of sample names: one key of any name, a `heading` role, generator tests on their own sources

This file holds the decision history of [spec 0004](index.md): the context, the options considered and the rationale. The build spec is in `index.md`.

## Context

The foundation ends at Hello World. Spec [0003](../0003-new-project-from-foundation/index.md) decided how a product starts from it, and its Follow-up list recorded what this spec answers: two foundation schemas still require sample names, and a product that replaces the greeting hits both. The forces at play:

- **The localization schema requires a key named `greeting_recipient`.** A catalog without that key fails with `en.json: data must contain ['greeting_recipient'] properties`. The key belongs to the sample screen, not to every product.
- **The token schema requires a typography role named `greeting`.** A token set without it fails with `tokens: data.typography.semantic must contain ['greeting'] properties`. The role is the large text style both apps use for their most prominent line, and its name ties it to one screen.
- **A product may not edit either schema without leaving the merge path.** Spec `0003` gives `design-system/schemas/`, `shared/specifications/`, `scripts/` and `tooling/` to the foundation. On a merge the product takes the foundation's side of those paths. Token values, catalogs and app sources are shared and merged by hand.
- **The generator tests read shared files from a foundation owned path.** `tooling/codegen/test_generation.py` loads the checkout's own tokens in three tests and copies the checkout's `design-system/` and `shared/` in a fourth, where it adds a French catalog with the key `greeting_recipient`. Run in a scratch clone at `7b6ca4f` with the catalog key replaced, the generator refuses the catalog and `test_stale_edited_and_missing_files` errors. One more test edits the scale `headline` and expects a `semibold` role, which only holds while the product keeps those token values.
- **The role name is a contract between both apps.** The generator turns the role into `FoundationTokens.typographyGreeting` in Swift and in Kotlin. `GreetingScreen.swift`, `FoundationTheme.kt` and `GreetingTest.kt` read it. The token conventions ask that a consumed role is renamed with every reader in the same change.
- **Spec `0003` fixes which names stay.** `FoundationTokens`, `FoundationTheme`, `foundation_strings.xml` and `shared/config/foundation.json` are kept by every product. A property inside `FoundationTokens` is not on that list.
- **The other required names describe a use.** The schema also requires eleven color roles, `body`, `page`, `content`, `surface` and `feedback`. None of them names a screen.
- **An empty catalog has no reader.** Both apps expect a string resource file with content, and the generator has always refused a catalog without the one required key.
- **One maintainer, and real caller first.** The repository rules ask for a real caller before a tool exists. A product that removes the sample is that caller, and it does not exist yet, so the proof has to run on a copy.

Without a decision, the first product that replaces the greeting edits two schemas and one test file that the foundation owns, and every later foundation release conflicts on those files.

## Options considered

### Option 1: Fix the two schemas in place, rename the role to `heading`, give the generator tests their own source tree

The localization schema swaps its required key for `minProperties: 1`. The required typography role is renamed to `heading` in the source, the schema, both generated files and the three readers. The generator tests read seven fixture files under `tooling/codegen/fixtures/sources/` in place of the checkout's catalog and tokens.

**Pros**:
- The product edits only shared and product owned paths when it replaces the greeting.
- The tests become independent of anything a product may change, so `--test` passes in every product.
- The fixture is itself a catalog and a token set with no greeting name, so the proof runs on every push.
- The generator code is not touched.

**Cons**:
- Seven fixture files are a second set of sources that must follow every schema change.
- The tests stop reading the checkout's own tokens, so only `--check` covers them.
- One generated property is renamed with no alias, which breaks a product that reads the old name until it renames its uses.

### Option 2: Fix the schemas and rename the role, keep the tests on the checkout's sources and make them generic

The schemas change as in Option 1. The tests keep loading the checkout's tokens and catalog, but ask them what they hold: the French catalog is a copy of the default catalog, and the typography test picks whichever role and scale it finds.

**Pros**:
- No fixture files to keep.
- The tests keep exercising the real sources of the checkout.

**Cons**:
- The tests still depend on the product's content. A product that already has a French catalog, or that changes a weight, can break them in ways the foundation cannot see from its own checkout.
- Tests that discover their inputs assert less. The typography test can no longer state the exact generated line.
- Nothing proves a catalog without the sample key, because the checkout's catalog still has it. That proof would need a separate fixture anyway.

### Option 3: Require no typography role at all

The localization schema changes as in Option 1. The token schema drops the required typography roles and asks only for at least one role of any name. Each product names its own text styles.

**Pros**:
- The schema names no typography role, so no later rename can break a product.
- A product keeps only the styles it uses.

**Cons**:
- `FoundationTheme.kt` and the iOS screen need some role to read. With none guaranteed, a product that deletes the role gets a compile error far from the token file, and the schema can no longer catch it.
- It goes further than the scope row asks. The row asks for a name that fits the purpose, not for the end of required roles.
- The other groups (color, spacing, radius, motion) would still require names, so typography alone would follow a different rule.

## Rationale

The force that settles it is the ownership split of spec `0003`. Schemas and `tooling/` belong to the foundation and arrive by merge. Tokens, catalogs and app sources are shared. A foundation owned file that names shared content breaks as soon as a product does what the foundation invites it to do. That is true of the two schema lines, and it is just as true of the tests, which is why Option 2 does not hold: it removes the names from the schemas and leaves the same coupling in `test_generation.py`.

Option 3 solves the rename for good but gives up a check the native code relies on. The Android theme reads a typography role by name. A required role is the one place where a missing role is reported next to its cause, and the scope row asks for a better name, not for fewer rules. Whether the schema should require fewer roles is left as a Follow-up for the first product to answer with evidence.

The design was run in a scratch clone before this spec was written. With the changes of Option 1 applied, `scripts/generate-design-tokens.sh` rewrote one line in each generated token file, `--check` passed, and nine tests passed under Python 3.9.6. With the clone's catalog replaced by the single key `welcome_title`, generation, `--check` and `--test` passed. With the clone's catalog and typography file emptied, `--test` still passed and `--check` refused them. `scripts/init-project.sh --test` passed in the clone, so the derivation test of spec `0003` is not disturbed by the new fixture files.

The calls made inside the chosen option. This spec was written in a coordinated run where the recommended option is taken and recorded, so each call below names its runner up. A call marked heavy is costly to reverse once it is built.

- **The role is named `heading` (heavy).** It says where the text is used: the line that heads a screen. It is not the name of a platform style, so it reads correctly beside SwiftUI `.title` and beside the Material slot `headlineLarge`. `title` was the runner up. It pairs well with `body`, but on Android it would sit in the `headlineLarge` slot while Material has its own, smaller `titleLarge`, which invites the wrong fix. `headline` was rejected because it is already the name of the primitive scale, and the conventions keep primitive names and role names apart. This call is heavy because the name is a contract both apps and every product read.
- **The role stays required.** The schema keeps `heading` and `body` as required typography roles. Dropping the requirement was the runner up (Option 3).
- **No alias for the old name.** `greeting` is renamed, not kept beside `heading`. The token conventions ask for one change across every reader, there are three readers, and a product that still reads the old name gets a compile error that names each place. Keeping `greeting` as a second role for one release was the runner up, and it would leave the sample name in the generated API of every product.
- **At least one key is written as `minProperties: 1`.** It is one standard Draft 7 keyword that the pinned validator already supports, and the refusal names the file. Allowing an empty catalog was the runner up. It was rejected because both apps expect a string resource with content and nothing calls for an empty one. A test in generator code was the other candidate, and it would move a shape rule out of the schema.
- **`greeting_recipient` stays in the sample.** The catalog, both apps and their tests keep the key. The scope row asks that the schema stop naming it, not that the sample change, and a rename would touch seven files for no gain. Renaming it to a neutral key such as `recipient_name` was the runner up.
- **The tests read a fixture tree of files.** Files mirror the layout the generator reads, so the test that copies a source tree into a temporary folder keeps its shape, and the tree is a readable example of the smallest valid source set. Building the same data as Python literals inside the test module was the runner up.
- **The fixture differs from the checkout's sources on purpose.** Its catalog key is `welcome_title`, its weight is `bold`, and its sizes are 30 and 36. A test that reads the wrong tree by mistake then fails. A byte for byte copy of the checkout's token files was the runner up, and it would hide exactly that mistake.
- **The proof has two parts.** A unit test generates and checks the fixture in a temporary folder on every push. A scratch clone step runs the real script with the catalog replaced, once, during verification. A `--root` flag on the generator with committed expected outputs was the runner up. It would add a public flag and a second set of generated files for one proof.
- **Only the two sample names change.** The other sixteen required role names describe a use and stay. The scale names `headline` and `reading`, which the generator maps to SwiftUI styles, also stay. They are a separate coupling and are listed as a Follow-up.
- **The generator code is left alone.** The property name already comes from the role name, so the rename needs no code change.
- **No `verify.md` from this spec.** `/develop` writes it from the Verification matrix in `index.md`, as it did for spec `0003`.
- **No References section.** Every decision here rests on the repository itself.

A cross check by a second model read the draft against the code. It confirmed the file list, the message texts and the fixture, and found that the scratch clone steps would have tested uncommitted work, that one expected result assumed a clean checkout, and that the names in the test module were left open. All of its findings are applied in `index.md`: the clone is made after a commit and restored between rows, the module names are written out, and the verification record edits have their own rows.

How this spec sits beside spec `0003`. It changes no name on the list that spec keeps, and it changes no owner. It leans on that spec's ownership table and makes one line of it true in practice: after this change, a product can replace the sample without editing a foundation owned path. The Follow-up line in spec `0003` that asked for this work is ticked in the same change.
