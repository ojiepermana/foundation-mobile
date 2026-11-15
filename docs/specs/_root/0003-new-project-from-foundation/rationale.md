# 0003. Rationale. A new project from the foundation: product identity in two files, one init command, updates by merge

This file holds the decision history of [spec 0003](index.md): the context, the options considered and the rationale. The build spec is in `index.md`.

## Context

> ⚠️ Premise note: This topic holds four decisions (which names change, how a copy is made, what happens to inherited records, how updates arrive). They are written as one spec because each one constrains the others, and a split would let them drift. The risk is building update machinery before any product exists. This spec therefore decides only what cannot be changed cheaply after the first product starts, and builds only what the first derivation calls. The first derived product is the real caller that ADR 0001 asks for. The command that takes a later foundation release is described, not built.

Nothing in the repository says how to start a product from it. The forces at play:

- **The two apps disagree on their own identity.** iOS is `dev.foundation.mobile`, shown as Mobile Foundation, version 1.0. Android is `foundation.mobile`, shown as Foundation, version 0.1.0. The Android ID is not in reverse DNS form (a domain written backwards, such as `com.acme.notes`).
- **Identity is spread over files the foundation keeps editing.** The values sit in `App.xcconfig`, `Project.xcconfig`, `project.pbxproj`, `app/build.gradle.kts` and `res/values/app.xml`. The iOS UI test bundle ID is written out twice in `project.pbxproj`.
- **Two products cannot share a device today.** Two copies of the foundation carry the same ID, so one installs over the other.
- **A copy inherits claims it never earned.** `docs/quality/verification.md` and `docs/scope/index.md` name a hosted run in the foundation repository. In a new product those results are not true.
- **The knowledge graph is tied to this checkout.** 74 tracked cache files sit under a folder named from the checkout path, and one entry holds an owner specific string.
- **Foundation fixes must reach products.** With several products, a fix that has to be typed again in each one will not be applied.
- **Stable names are what make a merge clean.** 31 code and config files and 13 paths carry the foundation name (`MobileFoundation`, `FoundationTokens`, `foundation.designsystem`, `foundation-core`). Renaming them in a product makes every later foundation change to those files a conflict.
- **`shared/config/README.md` keeps application IDs native.** Bundle and application IDs belong in Xcode or Gradle, not in the shared config schema.
- **One maintainer, and real caller first (R8).** A step no machine checks rests on one person, and no tool may exist before something calls it.

Without a decision, the first product would be renamed by search and replace, and its history, names and records would differ from the next product in ways nobody chose.

## Options considered

### Option 1: Clone and merge, product identity in two files, one init command

A product starts as a clone and keeps the foundation as a second remote. Only the display name, application ID and version change, and they live in one file per platform that the foundation never edits again. One command writes those files and resets the inherited records.

**Pros**:
- A foundation release reaches a product by `git merge`, with conflicts only where the product changed the same lines.
- The surface that changes is two files, so the command and its check stay small.
- The Xcode project, the scheme and the build scripts are never rewritten, which is the fragile part of any rename.

**Cons**:
- Foundation names stay visible in product code (`MobileFoundation.xcodeproj`, `FoundationTokens`, `foundation.designsystem`).
- A product carries the foundation's commit history.
- A command and its tests have to be kept for a job that runs once per product.

### Option 2: Template copy with a full rename

A product starts from the GitHub template button with a fresh history. A script renames everything: crates, Kotlin packages, generated type names, the Xcode project and scheme.

**Pros**:
- No trace of the foundation name in the product.
- A clean history that belongs to the product alone.

**Cons**:
- The histories are unrelated and every file differs, so a foundation fix is moved by hand as a patch, per product.
- The rename has to rewrite `project.pbxproj`, the scheme, the validator constants, both generators and the bindings, and each of those can break in a way only a native build shows.
- The script grows with every name the foundation adds.

### Option 3: A written checklist, no command

The README lists the edits. The maintainer makes them by hand for each product.

**Pros**:
- Nothing to build, test or keep running.
- Fits the rule that a tool needs a caller, since there is no tool.

**Cons**:
- Each product is renamed slightly differently, and a missed step shows up late (two apps that install over each other, a record that claims results from another repository).
- Nothing tells a contributor whether a checkout is fully derived.
- The list goes stale silently when the foundation moves a value.

## Rationale

The force that settles it is the number of products. With one product, a checklist (Option 3) would do. With several, the cost that repeats is not the first rename, it is every later foundation fix. Only a shared history and stable names make that a merge, and a merge is the one update path a single maintainer will keep using.

The engineer first chose to rename every name (Option 2), then chose product identity only once the conflict with merging was laid out. Renaming everything remains possible later inside one product, at the price of leaving the merge path. The reverse move is not possible, which is why the narrow choice comes first.

The calls made inside the chosen option, each confirmed with the engineer unless marked as a recommendation:

- **One name and one application ID as input.** The same ID is used on both platforms, with an override per platform for a product that already has different IDs in the stores.
- **Inherited scope rows and specs stay as history.** The evidence is what gets emptied: the verification record and the hosted run link.
- **The Linux proof runs on every push. The native proof runs by hand before a foundation tag.** `scripts/test.sh` does not read the application ID, so only a native build tests a changed identity, and that cost is paid once per release.
- **The Linux proof is one unit test, not a second run of `scripts/test.sh`.** A cross check showed that a full second run doubles the lint, the tests and a UniFFI compile while proving almost nothing new, since those steps never read the identity. A `--self-test` form that ran everything in a copy was the runner up.
- **Every native run compares the built app with the identity file.** The greeting tests never read the ID, so without that comparison a run under the sample identity would pass even if the build ignored the identity file.
- **Only identifiers follow a rename, never prose.** With product identity only, no document needs rewriting. The one command in the README that names the ID reads it from the identity file.
- **No References section.** Every decision here rests on the repository itself.
- **Recommendation: one identity file per platform that the foundation never edits again.** Git reports a conflict when two sides change neighbouring lines. Identity lines inside `Project.xcconfig` or `build.gradle.kts` sit next to lines the foundation will change. Leaving the values where they are and editing them in place was the runner up.
- **Recommendation: the identity files stay native.** `shared/config/README.md` keeps application IDs in Xcode or Gradle. One shared file read by both builds was the runner up, and it would break that rule and tie the two platforms together.
- **Recommendation: Python under `tooling/derive/`, with a shell entry in `scripts/`.** This is the shape the generators already use. Python 3.9 with the standard library only, no new dependency. A pure shell script was the runner up, and it lost on input checks and tests.
- **Recommendation: `--check` accepts two states, `foundation` and `derived`.** One check then runs unchanged in both repositories and catches a half finished derivation in either. A check that passes only after derivation was the runner up, and it would fail in the foundation itself.
- **Recommendation: `--check` does not look for hosted run links.** The command writes the record from a template, so the record is right by construction. A link test would depend on the exact spelling of a URL and on a file that `/scope` rewrites.
- **Recommendation: the command refuses to run on a derived checkout.** A second run would wipe the product's own verification record. A later change of name or ID is an edit of the two identity files.
- **Recommendation: the command does not edit scope rows.** `/scope` owns those files (spec `0002`), and a second writer would break when their shape changes. Marking inherited rows `existing` is one step in the written path.
- **Recommendation: after derivation the product owns `docs/scope/`, `docs/specs/` and the verification record.** On a later merge the product keeps its own side of those paths. No rule file links to a numbered row or spec, so nothing dangles. Sharing one numbering sequence with the foundation was the runner up, and it collides on the first row either side adds.
- **Recommendation: the origin line records where a product started and never changes.** Later releases are visible in `git log --merges`. Rewriting the line on each merge was the runner up, and it would make the word started untrue.
- **Recommendation: tags are named `foundation-vMAJOR.MINOR.PATCH`.** The prefix keeps them apart from a product's own release tags in the same clone. A plain `v` prefix was the runner up.
- **Recommendation: no changelog file and no sync command yet.** Tags and a path limited `git log` give the list of changes for one maintainer. Both get built when the first foundation release is merged into a product, which is their real caller.
