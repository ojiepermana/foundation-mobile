# Graph Report - mobile  (2026-11-15)

## Corpus Check
- 1 files · ~23,345 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 738 nodes · 1739 edges · 38 communities (37 shown, 1 thin omitted)
- Extraction: 77% EXTRACTED · 23% INFERRED · 0% AMBIGUOUS · INFERRED: 399 edges (avg confidence: 0.88)
- Token cost: 68,674 input · 41,917 output

## Community Hubs (Navigation)
- Swift UniFFI Bindings
- Kotlin FFI Structures and Callbacks
- Greeting Contract, Tests and CI
- Kotlin UniFFI Library Calls
- Native Greeting Screens
- Codegen Tooling and Accessibility
- Shared Resource Schemas
- Kotlin Rust Call Status
- Kotlin RustBuffer Handling
- Verification Record and UI Checks
- Kotlin FFI Converters
- ADR-0001 and Crate Ownership
- Design Token and Resource Rules
- Compliance, Dependency and ADR Rules
- Shared Config and Localization
- Spec 0001 Rule Set and Platform Rules
- Ownership Matrix and Change Path
- Design System Guide
- Token Conventions and Principles
- Spec 0001 Decision and Forces
- Lowest OS and Large Text Checks
- Scope Index and Planning Path
- Architecture Check Script
- iOS Greeting Scope
- Architecture Layer Boundaries
- Native Token Mapping
- Android Greeting Scope
- Kotlin Handle Map
- Review-Only Rules and Anti-Duplication
- Shared Scope and Hosted Results
- iOS Greeting UI Tests
- Generated File Rules
- FFI Extension Conventions
- Android Rust Build Script
- iOS Rust Build Script

## God Nodes (most connected - your core abstractions)
1. `UniffiLib` - 54 edges
2. `Spec 0001: One owner per responsibility, with rules kept beside the code` - 43 edges
3. `UniffiRustCallStatus` - 29 edges
4. `RustBuffer` - 27 edges
5. `Foundation verification 2026-11-14` - 24 edges
6. `Ownership matrix` - 23 edges
7. `Rule set R1-R19 (rule, owner file, enforcement)` - 22 edges
8. `Architecture compliance` - 20 edges
9. `Mobile foundation scope (index)` - 18 edges
10. `Decision: one owner per responsibility in an ownership matrix, topic-sized rule files, short AGENTS.md entry point, automated checks only where a machine is reliable` - 18 edges

## Surprising Connections (you probably didn't know these)
- `Greeting is a pure function; no application services exist` --references--> `hello()`  [INFERRED]
  docs/rules/service-rules.md → crates/core/src/lib.rs
- `iOS linkage and UI check (macOS CI job, XCTest)` --references--> `GreetingUITests`  [INFERRED]
  docs/quality/architecture-compliance.md → apps/ios/UITests/GreetingUITests.swift
- `iOS runtime result (iPhone 17 simulator, iOS 27.0, light and dark)` --references--> `GreetingUITests`  [INFERRED]
  docs/quality/verification.md → apps/ios/UITests/GreetingUITests.swift
- `Tokens, configuration and localization check` --references--> `GenerationTests`  [INFERRED]
  docs/quality/architecture-compliance.md → tooling/codegen/test_generation.py
- `Trace screen, generated binding, FFI export and core function before changing shared behavior` --references--> `GreetingScreen`  [INFERRED]
  docs/rules/development-rules.md → apps/ios/Presentation/GreetingScreen.swift

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Forces that motivate the one-owner-per-responsibility decision** — docs_specs_root_0001_ownership_development_rules_force_two_languages_downstream_of_one_source, docs_specs_root_0001_ownership_development_rules_force_generated_files_beside_handwritten_code, docs_specs_root_0001_ownership_development_rules_force_coding_agents_as_regular_contributors, docs_specs_root_0001_ownership_development_rules_force_one_maintainer, docs_specs_root_0001_ownership_development_rules_force_small_codebase, docs_specs_root_0001_ownership_development_rules_decision_one_owner_per_responsibility [EXTRACTED 1.00]
- **Rules that rest on review alone with no automated check** — docs_specs_root_0001_ownership_development_rules_r1_one_authoritative_owner, docs_specs_root_0001_ownership_development_rules_r3_app_trees_do_not_import_one_another, docs_specs_root_0001_ownership_development_rules_r8_real_caller_first, docs_specs_root_0001_ownership_development_rules_r9_search_before_adding, docs_specs_root_0001_ownership_development_rules_r11_handoff_reports_compiled_and_ran_separately, docs_specs_root_0001_ownership_development_rules_r14_bindgen_feature_host_only, docs_specs_root_0001_ownership_development_rules_r15_library_change_transitive_and_size_review, docs_specs_root_0001_ownership_development_rules_r16_breaking_change_is_a_migration, docs_specs_root_0001_ownership_development_rules_r18_service_proposal_requirements [EXTRACTED 1.00]
- **Machine enforcement chain: test.sh runs the validator and both generator drift checks, mirrored by the CI foundation job** — docs_specs_root_0001_ownership_development_rules_enforcement_test_script_and_three_policy_checks, scripts_test, tooling_validation_check_architecture, scripts_generate_bindings, scripts_generate_design_tokens, github_workflows_foundation_foundation_job [EXTRACTED 1.00]
- **Automated architecture compliance checks** — docs_quality_architecture_compliance_rust_format_and_lint, docs_quality_architecture_compliance_core_and_ffi_contract_tests, docs_quality_architecture_compliance_cargo_dependency_and_governance_check, docs_quality_architecture_compliance_uniffi_generated_files_check, docs_quality_architecture_compliance_tokens_config_localization_check, docs_quality_architecture_compliance_ios_linkage_and_ui_check, docs_quality_architecture_compliance_android_linkage_and_ui_check [EXTRACTED 1.00]
- **Greeting vertical slice: localized recipient through UniFFI to the Rust formatter** — readme_hello_world_greeting, shared_localization_readme_greeting_recipient, docs_architecture_overview_greeting_call_flow, docs_contracts_ffi_conventions_hello_contract, docs_architecture_overview_foundation_core_hello, docs_architecture_ownership_matrix_crates_mobile_ffi, docs_architecture_ownership_matrix_bindings, readme_uniffi [EXTRACTED 1.00]
- **Open (planned) scope items across the three workspaces** — docs_scope_root_007_one_planning_path, docs_scope_root_008_hosted_results_in_the_verification_record, docs_scope_ios_002_lowest_supported_ios_and_large_text, docs_scope_android_002_lowest_supported_android_and_large_text [EXTRACTED 1.00]
- **Canonical source over generated output: edit sources, regenerate, compare snapshots** — agents_never_hand_edit_generated_files, docs_architecture_ownership_matrix_derived_file_rule, docs_architecture_dependency_rules_one_way_generation, docs_decisions_adr_0001_foundation_checked_in_source_snapshots [INFERRED 0.85]
- **Design token pipeline from canonical JSON to native projections** — docs_design_system_token_conventions_canonical_token_sources, design_system_schemas_tokens_schema, scripts_generate_design_tokens, docs_design_system_platform_mapping_swiftui_token_projection, docs_design_system_platform_mapping_compose_token_projection, docs_quality_architecture_compliance_tokens_config_localization_check [INFERRED 0.85]
- **Neutral JSON sources validated and generated into native theme and string resources** — design_system_readme_token_files, design_system_readme_tokens_schema, shared_config_readme_foundation_json, shared_localization_readme_catalog_format, design_system_readme_generate_design_tokens_modes, tooling_codegen_requirements_fastjsonschema, design_system_readme_generated_semantic_api, shared_localization_readme_generated_native_strings [INFERRED 0.85]
- **Regenerate derived outputs with their canonical source, never hand-edit** — docs_rules_development_rules_regenerate_derived_files, docs_rules_design_system_rules_regenerate_projections, docs_quality_architecture_compliance_generated_drift_remediation, docs_rules_rust_rules_regenerate_after_signature_change, docs_rules_shared_resources_rules_generated_native_strings, docs_rules_anti_duplication_ffi_shapes_in_rust_export [INFERRED 0.85]
- **Tracer bullet greeting path from shared core to both native screens** — docs_scope_index_tracer_bullet_build_approach, docs_scope_root_002_shared_greeting_contract, docs_scope_root_002_shared_greeting_contract_one_string_in_one_string_out_contract, docs_scope_ios_001_native_ios_greeting, docs_scope_android_001_native_android_greeting, docs_scope_root_006_hosted_build_verification [INFERRED 0.85]
- **Verification evidence chain: local checks, hosted jobs and the verification record** — docs_scope_root_005_reproducible_local_builds_and_checks, docs_scope_root_006_hosted_build_verification, docs_scope_root_008_hosted_results_in_the_verification_record, docs_scope_index_hosted_run_43593365100, docs_scope_root_005_reproducible_local_builds_and_checks_stale_local_verification_record, docs_scope_root_008_hosted_results_in_the_verification_record_single_list_of_unverified_targets [INFERRED 0.85]

## Communities (38 total, 1 thin omitted)

### Community 0 - "Swift UniFFI Bindings"
Cohesion: 0.05
Nodes (64): Array, createReader(), createWriter(), Data, FfiConverter, FfiConverterPrimitive, FfiConverterRustBuffer, FfiConverterString (+56 more)

### Community 1 - "Kotlin FFI Structures and Callbacks"
Cohesion: 0.05
Nodes (38): Disposable, IntegrityCheckingUniffiLib, NoHandle, UniffiByValue, UniffiCallbackInterfaceClone, UniffiCallbackInterfaceFree, uniffiCheckApiChecksums(), uniffiCheckContractApiVersion() (+30 more)

### Community 2 - "Greeting Contract, Tests and CI"
Cohesion: 0.07
Nodes (48): hello(), preserves_empty_names_and_whitespace(), String, main(), hello(), String, target/, build/ and Gradle build directories excluded from source control, Mobile contract (FFI conventions) (+40 more)

### Community 4 - "Native Greeting Screens"
Cohesion: 0.06
Nodes (31): App, MainActivity, FoundationTheme(), gradlew script, die(), warn(), GreetingScreen(), MobileFoundationApp (+23 more)

### Community 5 - "Codegen Tooling and Accessibility"
Cohesion: 0.08
Nodes (26): Accessibility (design system), Status conveyed by text or semantics, not color alone, Honor platform reduced-motion setting, Text contrast check (4.5:1 minimum), W3C WCAG 2.2 contrast minimum guidance, Design system and resources result (seven generator tests), check_schema(), generate() (+18 more)

### Community 6 - "Shared Resource Schemas"
Cohesion: 0.08
Nodes (24): Draft 7 schemas in shared/specifications, defaultLocale, greeting_recipient, schemaVersion, additionalProperties, const, properties, defaultLocale (+16 more)

### Community 7 - "Kotlin Rust Call Status"
Cohesion: 0.12
Nodes (7): E, uniffiCheckCallStatus(), uniffiRustCall(), UniffiRustCallStatus, UniffiRustCallStatusErrorHandler, uniffiRustCallWithError(), U

### Community 8 - "Kotlin RustBuffer Handling"
Cohesion: 0.15
Nodes (9): ByReference, ByValue, ForeignBytes, `hello`(), RustBuffer, uniffiTraitInterfaceCall(), uniffiTraitInterfaceCallWithError(), kotlin (+1 more)

### Community 9 - "Verification Record and UI Checks"
Cohesion: 0.15
Nodes (19): GreetingTest, Android linkage and UI check (Linux CI job, emulator instrumentation), GitHub Actions CI jobs (macOS and Linux), iOS linkage and UI check (macOS CI job, XCTest), Physical hardware verification for simulator-inaccessible capabilities, Foundation verification 2026-11-14, Android compilation result (Gradle 9.3.1, AGP 9.1.0, Temurin 17), Android packaging 16 KiB alignment result (+11 more)

### Community 10 - "Kotlin FFI Converters"
Cohesion: 0.21
Nodes (7): FfiConverter, FfiConverterRustBuffer, FfiConverterString, FfiType, ByteBuffer, KotlinType, ULong

### Community 11 - "ADR-0001 and Crate Ownership"
Cohesion: 0.22
Nodes (19): Workspace edge: mobile-ffi depends on foundation-core (std-only core), Proc-macro exports define the cross-language API; bindgen feature gates host CLI deps, Architecture overview, foundation_core::hello (sole greeting formatter), Greeting call flow: SwiftUI/Compose -> generated binding -> C ABI/JNA -> mobile-ffi -> foundation-core, Color selection, font scaling, layout and accessibility run natively (no shared renderer), bindings/swift and bindings/kotlin: generated FFI source snapshots, crates/core: owner of shared behavior, domain rules and application validation (+11 more)

### Community 12 - "Design Token and Resource Rules"
Cohesion: 0.19
Nodes (19): Stable role names or same-change migration, Generated drift remediation, Tokens, configuration and localization check, Shared visual decisions and translations are generator inputs, Design system rules, Drift check plus verification in both appearances and larger text sizes, Regenerate native projections in the same change, Public role name changes require migrating both consumers (+11 more)

### Community 13 - "Compliance, Dependency and ADR Rules"
Cohesion: 0.19
Nodes (19): Dependency rules, New dependency edge needs an owning module, a use case and a test, Revisit conditions: dependency direction change, async native boundary, independently versioned clients, new shared crate or service, Capabilities outside the baseline (auth, ERP, transport, storage, sync, flags, desktop ports), Extension procedure: PRD plus short implementation plan with owner, contract, dependency direction and verification matrix, Architecture compliance, ADR and policy update for new dependency or material architecture change, Limits of CI checks (+11 more)

### Community 14 - "Shared Config and Localization"
Cohesion: 0.21
Nodes (17): Build-time generation: token JSON and locale JSON -> native theme inputs and localization resources, shared/config, shared/localization, shared/assets: owner of public settings, locale content and brand masters, Decision: neutral JSON tokens and validated shared sources generate native theme inputs and localization, Deferred: a second language end to end, 004 - Shared settings, text and brand assets (existing), Greeting sentence 'Hello, {name}!' formed in English by the core, Single English localization catalog and public fallback locale, Configuration guide (+9 more)

### Community 15 - "Spec 0001 Rule Set and Platform Rules"
Cohesion: 0.19
Nodes (17): Agent workflow: during implementation (place change in owning layer), Android rules, Compose presentation with native Material semantics, OS-specific capability stays in its own app, iOS rules, Native permissions, UIKit delegates and device lifecycle stay in the Apple adapter, SwiftUI presentation with Dynamic Type and adaptive appearance, Service and module rules (+9 more)

### Community 16 - "Ownership Matrix and Change Path"
Cohesion: 0.24
Nodes (15): AGENTS.md: Working in the mobile foundation, Agent workflow: before editing (locate owner, contract, callers, tests), Agent workflow: before handoff (run checks, report commands and unverified targets), App trees do not import one another; core never calls platform UI, Ownership matrix, apps/android: owner of Android UI, presentation state and OS APIs, apps/ios: owner of Apple UI, presentation state and OS APIs, docs/ and root AGENTS.md: architecture, ADRs and agent workflow (+7 more)

### Community 17 - "Design System Guide"
Cohesion: 0.20
Nodes (15): Design system guide, generate-design-tokens.sh modes: write, --check (drift), --test (failure cases), Generated semantic token API consumed by native apps, Five canonical token JSON files (primitives and semantic aliases), tokens.schema.json: single Draft 7 document keyed by filename stem, Layer: resources and tooling (build-host validation and generation), design-system/tokens and schemas: owner of canonical visual values and semantic roles, scripts/ and .github/workflows/: build and verification orchestration (+7 more)

### Community 18 - "Token Conventions and Principles"
Cohesion: 0.20
Nodes (15): Canonical token schema (tokens.schema.json), Per-target reading order and screen-reader review, Native controls styled with semantic tokens, Design principles, Canonical JSON propagates through code generation, Design definitions compile independently of Cargo and UniFFI, Layout, text measurement, gestures and focus stay in presentation, Semantic names for decisions both apps share (+7 more)

### Community 19 - "Spec 0001 Decision and Forces"
Cohesion: 0.30
Nodes (15): Spec 0001: One owner per responsibility, with rules kept beside the code, Decision: one owner per responsibility in an ownership matrix, topic-sized rule files, short AGENTS.md entry point, automated checks only where a machine is reliable, An exact dependency list, not a deny list, Follow-up: decide whether checks must pass before a change reaches main (branch rule or local hook), Follow-up: confirm or correct the inferred rationale, Force: coding agents are regular contributors and act on what they load, Force: generated files sit beside hand-written code (edits there are lost or hide a mismatch), Force: one maintainer, so no second reviewer by default (+7 more)

### Community 20 - "Lowest OS and Large Text Checks"
Cohesion: 0.24
Nodes (11): CoreImage, Android 002 - Lowest supported Android and large text (planned), Declared Android minimum API 24 not yet exercised, Android largest font scale check, iOS simulator results (iPhone 17 on iOS 27.0 local, iOS 26.5 hosted), iOS 002 - Lowest supported iOS and large text (planned), Declared iOS 17 deployment target not yet exercised, iOS largest accessibility text size check (+3 more)

### Community 21 - "Scope Index and Planning Path"
Cohesion: 0.25
Nodes (14): Single greeting as the minimal exercise of interop, linking, resources and display, Planning the next capability, Deliver one exercisable vertical slice at a time and record observed results, Android scope, Android app owns its screen, appearance changes and native localization lookup, Mobile foundation scope (index), Beta workflow (/check verify, then /test), Scope status legend and file numbering convention (+6 more)

### Community 22 - "Architecture Check Script"
Cohesion: 0.24
Nodes (12): Cargo dependency and governance check, Architecture policy result (dependency and required-document checks), Required document check should cover the scope index, Follow-up: a small import scan in check-architecture.py for R3, Follow-up: docs/specs and docs/scope are named by neither repository-structure.md nor REQUIRED_DOCS, R13: the governing documents exist and are not empty (REQUIRED_DOCS), R2: dependencies run one way, mobile-ffi -> foundation-core; core has no dependencies, R3: the two app trees do not import one another (+4 more)

### Community 23 - "iOS Greeting Scope"
Cohesion: 0.24
Nodes (9): Android physical device coverage unverified, Deferred: signing, physical device runs and store delivery, Deferred work beyond Hello World, iOS 001 - Native iOS greeting (existing), Native text style supporting Dynamic Type, Greeting exposed to accessibility in light and dark appearance, iOS physical device coverage unverified, Unsigned iOS device build linked successfully (+1 more)

### Community 24 - "Architecture Layer Boundaries"
Cohesion: 0.27
Nodes (11): Architecture boundaries, Documented capability boundary; adapters need an actual caller, Layer: design system (generated Swift/Kotlin values as shared visual vocabulary), Layer: native platform integration (Swift owns Apple services, Kotlin owns Android services), Layer: native presentation (views render, adapt to appearance, handle events), Layer: shared Rust (core owns behavior, FFI crate maps exports), Create a platform adapter directory only when a feature needs an OS capability, Smallest slice exercisable through its real caller (+3 more)

### Community 25 - "Native Token Mapping"
Cohesion: 0.35
Nodes (11): System text scaling via generated text styles, Native token mapping, Compose sp mapping of logical text units, Jetpack Compose token projection (FoundationTokens), Dynamic Type mapping of headline and reading scales, Logical spacing units adapt to display density, spacingPage role, SwiftUI token projection (FoundationTokens) (+3 more)

### Community 26 - "Android Greeting Scope"
Cohesion: 0.24
Nodes (8): FoundationTokens, Palette, Android 001 - Native Android greeting (existing), API 36 emulator results (arm64 local, x86_64 hosted) in light and dark, Android app packages both supported CPU architectures, 16 KiB memory page packaging, Hosted run 43593365100 on commit 6587579 (all three jobs passed), Three hosted jobs (foundation, iOS, Android) on the same revision

### Community 27 - "Kotlin Handle Map"
Cohesion: 0.42
Nodes (4): InternalException, T, UniffiHandleMap, UniffiNullRustCallStatusErrorHandler

### Community 28 - "Review-Only Rules and Anti-Duplication"
Cohesion: 0.39
Nodes (8): Anti-duplication rules, Locate the owner before adding a constant, rule, DTO, translation or asset, Reviewers assess semantic duplication, Follow-up: record reviewers per owner (CODEOWNERS) when a second contributor joins, R1: each responsibility has one authoritative owner (the matrix lists ten), R9: search before adding a constant, rule, data shape, translation or asset, Review-only rules with no automated check (R1, R3, R8, R9, R11, R14, R15, R16, R18), Premise: rule files stay authoritative; the spec records the decision, rule set and enforcement, not a second copy

### Community 29 - "Shared Scope and Hosted Results"
Cohesion: 0.46
Nodes (8): 005 - Reproducible local builds and checks (existing), Local verification record predates the hosted run, 006 - Hosted build verification (done), Android hosted job installs the supported SDK packages, 008 - Hosted results in the verification record (planned), Verification record with one list of unverified targets, Shared foundation scope, Follow-up: verification.md says hosted jobs have not run while the scope index records a passing run

### Community 30 - "iOS Greeting UI Tests"
Cohesion: 0.38
Nodes (5): GreetingUITests, UInt8, CIContext, XCTestCase, XCUIScreenshot

### Community 31 - "Generated File Rules"
Cohesion: 0.40
Nodes (6): Never hand-edit generated files, Generators consume neutral sources and never recover canonical values from native output, Derived file rule: change the canonical input and regenerate every output in the same review, Decision: keep generated source snapshots in version control and compare against fresh regeneration, Drift detection for checked-in bindings and resources, R5: a generated file is never edited by hand; change the source and regenerate every output

### Community 32 - "FFI Extension Conventions"
Cohesion: 0.33
Nodes (6): Explicit application records and enums; private core/transport shapes mapped at the adapter, Async and cancellation conventions for future exports, Compatibility: version breaking contracts and coordinate regeneration, both apps and release, Conventions for extending the mobile contract, Native capability callback interfaces limited to operations the core requires, Typed UniFFI errors with stable variants; user-facing messages translated natively

### Community 33 - "Android Rust Build Script"
Cohesion: 0.40
Nodes (4): CARGO_TARGET_AARCH64_LINUX_ANDROID_LINKER, CARGO_TARGET_X86_64_LINUX_ANDROID_LINKER, PATH, build-android-rust.sh script

### Community 34 - "iOS Rust Build Script"
Cohesion: 0.50
Nodes (3): CARGO_TARGET_DIR, PATH, build-ios-rust.sh script

## Knowledge Gaps
- **53 isolated node(s):** `NoHandle`, `UniffiWithHandle`, `apiChecksumMismatch`, `contractVersionMismatch`, `ok` (+48 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `.body` connect `Native Greeting Screens` to `Swift UniFFI Bindings`?**
  _High betweenness centrality (0.145) - this node is a cross-community bridge._
- **Why does `hello()` connect `Swift UniFFI Bindings` to `Native Greeting Screens`?**
  _High betweenness centrality (0.143) - this node is a cross-community bridge._
- **Why does `GreetingScreen` connect `Native Greeting Screens` to `Greeting Contract, Tests and CI`, `Spec 0001 Rule Set and Platform Rules`, `iOS Greeting Scope`?**
  _High betweenness centrality (0.139) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Foundation verification 2026-11-14` (e.g. with `Deliver one exercisable vertical slice at a time and record observed results` and `Record separately what compiled and what ran`) actually correct?**
  _`Foundation verification 2026-11-14` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `NoHandle`, `UniffiWithHandle`, `apiChecksumMismatch` to the rest of the system?**
  _53 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Swift UniFFI Bindings` be split into smaller, more focused modules?**
  _Cohesion score 0.05444596443228454 - nodes in this community are weakly interconnected._
- **Should `Kotlin FFI Structures and Callbacks` be split into smaller, more focused modules?**
  _Cohesion score 0.050078247261345854 - nodes in this community are weakly interconnected._