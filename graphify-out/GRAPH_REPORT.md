# Graph Report - mobile  (2026-11-15)

## Corpus Check
- Corpus is ~27,197 words - fits in a single context window. You may not need a graph.

## Summary
- 795 nodes · 2018 edges · 56 communities (44 shown, 12 thin omitted)
- Extraction: 76% EXTRACTED · 24% INFERRED · 0% AMBIGUOUS · INFERRED: 492 edges (avg confidence: 0.89)
- Token cost: 180,722 input · 0 output

## Community Hubs (Navigation)
- Swift UniFFI Bindings
- Kotlin RustBuffer Handling
- Accessibility and Contrast Checks
- Kotlin FFI Library Loading
- Kotlin FFI Callback Interfaces
- Kotlin Handle Map
- Kotlin UniFFI Library Calls
- Swift Foundation Tokens
- Kotlin Foreign Future Structs
- Greeting Screen Views
- iOS App Entry Point
- Android Activity and Theme
- iOS Greeting UI Tests
- Kotlin Foundation Tokens
- Kotlin Future Callback F32
- Kotlin Future Callback F64
- Kotlin Future Callback I16
- Kotlin Future Callback I64
- Kotlin Future Callback RustBuffer
- Kotlin Future Callback U16
- Kotlin Future Callback U32
- Kotlin Future Callback U64
- Verification Record and UI Checks
- Kotlin Future Callback U8
- Kotlin Future Callback Void
- Kotlin FFI Converters
- Kotlin Rust Call Status
- Planning Path, Rules and Compliance
- Resource Generator Script
- Shared Config and Localization
- Design System Guide
- Build Scripts and Handoff Checks
- Greeting Contract, Tests and CI
- Ownership Matrix and Agent Workflow
- Design Token and Resource Rules
- Hosted Build Verification
- Generated File Rules
- ADR-0001 and Layer Boundaries
- Platform Rules and Native Presentation
- Shared Config Schema
- Shared Scope and App Workspaces
- Lowest OS and Large Text Checks
- Localization Schema
- Generated Drift and Regeneration
- UniFFI Bindgen Tool
- Android Rust Build Script
- Gradle Wrapper Script
- iOS Rust Build Script
- Spec 0001 Decision and Forces
- Token Conventions and Principles
- Native Token Mapping
- App Greeting Scopes and Device Coverage
- Review-Only Rules and Anti-Duplication

## God Nodes (most connected - your core abstractions)
1. `Spec 0002: One planning path: a scope row first, then a spec` - 57 edges
2. `UniffiLib` - 54 edges
3. `Spec 0001: One owner per responsibility, with rules kept beside the code` - 53 edges
4. `Mobile foundation scope (index)` - 38 edges
5. `Decision: a new capability is planned as a scope row and designed in a spec before code; docs/plans and new ADRs are retired in a single change` - 38 edges
6. `Rollout: one change in fifteen ordered steps (rules, AGENTS.md, architecture docs, README, validator, delete docs/plans, scope files, spec 0001, knowledge graph)` - 33 edges
7. `UniffiRustCallStatus` - 29 edges
8. `Development rules` - 28 edges
9. `RustBuffer` - 27 edges
10. `ADR 0001: Native apps with a shared Rust core` - 27 edges

## Surprising Connections (you probably didn't know these)
- `Tokens, configuration and localization check` --references--> `GenerationTests`  [INFERRED]
  docs/quality/architecture-compliance.md → tooling/codegen/test_generation.py
- `Render the returned Rust string verbatim` --references--> `GreetingScreen`  [INFERRED]
  docs/rules/ios-rules.md → apps/ios/Presentation/GreetingScreen.swift
- `SwiftUI presentation with Dynamic Type and adaptive appearance` --references--> `GreetingScreen`  [INFERRED]
  docs/rules/ios-rules.md → apps/ios/Presentation/GreetingScreen.swift
- `iOS linkage and UI check (macOS CI job, XCTest)` --references--> `GreetingUITests`  [INFERRED]
  docs/quality/architecture-compliance.md → apps/ios/UITests/GreetingUITests.swift
- `iOS runtime result (iPhone 17 simulator, iOS 27.0, light and dark)` --references--> `GreetingUITests`  [INFERRED]
  docs/quality/verification.md → apps/ios/UITests/GreetingUITests.swift

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Automated architecture compliance checks** — docs_quality_architecture_compliance_rust_format_and_lint, docs_quality_architecture_compliance_core_and_ffi_contract_tests, docs_quality_architecture_compliance_cargo_dependency_and_governance_check, docs_quality_architecture_compliance_uniffi_generated_files_check, docs_quality_architecture_compliance_tokens_config_localization_check, docs_quality_architecture_compliance_ios_linkage_and_ui_check, docs_quality_architecture_compliance_android_linkage_and_ui_check [EXTRACTED 1.00]
- **Greeting vertical slice: localized recipient through UniFFI to the Rust formatter** — readme_hello_world_greeting, shared_localization_readme_greeting_recipient, docs_architecture_overview_greeting_call_flow, docs_contracts_ffi_conventions_hello_contract, docs_architecture_overview_foundation_core_hello, docs_architecture_ownership_matrix_crates_mobile_ffi, docs_architecture_ownership_matrix_bindings, readme_uniffi [EXTRACTED 1.00]
- **One planning path: a scope row first, then a spec before code, named by the agent instructions, the development rules and the repository structure** — docs_specs_root_0002_one_planning_path_decision_scope_row_then_spec, docs_specs_root_0002_one_planning_path_canonical_planning_pattern, docs_rules_development_rules_scope_row_then_spec, agents_scope_row_and_spec_before_code, docs_scope_root_007_one_planning_path, docs_scope_index, docs_architecture_repository_structure_docs_record_homes, docs_specs_root_0001_ownership_development_rules_r10_scope_row_and_spec_for_capability_spec_for_material_decision [EXTRACTED 1.00]
- **Open scope items across the three workspaces** — docs_scope_root_008_hosted_results_in_the_verification_record, docs_scope_ios_002_lowest_supported_ios_and_large_text, docs_scope_android_002_lowest_supported_android_and_large_text [EXTRACTED 1.00]
- **Forces that motivate the one-owner-per-responsibility decision** — docs_specs_root_0001_ownership_development_rules_force_two_languages_downstream_of_one_source, docs_specs_root_0001_ownership_development_rules_force_generated_files_beside_handwritten_code, docs_specs_root_0001_ownership_development_rules_force_coding_agents_as_regular_contributors, docs_specs_root_0001_ownership_development_rules_force_one_maintainer, docs_specs_root_0001_ownership_development_rules_force_small_codebase, docs_specs_root_0001_ownership_development_rules_decision_one_owner_per_responsibility [EXTRACTED 1.00]
- **Machine enforcement chain: test.sh runs the validator and both generator drift checks, mirrored by the CI foundation job** — docs_specs_root_0001_ownership_development_rules_enforcement_test_script_and_three_policy_checks, scripts_test, tooling_validation_check_architecture, scripts_generate_bindings, scripts_generate_design_tokens, github_workflows_foundation_foundation_job [EXTRACTED 1.00]
- **Rules that rest on review alone with no automated check** — docs_specs_root_0001_ownership_development_rules_r1_one_authoritative_owner, docs_specs_root_0001_ownership_development_rules_r3_app_trees_do_not_import_one_another, docs_specs_root_0001_ownership_development_rules_r8_real_caller_first, docs_specs_root_0001_ownership_development_rules_r9_search_before_adding, docs_specs_root_0001_ownership_development_rules_r11_handoff_reports_compiled_and_ran_separately, docs_specs_root_0001_ownership_development_rules_r14_bindgen_feature_host_only, docs_specs_root_0001_ownership_development_rules_r15_library_change_transitive_and_size_review, docs_specs_root_0001_ownership_development_rules_r16_breaking_change_is_a_migration, docs_specs_root_0001_ownership_development_rules_r18_service_proposal_requirements [EXTRACTED 1.00]
- **Spec triggers kept in their owner files: when a smaller change needs a spec** — docs_specs_root_0002_one_planning_path_trigger_owner_files, docs_rules_development_rules_spec_triggers_for_smaller_changes, docs_rules_service_rules_spec_for_new_crate_or_boundary, docs_quality_architecture_compliance_spec_for_architecture_change, docs_architecture_dependency_rules_new_edge_proposal, docs_contracts_ffi_conventions_compatibility_versioning, docs_decisions_adr_0001_foundation_revisit_conditions, docs_specs_root_0001_ownership_development_rules_spec_triggers [EXTRACTED 1.00]
- **Canonical source over generated output: edit sources, regenerate, compare snapshots** — agents_never_hand_edit_generated_files, docs_architecture_ownership_matrix_derived_file_rule, docs_architecture_dependency_rules_one_way_generation, docs_decisions_adr_0001_foundation_checked_in_source_snapshots [INFERRED 0.85]
- **Design token pipeline from canonical JSON to native projections** — docs_design_system_token_conventions_canonical_token_sources, design_system_schemas_tokens_schema, scripts_generate_design_tokens, docs_design_system_platform_mapping_swiftui_token_projection, docs_design_system_platform_mapping_compose_token_projection, docs_quality_architecture_compliance_tokens_config_localization_check [INFERRED 0.85]
- **Neutral JSON sources validated and generated into native theme and string resources** — design_system_readme_token_files, design_system_readme_tokens_schema, shared_config_readme_foundation_json, shared_localization_readme_catalog_format, design_system_readme_generate_design_tokens_modes, tooling_codegen_requirements_fastjsonschema, design_system_readme_generated_semantic_api, shared_localization_readme_generated_native_strings [INFERRED 0.85]
- **Regenerate derived outputs with their canonical source, never hand-edit** — docs_rules_development_rules_regenerate_derived_files, docs_rules_design_system_rules_regenerate_projections, docs_quality_architecture_compliance_generated_drift_remediation, docs_rules_rust_rules_regenerate_after_signature_change, docs_rules_shared_resources_rules_generated_native_strings, docs_rules_anti_duplication_ffi_shapes_in_rust_export [INFERRED 0.85]
- **Tracer bullet greeting path from shared core to both native screens** — docs_scope_index_tracer_bullet_build_approach, docs_scope_root_002_shared_greeting_contract, docs_scope_root_002_shared_greeting_contract_one_string_in_one_string_out_contract, docs_scope_ios_001_native_ios_greeting, docs_scope_android_001_native_android_greeting, docs_scope_root_006_hosted_build_verification [INFERRED 0.85]
- **Verification evidence chain: local checks, hosted jobs and the verification record** — docs_scope_root_005_reproducible_local_builds_and_checks, docs_scope_root_006_hosted_build_verification, docs_scope_root_008_hosted_results_in_the_verification_record, docs_scope_index_hosted_run_43593365100, docs_scope_root_005_reproducible_local_builds_and_checks_stale_local_verification_record, docs_scope_root_008_hosted_results_in_the_verification_record_single_list_of_unverified_targets [INFERRED 0.85]

## Communities (56 total, 12 thin omitted)

### Community 1 - "Swift UniFFI Bindings"
Cohesion: 0.05
Nodes (64): Data, FfiConverter, FfiConverterPrimitive, FfiConverterRustBuffer, FfiConverterString, ForeignBytes, InitializationResult, NSLock (+56 more)

### Community 12 - "Kotlin RustBuffer Handling"
Cohesion: 0.21
Nodes (5): ByValue, ForeignBytes, RustBuffer, `hello`(), Pointer

### Community 17 - "Accessibility and Contrast Checks"
Cohesion: 0.16
Nodes (7): GenerationTests, W3C WCAG 2.2 contrast minimum guidance, Design system and resources result (seven generator tests), Accessibility (design system), Status conveyed by text or semantics, not color alone, Honor platform reduced-motion setting, Text contrast check (4.5:1 minimum)

### Community 19 - "Kotlin FFI Library Loading"
Cohesion: 0.22
Nodes (7): Disposable, IntegrityCheckingUniffiLib, NoHandle, UniffiWithHandle, uniffiCheckApiChecksums(), uniffiCheckContractApiVersion(), use()

### Community 23 - "Kotlin FFI Callback Interfaces"
Cohesion: 0.18
Nodes (6): UniffiCallbackInterfaceClone, UniffiCallbackInterfaceFree, UniffiForeignFutureCompleteI32, UniffiForeignFutureCompleteI8, UniffiForeignFutureDroppedCallback, com

### Community 27 - "Kotlin Handle Map"
Cohesion: 0.36
Nodes (5): InternalException, UniffiHandleMap, UniffiNullRustCallStatusErrorHandler, T, kotlin

### Community 30 - "Swift Foundation Tokens"
Cohesion: 0.25
Nodes (7): FoundationTokens, Palette, CGFloat, Color, ColorScheme, Font, TimeInterval

### Community 31 - "Kotlin Foreign Future Structs"
Cohesion: 0.31
Nodes (6): ByReference, UniffiByValue, UniffiForeignFutureDroppedCallbackStruct, UniffiForeignFutureResultI32, UniffiForeignFutureResultI8, Structure

### Community 32 - "Greeting Screen Views"
Cohesion: 0.29
Nodes (8): GreetingScreen, GreetingScreen(), .body, String, View, Greeting as a single text element, Reviewers trace changed behavior from owner into each client, Trace screen, generated binding, FFI export and core function before changing shared behavior

### Community 34 - "iOS App Entry Point"
Cohesion: 0.29
Nodes (5): MobileFoundationApp, App, .body, Scene, SwiftUI

### Community 35 - "Android Activity and Theme"
Cohesion: 0.43
Nodes (4): MainActivity, FoundationTheme(), Bundle, ComponentActivity

### Community 36 - "iOS Greeting UI Tests"
Cohesion: 0.38
Nodes (5): GreetingUITests, UInt8, CIContext, XCTestCase, XCUIScreenshot

### Community 5 - "Verification Record and UI Checks"
Cohesion: 0.14
Nodes (24): GreetingTest, Android compilation result (Gradle 9.3.1, AGP 9.1.0, Temurin 17), Android packaging 16 KiB alignment result, Android runtime result (API 36 arm64 emulator, both appearances), CI configuration result (actionlint passed, hosted jobs not executed), iOS 26.5 simulator dark-appearance check did not pass, iOS compilation result (Xcode 27.1, Swift 6.4, arm64 and x86_64 simulators, unsigned device build), iOS runtime result (iPhone 17 simulator, iOS 27.0, light and dark) (+16 more)

### Community 7 - "Kotlin FFI Converters"
Cohesion: 0.17
Nodes (9): FfiConverter, FfiConverterRustBuffer, FfiConverterString, uniffiTraitInterfaceCall(), uniffiTraitInterfaceCallWithError(), FfiType, ByteBuffer, KotlinType (+1 more)

### Community 8 - "Kotlin Rust Call Status"
Cohesion: 0.12
Nodes (7): UniffiRustCallStatus, UniffiRustCallStatusErrorHandler, uniffiCheckCallStatus(), uniffiRustCall(), uniffiRustCallWithError(), E, U

### Community 0 - "Planning Path, Rules and Compliance"
Cohesion: 0.08
Nodes (87): Compatibility: version breaking contracts and coordinate regeneration, both apps and release, Revisit conditions: dependency direction change, async native boundary, independently versioned clients, new shared crate or service, Dependency rules, ADR 0001: Native apps with a shared Rust core, New dependency edge needs an owning module, a use case and a test, Architecture policy result (dependency and required-document checks), docs/ and root AGENTS.md: architecture, decision records, scope and agent workflow, docs/ record homes: docs/scope (what to build and its status), docs/specs (design and decision records), docs/decisions (the founding decision) (+79 more)

### Community 6 - "Resource Generator Script"
Cohesion: 0.14
Nodes (19): check_schema(), generate(), load(), projections(), unique_members(), validator(), native_text(), parse_template() (+11 more)

### Community 13 - "Shared Config and Localization"
Cohesion: 0.22
Nodes (16): Bundle development locale fixed to en, foundation.json: public build-time configuration (v1 schema), Locale catalog format: ll.json / ll-RR.json, stable snake_case keys, same keys as default en, Generated iOS Localizable.strings and Android foundation_strings.xml, Named {name} placeholders projected to positional string specifiers, Configuration guide, Localization guide, Only public settings in shared config; secrets via native credential store or CI secret store (+8 more)

### Community 14 - "Design System Guide"
Cohesion: 0.18
Nodes (15): generate-design-tokens.sh modes: write, --check (drift), --test (failure cases), Generated semantic token API consumed by native apps, Five canonical token JSON files (primitives and semantic aliases), tokens.schema.json: single Draft 7 document keyed by filename stem, Layer: resources and tooling (build-host validation and generation), fastjsonschema==2.21.2 (sha256 hash-pinned schema validator), Design system guide, Generators consume neutral sources and never recover canonical values from native output (+7 more)

### Community 15 - "Build Scripts and Handoff Checks"
Cohesion: 0.22
Nodes (13): CI job: android (JDK 17, API 36 emulator, Kotlin binding + Compose UI), CI job: ios (macos-26, Xcode 26.5, simulator + unsigned device link), Pass representative values through both generated languages, Light and dark appearance verification in CI, build-android.sh script, build-ios.sh script, Worked example: a change to shared behavior (core, export, regenerate bindings, both call sites, checks, report), Agent workflow: before handoff (run checks, report commands and unverified targets) (+5 more)

### Community 2 - "Greeting Contract, Tests and CI"
Cohesion: 0.09
Nodes (35): CI job: foundation (locked Rust build + scripts/test.sh on ubuntu-24.04), Mobile contract (FFI conventions), UniFFI derives native functions, buffer handling and contract checks; no raw pointers or hand-maintained C ABI declarations, hello(), preserves_empty_names_and_whitespace(), String, hello(), String (+27 more)

### Community 21 - "Ownership Matrix and Agent Workflow"
Cohesion: 0.26
Nodes (13): App trees do not import one another; core never calls platform UI, apps/android: owner of Android UI, presentation state and OS APIs, apps/ios: owner of Apple UI, presentation state and OS APIs, Canonical change path: before editing, while editing, before handoff, Force: coding agents are regular contributors and act on what they load, Force: agents act on what AGENTS.md links (and would write a PRD in a folder nobody reads), AGENTS.md: Working in the mobile foundation, Agent workflow: before commit (run /graphify . --update, stage graphify-out with the change) (+5 more)

### Community 25 - "Design Token and Resource Rules"
Cohesion: 0.33
Nodes (11): Brand assets guide, Draft 7 schemas in shared/specifications, Shared resources owner (build configuration, localization, brand assets), Design system rules, Shared resource ownership rules, Stable role names or same-change migration, Public role name changes require migrating both consumers, Draft 7 schema and native mappings updated together (+3 more)

### Community 33 - "Hosted Build Verification"
Cohesion: 0.29
Nodes (7): Mobile foundation CI workflow, CoreImage, XCTest, Android hosted job installs the supported SDK packages, iOS simulator boots in each system appearance before XCTest, Three hosted jobs (foundation, iOS, Android) on the same revision, 006 - Hosted build verification (done)

### Community 37 - "Generated File Rules"
Cohesion: 0.40
Nodes (6): Brand asset conventions: snake_case names, SVG/PNG masters, _light/_dark pairs, reproducible exports, Drift detection for checked-in bindings and resources, Force: generated files sit beside hand-written code (edits there are lost or hide a mismatch), Never hand-edit generated files, Derived file rule: change the canonical input and regenerate every output in the same review, R5: a generated file is never edited by hand; change the source and regenerate every output

### Community 4 - "ADR-0001 and Layer Boundaries"
Cohesion: 0.10
Nodes (32): Layer: design system (generated Swift/Kotlin values as shared visual vocabulary), Layer: native platform integration (Swift owns Apple services, Kotlin owns Android services), Layer: native presentation (views render, adapt to appearance, handle events), Layer: shared Rust (core owns behavior, FFI crate maps exports), Workspace edge: mobile-ffi depends on foundation-core (std-only core), Proc-macro exports define the cross-language API; bindgen feature gates host CLI deps, Explicit application records and enums; private core/transport shapes mapped at the adapter, Async and cancellation conventions for future exports (+24 more)

### Community 11 - "Platform Rules and Native Presentation"
Cohesion: 0.17
Nodes (16): Android rules, iOS rules, Checked-in Gradle wrapper, Compose presentation with native Material semantics, Application code displays the binding's return value, OS-specific capability stays in its own app, Native permissions, UIKit delegates and device lifecycle stay in the Apple adapter, Render the returned Rust string verbatim (+8 more)

### Community 18 - "Shared Config Schema"
Cohesion: 0.14
Nodes (13): additionalProperties, const, properties, defaultLocale, schemaVersion, required, $schema, const (+5 more)

### Community 20 - "Shared Scope and App Workspaces"
Cohesion: 0.27
Nodes (12): Android app owns its screen, appearance changes and native localization lookup, Apple app owns its screen, appearance changes and native localization lookup, Generated bindings (code that carries values between languages), Shared named visual values (color, type, spacing, corners, motion), Unproven corner and motion values, Android scope, iOS scope, 002 - Shared greeting contract (existing) (+4 more)

### Community 22 - "Lowest OS and Large Text Checks"
Cohesion: 0.27
Nodes (10): Android app packages both supported CPU architectures, 16 KiB memory page packaging, Declared Android minimum API 24 not yet exercised, Android largest font scale check, Native text style supporting Dynamic Type, Declared iOS 17 deployment target not yet exercised, iOS largest accessibility text size check, Android 002 - Lowest supported Android and large text (planned) (+2 more)

### Community 26 - "Localization Schema"
Cohesion: 0.18
Nodes (10): additionalProperties, minLength, type, propertyNames, pattern, required, $schema, title (+2 more)

### Community 28 - "Generated Drift and Regeneration"
Cohesion: 0.31
Nodes (9): PYTHONPATH, generate-design-tokens.sh script, Shared visual decisions and translations are generator inputs, Drift check plus verification in both appearances and larger text sizes, Regenerate native projections in the same change, Generated native strings owned by the resource generator, Generated drift remediation, Tokens, configuration and localization check (+1 more)

### Community 38 - "UniFFI Bindgen Tool"
Cohesion: 0.50
Nodes (4): main(), Design definitions compile independently of Cargo and UniFFI, UniFFI generator feature restricted to host tooling, R14: the UniFFI generator feature (bindgen) stays on host tooling

### Community 39 - "Android Rust Build Script"
Cohesion: 0.40
Nodes (4): CARGO_TARGET_AARCH64_LINUX_ANDROID_LINKER, CARGO_TARGET_X86_64_LINUX_ANDROID_LINKER, PATH, build-android-rust.sh script

### Community 41 - "Gradle Wrapper Script"
Cohesion: 0.83
Nodes (3): gradlew script, die(), warn()

### Community 52 - "iOS Rust Build Script"
Cohesion: 0.50
Nodes (3): CARGO_TARGET_DIR, PATH, build-ios-rust.sh script

### Community 10 - "Spec 0001 Decision and Forces"
Cohesion: 0.22
Nodes (18): Reviewers assess semantic duplication, Follow-up: decide whether checks must pass before a change reaches main (branch rule or local hook), Follow-up: confirm or correct the inferred rationale, Force: one maintainer, so no second reviewer by default, Force: two languages downstream of one source (a rule written in Swift and Kotlin drifts silently), Four routes a value takes to a screen: Rust behavior via generated bridge, visual tokens via generator, text and settings via a second generator, per-app code, Tradeoff: a direct push to main lands before a check can fail, Tradeoff: 'material' is a judgment call decided by the reviewer outside the written triggers (+10 more)

### Community 16 - "Token Conventions and Principles"
Cohesion: 0.22
Nodes (14): Canonical token schema (tokens.schema.json), Canonical token sources (colors, typography, spacing, radius, motion JSON), Primitive token (names a value), Semantic role (describes where to use a value), Design principles, Token conventions, Per-target reading order and screen-reader review, Native controls styled with semantic tokens (+6 more)

### Community 24 - "Native Token Mapping"
Cohesion: 0.35
Nodes (11): spacingPage role, typographyGreeting role, Native token mapping, System text scaling via generated text styles, Compose sp mapping of logical text units, Jetpack Compose token projection (FoundationTokens), Dynamic Type mapping of headline and reading scales, Logical spacing units adapt to display density (+3 more)

### Community 29 - "App Greeting Scopes and Device Coverage"
Cohesion: 0.33
Nodes (10): API 36 emulator results (arm64 local, x86_64 hosted) in light and dark, Android physical device coverage unverified, Greeting exposed to accessibility in light and dark appearance, iOS physical device coverage unverified, iOS simulator results (iPhone 17 on iOS 27.0 local, iOS 26.5 hosted), Unsigned iOS device build linked successfully, Android 001 - Native Android greeting (existing), iOS 001 - Native iOS greeting (existing) (+2 more)

### Community 9 - "Review-Only Rules and Anti-Duplication"
Cohesion: 0.17
Nodes (19): Native components guidelines, Anti-duplication rules, Reusable native component (introduced on demand), Locate the owner before adding a constant, rule, DTO, translation or asset, Introduce presentation state or a ViewModel only when needed, Follow-up: a small import scan in check-architecture.py for R3, Follow-up: record reviewers per owner (CODEOWNERS) when a second contributor joins, Force: the codebase is small (the foundation ends at one greeting) (+11 more)

## Knowledge Gaps
- **52 isolated node(s):** `NoHandle`, `UniffiWithHandle`, `Explicit application records and enums; private core/transport shapes mapped at the adapter`, `apiChecksumMismatch`, `contractVersionMismatch` (+47 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **12 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `.body` connect `iOS App Entry Point` to `Greeting Screen Views`, `Swift UniFFI Bindings`?**
  _High betweenness centrality (0.141) - this node is a cross-community bridge._
- **Why does `hello()` connect `Swift UniFFI Bindings` to `iOS App Entry Point`?**
  _High betweenness centrality (0.138) - this node is a cross-community bridge._
- **Why does `GreetingScreen` connect `Greeting Screen Views` to `iOS App Entry Point`, `Platform Rules and Native Presentation`?**
  _High betweenness centrality (0.138) - this node is a cross-community bridge._
- **Are the 7 inferred relationships involving `Mobile foundation scope (index)` (e.g. with `docs/ and root AGENTS.md: architecture, decision records, scope and agent workflow` and `docs/ record homes: docs/scope (what to build and its status), docs/specs (design and decision records), docs/decisions (the founding decision)`) actually correct?**
  _`Mobile foundation scope (index)` has 7 INFERRED edges - model-reasoned connections that need verification._
- **Are the 13 inferred relationships involving `Decision: a new capability is planned as a scope row and designed in a spec before code; docs/plans and new ADRs are retired in a single change` (e.g. with `Follow-up (settled by spec 0002): R10 sent a new capability to docs/plans while features are tracked in docs/scope` and `Canonical pattern: a scope row (the brief), a spec before code, one slice through its real caller, progress in the scope row and results in the verification record`) actually correct?**
  _`Decision: a new capability is planned as a scope row and designed in a spec before code; docs/plans and new ADRs are retired in a single change` has 13 INFERRED edges - model-reasoned connections that need verification._
- **What connects `NoHandle`, `UniffiWithHandle`, `Explicit application records and enums; private core/transport shapes mapped at the adapter` to the rest of the system?**
  _52 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Swift UniFFI Bindings` be split into smaller, more focused modules?**
  _Cohesion score 0.05444596443228454 - nodes in this community are weakly interconnected._