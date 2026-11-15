# Graph Report - mobile  (2026-11-15)

## Corpus Check
- Corpus is ~27,887 words - fits in a single context window. You may not need a graph.

## Summary
- 808 nodes · 2092 edges · 29 communities (28 shown, 1 thin omitted)
- Extraction: 75% EXTRACTED · 25% INFERRED · 0% AMBIGUOUS · INFERRED: 519 edges (avg confidence: 0.89)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Agent Workflow, Rules and Spec 0001
- Planning Path and Dependency Rules
- Swift UniFFI Bindings
- Kotlin FFI Library Loading
- Design Tokens and Architecture Boundaries
- Token Schema, Accessibility and Shared Resources
- Rust Core and Greeting Contract
- Kotlin UniFFI Library Calls
- Native App Shells and Theme Tokens
- Verification Record and CI Checks
- Kotlin FFI Converters
- Resource Generator Script
- Kotlin Rust Call Status
- Android Greeting and Supported OS Scopes
- Kotlin Handle Map and Lifting
- Config Schema
- Kotlin RustBuffer Handling
- Hosted Run and Simulator Results
- Localization Schema and Catalog
- iOS Greeting and Device Coverage
- Android and iOS Scope Ownership
- Reproducible Builds and Drift Checks
- iOS Greeting UI Tests
- Android Rust Build Script
- Gradle Wrapper Script
- iOS Rust Build Script

## God Nodes (most connected - your core abstractions)
1. `Spec 0002: One planning path: a scope row first, then a spec` - 57 edges
2. `UniffiLib` - 54 edges
3. `Spec 0001: One owner per responsibility, with rules kept beside the code` - 53 edges
4. `Decision: a new capability is planned as a scope row and designed in a spec before code; docs/plans and new ADRs are retired in a single change` - 38 edges
5. `Mobile foundation scope (index)` - 37 edges
6. `Foundation verification 2026-11-14` - 35 edges
7. `Rollout: one change in fifteen ordered steps (rules, AGENTS.md, architecture docs, README, validator, delete docs/plans, scope files, spec 0001, knowledge graph)` - 33 edges
8. `UniffiRustCallStatus` - 29 edges
9. `Development rules` - 28 edges
10. `RustBuffer` - 27 edges

## Surprising Connections (you probably didn't know these)
- `fastjsonschema==2.21.2 (sha256 hash-pinned schema validator)` --semantically_similar_to--> `SHA-pinned GitHub Actions with read-only contents permission`  [INFERRED] [semantically similar]
  tooling/codegen/requirements.txt → .github/workflows/foundation.yml
- `Compose presentation with native Material semantics` --references--> `GreetingScreen()`  [INFERRED]
  docs/rules/android-rules.md → apps/android/presentation/src/main/kotlin/foundation/presentation/GreetingScreen.kt
- `Trace screen, generated binding, FFI export and core function before changing shared behavior` --references--> `GreetingScreen()`  [INFERRED]
  docs/rules/development-rules.md → apps/android/presentation/src/main/kotlin/foundation/presentation/GreetingScreen.kt
- `Trace screen, generated binding, FFI export and core function before changing shared behavior` --references--> `GreetingScreen`  [INFERRED]
  docs/rules/development-rules.md → apps/ios/Presentation/GreetingScreen.swift
- `Render the returned Rust string verbatim` --references--> `GreetingScreen`  [INFERRED]
  docs/rules/ios-rules.md → apps/ios/Presentation/GreetingScreen.swift

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Neutral JSON sources validated and generated into native theme and string resources** — design_system_readme_token_files, design_system_readme_tokens_schema, shared_config_readme_foundation_json, shared_localization_readme_catalog_format, design_system_readme_generate_design_tokens_modes, tooling_codegen_requirements_fastjsonschema, design_system_readme_generated_semantic_api, shared_localization_readme_generated_native_strings [INFERRED 0.85]
- **Greeting vertical slice: localized recipient through UniFFI to the Rust formatter** — readme_hello_world_greeting, shared_localization_readme_greeting_recipient, docs_architecture_overview_greeting_call_flow, docs_contracts_ffi_conventions_hello_contract, docs_architecture_overview_foundation_core_hello, docs_architecture_ownership_matrix_crates_mobile_ffi, docs_architecture_ownership_matrix_bindings, readme_uniffi [EXTRACTED 1.00]
- **Canonical source over generated output: edit sources, regenerate, compare snapshots** — agents_never_hand_edit_generated_files, docs_architecture_ownership_matrix_derived_file_rule, docs_architecture_dependency_rules_one_way_generation, docs_decisions_adr_0001_foundation_checked_in_source_snapshots [INFERRED 0.85]
- **Design token pipeline from canonical JSON to native projections** — docs_design_system_token_conventions_canonical_token_sources, design_system_schemas_tokens_schema, scripts_generate_design_tokens, docs_design_system_platform_mapping_swiftui_token_projection, docs_design_system_platform_mapping_compose_token_projection, docs_quality_architecture_compliance_tokens_config_localization_check [INFERRED 0.85]
- **Automated architecture compliance checks** — docs_quality_architecture_compliance_rust_format_and_lint, docs_quality_architecture_compliance_core_and_ffi_contract_tests, docs_quality_architecture_compliance_cargo_dependency_and_governance_check, docs_quality_architecture_compliance_uniffi_generated_files_check, docs_quality_architecture_compliance_tokens_config_localization_check, docs_quality_architecture_compliance_ios_linkage_and_ui_check, docs_quality_architecture_compliance_android_linkage_and_ui_check [EXTRACTED 1.00]
- **Regenerate derived outputs with their canonical source, never hand-edit** — docs_rules_development_rules_regenerate_derived_files, docs_rules_design_system_rules_regenerate_projections, docs_quality_architecture_compliance_generated_drift_remediation, docs_rules_rust_rules_regenerate_after_signature_change, docs_rules_shared_resources_rules_generated_native_strings, docs_rules_anti_duplication_ffi_shapes_in_rust_export [INFERRED 0.85]
- **Hosted run 43593365100 as runtime evidence for the greeting contract, visual definitions, shared text and reproducible builds** — docs_scope_root_002_shared_greeting_contract, docs_scope_root_003_shared_visual_definitions, docs_scope_root_004_shared_settings_text_and_brand_assets, docs_scope_root_005_reproducible_local_builds_and_checks, docs_quality_verification_hosted_run_43593365100, docs_quality_verification [EXTRACTED 1.00]
- **Regenerate and compare checks that keep generated tokens, catalogs and bindings equal to their sources** — docs_scope_root_003_shared_visual_definitions_token_drift_check, docs_scope_root_004_shared_settings_text_and_brand_assets_single_english_catalog, docs_scope_root_005_reproducible_local_builds_and_checks_generated_output_drift_detection, scripts_test [INFERRED 0.85]
- **Verification evidence chain: local checks, hosted jobs and the verification record** — docs_scope_root_005_reproducible_local_builds_and_checks, docs_scope_root_006_hosted_build_verification, docs_scope_root_008_hosted_results_in_the_verification_record, docs_scope_index_hosted_run_43593365100, docs_scope_root_008_hosted_results_in_the_verification_record_single_list_of_unverified_targets [INFERRED 0.85]
- **Shared foundation features 001-005 verified done on commit 58e3d2c with scripts/test.sh** — docs_scope_root_001_ownership_and_development_rules, docs_scope_root_002_shared_greeting_contract, docs_scope_root_003_shared_visual_definitions, docs_scope_root_004_shared_settings_text_and_brand_assets, docs_scope_root_005_reproducible_local_builds_and_checks, scripts_test [EXTRACTED 1.00]
- **Tracer bullet greeting path from shared core to both native screens** — docs_scope_index_tracer_bullet_build_approach, docs_scope_root_002_shared_greeting_contract, docs_scope_root_002_shared_greeting_contract_one_string_in_one_string_out_contract, docs_scope_ios_001_native_ios_greeting, docs_scope_android_001_native_android_greeting, docs_scope_root_006_hosted_build_verification [INFERRED 0.85]
- **Forces that motivate the one-owner-per-responsibility decision** — docs_specs_root_0001_ownership_development_rules_force_two_languages_downstream_of_one_source, docs_specs_root_0001_ownership_development_rules_force_generated_files_beside_handwritten_code, docs_specs_root_0001_ownership_development_rules_force_coding_agents_as_regular_contributors, docs_specs_root_0001_ownership_development_rules_force_one_maintainer, docs_specs_root_0001_ownership_development_rules_force_small_codebase, docs_specs_root_0001_ownership_development_rules_decision_one_owner_per_responsibility [EXTRACTED 1.00]
- **Machine enforcement chain: test.sh runs the validator and both generator drift checks, mirrored by the CI foundation job** — docs_specs_root_0001_ownership_development_rules_enforcement_test_script_and_three_policy_checks, scripts_test, tooling_validation_check_architecture, scripts_generate_bindings, scripts_generate_design_tokens, github_workflows_foundation_foundation_job [EXTRACTED 1.00]
- **Rules that rest on review alone with no automated check** — docs_specs_root_0001_ownership_development_rules_r1_one_authoritative_owner, docs_specs_root_0001_ownership_development_rules_r3_app_trees_do_not_import_one_another, docs_specs_root_0001_ownership_development_rules_r8_real_caller_first, docs_specs_root_0001_ownership_development_rules_r9_search_before_adding, docs_specs_root_0001_ownership_development_rules_r11_handoff_reports_compiled_and_ran_separately, docs_specs_root_0001_ownership_development_rules_r14_bindgen_feature_host_only, docs_specs_root_0001_ownership_development_rules_r15_library_change_transitive_and_size_review, docs_specs_root_0001_ownership_development_rules_r16_breaking_change_is_a_migration, docs_specs_root_0001_ownership_development_rules_r18_service_proposal_requirements [EXTRACTED 1.00]
- **One planning path: a scope row first, then a spec before code, named by the agent instructions, the development rules and the repository structure** — docs_specs_root_0002_one_planning_path_decision_scope_row_then_spec, docs_specs_root_0002_one_planning_path_canonical_planning_pattern, docs_rules_development_rules_scope_row_then_spec, agents_scope_row_and_spec_before_code, docs_scope_root_007_one_planning_path, docs_scope_index, docs_architecture_repository_structure_docs_record_homes, docs_specs_root_0001_ownership_development_rules_r10_scope_row_and_spec_for_capability_spec_for_material_decision [EXTRACTED 1.00]
- **Spec triggers kept in their owner files: when a smaller change needs a spec** — docs_specs_root_0002_one_planning_path_trigger_owner_files, docs_rules_development_rules_spec_triggers_for_smaller_changes, docs_rules_service_rules_spec_for_new_crate_or_boundary, docs_quality_architecture_compliance_spec_for_architecture_change, docs_architecture_dependency_rules_new_edge_proposal, docs_contracts_ffi_conventions_compatibility_versioning, docs_decisions_adr_0001_foundation_revisit_conditions, docs_specs_root_0001_ownership_development_rules_spec_triggers [EXTRACTED 1.00]

## Communities (29 total, 1 thin omitted)

### Community 0 - "Agent Workflow, Rules and Spec 0001"
Cohesion: 0.05
Nodes (86): AGENTS.md: Working in the mobile foundation, Agent workflow: before commit (run /graphify . --update, stage graphify-out with the change), Agent workflow: before editing (locate owner, contract, callers, tests), Agent workflow: before handoff (run checks, report commands and unverified targets), Agent workflow: during implementation (place change in owning layer), Knowledge graph (graphify-out/, kept current with /graphify . --update), Never hand-edit generated files, App trees do not import one another; core never calls platform UI (+78 more)

### Community 1 - "Planning Path and Dependency Rules"
Cohesion: 0.08
Nodes (87): Plan a new capability in the scope and write its spec under docs/specs before code, Dependency rules, New dependency edge needs an owning module, a use case and a test, Architecture overview, docs/ and root AGENTS.md: architecture, decision records, scope and agent workflow, docs/ record homes: docs/scope (what to build and its status), docs/specs (design and decision records), docs/decisions (the founding decision), Mobile contract (FFI conventions), Compatibility: version breaking contracts and coordinate regeneration, both apps and release (+79 more)

### Community 2 - "Swift UniFFI Bindings"
Cohesion: 0.05
Nodes (64): Array, createReader(), createWriter(), Data, FfiConverter, FfiConverterPrimitive, FfiConverterRustBuffer, FfiConverterString (+56 more)

### Community 3 - "Kotlin FFI Library Loading"
Cohesion: 0.05
Nodes (38): Disposable, IntegrityCheckingUniffiLib, NoHandle, UniffiByValue, UniffiCallbackInterfaceClone, UniffiCallbackInterfaceFree, uniffiCheckApiChecksums(), uniffiCheckContractApiVersion() (+30 more)

### Community 4 - "Design Tokens and Architecture Boundaries"
Cohesion: 0.06
Nodes (64): Design system guide, generate-design-tokens.sh modes: write, --check (drift), --test (failure cases), Generated semantic token API consumed by native apps, Five canonical token JSON files (primitives and semantic aliases), tokens.schema.json: single Draft 7 document keyed by filename stem, Architecture boundaries, Documented capability boundary; adapters need an actual caller, Layer: design system (generated Swift/Kotlin values as shared visual vocabulary) (+56 more)

### Community 5 - "Token Schema, Accessibility and Shared Resources"
Cohesion: 0.06
Nodes (50): Canonical token schema (tokens.schema.json), Accessibility (design system), Per-target reading order and screen-reader review, Status conveyed by text or semantics, not color alone, Honor platform reduced-motion setting, System text scaling via generated text styles, Text contrast check (4.5:1 minimum), W3C WCAG 2.2 contrast minimum guidance (+42 more)

### Community 6 - "Rust Core and Greeting Contract"
Cohesion: 0.08
Nodes (38): hello(), preserves_empty_names_and_whitespace(), String, main(), hello(), String, Explicit application records and enums; private core/transport shapes mapped at the adapter, Async and cancellation conventions for future exports (+30 more)

### Community 8 - "Native App Shells and Theme Tokens"
Cohesion: 0.07
Nodes (26): App, MainActivity, FoundationTheme(), FoundationTokens, Palette, GreetingScreen(), MobileFoundationApp, .body (+18 more)

### Community 9 - "Verification Record and CI Checks"
Cohesion: 0.14
Nodes (28): GreetingTest, Android linkage and UI check (Linux CI job, emulator instrumentation), GitHub Actions CI jobs (macOS and Linux), iOS linkage and UI check (macOS CI job, XCTest), Physical hardware verification for simulator-inaccessible capabilities, Foundation verification 2026-11-14, Android compilation result (Gradle 9.3.1, AGP 9.1.0, Temurin 17), Android packaging 16 KiB alignment result (+20 more)

### Community 10 - "Kotlin FFI Converters"
Cohesion: 0.16
Nodes (9): FfiConverter, FfiConverterRustBuffer, FfiConverterString, FfiType, uniffiTraitInterfaceCall(), uniffiTraitInterfaceCallWithError(), ByteBuffer, KotlinType (+1 more)

### Community 11 - "Resource Generator Script"
Cohesion: 0.14
Nodes (19): check_schema(), generate(), load(), projections(), Validate authoritative sources, then materialize or check their projections., unique_members(), validator(), native_text() (+11 more)

### Community 12 - "Kotlin Rust Call Status"
Cohesion: 0.12
Nodes (7): E, uniffiCheckCallStatus(), uniffiRustCall(), UniffiRustCallStatus, UniffiRustCallStatusErrorHandler, uniffiRustCallWithError(), U

### Community 13 - "Android Greeting and Supported OS Scopes"
Cohesion: 0.22
Nodes (13): CoreImage, Android 001 - Native Android greeting (existing), API 36 emulator results (arm64 local, x86_64 hosted) in light and dark, Android app packages both supported CPU architectures, Android 002 - Lowest supported Android and large text (planned), 16 KiB memory page packaging, Declared Android minimum API 24 not yet exercised, Android largest font scale check (+5 more)

### Community 14 - "Kotlin Handle Map and Lifting"
Cohesion: 0.22
Nodes (6): `hello`(), InternalException, T, UniffiHandleMap, UniffiNullRustCallStatusErrorHandler, kotlin

### Community 15 - "Config Schema"
Cohesion: 0.14
Nodes (13): defaultLocale, schemaVersion, additionalProperties, const, properties, defaultLocale, schemaVersion, required (+5 more)

### Community 16 - "Kotlin RustBuffer Handling"
Cohesion: 0.26
Nodes (5): ByReference, ByValue, ForeignBytes, RustBuffer, Pointer

### Community 17 - "Hosted Run and Simulator Results"
Cohesion: 0.26
Nodes (12): Hosted run 43593365100 on commit 6587579 (all three jobs passed), iOS simulator results (iPhone 17 on iOS 27.0 local, iOS 26.5 hosted), 006 - Hosted build verification (done), Android hosted job installs the supported SDK packages, iOS simulator boots in each system appearance before XCTest, Three hosted jobs (foundation, iOS, Android) on the same revision, 008 - Hosted results in the verification record (done), Shared foundation scope (+4 more)

### Community 18 - "Localization Schema and Catalog"
Cohesion: 0.18
Nodes (10): greeting_recipient, additionalProperties, minLength, type, propertyNames, pattern, required, $schema (+2 more)

### Community 19 - "iOS Greeting and Device Coverage"
Cohesion: 0.27
Nodes (8): Android physical device coverage unverified, Deferred: signing, physical device runs and store delivery, iOS 001 - Native iOS greeting (existing), Native text style supporting Dynamic Type, Greeting exposed to accessibility in light and dark appearance, iOS physical device coverage unverified, Unsigned iOS device build linked successfully, SwiftUI

### Community 20 - "Android and iOS Scope Ownership"
Cohesion: 0.33
Nodes (9): Android scope, Android app owns its screen, appearance changes and native localization lookup, Beta workflow (/check verify, then /test), Tracer Bullet build approach, iOS scope, Apple app owns its screen, appearance changes and native localization lookup, 003 - Shared visual definitions (done), Shared named visual values (color, type, spacing, corners, motion) (+1 more)

### Community 21 - "Reproducible Builds and Drift Checks"
Cohesion: 0.36
Nodes (7): Rust format and lint check (rustfmt, Clippy warnings denied), Rust workspace result (Rust 1.100.0, locked build, three tests passed), Pinned compiler and locked dependencies (--locked), Regenerated token files match the checked in copies, 005 - Reproducible local builds and checks (done), Drift detection for checked-in bindings and resources (stale, edited and missing generated files), test.sh script

### Community 22 - "iOS Greeting UI Tests"
Cohesion: 0.38
Nodes (5): GreetingUITests, UInt8, CIContext, XCTestCase, XCUIScreenshot

### Community 23 - "Android Rust Build Script"
Cohesion: 0.40
Nodes (4): CARGO_TARGET_AARCH64_LINUX_ANDROID_LINKER, CARGO_TARGET_X86_64_LINUX_ANDROID_LINKER, PATH, build-android-rust.sh script

### Community 24 - "Gradle Wrapper Script"
Cohesion: 0.83
Nodes (3): gradlew script, die(), warn()

### Community 25 - "iOS Rust Build Script"
Cohesion: 0.50
Nodes (3): CARGO_TARGET_DIR, PATH, build-ios-rust.sh script

## Knowledge Gaps
- **52 isolated node(s):** `.body`, `CoreImage`, `XCTest`, `UniffiWithHandle`, `NoHandle` (+47 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `.body` connect `Native App Shells and Theme Tokens` to `Swift UniFFI Bindings`?**
  _High betweenness centrality (0.140) - this node is a cross-community bridge._
- **Why does `hello()` connect `Swift UniFFI Bindings` to `Native App Shells and Theme Tokens`?**
  _High betweenness centrality (0.137) - this node is a cross-community bridge._
- **Why does `GreetingScreen` connect `Native App Shells and Theme Tokens` to `Agent Workflow, Rules and Spec 0001`, `iOS Greeting and Device Coverage`, `Token Schema, Accessibility and Shared Resources`?**
  _High betweenness centrality (0.135) - this node is a cross-community bridge._
- **Are the 13 inferred relationships involving `Decision: a new capability is planned as a scope row and designed in a spec before code; docs/plans and new ADRs are retired in a single change` (e.g. with `Follow-up (settled by spec 0002): R10 sent a new capability to docs/plans while features are tracked in docs/scope` and `Canonical pattern: a scope row (the brief), a spec before code, one slice through its real caller, progress in the scope row and results in the verification record`) actually correct?**
  _`Decision: a new capability is planned as a scope row and designed in a spec before code; docs/plans and new ADRs are retired in a single change` has 13 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `Mobile foundation scope (index)` (e.g. with `docs/ and root AGENTS.md: architecture, decision records, scope and agent workflow` and `docs/ record homes: docs/scope (what to build and its status), docs/specs (design and decision records), docs/decisions (the founding decision)`) actually correct?**
  _`Mobile foundation scope (index)` has 7 INFERRED edges - model-reasoned connections that need verification._
- **What connects `.body`, `CoreImage`, `XCTest` to the rest of the system?**
  _52 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Agent Workflow, Rules and Spec 0001` be split into smaller, more focused modules?**
  _Cohesion score 0.052184769038701624 - nodes in this community are weakly interconnected._