# 0001. One owner per responsibility, with rules kept beside the code

**Date**: 2026-11-14
**Status**: Accepted

## Summary

Every shared responsibility in this repository has exactly one owner, and a contributor finds that owner in the ownership matrix before changing anything. The rules live as short files under `docs/`, the root `AGENTS.md` points into them, and one validator script plus two generator checks guard the parts a machine can judge. The rest rests on review. This spec records that standard as it shipped. It does not change any rule, and the rule files stay the place to edit.

## Context

> ⚠️ Premise note: A spec that restates rules which already live in `docs/` becomes a second copy, and a second copy is what the standard forbids. This spec records the decision, the rule set by name and how each rule is enforced. The rule files stay authoritative. When a rule changes, change its file first and update the matching row here in the same change.

The repository builds two native apps (SwiftUI and Jetpack Compose) on one Rust core. A value can reach a screen by four routes: Rust behavior through a generated bridge, visual tokens through a generator, text and settings through a second generator, and code written in each app. Each route gives a contributor a chance to define the same thing twice.

The forces at play:

- **Two languages downstream of one source.** A rule written once in Swift and once in Kotlin drifts without any build failing.
- **Generated files sit beside code written by hand.** The Swift and Kotlin bindings, both token files and the native string resources are outputs. An edit made there is lost on the next generation, or worse, survives and hides a mismatch.
- **Coding agents are regular contributors.** An agent acts on what it loads. It needs a short entry point and a clear route to the one file that governs the change in front of it.
- **One maintainer.** Every commit so far comes from one author (as of `f62c964`), so there is no second reviewer by default. Anything a machine does not check depends on that one person's attention.
- **The codebase is small.** The foundation ends at one greeting. Rules that cost more than the code they protect would be the wrong trade.

Without a decision, the first product feature would have to guess where shared behavior goes, when a new module is justified and which checks count as done.

## Options considered

Options considered were not documented at decision time. `ADR-0001` records the alternatives for the architecture itself (a shared UI runtime, or the behavior written twice), not for the shape of the rules.

One observation from the repository, stated as fact and not as a recorded alternative: it has no `CODEOWNERS` file, no import boundary lint (a check on which module may import which) inside either app, and no single long contributing guide.

## Decision

**Chosen option**: one owner per responsibility, recorded in an ownership matrix, with topic sized rule files under `docs/`, a short `AGENTS.md` as the entry point, and automated checks only where a machine can give a reliable answer.

Every responsibility has one authoritative owner, every change starts at that owner, and a new capability or a material change to ownership, contract or dependency needs a written decision before code.

## Rationale

The engineer asked for a best reading of the repository in place of an interview. Each point below is inferred from what shipped, and is listed again in Follow-up for confirmation.

- **Small files, one topic each (inferred).** A contributor or agent changing Android packaging loads `android-rules.md` and nothing about tokens. That answers the force of agents acting on what they load.
- **A matrix before any rule (inferred).** With two languages downstream of one source, the first question is always where the thing lives. Putting that in one table makes the answer a lookup, not a judgment.
- **Automate only what a machine can judge (stated in the repository).** `architecture-compliance.md` says the checks can detect drift or a missing document, and cannot decide whether two algorithms mean the same thing, whether a document is accurate, or whether a boundary serves a real use. The validator is kept small for that reason.
- **An exact dependency list, not a deny list (inferred).** The validator compares each Rust crate's direct dependencies to a fixed set of names. Any new Cargo dependency fails until the policy changes in the same change. With one maintainer, that failure is the second reviewer.
- **Real caller first (inferred).** With one greeting in the codebase, every service, adapter or view model added early would be a guess about a future feature. The rule keeps the foundation the size of what it proves.

## Standard definition

**Canonical pattern**:

The path every change follows, as written in `AGENTS.md`:

```text
Before editing   read docs/architecture/ownership-matrix.md
                 find the owner, its public contract, its callers and its tests
                 search both apps and the shared sources for an existing implementation

While editing    shared behavior          -> crates/core
                 a mobile API shape       -> the annotated export in crates/mobile-ffi
                 presentation, OS access  -> the owning app (apps/ios or apps/android)
                 shared visual values     -> design-system/tokens
                 shared copy, settings    -> shared/
                 then regenerate every derived output in the same change

Before handoff   scripts/test.sh
                 the build and device checks for each affected platform
                 for a contract change, both clients
                 report: exact commands, target and toolchain, observed result,
                         and any target not verified
```

A worked example, a change to shared behavior:

```text
1. crates/core/src/lib.rs          change the behavior, test the edge values here
2. crates/mobile-ffi/src/lib.rs    touch the export only if the shape changes
3. scripts/generate-bindings.sh    regenerate Swift and Kotlin in one run
4. apps/ios and apps/android       review both call sites
5. scripts/test.sh                 shared checks
6. scripts/build-ios.sh simulator, then scripts/build-ios.sh test "$SIMULATOR_UDID"
7. scripts/build-android.sh, then scripts/build-android.sh :app:connectedDebugAndroidTest
8. report what compiled and what ran, per platform
```

The rule set. The file named in each row is the owner of the wording.

| # | Rule | Owner file | Enforced by |
| --- | --- | --- | --- |
| R1 | Each responsibility has one authoritative owner. The matrix lists ten. | `docs/architecture/ownership-matrix.md` | Review |
| R2 | Dependencies run one way, `mobile-ffi → foundation-core`. The core has no dependencies, so no UI or UniFFI code. `mobile-ffi` depends on the core and `uniffi` only. | `docs/architecture/dependency-rules.md` | `tooling/validation/check-architecture.py` (exact match on direct dependencies, including optional, target, build and dev) |
| R3 | The two app trees do not import one another. Each depends on its own SDK, the generated bindings, its native theme and its resources. | `docs/architecture/dependency-rules.md` | Review. Separate build systems (Xcode and Gradle) make a cross import hard, not impossible |
| R4 | Shared behavior lives in the core. The export stays thin. A mobile API changes at the Rust export, and both clients stay on the same contract. | `docs/rules/rust-rules.md`, `docs/contracts/ffi-conventions.md` | `cargo test` in `scripts/test.sh` (runs `tests/contracts/greeting.rs`), `scripts/generate-bindings.sh --check`, review |
| R5 | A generated file is never edited by hand. Change its source and regenerate every output in the same change. | `docs/rules/development-rules.md` | `scripts/generate-bindings.sh --check`, `scripts/generate-design-tokens.sh --check` |
| R6 | Shared visual values live in tokens. Shared copy, settings and brand sources live under `shared/`. A generator never reads values back from native output. | `docs/rules/design-system-rules.md`, `docs/rules/shared-resources-rules.md` | `scripts/generate-design-tokens.sh --check` and `--test` catch drift and stale outputs. Which way values flow, and a value copied into native code as a literal, rest on review |
| R7 | Presentation and OS integration belong to the owning app and follow that platform's rules. | `docs/rules/ios-rules.md`, `docs/rules/android-rules.md` | UI tests in CI for the greeting, review for the rest |
| R8 | Real caller first. A service, adapter, view model or capability interface needs an actual caller before it exists. Each change is the smallest slice its real caller can exercise. | `docs/rules/service-rules.md`, `docs/architecture/boundaries.md` | Review |
| R9 | Search before adding. Look in the crates, the canonical inputs and both apps before adding a constant, rule, data shape, translation or asset. | `docs/rules/anti-duplication.md` | Review |
| R10 | A new capability needs a scope row and a spec. A material ownership, contract or dependency decision needs a spec, with the affected architecture documents updated in the same change. | `AGENTS.md`, `docs/rules/development-rules.md` | The validator fails on a Cargo dependency or workspace crate the policy does not list. Native (Gradle and Xcode) dependencies and the record itself rest on review |
| R11 | A handoff reports what compiled and what ran as two separate facts, per platform. | `docs/rules/development-rules.md`, `AGENTS.md` | Review, with CI as a second run |
| R12 | Binaries, signing material, SDK paths and IDE user data stay out of the repository. The compiler and dependencies are pinned and builds use `--locked`. | `docs/rules/development-rules.md`, `docs/rules/rust-rules.md` | `.gitignore` covers build output, SDK paths and IDE user data. It has no pattern for signing material, which rests on review. `rust-toolchain.toml` and `Cargo.lock` pin, and every script passes `--locked` |
| R13 | The governing documents exist and are not empty. | `tooling/validation/check-architecture.py` (two lists: `REQUIRED_DOCS` for `docs/`, and a second list for `AGENTS.md` and the README files) | The validator, run by `scripts/test.sh` and CI |
| R14 | The UniFFI generator feature (`bindgen`) stays on host tooling. Both mobile libraries build with default features. | `docs/architecture/dependency-rules.md`, `docs/rules/rust-rules.md` | Review. The build scripts leave the feature off, and nothing stops a change to that |
| R15 | A library change gets a review of its transitive dependencies (what it pulls in) and its effect on binary size. | `docs/architecture/dependency-rules.md` | Review |
| R16 | A breaking change is a migration. A renamed token role migrates both consumers, an incompatible resource format needs a documented rollout, and a breaking contract is versioned with both apps released together. | `docs/rules/design-system-rules.md`, `docs/rules/shared-resources-rules.md`, `docs/contracts/ffi-conventions.md` | Review |
| R17 | Bridge hygiene. Generated bindings ship with a library built from the same revision. No raw pointer reaches a native view, and nobody maintains C declarations by hand. After a signature change or a UniFFI upgrade, regenerate and run both apps. | `docs/contracts/ffi-conventions.md`, `docs/rules/rust-rules.md` | `scripts/generate-bindings.sh --check` for the binding tree, review for the rest |
| R18 | A service proposal names its single responsibility, the existing module that might own it, its caller and why extraction pays. It documents the owner, public operations and data, permitted dependencies, errors, lifecycle, concurrency, cancellation and tests, and rejects cycles before a crate is added. | `docs/rules/service-rules.md` | Review. Cargo rejects a cycle between crates, and the validator fails on a new workspace crate |
| R19 | A visual change is verified on the affected screen in both appearances (light and dark) and at larger text sizes. | `docs/rules/design-system-rules.md`, `docs/rules/ios-rules.md`, `docs/rules/android-rules.md` | CI runs the greeting in both appearances. Nothing checks large text yet |

When R10 asks for a spec. The triggers are written in four places:

- `ADR-0001`: a capability changes the dependency direction, crosses the native boundary asynchronously, needs clients versioned apart, or adds a shared crate or service.
- `docs/quality/architecture-compliance.md`: a new dependency or a material change to the architecture, together with a policy update in the validator.
- `docs/rules/service-rules.md`: a change that introduces a crate or moves an ownership boundary.
- `docs/architecture/dependency-rules.md`: a new dependency edge, which also needs an owning module, a use case and a test.

Who approves: `architecture-compliance.md` gives reviewers the approval of new services and framework dependencies. Today the only reviewer is the maintainer (inferred, the repository names no one else).

**Replaces**:

- A shared rule or validation written in Swift or Kotlin
- A generated binding, token file or string resource edited by hand
- A crate dependency added without a change to the policy in the validator
- Code in one app tree that imports from the other
- A service, adapter or view model added ahead of its first caller
- A token value or shared string copied into native code as a literal

**Enforcement**:

`scripts/test.sh` runs format, lint and tests (rustfmt, Clippy with warnings denied, `cargo test`), then three policy checks. The `foundation` job in `.github/workflows/foundation.yml` runs the same script:

1. `tooling/validation/check-architecture.py` covers workspace members and their locations, the names of each crate's direct dependencies, the core resolving to its workspace path, and the presence of every required document. It does not compare versions or features, and it sees only workspace members and Cargo.
2. `scripts/generate-bindings.sh --check` regenerates Swift and Kotlin in a temporary directory and compares the whole tree.
3. `scripts/generate-design-tokens.sh --check` validates the canonical data and compares the native outputs. `--test` exercises the failure cases.

The `ios` and `android` jobs build both apps and run the greeting on a simulator and an emulator.

Review only, with no automated check: R1, R3, R8, R9, R11, R14, R15, R16 and R18, plus native (Gradle and Xcode) dependencies, the accuracy of any document, and whether two pieces of code mean the same thing.

Partly checked: R6, R7, R10, R12, R17 and R19. Each row above says which part.

**Rollout**:

In force since the first foundation commit on 2026-11-14. It applies to all code now. Nothing needs migrating.

**Exceptions**:

- A test may state the expected greeting as a literal. Application code displays what the binding returns.
- A derived file may live beside its consumer (for example `apps/ios/DesignSystem/Generated/`).
- The Gradle wrapper JAR is a binary kept in the repository on purpose, as a versioned bootstrap dependency with an upstream checksum.
- An OS specific capability stays in its app until a shared contract and owner can be named.

## Consequences

**Positive**:

- A contributor or agent reaches the governing file in two steps: `AGENTS.md`, then the matrix or one rule file.
- A hand edit to any generated file fails the checks, on a laptop and in CI.
- A new Rust crate or Cargo dependency cannot land quietly. The validator fails until the policy is changed in the same change, which makes the decision visible in the diff.
- The foundation stays the size of what it proves. Nothing exists for a feature that has not arrived.

**Negative / tradeoffs**:

- Nine of the nineteen rules rest on review alone, six more are only partly checked, and there is one reviewer. A duplicate rule in Swift and Kotlin, an import across app trees, or a new Gradle or Xcode dependency would pass every check.
- CI runs on every push, so a direct push to `main` lands before a check can fail. Nothing in the repository requires the checks to pass first.
- The validator sees only Cargo workspace members. A Rust project placed outside the workspace is invisible to it.
- No check reads a document for truth. A stale statement survives until someone notices (see the verification record item in Follow-up).
- The dependency policy and the list of required documents are constants inside the validator. Adding a document or a dependency means editing the script as well.
- Many small files mean many links. Every relative link resolved when this spec was written (as of `f62c964`), and nothing checks that tomorrow.
- "Material" is a judgment call. The written triggers sit in four files, and anything outside them is decided by the reviewer.

**Neutral**:

- The first feature that needs a record, a typed error or an async call across the bridge will trigger R10 and a new spec. That is the standard working as intended.
- A second contributor changes the review assumption. That is the moment to name reviewers per owner.

## Follow-up

- [ ] Confirm or correct the inferred rationale: small files chosen for agent and contributor loading, the matrix as the first lookup, the exact dependency list as a stand in for a second reviewer, real caller first as a guard against speculative layers, and the maintainer as the one who decides what is material.
- [x] R10 sends a new capability to `docs/plans/`, while features are tracked in `docs/scope/`. Already planned as scope row `007 One planning path`. Settled by [0002](0002-one-planning-path.md).
- [x] This spec opens `docs/specs/` beside `docs/decisions/` and `docs/plans/`. `repository-structure.md` and the validator's `REQUIRED_DOCS` name neither `docs/specs/` nor `docs/scope/`. Settle how the three relate inside row `007`. Settled by [0002](0002-one-planning-path.md).
- [ ] `docs/quality/verification.md` says the hosted jobs have not run, while the scope index records a passing run on `6587579`. Already planned as scope row `008`.
- [x] Record keeping that no file settles yet: how ADR and plan files are named and numbered, whether a new ADR joins `REQUIRED_DOCS`, how an ADR is superseded, and whether a spec under `docs/specs/` counts as the record R10 asks for. Settle these inside row `007`. Settled by [0002](0002-one-planning-path.md).
- [ ] R19 asks for larger text sizes and nothing checks them. Already planned as scope row `002` in both the iOS and Android workspaces.
- [ ] Decide whether the checks must pass before a change reaches `main` (a branch rule or a local hook). Today a direct push lands first.
- [ ] R3 has no automated check. A small import scan in `check-architecture.py` becomes worth adding when the first feature brings a module that both apps could reach for.
- [ ] When a second contributor joins, record reviewers per owner (a `CODEOWNERS` file is the usual home) so R1, R8 and R9 no longer rest on one person.
