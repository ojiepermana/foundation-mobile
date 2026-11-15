# Graph Report - mobile  (2026-11-15)

## Corpus Check
- 5 files · ~34,826 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 928 nodes · 2474 edges · 48 communities
- Extraction: 75% EXTRACTED · 25% INFERRED · 0% AMBIGUOUS · INFERRED: 620 edges (avg confidence: 0.89)
- Token cost: 14,500 input · 21,000 output

## Community Hubs (Navigation)
- Swift UniFFI Bindings
- Kotlin FFI Library Loading
- Design Tokens and Architecture Boundaries
- Kotlin UniFFI Library Calls
- Resource Generator and Accessibility
- Planning Path and Spec 0002
- Anti-Duplication and Review Rules
- Spec 0003 Derived Project Path
- Agent Workflow and Architecture Overview
- Rust Core and Greeting Contract
- Verification Record and CI Checks
- Kotlin RustBuffer Handling
- Native Greeting and Supported OS Scopes
- Kotlin FFI Converters
- Ownership Matrix and App Boundaries
- Scope Workspaces and Build Approach
- Governance Checks and Scope Legend
- Init Command State Check
- Dependency Rules and FFI Conventions
- Shared Checks and Derived Workflow Run
- Localization Schema and Sample Names
- Native Component and Android Rules
- Rust Checks and Derivation Test
- Config Schema
- Native Token Mapping and Text Scaling
- Derivation Decision and Rationale
- iOS App Shell and Tokens
- Android Theme Tokens
- Kotlin Rust Call Status
- Design Principles
- Reproducible Builds and Foundation Origin
- Native Identity Config Files
- Android App Shell
- Product Identity Files and Criteria
- Design System and Shared Resource Rules
- Generated Drift and Regeneration
- Kotlin Handle Map and Lifting
- Design System Guide and Token Schema
- Hosted Run and Simulator Results
- iOS Greeting UI Tests
- Gradle Wrapper Script
- Mobile Contract Extension Conventions
- Kotlin FFI Integrity Checks
- Android Rust Build Script
- iOS Rust Build Script

## God Nodes (most connected - your core abstractions)
1. `Spec 0003: A new project from the foundation: product identity in two files, one init command, updates by merge (Proposed)` - 62 edges
2. `Spec 0002: One planning path: a scope row first, then a spec` - 60 edges
3. `Spec 0001: One owner per responsibility, with rules kept beside the code` - 56 edges
4. `UniffiLib` - 54 edges
5. `Foundation verification 2026-11-14` - 43 edges
6. `Mobile foundation scope (index)` - 42 edges
7. `Decision: a new capability is planned as a scope row and designed in a spec before code; docs/plans and new ADRs are retired in a single change` - 38 edges
8. `Rollout: one change in fifteen ordered steps (rules, AGENTS.md, architecture docs, README, validator, delete docs/plans, scope files, spec 0001, knowledge graph)` - 33 edges
9. `UniffiRustCallStatus` - 29 edges
10. `ADR 0001: Native apps with a shared Rust core` - 29 edges

## Surprising Connections (you probably didn't know these)
- `iOS linkage and UI check (macOS CI job, XCTest)` --references--> `GreetingUITests`  [INFERRED]
  docs/quality/architecture-compliance.md → apps/ios/UITests/GreetingUITests.swift
- `Hosted ios job result (macos-26-arm64, Xcode 26.5, iPhone 17 simulator on iOS 26.5, light and dark)` --references--> `GreetingUITests`  [INFERRED]
  docs/quality/verification.md → apps/ios/UITests/GreetingUITests.swift
- `iOS runtime result (iPhone 17 simulator, iOS 27.0, light and dark)` --references--> `GreetingUITests`  [INFERRED]
  docs/quality/verification.md → apps/ios/UITests/GreetingUITests.swift
- `Tokens, configuration and localization check` --references--> `GenerationTests`  [INFERRED]
  docs/quality/architecture-compliance.md → tooling/codegen/test_generation.py
- `Greeting as a single text element` --references--> `GreetingScreen`  [INFERRED]
  docs/design-system/component-guidelines.md → apps/ios/Presentation/GreetingScreen.swift

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **One init command turns a foundation clone into a derived product: identity files, README origin line, empty verification record, removed knowledge graph** — scripts_init_project, tooling_derive_init_project, apps_ios_config_identity, apps_android_identity, docs_specs_root_0003_new_project_from_foundation_readme_origin_line, docs_specs_root_0003_new_project_from_foundation_empty_verification_record, docs_specs_root_0003_new_project_from_foundation_init_write_set, docs_specs_root_0003_new_project_from_foundation_repository_states_foundation_derived_mixed [EXTRACTED 1.00]
- **Proof that derivation still works: --check state test, derivation unit test on a temporary copy in scripts/test.sh, CI identity comparison, manual workflow run with derived set** — docs_specs_root_0003_new_project_from_foundation_check_form, docs_specs_root_0003_new_project_from_foundation_test_form, docs_specs_root_0003_new_project_from_foundation_derivation_test, docs_specs_root_0003_new_project_from_foundation_ci_identity_comparison, docs_specs_root_0003_new_project_from_foundation_workflow_derived_input, scripts_test, github_workflows_foundation [INFERRED 0.85]
- **Tracer bullet greeting path from shared core to both native screens** — docs_scope_index_tracer_bullet_build_approach, docs_scope_root_002_shared_greeting_contract, docs_scope_root_002_shared_greeting_contract_one_string_in_one_string_out_contract, docs_scope_ios_001_native_ios_greeting, docs_scope_android_001_native_android_greeting, docs_scope_root_006_hosted_build_verification [INFERRED 0.85]
- **Hosted run 43593365100 as runtime evidence for the greeting contract, visual definitions, shared text and reproducible builds** — docs_scope_root_002_shared_greeting_contract, docs_scope_root_003_shared_visual_definitions, docs_scope_root_004_shared_settings_text_and_brand_assets, docs_scope_root_005_reproducible_local_builds_and_checks, docs_quality_verification_hosted_run_43593365100, docs_quality_verification [EXTRACTED 1.00]
- **Regenerate and compare checks that keep generated tokens, catalogs and bindings equal to their sources** — docs_scope_root_003_shared_visual_definitions_token_drift_check, docs_scope_root_004_shared_settings_text_and_brand_assets_single_english_catalog, docs_scope_root_005_reproducible_local_builds_and_checks_generated_output_drift_detection, scripts_test [INFERRED 0.85]
- **Automated architecture compliance checks** — docs_quality_architecture_compliance_rust_format_and_lint, docs_quality_architecture_compliance_core_and_ffi_contract_tests, docs_quality_architecture_compliance_cargo_dependency_and_governance_check, docs_quality_architecture_compliance_uniffi_generated_files_check, docs_quality_architecture_compliance_tokens_config_localization_check, docs_quality_architecture_compliance_ios_linkage_and_ui_check, docs_quality_architecture_compliance_android_linkage_and_ui_check [EXTRACTED 1.00]
- **Greeting vertical slice: localized recipient through UniFFI to the Rust formatter** — readme_hello_world_greeting, shared_localization_readme_greeting_recipient, docs_architecture_overview_greeting_call_flow, docs_contracts_ffi_conventions_hello_contract, docs_architecture_overview_foundation_core_hello, docs_architecture_ownership_matrix_crates_mobile_ffi, docs_architecture_ownership_matrix_bindings, readme_uniffi [EXTRACTED 1.00]
- **One planning path: a scope row first, then a spec before code, named by the agent instructions, the development rules and the repository structure** — docs_specs_root_0002_one_planning_path_decision_scope_row_then_spec, docs_specs_root_0002_one_planning_path_canonical_planning_pattern, docs_rules_development_rules_scope_row_then_spec, agents_scope_row_and_spec_before_code, docs_scope_root_007_one_planning_path, docs_scope_index, docs_architecture_repository_structure_docs_record_homes, docs_specs_root_0001_ownership_development_rules_r10_scope_row_and_spec_for_capability_spec_for_material_decision [EXTRACTED 1.00]
- **Forces that motivate the one-owner-per-responsibility decision** — docs_specs_root_0001_ownership_development_rules_force_two_languages_downstream_of_one_source, docs_specs_root_0001_ownership_development_rules_force_generated_files_beside_handwritten_code, docs_specs_root_0001_ownership_development_rules_force_coding_agents_as_regular_contributors, docs_specs_root_0001_ownership_development_rules_force_one_maintainer, docs_specs_root_0001_ownership_development_rules_force_small_codebase, docs_specs_root_0001_ownership_development_rules_decision_one_owner_per_responsibility [EXTRACTED 1.00]
- **Machine enforcement chain: test.sh runs the validator and both generator drift checks, mirrored by the CI foundation job** — docs_specs_root_0001_ownership_development_rules_enforcement_test_script_and_three_policy_checks, scripts_test, tooling_validation_check_architecture, scripts_generate_bindings, scripts_generate_design_tokens, github_workflows_foundation_foundation_job [EXTRACTED 1.00]
- **Rules that rest on review alone with no automated check** — docs_specs_root_0001_ownership_development_rules_r1_one_authoritative_owner, docs_specs_root_0001_ownership_development_rules_r3_app_trees_do_not_import_one_another, docs_specs_root_0001_ownership_development_rules_r8_real_caller_first, docs_specs_root_0001_ownership_development_rules_r9_search_before_adding, docs_specs_root_0001_ownership_development_rules_r11_handoff_reports_compiled_and_ran_separately, docs_specs_root_0001_ownership_development_rules_r14_bindgen_feature_host_only, docs_specs_root_0001_ownership_development_rules_r15_library_change_transitive_and_size_review, docs_specs_root_0001_ownership_development_rules_r16_breaking_change_is_a_migration, docs_specs_root_0001_ownership_development_rules_r18_service_proposal_requirements [EXTRACTED 1.00]
- **Spec triggers kept in their owner files: when a smaller change needs a spec** — docs_specs_root_0002_one_planning_path_trigger_owner_files, docs_rules_development_rules_spec_triggers_for_smaller_changes, docs_rules_service_rules_spec_for_new_crate_or_boundary, docs_quality_architecture_compliance_spec_for_architecture_change, docs_architecture_dependency_rules_new_edge_proposal, docs_contracts_ffi_conventions_compatibility_versioning, docs_decisions_adr_0001_foundation_revisit_conditions, docs_specs_root_0001_ownership_development_rules_spec_triggers [EXTRACTED 1.00]
- **Canonical source over generated output: edit sources, regenerate, compare snapshots** — agents_never_hand_edit_generated_files, docs_architecture_ownership_matrix_derived_file_rule, docs_architecture_dependency_rules_one_way_generation, docs_decisions_adr_0001_foundation_checked_in_source_snapshots [INFERRED 0.85]
- **Design token pipeline from canonical JSON to native projections** — docs_design_system_token_conventions_canonical_token_sources, design_system_schemas_tokens_schema, scripts_generate_design_tokens, docs_design_system_platform_mapping_swiftui_token_projection, docs_design_system_platform_mapping_compose_token_projection, docs_quality_architecture_compliance_tokens_config_localization_check [INFERRED 0.85]
- **Neutral JSON sources validated and generated into native theme and string resources** — design_system_readme_token_files, design_system_readme_tokens_schema, shared_config_readme_foundation_json, shared_localization_readme_catalog_format, design_system_readme_generate_design_tokens_modes, tooling_codegen_requirements_fastjsonschema, design_system_readme_generated_semantic_api, shared_localization_readme_generated_native_strings [INFERRED 0.85]
- **Regenerate derived outputs with their canonical source, never hand-edit** — docs_rules_development_rules_regenerate_derived_files, docs_rules_design_system_rules_regenerate_projections, docs_quality_architecture_compliance_generated_drift_remediation, docs_rules_rust_rules_regenerate_after_signature_change, docs_rules_shared_resources_rules_generated_native_strings, docs_rules_anti_duplication_ffi_shapes_in_rust_export [INFERRED 0.85]
- **Verification evidence chain: local checks, hosted jobs and the verification record** — docs_scope_root_005_reproducible_local_builds_and_checks, docs_scope_root_006_hosted_build_verification, docs_scope_root_008_hosted_results_in_the_verification_record, docs_scope_index_hosted_run_43593365100, docs_scope_root_008_hosted_results_in_the_verification_record_single_list_of_unverified_targets [INFERRED 0.85]

## Communities (48 total, 0 thin omitted)

### Community 0 - "Swift UniFFI Bindings"
Cohesion: 0.05
Nodes (64): Array, createReader(), createWriter(), Data, FfiConverter, FfiConverterPrimitive, FfiConverterRustBuffer, FfiConverterString (+56 more)

### Community 1 - "Kotlin FFI Library Loading"
Cohesion: 0.06
Nodes (34): Disposable, NoHandle, UniffiByValue, UniffiCallbackInterfaceClone, UniffiCallbackInterfaceFree, UniffiForeignFutureCompleteF32, UniffiForeignFutureCompleteF64, UniffiForeignFutureCompleteI16 (+26 more)

### Community 2 - "Design Tokens and Architecture Boundaries"
Cohesion: 0.06
Nodes (55): Knowledge graph (graphify-out/, kept current with /graphify . --update), Never hand-edit generated files, Architecture boundaries, Layer: design system (generated Swift/Kotlin values as shared visual vocabulary), Layer: native platform integration (Swift owns Apple services, Kotlin owns Android services), Layer: native presentation (views render, adapt to appearance, handle events), Layer: resources and tooling (build-host validation and generation), Layer: shared Rust (core owns behavior, FFI crate maps exports) (+47 more)

### Community 3 - "Kotlin UniFFI Library Calls"
Cohesion: 0.06
Nodes (3): UniffiLib, UniffiRustCallStatus, UniffiRustFutureContinuationCallback

### Community 4 - "Resource Generator and Accessibility"
Cohesion: 0.08
Nodes (28): Accessibility (design system), Per-target reading order and screen-reader review, Status conveyed by text or semantics, not color alone, Honor platform reduced-motion setting, Text contrast check (4.5:1 minimum), W3C WCAG 2.2 contrast minimum guidance, Design system and resources result (seven generator tests), Light and dark text meet the documented contrast threshold (+20 more)

### Community 5 - "Planning Path and Spec 0002"
Cohesion: 0.12
Nodes (39): Deferred work beyond Hello World, The list of deferred work lives in one file, Premise: rule files stay authoritative; the spec records the decision, rule set and enforcement, not a second copy, Spec 0002: One planning path: a scope row first, then a spec, ADR 0001 is not reworded, Decide first, always: a spec before code reaches main, Decision: a new capability is planned as a scope row and designed in a spec before code; docs/plans and new ADRs are retired in a single change, Delete the guide, do not leave a pointer (+31 more)

### Community 6 - "Anti-Duplication and Review Rules"
Cohesion: 0.13
Nodes (34): Rejected alternative: implementing application behavior independently in both apps, Limits of CI checks, Reviewers trace changed behavior from owner into each client, Anti-duplication rules, Locate the owner before adding a constant, rule, DTO, translation or asset, Reviewers assess semantic duplication, Spec 0001: One owner per responsibility, with rules kept beside the code, Automate only what a machine can judge (+26 more)

### Community 7 - "Spec 0003 Derived Project Path"
Cohesion: 0.11
Nodes (33): A new product would carry the foundation's verification record, scope rows, hosted run links and knowledge graph as its own, Spec 0003: A new project from the foundation: product identity in two files, one init command, updates by merge (Proposed), AC-11: README.md has a section with the full path from clone to first results, path ownership, taking a later release and foundation tagging, AC-5: the verification record becomes the empty record naming the product, foundation URL and revision, with every target unverified, Empty verification record: names the product, foundation URL and ref, lists every target as still unverified, holds no hosted run link, Follow-up: build the command that takes a foundation release (fetch, merge, apply the ownership table) when the first release is merged into a product, Follow-up: decide where dependency update bots run (a bot in every product changes foundation owned files and will conflict with merges), Follow-up: write how a change proven in a product returns to the foundation once a product closes a Deferred item (+25 more)

### Community 8 - "Agent Workflow and Architecture Overview"
Cohesion: 0.17
Nodes (31): AGENTS.md: Working in the mobile foundation, Agent workflow: before commit (run /graphify . --update, stage graphify-out with the change), Agent workflow: before handoff (run checks, report commands and unverified targets), Agent workflow: during implementation (place change in owning layer), Plan a new capability in the scope and write its spec under docs/specs before code, Architecture overview, docs/ and root AGENTS.md: architecture, decision records, scope and agent workflow, docs/ record homes: docs/scope (what to build and its status), docs/specs (design and decision records), docs/decisions (the founding decision) (+23 more)

### Community 9 - "Rust Core and Greeting Contract"
Cohesion: 0.12
Nodes (26): hello(), preserves_empty_names_and_whitespace(), String, main(), hello(), String, tests/contracts: Cargo integration tests for exported behavior, Core and FFI contract tests (locked Cargo tests) (+18 more)

### Community 10 - "Verification Record and CI Checks"
Cohesion: 0.15
Nodes (27): GreetingTest, Android linkage and UI check (Linux CI job, emulator instrumentation), GitHub Actions CI jobs (macOS and Linux), iOS linkage and UI check (macOS CI job, XCTest), Physical hardware verification for simulator-inaccessible capabilities, Foundation verification 2026-11-14, Android compilation result (Gradle 9.3.1, AGP 9.1.0, Temurin 17), Android packaging 16 KiB alignment result (+19 more)

### Community 11 - "Kotlin RustBuffer Handling"
Cohesion: 0.14
Nodes (9): ByReference, ByValue, ForeignBytes, `hello`(), RustBuffer, uniffiTraitInterfaceCall(), uniffiTraitInterfaceCallWithError(), kotlin (+1 more)

### Community 12 - "Native Greeting and Supported OS Scopes"
Cohesion: 0.16
Nodes (20): CoreImage, Android 001 - Native Android greeting (existing), API 36 emulator results (arm64 local, x86_64 hosted) in light and dark, Android app packages both supported CPU architectures, Android physical device coverage unverified, Android 002 - Lowest supported Android and large text (planned), 16 KiB memory page packaging, Declared Android minimum API 24 not yet exercised (+12 more)

### Community 13 - "Kotlin FFI Converters"
Cohesion: 0.21
Nodes (7): FfiConverter, FfiConverterRustBuffer, FfiConverterString, FfiType, ByteBuffer, KotlinType, ULong

### Community 14 - "Ownership Matrix and App Boundaries"
Cohesion: 0.23
Nodes (19): Agent workflow: before editing (locate owner, contract, callers, tests), App trees do not import one another; core never calls platform UI, Ownership matrix, apps/android: owner of Android UI, presentation state and OS APIs, apps/ios: owner of Apple UI, presentation state and OS APIs, design-system/tokens and schemas: owner of canonical visual values and semantic roles, scripts/ and .github/workflows/: build and verification orchestration, shared/config, shared/localization, shared/assets: owner of public settings, locale content and brand masters (+11 more)

### Community 15 - "Scope Workspaces and Build Approach"
Cohesion: 0.19
Nodes (18): Android scope, Android app owns its screen, appearance changes and native localization lookup, Beta workflow (/check verify, then /test), Tracer Bullet build approach, Workspace completion at a glance: shared foundation 8 of 10 (open 009, 010), iOS 1 of 2, Android 1 of 2, iOS scope, Apple app owns its screen, appearance changes and native localization lookup, 002 - Shared greeting contract (done) (+10 more)

### Community 16 - "Governance Checks and Scope Legend"
Cohesion: 0.21
Nodes (17): Cargo dependency and governance check, Architecture policy result (dependency and required-document checks), Scope status legend and file numbering convention, 007 - One planning path (done), Required document check covers the scope index, Follow-up (settled by spec 0002): record keeping (ADR and plan naming, REQUIRED_DOCS membership, superseding, whether a spec satisfies R10), Follow-up (settled by spec 0002): docs/specs and docs/scope were named by neither repository-structure.md nor REQUIRED_DOCS, R13: the governing documents exist and are not empty (REQUIRED_DOCS) (+9 more)

### Community 17 - "Init Command State Check"
Cohesion: 0.15
Nodes (19): The two apps disagree on their own identity (iOS dev.foundation.mobile / Mobile Foundation / 1.0, Android foundation.mobile / Foundation / 0.1.0), AC-7: the command refuses, changes nothing and exits 2 with a one line reason (bad input, default ID, dirty tree, derived or mixed checkout, missing foundation URL or ref), AC-8: init-project.sh --check prints foundation or derived and exits 0, exits 1 naming each mismatch in a mixed state; scripts/test.sh runs it, Recommendation: --check accepts two states, foundation and derived, init-project.sh --check: prints foundation or derived (exit 0) or names each mismatch in a mixed state (exit 1), Recommendation: the command refuses to run on a derived checkout, Default foundation identity: dev.foundation.mobile, Mobile Foundation, version 0.1.0, build 1, Follow-up: decide in the release path spec whether the iOS and Android versions must match, and add that test to --check if they must (+11 more)

### Community 18 - "Dependency Rules and FFI Conventions"
Cohesion: 0.28
Nodes (18): Documented capability boundary; adapters need an actual caller, Dependency rules, New dependency edge needs an owning module, a use case and a test, Mobile contract (FFI conventions), Compatibility: version breaking contracts and coordinate regeneration, both apps and release, Revisit conditions: dependency direction change, async native boundary, independently versioned clients, new shared crate or service, Architecture compliance, Spec under docs/specs and policy update for a new dependency or material architecture change (+10 more)

### Community 19 - "Shared Checks and Derived Workflow Run"
Cohesion: 0.23
Nodes (15): Enforcement: scripts/test.sh runs format, lint, tests and three policy checks; CI runs the same script plus iOS and Android jobs, Worked example: a change to shared behavior (core, export, regenerate bindings, both call sites, checks, report), AC-10: the workflow accepts a manual run with the derived input, and every native job compares the built app's ID and display name with the identity file, CI identity comparison: each native job compares the built app's ID and display name (PlistBuddy on Info.plist, aapt2 dump badging on the debug APK) with its identity file and fails on a difference, Release the foundation: run the workflow by hand with derived set, then push an annotated foundation-vMAJOR.MINOR.PATCH tag on main, Workflow input derived (workflow_dispatch boolean): the ios and android jobs run the command on the runner checkout, then build and test under the sample identity, Mobile foundation CI workflow, CI job: android (JDK 17, API 36 emulator, Kotlin binding + Compose UI) (+7 more)

### Community 20 - "Localization Schema and Sample Names"
Cohesion: 0.17
Nodes (15): Canonical token schema (tokens.schema.json), 010 - Schemas free of sample names (planned, needs a decision), Replace the greeting with a first feature without editing a foundation schema, Foundation schemas require sample names: the greeting_recipient key in the localization schema and the greeting typography role in the token schema, Follow-up: two foundation schemas still require sample names (greeting_recipient, the greeting role); this deserves its own scope row, greeting_recipient, additionalProperties, minLength (+7 more)

### Community 21 - "Native Component and Android Rules"
Cohesion: 0.16
Nodes (15): Native components guidelines, Reusable native component (introduced on demand), Android rules, New ABI requires Rust cross-build and runtime test, Application code displays the binding's return value, OS-specific capability stays in its own app, Drift check plus verification in both appearances and larger text sizes, iOS rules (+7 more)

### Community 22 - "Rust Checks and Derivation Test"
Cohesion: 0.23
Nodes (13): Rust format and lint check (rustfmt, Clippy warnings denied), Rust workspace result (Rust 1.100.0, locked build, three tests passed), AC-9: init-project.sh --test runs the unit tests including the derivation on a temporary copy; scripts/test.sh runs it so the foundation CI job proves the command on every push, Derivation test: copies the files git lists to a temporary folder, runs the copy's own command with sample values, requires --check to print derived and check-architecture.py to pass, then removes the copy, The Linux proof runs on every push; the native proof runs by hand before a foundation tag, The Linux proof is one unit test, not a second run of scripts/test.sh, Sample values: --name "Zoë's Proof" --app-id dev.example.derived, foundation URL https://example.invalid/foundation, ref foundation-v0.0.0, date 2026-01-01, init-project.sh --test: runs the unit tests under tooling/derive/ (+5 more)

### Community 23 - "Config Schema"
Cohesion: 0.14
Nodes (13): defaultLocale, schemaVersion, additionalProperties, const, properties, defaultLocale, schemaVersion, required (+5 more)

### Community 24 - "Native Token Mapping and Text Scaling"
Cohesion: 0.29
Nodes (13): System text scaling via generated text styles, Native token mapping, Compose sp mapping of logical text units, Jetpack Compose token projection (FoundationTokens), Dynamic Type mapping of headline and reading scales, Logical spacing units adapt to display density, spacingPage role, SwiftUI token projection (FoundationTokens) (+5 more)

### Community 25 - "Derivation Decision and Rationale"
Cohesion: 0.24
Nodes (13): Done when (009): one recorded decision, one command, a hosted check on a temporary copy, clean inherited records, recorded foundation revision, Recommendation: --check does not look for hosted run links, Decision: a product is a clone that changes only its display name, application ID and version through scripts/init-project.sh, keeps every other name, starts with an empty verification record and merges foundation-v tags, Force: stable names make a merge clean (31 code and config files and 13 paths carry the foundation name), The narrow choice comes first: a full rename stays possible later inside one product, the reverse move does not, Every native run compares the built app with the identity file, No References section, One name and one application ID as input (+5 more)

### Community 26 - "iOS App Shell and Tokens"
Cohesion: 0.18
Nodes (9): App, MobileFoundationApp, .body, GreetingScreen, .body, String, Scene, SwiftUI (+1 more)

### Community 27 - "Android Theme Tokens"
Cohesion: 0.20
Nodes (9): FoundationTokens, Palette, FoundationTokens, Palette, CGFloat, Color, ColorScheme, Font (+1 more)

### Community 28 - "Kotlin Rust Call Status"
Cohesion: 0.23
Nodes (7): E, uniffiCheckCallStatus(), UniffiForeignFutureCompleteVoid, uniffiRustCall(), UniffiRustCallStatusErrorHandler, uniffiRustCallWithError(), U

### Community 29 - "Design Principles"
Cohesion: 0.24
Nodes (12): Native controls styled with semantic tokens, Design principles, Canonical JSON propagates through code generation, Design definitions compile independently of Cargo and UniFFI, Layout, text measurement, gestures and focus stay in presentation, Semantic names for decisions both apps share, Token conventions, Canonical token sources (colors, typography, spacing, radius, motion JSON) (+4 more)

### Community 30 - "Reproducible Builds and Foundation Origin"
Cohesion: 0.18
Nodes (11): target/, build/ and Gradle build directories excluded from source control, Pinned compiler and locked dependencies (--locked), R12: binaries, signing material, SDK paths and IDE data stay out; compiler and dependencies pinned, builds use --locked, AC-6: README.md has the product name as title on line 1 and the origin line on line 3 followed by one blank line, Foundation ref resolution: --foundation-ref, else the highest foundation-v* tag exactly at HEAD, else the full HEAD commit ID, Foundation URL sourcing and normalization: --foundation-url, else the foundation remote, else origin; https, http, ssh and user@host:path forms written as https without user, token, .git or trailing slash, Recommendation: tags are named foundation-vMAJOR.MINOR.PATCH, Neutral: /develop moves the spec to In Progress and Accepted with scope row 009; creating the first tag foundation-v0.1.0 is the maintainer's step (+3 more)

### Community 31 - "Native Identity Config Files"
Cohesion: 0.31
Nodes (9): apps/android/app/src/main/AndroidManifest.xml, apps/android/app/src/main/res/values/app.xml (app_name string), apps/ios/Config/App.xcconfig (iOS app build settings), apps/ios/Config/Project.xcconfig (iOS project build settings), apps/ios/MobileFoundation.xcodeproj/project.pbxproj (Xcode project file), Android build reads identity.properties: app/build.gradle.kts loads applicationId, versionName and versionCode, the label reaches the manifest as the appLabel placeholder, namespace stays foundation.mobile, Force: identity is spread over files the foundation keeps editing (App.xcconfig, Project.xcconfig, project.pbxproj, app/build.gradle.kts, res/values/app.xml), iOS build reads Identity.xcconfig: Project.xcconfig includes it, App.xcconfig maps the bundle ID and display name, the UI test bundle ID is derived as $(APP_BUNDLE_IDENTIFIER).uitests (+1 more)

### Community 32 - "Android App Shell"
Cohesion: 0.29
Nodes (6): MainActivity, FoundationTheme(), GreetingScreen(), Bundle, ComponentActivity, Greeting as a single text element

### Community 33 - "Product Identity Files and Criteria"
Cohesion: 0.36
Nodes (10): apps/android/identity.properties (Android identity file: applicationId, displayName, versionName, versionCode), apps/ios/Config/Identity.xcconfig (iOS identity file: APP_BUNDLE_IDENTIFIER, APP_DISPLAY_NAME, MARKETING_VERSION, CURRENT_PROJECT_VERSION), Build steps (009): identity file per platform (AC-1, AC-2), init command with state check and unit tests (AC-3 to AC-9), workflow derived input and identity comparison (AC-10), README path and document updates (AC-11, AC-12), AC-1: both apps carry the same default identity, read from Identity.xcconfig and identity.properties, stated nowhere else under apps/, AC-2: with the default identity scripts/test.sh passes, both apps build and the greeting tests pass in both appearances, AC-3: init-project.sh --name --app-id writes name, ID, version 0.1.0 and build 1 into both identity files, with per-value overrides, AC-4: the write set is exactly the two identity files, README.md, the verification record and the removed graphify-out/ files; nothing is renamed, Build plan: eleven steps, one thin thread first (identity from its file through each build into the running app), then the command, then the proofs and the written path (+2 more)

### Community 34 - "Design System and Shared Resource Rules"
Cohesion: 0.36
Nodes (10): Stable role names or same-change migration, Design system rules, Public role name changes require migrating both consumers, Draft 7 schema and native mappings updated together, Shared visual values live in design-system/tokens, Shared resource ownership rules, Draft 7 schemas in shared/specifications, Incompatible source format changes treated as migrations (+2 more)

### Community 35 - "Generated Drift and Regeneration"
Cohesion: 0.29
Nodes (9): Generated drift remediation, Tokens, configuration and localization check, Shared visual decisions and translations are generator inputs, Regenerate native projections in the same change, Regenerate derived files alongside canonical inputs, Generated native strings owned by the resource generator, Done when (010): the localization schema asks for at least one key and names none, the typography role is named for its purpose, native themes and generator tests follow, and a greeting-free catalog and token set pass generate-design-tokens.sh --check, PYTHONPATH (+1 more)

### Community 36 - "Kotlin Handle Map and Lifting"
Cohesion: 0.42
Nodes (4): InternalException, T, UniffiHandleMap, UniffiNullRustCallStatusErrorHandler

### Community 37 - "Design System Guide and Token Schema"
Cohesion: 0.36
Nodes (8): Design system guide, generate-design-tokens.sh modes: write, --check (drift), --test (failure cases), Generated semantic token API consumed by native apps, Five canonical token JSON files (primitives and semantic aliases), tokens.schema.json: single Draft 7 document keyed by filename stem, SHA-pinned GitHub Actions with read-only contents permission, Shared build and generation commands, fastjsonschema==2.21.2 (sha256 hash-pinned schema validator)

### Community 38 - "Hosted Run and Simulator Results"
Cohesion: 0.39
Nodes (8): Hosted run 43593365100 on commit 6587579 (all three jobs passed), iOS simulator results (iPhone 17 on iOS 27.0 local, iOS 26.5 hosted), 006 - Hosted build verification (done), Android hosted job installs the supported SDK packages, iOS simulator boots in each system appearance before XCTest, Three hosted jobs (foundation, iOS, Android) on the same revision, 008 - Hosted results in the verification record (done), Follow-up: verification.md says hosted jobs have not run while the scope index records a passing run

### Community 39 - "iOS Greeting UI Tests"
Cohesion: 0.38
Nodes (5): GreetingUITests, UInt8, CIContext, XCTestCase, XCUIScreenshot

### Community 40 - "Gradle Wrapper Script"
Cohesion: 0.47
Nodes (5): gradlew script, die(), warn(), Checked-in Gradle wrapper, Binaries, signing material, SDK paths and IDE data stay outside the repository

### Community 41 - "Mobile Contract Extension Conventions"
Cohesion: 0.47
Nodes (6): Explicit application records and enums; private core/transport shapes mapped at the adapter, Async and cancellation conventions for future exports, Conventions for extending the mobile contract, Native capability callback interfaces limited to operations the core requires, Typed UniFFI errors with stable variants; user-facing messages translated natively, Records, typed errors, async calls and native callbacks have no caller or test yet

### Community 42 - "Kotlin FFI Integrity Checks"
Cohesion: 0.60
Nodes (3): IntegrityCheckingUniffiLib, uniffiCheckApiChecksums(), uniffiCheckContractApiVersion()

### Community 43 - "Android Rust Build Script"
Cohesion: 0.40
Nodes (4): CARGO_TARGET_AARCH64_LINUX_ANDROID_LINKER, CARGO_TARGET_X86_64_LINUX_ANDROID_LINKER, PATH, build-android-rust.sh script

### Community 44 - "iOS Rust Build Script"
Cohesion: 0.50
Nodes (3): CARGO_TARGET_DIR, PATH, build-ios-rust.sh script

## Knowledge Gaps
- **55 isolated node(s):** `NoHandle`, `UniffiWithHandle`, `build-android.sh script`, `build-ios.sh script`, `PYTHONPATH` (+50 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `.body` connect `iOS App Shell and Tokens` to `Swift UniFFI Bindings`?**
  _High betweenness centrality (0.130) - this node is a cross-community bridge._
- **Why does `hello()` connect `Swift UniFFI Bindings` to `iOS App Shell and Tokens`?**
  _High betweenness centrality (0.128) - this node is a cross-community bridge._
- **Why does `GreetingScreen` connect `iOS App Shell and Tokens` to `Android App Shell`, `Rust Core and Greeting Contract`, `Native Component and Android Rules`, `Native Token Mapping and Text Scaling`?**
  _High betweenness centrality (0.126) - this node is a cross-community bridge._
- **What connects `NoHandle`, `UniffiWithHandle`, `build-android.sh script` to the rest of the system?**
  _55 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Swift UniFFI Bindings` be split into smaller, more focused modules?**
  _Cohesion score 0.05444596443228454 - nodes in this community are weakly interconnected._
- **Should `Kotlin FFI Library Loading` be split into smaller, more focused modules?**
  _Cohesion score 0.055288461538461536 - nodes in this community are weakly interconnected._
- **Should `Design Tokens and Architecture Boundaries` be split into smaller, more focused modules?**
  _Cohesion score 0.0647307924984876 - nodes in this community are weakly interconnected._