# Graph Report - mobile  (2026-11-15)

## Corpus Check
- 1 files · ~23,378 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 740 nodes · 1744 edges · 44 communities (36 shown, 8 thin omitted)
- Extraction: 77% EXTRACTED · 23% INFERRED · 0% AMBIGUOUS · INFERRED: 403 edges (avg confidence: 0.87)
- Token cost: 58,411 input · 4,129 output

## Community Hubs (Navigation)
- Swift UniFFI Bindings
- Ownership Matrix and Boundaries
- Design System and Token Mapping
- Rust Rules, FFI Contract and Agent Workflow
- Kotlin UniFFI Library Calls
- Codegen Tooling and Accessibility
- Verification Record and UI Checks
- Kotlin RustBuffer Handling
- Native Greeting Screens
- Kotlin Rust Call Status
- Scope Index and Planning Path
- Spec 0001 Rule Set and Service Rules
- Design Token and Resource Rules
- Spec 0001 Decision and Forces
- Kotlin FFI Converters
- Kotlin Callback Interfaces
- Lowest OS and Large Text Checks
- Kotlin FFI Structures
- Shared Resource Schemas
- Architecture Compliance and Test Script
- Core Greeting Contract and Tests
- ADR-0001 and Dependency Rules
- Platform Rules and Implementation Workflow
- Architecture Check Script
- Development Rules and Generated Files
- Localization Schema
- iOS Greeting Scope
- Kotlin Bindings Runtime Helpers
- Kotlin Handle Map
- iOS Greeting UI Tests
- Hosted CI Verification
- Kotlin Contract Integrity Checks
- Android Rust Build Script
- Kotlin Future F32 Callbacks
- Kotlin Future I16 Callbacks
- Kotlin Future I64 Callbacks
- Kotlin Future RustBuffer Callbacks
- Kotlin Future U16 Callbacks
- Kotlin Future U32 Callbacks
- Kotlin Future U64 Callbacks
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
- `iOS linkage and UI check (macOS CI job, XCTest)` --references--> `GreetingUITests`  [INFERRED]
  docs/quality/architecture-compliance.md → apps/ios/UITests/GreetingUITests.swift
- `iOS runtime result (iPhone 17 simulator, iOS 27.0, light and dark)` --references--> `GreetingUITests`  [INFERRED]
  docs/quality/verification.md → apps/ios/UITests/GreetingUITests.swift
- `SwiftUI presentation with Dynamic Type and adaptive appearance` --references--> `GreetingScreen`  [INFERRED]
  docs/rules/ios-rules.md → apps/ios/Presentation/GreetingScreen.swift
- `Tokens, configuration and localization check` --references--> `GenerationTests`  [INFERRED]
  docs/quality/architecture-compliance.md → tooling/codegen/test_generation.py
- `Compose presentation with native Material semantics` --references--> `GreetingScreen()`  [INFERRED]
  docs/rules/android-rules.md → apps/android/presentation/src/main/kotlin/foundation/presentation/GreetingScreen.kt

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Agent change workflow: before editing, during implementation, before handoff, before commit** — agents_before_editing, agents_during_implementation, agents_before_handoff, agents_before_commit [EXTRACTED 1.00]
- **Derived outputs are regenerated from their source, never hand-edited** — agents_never_hand_edit_generated_files, agents_knowledge_graph, docs_architecture_ownership_matrix_derived_file_rule, docs_architecture_dependency_rules_one_way_generation [INFERRED 0.75]
- **Automated architecture compliance checks** — docs_quality_architecture_compliance_rust_format_and_lint, docs_quality_architecture_compliance_core_and_ffi_contract_tests, docs_quality_architecture_compliance_cargo_dependency_and_governance_check, docs_quality_architecture_compliance_uniffi_generated_files_check, docs_quality_architecture_compliance_tokens_config_localization_check, docs_quality_architecture_compliance_ios_linkage_and_ui_check, docs_quality_architecture_compliance_android_linkage_and_ui_check [EXTRACTED 1.00]
- **Greeting vertical slice: localized recipient through UniFFI to the Rust formatter** — readme_hello_world_greeting, shared_localization_readme_greeting_recipient, docs_architecture_overview_greeting_call_flow, docs_contracts_ffi_conventions_hello_contract, docs_architecture_overview_foundation_core_hello, docs_architecture_ownership_matrix_crates_mobile_ffi, docs_architecture_ownership_matrix_bindings, readme_uniffi [EXTRACTED 1.00]
- **Open (planned) scope items across the three workspaces** — docs_scope_root_007_one_planning_path, docs_scope_root_008_hosted_results_in_the_verification_record, docs_scope_ios_002_lowest_supported_ios_and_large_text, docs_scope_android_002_lowest_supported_android_and_large_text [EXTRACTED 1.00]
- **Forces that motivate the one-owner-per-responsibility decision** — docs_specs_root_0001_ownership_development_rules_force_two_languages_downstream_of_one_source, docs_specs_root_0001_ownership_development_rules_force_generated_files_beside_handwritten_code, docs_specs_root_0001_ownership_development_rules_force_coding_agents_as_regular_contributors, docs_specs_root_0001_ownership_development_rules_force_one_maintainer, docs_specs_root_0001_ownership_development_rules_force_small_codebase, docs_specs_root_0001_ownership_development_rules_decision_one_owner_per_responsibility [EXTRACTED 1.00]
- **Machine enforcement chain: test.sh runs the validator and both generator drift checks, mirrored by the CI foundation job** — docs_specs_root_0001_ownership_development_rules_enforcement_test_script_and_three_policy_checks, scripts_test, tooling_validation_check_architecture, scripts_generate_bindings, scripts_generate_design_tokens, github_workflows_foundation_foundation_job [EXTRACTED 1.00]
- **Rules that rest on review alone with no automated check** — docs_specs_root_0001_ownership_development_rules_r1_one_authoritative_owner, docs_specs_root_0001_ownership_development_rules_r3_app_trees_do_not_import_one_another, docs_specs_root_0001_ownership_development_rules_r8_real_caller_first, docs_specs_root_0001_ownership_development_rules_r9_search_before_adding, docs_specs_root_0001_ownership_development_rules_r11_handoff_reports_compiled_and_ran_separately, docs_specs_root_0001_ownership_development_rules_r14_bindgen_feature_host_only, docs_specs_root_0001_ownership_development_rules_r15_library_change_transitive_and_size_review, docs_specs_root_0001_ownership_development_rules_r16_breaking_change_is_a_migration, docs_specs_root_0001_ownership_development_rules_r18_service_proposal_requirements [EXTRACTED 1.00]
- **Canonical source over generated output: edit sources, regenerate, compare snapshots** — agents_never_hand_edit_generated_files, docs_architecture_ownership_matrix_derived_file_rule, docs_architecture_dependency_rules_one_way_generation, docs_decisions_adr_0001_foundation_checked_in_source_snapshots [INFERRED 0.85]
- **Design token pipeline from canonical JSON to native projections** — docs_design_system_token_conventions_canonical_token_sources, design_system_schemas_tokens_schema, scripts_generate_design_tokens, docs_design_system_platform_mapping_swiftui_token_projection, docs_design_system_platform_mapping_compose_token_projection, docs_quality_architecture_compliance_tokens_config_localization_check [INFERRED 0.85]
- **Neutral JSON sources validated and generated into native theme and string resources** — design_system_readme_token_files, design_system_readme_tokens_schema, shared_config_readme_foundation_json, shared_localization_readme_catalog_format, design_system_readme_generate_design_tokens_modes, tooling_codegen_requirements_fastjsonschema, design_system_readme_generated_semantic_api, shared_localization_readme_generated_native_strings [INFERRED 0.85]
- **Regenerate derived outputs with their canonical source, never hand-edit** — docs_rules_development_rules_regenerate_derived_files, docs_rules_design_system_rules_regenerate_projections, docs_quality_architecture_compliance_generated_drift_remediation, docs_rules_rust_rules_regenerate_after_signature_change, docs_rules_shared_resources_rules_generated_native_strings, docs_rules_anti_duplication_ffi_shapes_in_rust_export [INFERRED 0.85]
- **Tracer bullet greeting path from shared core to both native screens** — docs_scope_index_tracer_bullet_build_approach, docs_scope_root_002_shared_greeting_contract, docs_scope_root_002_shared_greeting_contract_one_string_in_one_string_out_contract, docs_scope_ios_001_native_ios_greeting, docs_scope_android_001_native_android_greeting, docs_scope_root_006_hosted_build_verification [INFERRED 0.85]
- **Verification evidence chain: local checks, hosted jobs and the verification record** — docs_scope_root_005_reproducible_local_builds_and_checks, docs_scope_root_006_hosted_build_verification, docs_scope_root_008_hosted_results_in_the_verification_record, docs_scope_index_hosted_run_43593365100, docs_scope_root_005_reproducible_local_builds_and_checks_stale_local_verification_record, docs_scope_root_008_hosted_results_in_the_verification_record_single_list_of_unverified_targets [INFERRED 0.85]

## Communities (44 total, 8 thin omitted)

### Community 0 - "Swift UniFFI Bindings"
Cohesion: 0.05
Nodes (64): Array, createReader(), createWriter(), Data, FfiConverter, FfiConverterPrimitive, FfiConverterRustBuffer, FfiConverterString (+56 more)

### Community 1 - "Ownership Matrix and Boundaries"
Cohesion: 0.08
Nodes (53): Architecture boundaries, Documented capability boundary; adapters need an actual caller, Layer: design system (generated Swift/Kotlin values as shared visual vocabulary), Layer: native platform integration (Swift owns Apple services, Kotlin owns Android services), Layer: native presentation (views render, adapt to appearance, handle events), Layer: resources and tooling (build-host validation and generation), Layer: shared Rust (core owns behavior, FFI crate maps exports), App trees do not import one another; core never calls platform UI (+45 more)

### Community 2 - "Design System and Token Mapping"
Cohesion: 0.07
Nodes (44): FoundationTokens, Palette, FoundationTokens, Palette, CGFloat, Color, ColorScheme, Design system guide (+36 more)

### Community 3 - "Rust Rules, FFI Contract and Agent Workflow"
Cohesion: 0.08
Nodes (38): Agent workflow: before commit (run /graphify . --update, stage graphify-out with the change), Agent workflow: before handoff (run checks, report commands and unverified targets), Knowledge graph (graphify-out/, kept current with /graphify . --update), gradlew script, die(), warn(), main(), hello() (+30 more)

### Community 5 - "Codegen Tooling and Accessibility"
Cohesion: 0.08
Nodes (26): Accessibility (design system), Status conveyed by text or semantics, not color alone, Honor platform reduced-motion setting, Text contrast check (4.5:1 minimum), W3C WCAG 2.2 contrast minimum guidance, Design system and resources result (seven generator tests), check_schema(), generate() (+18 more)

### Community 6 - "Verification Record and UI Checks"
Cohesion: 0.13
Nodes (25): GreetingTest, Deliver one exercisable vertical slice at a time and record observed results, Android linkage and UI check (Linux CI job, emulator instrumentation), GitHub Actions CI jobs (macOS and Linux), iOS linkage and UI check (macOS CI job, XCTest), Physical hardware verification for simulator-inaccessible capabilities, Foundation verification 2026-11-14, Android compilation result (Gradle 9.3.1, AGP 9.1.0, Temurin 17) (+17 more)

### Community 7 - "Kotlin RustBuffer Handling"
Cohesion: 0.14
Nodes (7): ByReference, ByValue, `hello`(), RustBuffer, uniffiTraitInterfaceCall(), uniffiTraitInterfaceCallWithError(), kotlin

### Community 8 - "Native Greeting Screens"
Cohesion: 0.11
Nodes (19): App, MainActivity, FoundationTheme(), GreetingScreen(), MobileFoundationApp, .body, GreetingScreen, .body (+11 more)

### Community 9 - "Kotlin Rust Call Status"
Cohesion: 0.13
Nodes (7): E, uniffiCheckCallStatus(), uniffiRustCall(), UniffiRustCallStatus, UniffiRustCallStatusErrorHandler, uniffiRustCallWithError(), U

### Community 10 - "Scope Index and Planning Path"
Cohesion: 0.19
Nodes (21): Planning the next capability, Android scope, Android app owns its screen, appearance changes and native localization lookup, Mobile foundation scope (index), Beta workflow (/check verify, then /test), Deferred: a contract beyond one string (record, typed error, async call), Deferred work beyond Hello World, Scope status legend and file numbering convention (+13 more)

### Community 11 - "Spec 0001 Rule Set and Service Rules"
Cohesion: 0.16
Nodes (22): Anti-duplication rules, Locate the owner before adding a constant, rule, DTO, translation or asset, OS-specific capability stays in its own app, Reviewers assess semantic duplication, Native permissions, UIKit delegates and device lifecycle stay in the Apple adapter, Introduce presentation state or a ViewModel only when needed, Service and module rules, Keep a capability beside its first caller (+14 more)

### Community 12 - "Design Token and Resource Rules"
Cohesion: 0.20
Nodes (19): Stable role names or same-change migration, Generated drift remediation, Tokens, configuration and localization check, Shared visual decisions and translations are generator inputs, Design system rules, Drift check plus verification in both appearances and larger text sizes, Regenerate native projections in the same change, Public role name changes require migrating both consumers (+11 more)

### Community 13 - "Spec 0001 Decision and Forces"
Cohesion: 0.24
Nodes (18): AGENTS.md: Working in the mobile foundation, 001 - Ownership and development rules (existing), One owner per shared responsibility, Spec 0001: One owner per responsibility, with rules kept beside the code, Decision: one owner per responsibility in an ownership matrix, topic-sized rule files, short AGENTS.md entry point, automated checks only where a machine is reliable, Follow-up: decide whether checks must pass before a change reaches main (branch rule or local hook), Follow-up: confirm or correct the inferred rationale, Follow-up: unsettled record keeping (ADR and plan naming, REQUIRED_DOCS membership, superseding, whether a spec satisfies R10) (+10 more)

### Community 14 - "Kotlin FFI Converters"
Cohesion: 0.22
Nodes (7): FfiConverter, FfiConverterRustBuffer, FfiConverterString, FfiType, ByteBuffer, KotlinType, ULong

### Community 15 - "Kotlin Callback Interfaces"
Cohesion: 0.12
Nodes (9): UniffiCallbackInterfaceClone, UniffiCallbackInterfaceFree, UniffiForeignFutureCompleteF64, UniffiForeignFutureCompleteI32, UniffiForeignFutureCompleteI8, UniffiForeignFutureCompleteU8, UniffiForeignFutureCompleteVoid, UniffiForeignFutureDroppedCallback (+1 more)

### Community 16 - "Lowest OS and Large Text Checks"
Cohesion: 0.22
Nodes (13): CoreImage, Android 001 - Native Android greeting (existing), API 36 emulator results (arm64 local, x86_64 hosted) in light and dark, Android app packages both supported CPU architectures, Android 002 - Lowest supported Android and large text (planned), 16 KiB memory page packaging, Declared Android minimum API 24 not yet exercised, Android largest font scale check (+5 more)

### Community 17 - "Kotlin FFI Structures"
Cohesion: 0.21
Nodes (8): UniffiByValue, UniffiForeignFutureDroppedCallbackStruct, UniffiForeignFutureResultF64, UniffiForeignFutureResultI32, UniffiForeignFutureResultI8, UniffiForeignFutureResultU8, UniffiForeignFutureResultVoid, Structure

### Community 18 - "Shared Resource Schemas"
Cohesion: 0.14
Nodes (13): defaultLocale, schemaVersion, additionalProperties, const, properties, defaultLocale, schemaVersion, required (+5 more)

### Community 19 - "Architecture Compliance and Test Script"
Cohesion: 0.24
Nodes (12): Agent workflow: before editing (locate owner, contract, callers, tests), Architecture compliance, Limits of CI checks, Reviewers trace changed behavior from owner into each client, Rust format and lint check (rustfmt, Clippy warnings denied), Rust workspace result (Rust 1.100.0, locked build, three tests passed), Pinned compiler and locked dependencies (--locked), Automate only what a machine can judge (+4 more)

### Community 20 - "Core Greeting Contract and Tests"
Cohesion: 0.22
Nodes (11): hello(), preserves_empty_names_and_whitespace(), String, Core and FFI contract tests (locked Cargo tests), Greeting accepts the caller's complete Unicode string, Greeting is a pure function; no application services exist, Deferred: a second language end to end, 004 - Shared settings, text and brand assets (existing) (+3 more)

### Community 21 - "ADR-0001 and Dependency Rules"
Cohesion: 0.27
Nodes (13): Dependency rules, New dependency edge needs an owning module, a use case and a test, Generators consume neutral sources and never recover canonical values from native output, ADR 0001: Native apps with a shared Rust core, Decision: keep generated source snapshots in version control and compare against fresh regeneration, Rejected alternative: implementing application behavior independently in both apps, Rejected alternative: shared UI runtime, Revisit conditions: dependency direction change, async native boundary, independently versioned clients, new shared crate or service (+5 more)

### Community 22 - "Platform Rules and Implementation Workflow"
Cohesion: 0.27
Nodes (12): Agent workflow: during implementation (place change in owning layer), Single greeting as the minimal exercise of interop, linking, resources and display, Android rules, Compose presentation with native Material semantics, iOS rules, SwiftUI presentation with Dynamic Type and adaptive appearance, Force: the codebase is small (the foundation ends at one greeting), Partly checked rules (R6, R7, R10, R12, R17, R19) (+4 more)

### Community 23 - "Architecture Check Script"
Cohesion: 0.32
Nodes (10): Cargo dependency and governance check, Architecture policy result (dependency and required-document checks), Required document check should cover the scope index, An exact dependency list, not a deny list, Follow-up: docs/specs and docs/scope are named by neither repository-structure.md nor REQUIRED_DOCS, R13: the governing documents exist and are not empty (REQUIRED_DOCS), R2: dependencies run one way, mobile-ffi -> foundation-core; core has no dependencies, Tradeoff: the validator sees only Cargo workspace members; policy and required documents are constants inside the script (+2 more)

### Community 24 - "Development Rules and Generated Files"
Cohesion: 0.22
Nodes (11): Never hand-edit generated files, Derived file rule: change the canonical input and regenerate every output in the same review, ADR and policy update for new dependency or material architecture change, Development rules, Plan for a new capability, ADR for a material architectural trade-off, Smallest slice exercisable through its real caller, ADR when introducing a crate or changing an ownership boundary, Drift detection for checked-in bindings and resources (+3 more)

### Community 25 - "Localization Schema"
Cohesion: 0.18
Nodes (10): greeting_recipient, additionalProperties, minLength, type, propertyNames, pattern, required, $schema (+2 more)

### Community 26 - "iOS Greeting Scope"
Cohesion: 0.27
Nodes (8): Android physical device coverage unverified, Deferred: signing, physical device runs and store delivery, iOS 001 - Native iOS greeting (existing), Native text style supporting Dynamic Type, Greeting exposed to accessibility in light and dark appearance, iOS physical device coverage unverified, Unsigned iOS device build linked successfully, SwiftUI

### Community 27 - "Kotlin Bindings Runtime Helpers"
Cohesion: 0.24
Nodes (6): Disposable, ForeignBytes, NoHandle, UniffiWithHandle, use(), Pointer

### Community 28 - "Kotlin Handle Map"
Cohesion: 0.42
Nodes (4): InternalException, T, UniffiHandleMap, UniffiNullRustCallStatusErrorHandler

### Community 29 - "iOS Greeting UI Tests"
Cohesion: 0.38
Nodes (5): GreetingUITests, UInt8, CIContext, XCTestCase, XCUIScreenshot

### Community 30 - "Hosted CI Verification"
Cohesion: 0.43
Nodes (7): Hosted run 43593365100 on commit 6587579 (all three jobs passed), iOS simulator results (iPhone 17 on iOS 27.0 local, iOS 26.5 hosted), 006 - Hosted build verification (done), Android hosted job installs the supported SDK packages, iOS simulator boots in each system appearance before XCTest, Three hosted jobs (foundation, iOS, Android) on the same revision, Mobile foundation CI workflow

### Community 31 - "Kotlin Contract Integrity Checks"
Cohesion: 0.60
Nodes (3): IntegrityCheckingUniffiLib, uniffiCheckApiChecksums(), uniffiCheckContractApiVersion()

### Community 32 - "Android Rust Build Script"
Cohesion: 0.40
Nodes (4): CARGO_TARGET_AARCH64_LINUX_ANDROID_LINKER, CARGO_TARGET_X86_64_LINUX_ANDROID_LINKER, PATH, build-android-rust.sh script

### Community 40 - "iOS Rust Build Script"
Cohesion: 0.50
Nodes (3): CARGO_TARGET_DIR, PATH, build-ios-rust.sh script

## Knowledge Gaps
- **53 isolated node(s):** `NoHandle`, `UniffiWithHandle`, `Explicit application records and enums; private core/transport shapes mapped at the adapter`, `apiChecksumMismatch`, `contractVersionMismatch` (+48 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **8 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `.body` connect `Native Greeting Screens` to `Swift UniFFI Bindings`?**
  _High betweenness centrality (0.145) - this node is a cross-community bridge._
- **Why does `hello()` connect `Swift UniFFI Bindings` to `Native Greeting Screens`?**
  _High betweenness centrality (0.143) - this node is a cross-community bridge._
- **Why does `GreetingScreen` connect `Native Greeting Screens` to `iOS Greeting Scope`, `Platform Rules and Implementation Workflow`?**
  _High betweenness centrality (0.139) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Foundation verification 2026-11-14` (e.g. with `Deliver one exercisable vertical slice at a time and record observed results` and `Record separately what compiled and what ran`) actually correct?**
  _`Foundation verification 2026-11-14` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `NoHandle`, `UniffiWithHandle`, `Explicit application records and enums; private core/transport shapes mapped at the adapter` to the rest of the system?**
  _53 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Swift UniFFI Bindings` be split into smaller, more focused modules?**
  _Cohesion score 0.05444596443228454 - nodes in this community are weakly interconnected._
- **Should `Ownership Matrix and Boundaries` be split into smaller, more focused modules?**
  _Cohesion score 0.07792207792207792 - nodes in this community are weakly interconnected._