# Graph Report - mobile  (2026-11-15)

## Corpus Check
- 20 files · ~70,395 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1027 nodes · 2815 edges · 50 communities
- Extraction: 76% EXTRACTED · 24% INFERRED · 0% AMBIGUOUS · INFERRED: 676 edges (avg confidence: 0.89)
- Token cost: 255,756 input · 0 output

## Community Hubs (Navigation)
- Swift UniFFI Bindings
- Kotlin FFI Library Loading
- Kotlin UniFFI Library Calls
- Rust Core and Greeting Contract
- Planning Path and Spec 0002
- Native App Shells and Tokens
- Derivation Command
- Derivation Command Tests
- Spec 0001 Ownership Rules
- Rule Set and Agent Workflow
- Governance Checks in test.sh
- Spec 0003 Criteria and Check
- Verification Record and UI Tests
- Spec 0003 Decision History
- Founding Decision and Dependency Rules
- CI Workflow and Derived Run
- Native Greeting and Supported OS Scopes
- Resource Generator
- Kotlin RustBuffer Handling
- Shared Config and Localization
- Repository Structure and Layers
- Kotlin FFI Converters
- Scope 009 and Value Sourcing
- Generator Tests and Accessibility
- Product Identity Files
- Schemas and Sample Names
- Scope Workspaces and Build Approach
- Design Principles and Token Conventions
- Design System and Shared Resource Rules
- Verification Scopes and Unverified Targets
- Kotlin Rust Call Status
- Native Token Mapping and Text Scaling
- Derivation Test on a Copy
- Mobile Contract Extension Conventions
- Empty Verification Record
- Generated Files and Drift
- Kotlin Handle Map and Lifting
- Design System Guide and Token Schema
- README and Starting a Product
- Config Schema
- Android App Shell
- Shared Visual Definitions
- Config Schema Properties
- iOS Greeting UI Tests
- Kotlin FFI Integrity Checks
- Android Rust Build Script
- iOS Rust Build Script

## God Nodes (most connected - your core abstractions)
1. `Spec 0002: One planning path: a scope row first, then a spec` - 60 edges
2. `Spec 0001: One owner per responsibility, with rules kept beside the code` - 56 edges
3. `UniffiLib` - 54 edges
4. `Spec 0003: A new project from the foundation: product identity in two files, one init command, updates by merge (In Progress)` - 52 edges
5. `Foundation verification 2026-11-15` - 51 edges
6. `Mobile foundation scope (index)` - 43 edges
7. `Decision: a new capability is planned as a scope row and designed in a spec before code; docs/plans and new ADRs are retired in a single change` - 38 edges
8. `Spec 0003 rationale: decision history of the new project spec (context, options considered, rationale)` - 34 edges
9. `Rollout: one change in fifteen ordered steps (rules, AGENTS.md, architecture docs, README, validator, delete docs/plans, scope files, spec 0001, knowledge graph)` - 33 edges
10. `Ownership matrix` - 30 edges

## Surprising Connections (you probably didn't know these)
- `Product identity result (2026-11-15: test.sh passed with --check printing foundation and --test passing 21 unit tests; both apps carried dev.foundation.mobile, Mobile Foundation, 0.1.0, build 1; a copy derived as Zoë's Proof built and matched its identity file)` --references--> `GreetingTest`  [INFERRED]
  docs/quality/verification.md → apps/android/app/src/androidTest/kotlin/foundation/mobile/GreetingTest.kt
- `Trace screen, generated binding, FFI export and core function before changing shared behavior` --references--> `GreetingScreen`  [INFERRED]
  docs/rules/development-rules.md → apps/ios/Presentation/GreetingScreen.swift
- `SwiftUI presentation with Dynamic Type and adaptive appearance` --references--> `GreetingScreen`  [INFERRED]
  docs/rules/ios-rules.md → apps/ios/Presentation/GreetingScreen.swift
- `Product identity result (2026-11-15: test.sh passed with --check printing foundation and --test passing 21 unit tests; both apps carried dev.foundation.mobile, Mobile Foundation, 0.1.0, build 1; a copy derived as Zoë's Proof built and matched its identity file)` --references--> `GreetingUITests`  [INFERRED]
  docs/quality/verification.md → apps/ios/UITests/GreetingUITests.swift
- `Greeting as a single text element` --references--> `GreetingScreen()`  [INFERRED]
  docs/design-system/component-guidelines.md → apps/android/presentation/src/main/kotlin/foundation/presentation/GreetingScreen.kt

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Proof that derivation still works: --check state test, derivation unit test on a temporary copy in scripts/test.sh, CI identity comparison in both native jobs, manual workflow run with derived set** — docs_specs_root_0003_new_project_from_foundation_index_check_form, docs_specs_root_0003_new_project_from_foundation_index_test_form, docs_specs_root_0003_new_project_from_foundation_index_derivation_test, docs_specs_root_0003_new_project_from_foundation_index_ci_identity_comparison, docs_specs_root_0003_new_project_from_foundation_index_workflow_derived_input, scripts_test, github_workflows_foundation, github_workflows_foundation_derived_input, github_workflows_foundation_derive_sample_product_step, github_workflows_foundation_ios_identity_comparison_step, github_workflows_foundation_android_identity_comparison_step [INFERRED 0.85]
- **One init command turns a foundation clone into a derived product: identity files, README origin line, empty verification record, removed knowledge graph** — scripts_init_project, tooling_derive_init_project, apps_ios_config_identity, apps_android_identity, docs_specs_root_0003_new_project_from_foundation_index_readme_origin_line, docs_specs_root_0003_new_project_from_foundation_index_empty_verification_record, tooling_derive_verification_record, docs_specs_root_0003_new_project_from_foundation_index_init_write_set, docs_specs_root_0003_new_project_from_foundation_index_repository_states_foundation_derived_mixed [EXTRACTED 1.00]
- **Automated architecture compliance checks** — docs_quality_architecture_compliance_rust_format_and_lint, docs_quality_architecture_compliance_core_and_ffi_contract_tests, docs_quality_architecture_compliance_cargo_dependency_and_governance_check, docs_quality_architecture_compliance_project_identity_state_check, docs_quality_architecture_compliance_uniffi_generated_files_check, docs_quality_architecture_compliance_tokens_config_localization_check, docs_quality_architecture_compliance_ios_linkage_and_ui_check, docs_quality_architecture_compliance_android_linkage_and_ui_check [EXTRACTED 1.00]
- **Forces that motivate the one-owner-per-responsibility decision** — docs_specs_root_0001_ownership_development_rules_force_two_languages_downstream_of_one_source, docs_specs_root_0001_ownership_development_rules_force_generated_files_beside_handwritten_code, docs_specs_root_0001_ownership_development_rules_force_coding_agents_as_regular_contributors, docs_specs_root_0001_ownership_development_rules_force_one_maintainer, docs_specs_root_0001_ownership_development_rules_force_small_codebase, docs_specs_root_0001_ownership_development_rules_decision_one_owner_per_responsibility [EXTRACTED 1.00]
- **Machine enforcement chain: test.sh runs the validator and both generator drift checks, mirrored by the CI foundation job** — docs_specs_root_0001_ownership_development_rules_enforcement_test_script_and_three_policy_checks, scripts_test, tooling_validation_check_architecture, scripts_generate_bindings, scripts_generate_design_tokens, github_workflows_foundation_foundation_job [EXTRACTED 1.00]
- **Rules that rest on review alone with no automated check** — docs_specs_root_0001_ownership_development_rules_r1_one_authoritative_owner, docs_specs_root_0001_ownership_development_rules_r3_app_trees_do_not_import_one_another, docs_specs_root_0001_ownership_development_rules_r8_real_caller_first, docs_specs_root_0001_ownership_development_rules_r9_search_before_adding, docs_specs_root_0001_ownership_development_rules_r11_handoff_reports_compiled_and_ran_separately, docs_specs_root_0001_ownership_development_rules_r14_bindgen_feature_host_only, docs_specs_root_0001_ownership_development_rules_r15_library_change_transitive_and_size_review, docs_specs_root_0001_ownership_development_rules_r16_breaking_change_is_a_migration, docs_specs_root_0001_ownership_development_rules_r18_service_proposal_requirements [EXTRACTED 1.00]
- **Canonical source over generated output: edit sources, regenerate, compare snapshots** — agents_never_hand_edit_generated_files, docs_architecture_ownership_matrix_derived_file_rule, docs_architecture_dependency_rules_one_way_generation, docs_decisions_adr_0001_foundation_checked_in_source_snapshots [INFERRED 0.85]
- **Tracer bullet greeting path from shared core to both native screens** — docs_scope_index_tracer_bullet_build_approach, docs_scope_root_002_shared_greeting_contract, docs_scope_root_002_shared_greeting_contract_one_string_in_one_string_out_contract, docs_scope_ios_001_native_ios_greeting, docs_scope_android_001_native_android_greeting, docs_scope_root_006_hosted_build_verification [INFERRED 0.85]
- **Hosted run 43593365100 as runtime evidence for the greeting contract, visual definitions, shared text and reproducible builds** — docs_scope_root_002_shared_greeting_contract, docs_scope_root_003_shared_visual_definitions, docs_scope_root_004_shared_settings_text_and_brand_assets, docs_scope_root_005_reproducible_local_builds_and_checks, docs_quality_verification_hosted_run_43593365100, docs_quality_verification [EXTRACTED 1.00]
- **Regenerate and compare checks that keep generated tokens, catalogs and bindings equal to their sources** — docs_scope_root_003_shared_visual_definitions_token_drift_check, docs_scope_root_004_shared_settings_text_and_brand_assets_single_english_catalog, docs_scope_root_005_reproducible_local_builds_and_checks_generated_output_drift_detection, scripts_test [INFERRED 0.85]
- **Greeting vertical slice: localized recipient through UniFFI to the Rust formatter** — readme_hello_world_greeting, shared_localization_readme_greeting_recipient, docs_architecture_overview_greeting_call_flow, docs_contracts_ffi_conventions_hello_contract, docs_architecture_overview_foundation_core_hello, docs_architecture_ownership_matrix_crates_mobile_ffi, docs_architecture_ownership_matrix_bindings, readme_uniffi [EXTRACTED 1.00]
- **One planning path: a scope row first, then a spec before code, named by the agent instructions, the development rules and the repository structure** — docs_specs_root_0002_one_planning_path_decision_scope_row_then_spec, docs_specs_root_0002_one_planning_path_canonical_planning_pattern, docs_rules_development_rules_scope_row_then_spec, agents_scope_row_and_spec_before_code, docs_scope_root_007_one_planning_path, docs_scope_index, docs_architecture_repository_structure_docs_record_homes, docs_specs_root_0001_ownership_development_rules_r10_scope_row_and_spec_for_capability_spec_for_material_decision [EXTRACTED 1.00]
- **Spec triggers kept in their owner files: when a smaller change needs a spec** — docs_specs_root_0002_one_planning_path_trigger_owner_files, docs_rules_development_rules_spec_triggers_for_smaller_changes, docs_rules_service_rules_spec_for_new_crate_or_boundary, docs_quality_architecture_compliance_spec_for_architecture_change, docs_architecture_dependency_rules_new_edge_proposal, docs_contracts_ffi_conventions_compatibility_versioning, docs_decisions_adr_0001_foundation_revisit_conditions, docs_specs_root_0001_ownership_development_rules_spec_triggers [EXTRACTED 1.00]
- **Design token pipeline from canonical JSON to native projections** — docs_design_system_token_conventions_canonical_token_sources, design_system_schemas_tokens_schema, scripts_generate_design_tokens, docs_design_system_platform_mapping_swiftui_token_projection, docs_design_system_platform_mapping_compose_token_projection, docs_quality_architecture_compliance_tokens_config_localization_check [INFERRED 0.85]
- **Neutral JSON sources validated and generated into native theme and string resources** — design_system_readme_token_files, design_system_readme_tokens_schema, shared_config_readme_foundation_json, shared_localization_readme_catalog_format, design_system_readme_generate_design_tokens_modes, tooling_codegen_requirements_fastjsonschema, design_system_readme_generated_semantic_api, shared_localization_readme_generated_native_strings [INFERRED 0.85]
- **Regenerate derived outputs with their canonical source, never hand-edit** — docs_rules_development_rules_regenerate_derived_files, docs_rules_design_system_rules_regenerate_projections, docs_quality_architecture_compliance_generated_drift_remediation, docs_rules_rust_rules_regenerate_after_signature_change, docs_rules_shared_resources_rules_generated_native_strings, docs_rules_anti_duplication_ffi_shapes_in_rust_export [INFERRED 0.85]
- **Verification evidence chain: local checks, hosted jobs and the verification record** — docs_scope_root_005_reproducible_local_builds_and_checks, docs_scope_root_006_hosted_build_verification, docs_scope_root_008_hosted_results_in_the_verification_record, docs_scope_root_008_hosted_results_in_the_verification_record_single_list_of_unverified_targets [INFERRED 0.85]

## Communities (50 total, 0 thin omitted)

### Community 0 - "Swift UniFFI Bindings"
Cohesion: 0.05
Nodes (64): Array, createReader(), createWriter(), Data, FfiConverter, FfiConverterPrimitive, FfiConverterRustBuffer, FfiConverterString (+56 more)

### Community 1 - "Kotlin FFI Library Loading"
Cohesion: 0.06
Nodes (34): Disposable, NoHandle, UniffiByValue, UniffiCallbackInterfaceClone, UniffiCallbackInterfaceFree, UniffiForeignFutureCompleteF32, UniffiForeignFutureCompleteF64, UniffiForeignFutureCompleteI16 (+26 more)

### Community 2 - "Kotlin UniFFI Library Calls"
Cohesion: 0.06
Nodes (3): UniffiLib, UniffiRustCallStatus, UniffiRustFutureContinuationCallback

### Community 3 - "Rust Core and Greeting Contract"
Cohesion: 0.08
Nodes (42): hello(), preserves_empty_names_and_whitespace(), String, main(), hello(), String, Workspace edge: mobile-ffi depends on foundation-core (std-only core), Proc-macro exports define the cross-language API; bindgen feature gates host CLI deps (+34 more)

### Community 4 - "Planning Path and Spec 0002"
Cohesion: 0.12
Nodes (40): Deferred work beyond Hello World, The list of deferred work lives in one file, Follow-up (settled by spec 0002): R10 sent a new capability to docs/plans while features are tracked in docs/scope, Premise: rule files stay authoritative; the spec records the decision, rule set and enforcement, not a second copy, Spec 0002: One planning path: a scope row first, then a spec, ADR 0001 is not reworded, Decide first, always: a spec before code reaches main, Decision: a new capability is planned as a scope row and designed in a spec before code; docs/plans and new ADRs are retired in a single change (+32 more)

### Community 5 - "Native App Shells and Tokens"
Cohesion: 0.07
Nodes (27): App, gradlew script, die(), warn(), MobileFoundationApp, .body, FoundationTokens, Palette (+19 more)

### Community 6 - "Derivation Command"
Cohesion: 0.12
Nodes (31): Exception, check(), derive(), foundation_ref(), foundation_url(), git(), identity_text(), in_git() (+23 more)

### Community 7 - "Derivation Command Tests"
Cohesion: 0.16
Nodes (4): Checkout, DerivationTests, OutsideGitTests, A small foundation checkout in a temporary folder, in git unless a test says…

### Community 8 - "Spec 0001 Ownership Rules"
Cohesion: 0.15
Nodes (32): Ownership matrix, Rejected alternative: implementing application behavior independently in both apps, 001 - Ownership and development rules (done), One owner per shared responsibility (ten responsibilities in the ownership matrix), Spec 0001: One owner per responsibility, with rules kept beside the code, Automate only what a machine can judge, Decision: one owner per responsibility in an ownership matrix, topic-sized rule files, short AGENTS.md entry point, automated checks only where a machine is reliable, An exact dependency list, not a deny list (+24 more)

### Community 9 - "Rule Set and Agent Workflow"
Cohesion: 0.11
Nodes (31): AGENTS.md: Working in the mobile foundation, Agent workflow: before commit (run /graphify . --update, stage graphify-out with the change), Agent workflow: before editing (locate owner, contract, callers, tests), Agent workflow: before handoff (run checks, report commands and unverified targets), Agent workflow: during implementation (place change in owning layer), GreetingScreen(), Reviewers trace changed behavior from owner into each client, Android rules (+23 more)

### Community 10 - "Governance Checks in test.sh"
Cohesion: 0.13
Nodes (27): Cargo dependency and governance check, Limits of CI checks, Rust format and lint check (rustfmt, Clippy warnings denied), Architecture policy result (dependency and required-document checks), Reviewers assess semantic duplication, Specs are numbered NNNN-kebab-title.md in the folder mirroring the scope workspace; a replaced record is marked superseded; ADR 0001 stays the founding record, 007 - One planning path (done), Required document check covers the scope index (+19 more)

### Community 11 - "Spec 0003 Criteria and Check"
Cohesion: 0.15
Nodes (29): Build steps (009): identity file per platform (AC-1, AC-2, done), init command with state check and unit tests (AC-3 to AC-9, done), workflow derived input and identity comparison (AC-10, open), README path and document updates (AC-11, AC-12, done), Spec 0003: A new project from the foundation: product identity in two files, one init command, updates by merge (In Progress), AC-1: both apps carry the same default identity, read from Identity.xcconfig and identity.properties, stated nowhere else under apps/, AC-11: README.md has a section with the full path from clone to first results, path ownership, taking a later release and foundation tagging, AC-2: with the default identity scripts/test.sh passes, both apps build and the greeting tests pass in both appearances, AC-4: the write set is exactly the two identity files, README.md, the verification record and the removed graphify-out/ files; nothing is renamed, AC-6: README.md has the product name as title on line 1 and the origin line on line 3 followed by one blank line, AC-7: the command refuses, changes nothing and exits 2 with a one line reason (bad input, default ID, dirty tree, derived or mixed checkout, missing foundation URL or ref) (+21 more)

### Community 12 - "Verification Record and UI Tests"
Cohesion: 0.15
Nodes (25): GreetingTest, GreetingUITests, Android linkage and UI check (Linux CI job, emulator instrumentation), GitHub Actions CI jobs (macOS and Linux), iOS linkage and UI check (macOS CI job, XCTest), Foundation verification 2026-11-15, Android compilation result (Gradle 9.3.1, AGP 9.1.0, Temurin 17), Android runtime result (API 36 arm64 emulator, both appearances) (+17 more)

### Community 13 - "Spec 0003 Decision History"
Cohesion: 0.14
Nodes (27): apps/ios/MobileFoundation.xcodeproj/project.pbxproj (Xcode project file), Decision: a product is a clone that changes only its display name, application ID and version through scripts/init-project.sh, keeps every other name, starts with an empty verification record and merges foundation-v tags, Follow-up: revisit keeping MobileFoundation as the Xcode project and scheme name if it confuses contributors to a product, Names the foundation keeps: MobileFoundation project, targets and scheme, rootProject.name, crates foundation-core and mobile-ffi, mobile_ffi namespace, Kotlin packages, FoundationTokens, FoundationTheme, foundation_strings.xml, foundation.json, the workflow file, Tradeoff: a command and its unit tests are kept for a job that runs once per product, Tradeoff: foundation names stay in product code (MobileFoundation project, scheme and bundle, Foundation-prefixed types and packages); users see only the display name, Tradeoff: later foundation scope rows and specs do not flow into products; the reason behind a new foundation rule is read in the foundation repository, Tradeoff: the Linux proof builds nothing, so a change that breaks a derived native build can sit on main until the next manual derived run (+19 more)

### Community 14 - "Founding Decision and Dependency Rules"
Cohesion: 0.24
Nodes (25): Plan a new capability in the scope and write its spec under docs/specs before code, Dependency rules, New dependency edge needs an owning module, a use case and a test, Architecture overview, Color selection, font scaling, layout and accessibility run natively (no shared renderer), Mobile contract (FFI conventions), Compatibility: version breaking contracts and coordinate regeneration, both apps and release, ADR 0001: Native apps with a shared Rust core (+17 more)

### Community 15 - "CI Workflow and Derived Run"
Cohesion: 0.16
Nodes (23): Pass representative values through both generated languages, Unverified: the workflow with the derived input and the identity comparison steps has not run on a hosted runner; no run with derived set has happened yet, AC-10: the workflow accepts a manual run with the derived input, and every native job compares the built app's ID and display name with the identity file, Foundation ref resolution: --foundation-ref, else the highest foundation-v* tag exactly at HEAD, else the full HEAD commit ID, Release the foundation: run the workflow by hand with derived set, then push an annotated foundation-vMAJOR.MINOR.PATCH tag on main, Sample values: --name "Zoë's Proof" --app-id dev.example.derived, foundation URL https://example.invalid/foundation, ref foundation-v0.0.0, date 2026-01-01, Workflow input derived (workflow_dispatch boolean): the ios and android jobs run the command on the runner checkout, then build and test under the sample identity, Recommendation: tags are named foundation-vMAJOR.MINOR.PATCH (+15 more)

### Community 16 - "Native Greeting and Supported OS Scopes"
Cohesion: 0.15
Nodes (22): CoreImage, Android 001 - Native Android greeting (existing), API 36 emulator results (arm64 local, x86_64 hosted) in light and dark, Android app packages both supported CPU architectures, Android physical device coverage unverified, Android 002 - Lowest supported Android and large text (planned), 16 KiB memory page packaging, Declared Android minimum API 24 not yet exercised (+14 more)

### Community 17 - "Resource Generator"
Cohesion: 0.14
Nodes (19): check_schema(), generate(), load(), projections(), Validate authoritative sources, then materialize or check their projections., unique_members(), validator(), native_text() (+11 more)

### Community 18 - "Kotlin RustBuffer Handling"
Cohesion: 0.14
Nodes (9): ByReference, ByValue, ForeignBytes, `hello`(), RustBuffer, uniffiTraitInterfaceCall(), uniffiTraitInterfaceCallWithError(), kotlin (+1 more)

### Community 19 - "Shared Config and Localization"
Cohesion: 0.16
Nodes (20): Build-time generation: token JSON and locale JSON -> native theme inputs and localization resources, Deferred: a second language end to end, 004 - Shared settings, text and brand assets (done), shared/assets/ owns future brand artwork and its exports, Greeting sentence 'Hello, {name}!' formed in English by the core, Invalid settings, resource keys and mismatched translation placeholders are rejected, Single English localization catalog and public fallback locale, Force: shared/config/README.md keeps bundle and application IDs in Xcode or Gradle, not in the shared config schema (+12 more)

### Community 20 - "Repository Structure and Layers"
Cohesion: 0.16
Nodes (21): Architecture boundaries, Documented capability boundary; adapters need an actual caller, Layer: design system (generated Swift/Kotlin values as shared visual vocabulary), Layer: native platform integration (Swift owns Apple services, Kotlin owns Android services), Layer: native presentation (views render, adapt to appearance, handle events), Layer: resources and tooling (build-host validation and generation), Layer: shared Rust (core owns behavior, FFI crate maps exports), App trees do not import one another; core never calls platform UI (+13 more)

### Community 21 - "Kotlin FFI Converters"
Cohesion: 0.21
Nodes (7): FfiConverter, FfiConverterRustBuffer, FfiConverterString, FfiType, ByteBuffer, KotlinType, ULong

### Community 22 - "Scope 009 and Value Sourcing"
Cohesion: 0.16
Nodes (17): apps/android/app/src/main/AndroidManifest.xml, apps/android/app/src/main/res/values/app.xml (the app_name string leaves this file; the label comes from the appLabel manifest placeholder), apps/ios/Config/App.xcconfig (iOS app build settings), apps/ios/Config/Project.xcconfig (iOS project build settings), 009 - A new project from the foundation (in-progress), Done when (009): one recorded decision, one command, a hosted check on a temporary copy, clean inherited records, recorded foundation revision, The two apps disagree on their own identity (iOS dev.foundation.mobile / Mobile Foundation / 1.0, Android foundation.mobile / Foundation / 0.1.0), Turn the repository into a new product without hunting for names by hand (+9 more)

### Community 23 - "Generator Tests and Accessibility"
Cohesion: 0.14
Nodes (14): Accessibility (design system), Status conveyed by text or semantics, not color alone, Honor platform reduced-motion setting, Text contrast check (4.5:1 minimum), W3C WCAG 2.2 contrast minimum guidance, Generated drift remediation, Tokens, configuration and localization check, Design system and resources result (seven generator tests) (+6 more)

### Community 24 - "Product Identity Files"
Cohesion: 0.28
Nodes (17): apps/android/identity.properties (Android identity file: applicationId, displayName, versionName, versionCode), apps/ios/Config/Identity.xcconfig (iOS identity file: APP_BUNDLE_IDENTIFIER, APP_DISPLAY_NAME, MARKETING_VERSION, CURRENT_PROJECT_VERSION), Product identity (display name, application IDs, app version): owned by apps/ios/Config/Identity.xcconfig and apps/android/identity.properties; consumed by the Xcode and Gradle builds and scripts/init-project.sh, Project identity state check (init-project.sh --check and --test, CI identity comparison), Product identity result (2026-11-15: test.sh passed with --check printing foundation and --test passing 21 unit tests; both apps carried dev.foundation.mobile, Mobile Foundation, 0.1.0, build 1; a copy derived as Zoë's Proof built and matched its identity file), AC-3: init-project.sh --name --app-id writes name, ID, version 0.1.0 and build 1 into both identity files, with per-value overrides, Build plan: eleven steps, one thin thread first (identity from its file through each build into the running app), then the command, then the proofs and the written path, CI identity comparison: each native job compares the built app's ID and display name (PlistBuddy on Info.plist, aapt2 dump badging on the debug APK) with its identity file and fails on a difference (+9 more)

### Community 25 - "Schemas and Sample Names"
Cohesion: 0.15
Nodes (17): Canonical token schema (tokens.schema.json), Draft 7 schema and native mappings updated together, Draft 7 schemas in shared/specifications, 010 - Schemas free of sample names (planned, needs a decision), Replace the greeting with a first feature without editing a foundation schema, Foundation schemas require sample names: the greeting_recipient key in the localization schema and the greeting typography role in the token schema, Follow-up: two foundation schemas still require sample names (greeting_recipient, the greeting role); this deserves its own scope row, greeting_recipient (+9 more)

### Community 26 - "Scope Workspaces and Build Approach"
Cohesion: 0.24
Nodes (16): Android scope, Android app owns its screen, appearance changes and native localization lookup, Mobile foundation scope (index), Beta workflow (/check verify, then /test), Scope status legend and file numbering convention, Tracer Bullet build approach, Workspace completion at a glance: shared foundation 8 of 10 (open 009, 010), iOS 1 of 2, Android 1 of 2, iOS scope (+8 more)

### Community 27 - "Design Principles and Token Conventions"
Cohesion: 0.21
Nodes (14): Per-target reading order and screen-reader review, Native controls styled with semantic tokens, Design principles, Canonical JSON propagates through code generation, Design definitions compile independently of Cargo and UniFFI, Layout, text measurement, gestures and focus stay in presentation, Semantic names for decisions both apps share, Token conventions (+6 more)

### Community 28 - "Design System and Shared Resource Rules"
Cohesion: 0.25
Nodes (13): Stable role names or same-change migration, Design system rules, Public role name changes require migrating both consumers, Shared resource ownership rules, Shared resources owner (build configuration, localization, brand assets), Incompatible source format changes treated as migrations, Done when (010): the localization schema asks for at least one key and names none, the typography role is named for its purpose, native themes and generator tests follow, and a greeting-free catalog and token set pass generate-design-tokens.sh --check, R16: a breaking change is a migration (token role, resource format, versioned contract) (+5 more)

### Community 29 - "Verification Scopes and Unverified Targets"
Cohesion: 0.15
Nodes (14): Physical hardware verification for simulator-inaccessible capabilities, Android packaging 16 KiB alignment result, iOS compilation result (Xcode 27.1, Swift 6.4, arm64 and x86_64 simulators, unsigned device build), Still unverified targets (the workflow with the derived input and identity comparison steps, physical devices, signed distribution, minimum OS versions, 16 KiB-page Android runtime, x86_64 iOS simulator runtime), Consistent Rust target, NDK linker, minimum API, ABI filters and JNI libraries, Rust archive must match the selected SDK and CPU, 005 - Reproducible local builds and checks (done), Verification record names the targets exercised and the limits of those results (+6 more)

### Community 30 - "Kotlin Rust Call Status"
Cohesion: 0.23
Nodes (7): E, uniffiCheckCallStatus(), UniffiForeignFutureCompleteVoid, uniffiRustCall(), UniffiRustCallStatusErrorHandler, uniffiRustCallWithError(), U

### Community 31 - "Native Token Mapping and Text Scaling"
Cohesion: 0.30
Nodes (12): System text scaling via generated text styles, Native token mapping, Compose sp mapping of logical text units, Jetpack Compose token projection (FoundationTokens), Dynamic Type mapping of headline and reading scales, Logical spacing units adapt to display density, spacingPage role, SwiftUI token projection (FoundationTokens) (+4 more)

### Community 32 - "Derivation Test on a Copy"
Cohesion: 0.21
Nodes (9): AC-9: init-project.sh --test runs the unit tests including the derivation on a temporary copy; scripts/test.sh runs it so the foundation CI job proves the command on every push, Derivation test: copies the files git lists to a temporary folder, runs the copy's own command with sample values, requires --check to print derived and check-architecture.py to pass, then removes the copy, init-project.sh --test: runs the unit tests under tooling/derive/, Unit tests create their own repository in a temporary folder with isolated git configuration; no test touches the real checkout, User stories: one command names a clone, foundation releases arrive by merge, the verification record lists only what ran here, every push proves the command still works, The Linux proof is one unit test, not a second run of scripts/test.sh, Checks for the derivation command: every write, every refusal and both clean…, Run the checked in command on a temporary copy of this checkout. The checkout… (+1 more)

### Community 33 - "Mobile Contract Extension Conventions"
Cohesion: 0.25
Nodes (11): Explicit application records and enums; private core/transport shapes mapped at the adapter, Async and cancellation conventions for future exports, Conventions for extending the mobile contract, Native capability callback interfaces limited to operations the core requires, Typed UniFFI errors with stable variants; user-facing messages translated natively, Deferred: a contract beyond one string (record, typed error, async call), Records, typed errors, async calls and native callbacks have no caller or test yet, Neutral: the first feature needing a record, typed error or async call across the bridge triggers R10 and a new spec (+3 more)

### Community 34 - "Empty Verification Record"
Cohesion: 0.22
Nodes (11): A new product would carry the foundation's verification record, scope rows, hosted run links and knowledge graph as its own, AC-5: the verification record becomes the empty record naming the product, foundation URL and revision, with every target unverified, Empty verification record: names the product, foundation URL and ref, lists every target as still unverified, holds no hosted run link, Positive: products install side by side under their own name and ID, a foundation fix reaches every product by one merge, a half derived checkout fails scripts/test.sh, records start empty, the identity mismatch is gone, every native run proves the built identity, Recommendation: --check does not look for hosted run links, Force: a copy inherits claims it never earned (the verification record and the scope index name a hosted run in the foundation repository), Force: the knowledge graph is tied to this checkout (74 tracked cache files under a path-named folder, one owner specific string), Force: two copies of the foundation carry the same ID, so one installs over the other (+3 more)

### Community 35 - "Generated Files and Drift"
Cohesion: 0.24
Nodes (9): Knowledge graph (graphify-out/, kept current with /graphify . --update), Never hand-edit generated files, Generators consume neutral sources and never recover canonical values from native output, Derived file rule: change the canonical input and regenerate every output in the same review, Decision: keep generated source snapshots in version control and compare against fresh regeneration, Regenerated token files match the checked in copies, Drift detection for checked-in bindings and resources (stale, edited and missing generated files), R5: a generated file is never edited by hand; change the source and regenerate every output (+1 more)

### Community 36 - "Kotlin Handle Map and Lifting"
Cohesion: 0.42
Nodes (4): InternalException, T, UniffiHandleMap, UniffiNullRustCallStatusErrorHandler

### Community 37 - "Design System Guide and Token Schema"
Cohesion: 0.36
Nodes (8): Design system guide, generate-design-tokens.sh modes: write, --check (drift), --test (failure cases), Generated semantic token API consumed by native apps, Five canonical token JSON files (primitives and semantic aliases), tokens.schema.json: single Draft 7 document keyed by filename stem, SHA-pinned GitHub Actions with read-only contents permission, Shared build and generation commands, fastjsonschema==2.21.2 (sha256 hash-pinned schema validator)

### Community 38 - "README and Starting a Product"
Cohesion: 0.44
Nodes (9): Follow-up: build the command that takes a foundation release (fetch, merge, apply the ownership table) when the first release is merged into a product, Follow-up: decide where dependency update bots run (a bot in every product changes foundation owned files and will conflict with merges), Path ownership after derivation: product owned paths keep the product's side, foundation owned paths take the foundation's side, shared paths merge by hand, README section 'Start a project from this foundation': clone at a tag, create a branch, rename the remote, run the command, add origin, rebuild the graph, mark inherited rows existing, commit, record first results, Take a later foundation release: git fetch foundation --tags, git merge foundation-vX.Y.Z, keep the product's side on product owned paths, rebuild the graph, run every check, Tradeoff: every merge of a foundation release reports conflicts on product owned paths, resolved by hand until the sync command exists, README: Native mobile foundation, Take a later foundation release (git fetch foundation --tags, git merge foundation-vX.Y.Z, keep the product's side on product owned paths) (+1 more)

### Community 39 - "Config Schema"
Cohesion: 0.25
Nodes (7): defaultLocale, schemaVersion, additionalProperties, required, $schema, title, type

### Community 40 - "Android App Shell"
Cohesion: 0.43
Nodes (4): MainActivity, FoundationTheme(), Bundle, ComponentActivity

### Community 41 - "Shared Visual Definitions"
Cohesion: 0.38
Nodes (5): FoundationTokens, Palette, 003 - Shared visual definitions (done), Shared named visual values (color, type, spacing, corners, motion), Unproven corner and motion values

### Community 42 - "Config Schema Properties"
Cohesion: 0.33
Nodes (6): const, properties, defaultLocale, schemaVersion, const, type

### Community 43 - "iOS Greeting UI Tests"
Cohesion: 0.50
Nodes (3): UInt8, CIContext, XCUIScreenshot

### Community 44 - "Kotlin FFI Integrity Checks"
Cohesion: 0.60
Nodes (3): IntegrityCheckingUniffiLib, uniffiCheckApiChecksums(), uniffiCheckContractApiVersion()

### Community 45 - "Android Rust Build Script"
Cohesion: 0.40
Nodes (4): CARGO_TARGET_AARCH64_LINUX_ANDROID_LINKER, CARGO_TARGET_X86_64_LINUX_ANDROID_LINKER, PATH, build-android-rust.sh script

### Community 46 - "iOS Rust Build Script"
Cohesion: 0.50
Nodes (3): CARGO_TARGET_DIR, PATH, build-ios-rust.sh script

## Knowledge Gaps
- **56 isolated node(s):** `NoHandle`, `UniffiWithHandle`, `Explicit application records and enums; private core/transport shapes mapped at the adapter`, `apiChecksumMismatch`, `contractVersionMismatch` (+51 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `.body` connect `Native App Shells and Tokens` to `Swift UniFFI Bindings`?**
  _High betweenness centrality (0.146) - this node is a cross-community bridge._
- **Why does `hello()` connect `Swift UniFFI Bindings` to `Native App Shells and Tokens`?**
  _High betweenness centrality (0.144) - this node is a cross-community bridge._
- **Why does `GreetingScreen` connect `Native App Shells and Tokens` to `Rule Set and Agent Workflow`?**
  _High betweenness centrality (0.140) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Foundation verification 2026-11-15` (e.g. with `Record separately what compiled and what ran` and `tooling/derive/verification-record.md (empty verification record template for a derived product)`) actually correct?**
  _`Foundation verification 2026-11-15` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `NoHandle`, `UniffiWithHandle`, `Explicit application records and enums; private core/transport shapes mapped at the adapter` to the rest of the system?**
  _56 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Swift UniFFI Bindings` be split into smaller, more focused modules?**
  _Cohesion score 0.05444596443228454 - nodes in this community are weakly interconnected._
- **Should `Kotlin FFI Library Loading` be split into smaller, more focused modules?**
  _Cohesion score 0.055288461538461536 - nodes in this community are weakly interconnected._