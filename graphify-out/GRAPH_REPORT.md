# Graph Report - mobile  (2026-11-15)

## Corpus Check
- 3 files · ~72,299 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1071 nodes · 2932 edges · 50 communities
- Extraction: 76% EXTRACTED · 24% INFERRED · 0% AMBIGUOUS · INFERRED: 695 edges (avg confidence: 0.89)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Swift UniFFI Bindings
- Ownership Matrix and Shared Resources
- Kotlin FFI Library Loading
- Scope 009 Coordination Records
- Kotlin UniFFI Library Calls
- Planning Path and Spec 0002
- Spec 0001 Ownership Rules
- Rust Core and Greeting Contract
- Derivation Command Tests
- CI Workflow and Derived Run
- Derivation Command
- Verification Record and UI Tests
- Spec 0003 Decision History
- Development Rules and Spec Triggers
- Native Greeting and Supported OS Scopes
- Spec 0003 Acceptance Criteria
- Resource Generator
- Kotlin FFI Converters
- Architecture Policy Checks
- Product Identity Files
- Platform Rules and Anti-Duplication
- Kotlin RustBuffer Handling
- Native Tokens and Visual Definitions
- Scope Workspaces and Build Approach
- Identity Value Sourcing
- Init Command and Repository States
- Config Schema
- Generator Tests and Drift Checks
- README and Starting a Product
- iOS App Shell
- Kotlin Rust Call Status
- Mobile Contract Extension Conventions
- Native Token Mapping and Text Scaling
- Design Principles and Token Conventions
- Localization Schema
- Kotlin Handle Map and Lifting
- Scope 010 and Token Generation Script
- Android App Shell
- Design System Accessibility
- Design System and Shared Resource Rules
- Native Component Guidelines
- iOS Greeting UI Tests
- Kotlin FFI Integrity Checks
- Hosted Build Verification Scopes
- Android Rust Build Script
- Android Gradle Wrapper
- iOS Rust Build Script

## God Nodes (most connected - your core abstractions)
1. `Spec 0002: One planning path: a scope row first, then a spec` - 60 edges
2. `Spec 0001: One owner per responsibility, with rules kept beside the code` - 56 edges
3. `UniffiLib` - 54 edges
4. `Foundation verification 2026-11-15` - 54 edges
5. `Spec 0003: A new project from the foundation: product identity in two files, one init command, updates by merge (In Progress)` - 53 edges
6. `Mobile foundation scope (index)` - 43 edges
7. `Decision: a new capability is planned as a scope row and designed in a spec before code; docs/plans and new ADRs are retired in a single change` - 38 edges
8. `Spec 0003 rationale: decision history of the new project spec (context, options considered, rationale)` - 35 edges
9. `Rollout: one change in fifteen ordered steps (rules, AGENTS.md, architecture docs, README, validator, delete docs/plans, scope files, spec 0001, knowledge graph)` - 33 edges
10. `Ownership matrix` - 30 edges

## Surprising Connections (you probably didn't know these)
- `Product identity result (2026-11-15: test.sh passed with --check printing foundation and --test passing 21 unit tests; both apps carried dev.foundation.mobile, Mobile Foundation, 0.1.0, build 1; a copy derived as Zoë's Proof built and matched its identity file)` --references--> `GreetingTest`  [INFERRED]
  docs/quality/verification.md → apps/android/app/src/androidTest/kotlin/foundation/mobile/GreetingTest.kt
- `Product identity result (2026-11-15: test.sh passed with --check printing foundation and --test passing 21 unit tests; both apps carried dev.foundation.mobile, Mobile Foundation, 0.1.0, build 1; a copy derived as Zoë's Proof built and matched its identity file)` --references--> `GreetingUITests`  [INFERRED]
  docs/quality/verification.md → apps/ios/UITests/GreetingUITests.swift
- `Greeting as a single text element` --references--> `GreetingScreen`  [INFERRED]
  docs/design-system/component-guidelines.md → apps/ios/Presentation/GreetingScreen.swift
- `Trace screen, generated binding, FFI export and core function before changing shared behavior` --references--> `GreetingScreen`  [INFERRED]
  docs/rules/development-rules.md → apps/ios/Presentation/GreetingScreen.swift
- `Render the returned Rust string verbatim` --references--> `GreetingScreen`  [INFERRED]
  docs/rules/ios-rules.md → apps/ios/Presentation/GreetingScreen.swift

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Coordination records of scope 009: the log, the general brief rules and the manual steps list, all tied to the scope row** — docs_scope_coordination_009_a_new_project_from_the_foundation_log, docs_scope_coordination_009_a_new_project_from_the_foundation_brief_umum, docs_scope_coordination_009_a_new_project_from_the_foundation_manual, docs_scope_root_009_a_new_project_from_the_foundation [EXTRACTED 1.00]
- **Wave 1 ownership split: developer on the verification record, checker on the verify.md ticks, tester on the derivation tests, with no overlap** — docs_scope_coordination_009_a_new_project_from_the_foundation_log_dev_f009_m3, docs_scope_coordination_009_a_new_project_from_the_foundation_log_chk_f009_verify, docs_scope_coordination_009_a_new_project_from_the_foundation_log_tst_f009_test, docs_quality_verification, docs_specs_root_0003_new_project_from_foundation_verify, tooling_derive_test_init_project, docs_scope_coordination_009_a_new_project_from_the_foundation_log_parallel_start [EXTRACTED 1.00]
- **Manual step flow: a sub-session reports a manual step, the lead lists it, the user runs it and the checker ticks verify.md from the result** — docs_scope_coordination_009_a_new_project_from_the_foundation_brief_umum_manual_steps_rule, docs_scope_coordination_009_a_new_project_from_the_foundation_manual, docs_scope_coordination_009_a_new_project_from_the_foundation_manual_summary, docs_scope_coordination_009_a_new_project_from_the_foundation_manual_result_routing, docs_scope_coordination_009_a_new_project_from_the_foundation_log_chk_f009_verify, docs_specs_root_0003_new_project_from_foundation_verify [INFERRED 0.85]
- **Automated architecture compliance checks** — docs_quality_architecture_compliance_rust_format_and_lint, docs_quality_architecture_compliance_core_and_ffi_contract_tests, docs_quality_architecture_compliance_cargo_dependency_and_governance_check, docs_quality_architecture_compliance_project_identity_state_check, docs_quality_architecture_compliance_uniffi_generated_files_check, docs_quality_architecture_compliance_tokens_config_localization_check, docs_quality_architecture_compliance_ios_linkage_and_ui_check, docs_quality_architecture_compliance_android_linkage_and_ui_check [EXTRACTED 1.00]
- **Hosted run 43593365100 as runtime evidence for the greeting contract, visual definitions, shared text and reproducible builds** — docs_scope_root_002_shared_greeting_contract, docs_scope_root_003_shared_visual_definitions, docs_scope_root_004_shared_settings_text_and_brand_assets, docs_scope_root_005_reproducible_local_builds_and_checks, docs_quality_verification_hosted_run_43593365100, docs_quality_verification [EXTRACTED 1.00]
- **One init command turns a foundation clone into a derived product: identity files, README origin line, empty verification record, removed knowledge graph** — scripts_init_project, tooling_derive_init_project, apps_ios_config_identity, apps_android_identity, docs_specs_root_0003_new_project_from_foundation_index_readme_origin_line, docs_specs_root_0003_new_project_from_foundation_index_empty_verification_record, tooling_derive_verification_record, docs_specs_root_0003_new_project_from_foundation_index_init_write_set, docs_specs_root_0003_new_project_from_foundation_index_repository_states_foundation_derived_mixed [EXTRACTED 1.00]
- **Forces that motivate the one-owner-per-responsibility decision** — docs_specs_root_0001_ownership_development_rules_force_two_languages_downstream_of_one_source, docs_specs_root_0001_ownership_development_rules_force_generated_files_beside_handwritten_code, docs_specs_root_0001_ownership_development_rules_force_coding_agents_as_regular_contributors, docs_specs_root_0001_ownership_development_rules_force_one_maintainer, docs_specs_root_0001_ownership_development_rules_force_small_codebase, docs_specs_root_0001_ownership_development_rules_decision_one_owner_per_responsibility [EXTRACTED 1.00]
- **Machine enforcement chain: test.sh runs the validator and both generator drift checks, mirrored by the CI foundation job** — docs_specs_root_0001_ownership_development_rules_enforcement_test_script_and_three_policy_checks, scripts_test, tooling_validation_check_architecture, scripts_generate_bindings, scripts_generate_design_tokens, github_workflows_foundation_foundation_job [EXTRACTED 1.00]
- **Rules that rest on review alone with no automated check** — docs_specs_root_0001_ownership_development_rules_r1_one_authoritative_owner, docs_specs_root_0001_ownership_development_rules_r3_app_trees_do_not_import_one_another, docs_specs_root_0001_ownership_development_rules_r8_real_caller_first, docs_specs_root_0001_ownership_development_rules_r9_search_before_adding, docs_specs_root_0001_ownership_development_rules_r11_handoff_reports_compiled_and_ran_separately, docs_specs_root_0001_ownership_development_rules_r14_bindgen_feature_host_only, docs_specs_root_0001_ownership_development_rules_r15_library_change_transitive_and_size_review, docs_specs_root_0001_ownership_development_rules_r16_breaking_change_is_a_migration, docs_specs_root_0001_ownership_development_rules_r18_service_proposal_requirements [EXTRACTED 1.00]
- **Canonical source over generated output: edit sources, regenerate, compare snapshots** — agents_never_hand_edit_generated_files, docs_architecture_ownership_matrix_derived_file_rule, docs_architecture_dependency_rules_one_way_generation, docs_decisions_adr_0001_foundation_checked_in_source_snapshots [INFERRED 0.85]
- **Proof that derivation still works: --check state test, derivation unit test on a temporary copy in scripts/test.sh, CI identity comparison in both native jobs, manual workflow run with derived set** — docs_specs_root_0003_new_project_from_foundation_index_check_form, docs_specs_root_0003_new_project_from_foundation_index_test_form, docs_specs_root_0003_new_project_from_foundation_index_derivation_test, docs_specs_root_0003_new_project_from_foundation_index_ci_identity_comparison, docs_specs_root_0003_new_project_from_foundation_index_workflow_derived_input, scripts_test, github_workflows_foundation, github_workflows_foundation_derived_input, github_workflows_foundation_derive_sample_product_step, github_workflows_foundation_ios_identity_comparison_step, github_workflows_foundation_android_identity_comparison_step [INFERRED 0.85]
- **Regenerate and compare checks that keep generated tokens, catalogs and bindings equal to their sources** — docs_scope_root_003_shared_visual_definitions_token_drift_check, docs_scope_root_004_shared_settings_text_and_brand_assets_single_english_catalog, docs_scope_root_005_reproducible_local_builds_and_checks_generated_output_drift_detection, scripts_test [INFERRED 0.85]
- **Tracer bullet greeting path from shared core to both native screens** — docs_scope_index_tracer_bullet_build_approach, docs_scope_root_002_shared_greeting_contract, docs_scope_root_002_shared_greeting_contract_one_string_in_one_string_out_contract, docs_scope_ios_001_native_ios_greeting, docs_scope_android_001_native_android_greeting, docs_scope_root_006_hosted_build_verification [INFERRED 0.85]
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

### Community 1 - "Ownership Matrix and Shared Resources"
Cohesion: 0.06
Nodes (79): Agent workflow: before editing (locate owner, contract, callers, tests), Never hand-edit generated files, Design system guide, generate-design-tokens.sh modes: write, --check (drift), --test (failure cases), Generated semantic token API consumed by native apps, Five canonical token JSON files (primitives and semantic aliases), tokens.schema.json: single Draft 7 document keyed by filename stem, Architecture boundaries (+71 more)

### Community 2 - "Kotlin FFI Library Loading"
Cohesion: 0.06
Nodes (34): Disposable, NoHandle, UniffiByValue, UniffiCallbackInterfaceClone, UniffiCallbackInterfaceFree, UniffiForeignFutureCompleteF32, UniffiForeignFutureCompleteF64, UniffiForeignFutureCompleteI16 (+26 more)

### Community 3 - "Scope 009 Coordination Records"
Cohesion: 0.06
Nodes (52): Agent workflow: before commit (run /graphify . --update, stage graphify-out with the change), Knowledge graph (graphify-out/, kept current with /graphify . --update), General brief rules (Aturan umum brief) for the sub-sessions of the scope 009 coordination: the fixed part of every brief; the brief wins where it differs, Always forbidden for sub-sessions: docs/scope/, AGENTS.md, graphify-out/, spec content other than the Status line and the verify.md ticks (checker only), other specs, and files outside the brief's allowed list, Decisions in auto mode: for an ambiguous AC read the spec's rationale.md, take the reading closest to the AC text and record it under Tafsiran AC; needs-decision goes to the lead only when the AC text or a spec decision must change, Commit rule for sub-sessions: one commit per step, an imperative English subject without prefix like the repository history, plus the Co-Authored-By trailer, Disk rule: 32 GiB free at the start; only the checker runs full native builds, one at a time; below 10 GiB free stop and report blocked; remove target/, build/ and apps/android/**/build and the temporary clone before reporting done, Graph and commit: the lead fulfils the AGENTS.md /graphify . --update rule when merging to main; sub-sessions never run graphify update and never stage anything under graphify-out/ (+44 more)

### Community 4 - "Kotlin UniFFI Library Calls"
Cohesion: 0.06
Nodes (3): UniffiLib, UniffiRustCallStatus, UniffiRustFutureContinuationCallback

### Community 5 - "Planning Path and Spec 0002"
Cohesion: 0.11
Nodes (45): ADR 0001: Native apps with a shared Rust core, Specs are numbered NNNN-kebab-title.md in the folder mirroring the scope workspace; a replaced record is marked superseded; ADR 0001 stays the founding record, Deferred work beyond Hello World, 007 - One planning path (done), The list of deferred work lives in one file, Former split planning path: docs/plans guide versus docs/scope (before this change), Follow-up (settled by spec 0002): R10 sent a new capability to docs/plans while features are tracked in docs/scope, Follow-up (settled by spec 0002): record keeping (ADR and plan naming, REQUIRED_DOCS membership, superseding, whether a spec satisfies R10) (+37 more)

### Community 6 - "Spec 0001 Ownership Rules"
Cohesion: 0.13
Nodes (37): AGENTS.md: Working in the mobile foundation, Rejected alternative: implementing application behavior independently in both apps, 001 - Ownership and development rules (done), One owner per shared responsibility (ten responsibilities in the ownership matrix), Spec 0001: One owner per responsibility, with rules kept beside the code, Decision: one owner per responsibility in an ownership matrix, topic-sized rule files, short AGENTS.md entry point, automated checks only where a machine is reliable, An exact dependency list, not a deny list, Follow-up: decide whether checks must pass before a change reaches main (branch rule or local hook) (+29 more)

### Community 7 - "Rust Core and Greeting Contract"
Cohesion: 0.11
Nodes (28): hello(), preserves_empty_names_and_whitespace(), String, main(), hello(), String, tests/contracts: Cargo integration tests for exported behavior, Core and FFI contract tests (locked Cargo tests) (+20 more)

### Community 8 - "Derivation Command Tests"
Cohesion: 0.16
Nodes (4): Checkout, DerivationTests, OutsideGitTests, A small foundation checkout in a temporary folder, in git unless a test says…

### Community 9 - "CI Workflow and Derived Run"
Cohesion: 0.13
Nodes (29): Agent workflow: before handoff (run checks, report commands and unverified targets), Pass representative values through both generated languages, Unverified: the workflow with the derived input and the identity comparison steps has not run on a hosted runner; no run with derived set has happened yet, Verification before reporting: scripts/test.sh must exit 0; build-ios.sh simulator, device and test in light and dark when apps/ios/ changed; build-android.sh assemble and connectedDebugAndroidTest in both night modes when apps/android/ changed; git status clean and the diff against main limited to ownership files, Hosted run 43701289339 (workflow_dispatch with derived active, on revision 4a153fe): already running when coordination began and not triggered by the lead; the developer waits for it and records it, no second run is triggered, Enforcement: scripts/test.sh runs format, lint, tests and three policy checks; CI runs the same script plus iOS and Android jobs, Neutral: /develop moves the spec to In Progress and Accepted with scope row 009; creating the first tag foundation-v0.1.0 is the maintainer's step, Release the foundation: run the workflow by hand with derived set, then push an annotated foundation-vMAJOR.MINOR.PATCH tag on main (+21 more)

### Community 10 - "Derivation Command"
Cohesion: 0.12
Nodes (30): Exception, check(), derive(), foundation_ref(), foundation_url(), git(), identity_text(), in_git() (+22 more)

### Community 11 - "Verification Record and UI Tests"
Cohesion: 0.14
Nodes (29): GreetingTest, GreetingUITests, Android linkage and UI check (Linux CI job, emulator instrumentation), GitHub Actions CI jobs (macOS and Linux), iOS linkage and UI check (macOS CI job, XCTest), Physical hardware verification for simulator-inaccessible capabilities, Foundation verification 2026-11-15, Android compilation result (Gradle 9.3.1, AGP 9.1.0, Temurin 17) (+21 more)

### Community 12 - "Spec 0003 Decision History"
Cohesion: 0.12
Nodes (31): A new product would carry the foundation's verification record, scope rows, hosted run links and knowledge graph as its own, Decision: a product is a clone that changes only its display name, application ID and version through scripts/init-project.sh, keeps every other name, starts with an empty verification record and merges foundation-v tags, Empty verification record: names the product, foundation URL and ref, lists every target as still unverified, holds no hosted run link, User stories: one command names a clone, foundation releases arrive by merge, the verification record lists only what ran here, every push proves the command still works, Spec 0003 rationale: decision history of the new project spec (context, options considered, rationale), Recommendation: --check does not look for hosted run links, Recommendation: the command does not edit scope rows, Recommendation: the command refuses to run on a derived checkout (+23 more)

### Community 13 - "Development Rules and Spec Triggers"
Cohesion: 0.26
Nodes (24): Agent workflow: during implementation (place change in owning layer), Plan a new capability in the scope and write its spec under docs/specs before code, Dependency rules, New dependency edge needs an owning module, a use case and a test, Architecture overview, Mobile contract (FFI conventions), Compatibility: version breaking contracts and coordinate regeneration, both apps and release, Revisit conditions: dependency direction change, async native boundary, independently versioned clients, new shared crate or service (+16 more)

### Community 14 - "Native Greeting and Supported OS Scopes"
Cohesion: 0.15
Nodes (22): CoreImage, Android 001 - Native Android greeting (existing), API 36 emulator results (arm64 local, x86_64 hosted) in light and dark, Android app packages both supported CPU architectures, Android physical device coverage unverified, Android 002 - Lowest supported Android and large text (planned), 16 KiB memory page packaging, Declared Android minimum API 24 not yet exercised (+14 more)

### Community 15 - "Spec 0003 Acceptance Criteria"
Cohesion: 0.17
Nodes (24): Build steps (009): identity file per platform (AC-1, AC-2, done), init command with state check and unit tests (AC-3 to AC-9, done), workflow derived input and identity comparison (AC-10, open), README path and document updates (AC-11, AC-12, done), Spec 0003: A new project from the foundation: product identity in two files, one init command, updates by merge (In Progress), AC-10: the workflow accepts a manual run with the derived input, and every native job compares the built app's ID and display name with the identity file, AC-2: with the default identity scripts/test.sh passes, both apps build and the greeting tests pass in both appearances, AC-3: init-project.sh --name --app-id writes name, ID, version 0.1.0 and build 1 into both identity files, with per-value overrides, AC-4: the write set is exactly the two identity files, README.md, the verification record and the removed graphify-out/ files; nothing is renamed, AC-5: the verification record becomes the empty record naming the product, foundation URL and revision, with every target unverified, AC-6: README.md has the product name as title on line 1 and the origin line on line 3 followed by one blank line (+16 more)

### Community 16 - "Resource Generator"
Cohesion: 0.14
Nodes (19): check_schema(), generate(), load(), projections(), Validate authoritative sources, then materialize or check their projections., unique_members(), validator(), native_text() (+11 more)

### Community 17 - "Kotlin FFI Converters"
Cohesion: 0.17
Nodes (9): FfiConverter, FfiConverterRustBuffer, FfiConverterString, FfiType, uniffiTraitInterfaceCall(), uniffiTraitInterfaceCallWithError(), ByteBuffer, KotlinType (+1 more)

### Community 18 - "Architecture Policy Checks"
Cohesion: 0.15
Nodes (21): Cargo dependency and governance check, Limits of CI checks, Architecture policy result (dependency and required-document checks), Services call each other through public interfaces; cycles rejected, Service proposal checklist, Required document check covers the scope index, Automate only what a machine can judge, Follow-up (settled by spec 0002): docs/specs and docs/scope were named by neither repository-structure.md nor REQUIRED_DOCS (+13 more)

### Community 19 - "Product Identity Files"
Cohesion: 0.19
Nodes (22): apps/android/identity.properties (Android identity file: applicationId, displayName, versionName, versionCode), apps/ios/Config/Identity.xcconfig (iOS identity file: APP_BUNDLE_IDENTIFIER, APP_DISPLAY_NAME, MARKETING_VERSION, CURRENT_PROJECT_VERSION), Product identity (display name, application IDs, app version): owned by apps/ios/Config/Identity.xcconfig and apps/android/identity.properties; consumed by the Xcode and Gradle builds and scripts/init-project.sh, Project identity state check (init-project.sh --check and --test, CI identity comparison), Product identity result (2026-11-15: test.sh passed with --check printing foundation and --test passing 21 unit tests; both apps carried dev.foundation.mobile, Mobile Foundation, 0.1.0, build 1; a copy derived as Zoë's Proof built and matched its identity file), The two apps disagree on their own identity (iOS dev.foundation.mobile / Mobile Foundation / 1.0, Android foundation.mobile / Foundation / 0.1.0), AC-1: both apps carry the same default identity, read from Identity.xcconfig and identity.properties, stated nowhere else under apps/, CI identity comparison: each native job compares the built app's ID and display name (PlistBuddy on Info.plist, aapt2 dump badging on the debug APK) with its identity file and fails on a difference (+14 more)

### Community 20 - "Platform Rules and Anti-Duplication"
Cohesion: 0.13
Nodes (22): GreetingScreen(), Reviewers trace changed behavior from owner into each client, Android rules, Checked-in Gradle wrapper, Compose presentation with native Material semantics, Anti-duplication rules, Application code displays the binding's return value, Locate the owner before adding a constant, rule, DTO, translation or asset (+14 more)

### Community 21 - "Kotlin RustBuffer Handling"
Cohesion: 0.16
Nodes (7): ByReference, ByValue, ForeignBytes, `hello`(), RustBuffer, kotlin, Pointer

### Community 22 - "Native Tokens and Visual Definitions"
Cohesion: 0.13
Nodes (14): FoundationTokens, Palette, FoundationTokens, Palette, CGFloat, Color, ColorScheme, 003 - Shared visual definitions (done) (+6 more)

### Community 23 - "Scope Workspaces and Build Approach"
Cohesion: 0.24
Nodes (16): Progress is recorded in the scope row; what ran is recorded in the verification record, Android scope, Android app owns its screen, appearance changes and native localization lookup, Mobile foundation scope (index), Beta workflow (/check verify, then /test), Scope status legend and file numbering convention, Tracer Bullet build approach, Workspace completion at a glance: shared foundation 8 of 10 (open 009, 010), iOS 1 of 2, Android 1 of 2 (+8 more)

### Community 24 - "Identity Value Sourcing"
Cohesion: 0.20
Nodes (14): apps/android/app/src/main/AndroidManifest.xml, apps/android/app/src/main/res/values/app.xml (the app_name string leaves this file; the label comes from the appLabel manifest placeholder), apps/ios/Config/App.xcconfig (iOS app build settings), apps/ios/Config/Project.xcconfig (iOS project build settings), apps/ios/MobileFoundation.xcodeproj/project.pbxproj (Xcode project file), Android build reads identity.properties: app/build.gradle.kts loads applicationId, versionName and versionCode, the label reaches the manifest as the appLabel placeholder, namespace stays foundation.mobile, Foundation ref resolution: --foundation-ref, else the highest foundation-v* tag exactly at HEAD, else the full HEAD commit ID, Foundation URL sourcing and normalization: --foundation-url, else the foundation remote, else origin; https, http, ssh and user@host:path forms written as https without user, token, .git or trailing slash (+6 more)

### Community 25 - "Init Command and Repository States"
Cohesion: 0.26
Nodes (14): Derivation only on a copy: init-project.sh with --name rewrites README.md and the verification record and removes graphify-out/, so that form runs only in a temporary clone in the session scratchpad; --check and --test are safe in the worktree, Decision: the tester installs no new tool and test-preferences.json is not created; the framework is the existing Python unittest run through scripts/init-project.sh --test, Done when (009): one recorded decision, one command, a hosted check on a temporary copy, clean inherited records, recorded foundation revision, init-project.sh --check: prints foundation or derived (exit 0) or names each mismatch in a mixed state (exit 1), Derivation test: copies the files git lists to a temporary folder, runs the copy's own command with sample values, requires --check to print derived and check-architecture.py to pass, then removes the copy, Init write set: the two identity files, the README title and origin line, the empty verification record and the removal of graphify-out/, Key invariants: a checkout is foundation or derived, each identity value has one home per platform, the command renames nothing, never runs on a derived or mixed checkout, never changes git state, and foundation tags match foundation-v*, Repository states: foundation (both IDs default, no origin line), derived (neither ID default, valid origin line), mixed (anything else) (+6 more)

### Community 26 - "Config Schema"
Cohesion: 0.14
Nodes (13): defaultLocale, schemaVersion, additionalProperties, const, properties, defaultLocale, schemaVersion, required (+5 more)

### Community 27 - "Generator Tests and Drift Checks"
Cohesion: 0.19
Nodes (9): Generated drift remediation, Tokens, configuration and localization check, Design system and resources result (seven generator tests), Shared visual decisions and translations are generator inputs, Drift check plus verification in both appearances and larger text sizes, Regenerate native projections in the same change, Regenerate derived files alongside canonical inputs, Generated native strings owned by the resource generator (+1 more)

### Community 28 - "README and Starting a Product"
Cohesion: 0.31
Nodes (13): AC-11: README.md has a section with the full path from clone to first results, path ownership, taking a later release and foundation tagging, Follow-up: build the command that takes a foundation release (fetch, merge, apply the ownership table) when the first release is merged into a product, Follow-up: decide where dependency update bots run (a bot in every product changes foundation owned files and will conflict with merges), Path ownership after derivation: product owned paths keep the product's side, foundation owned paths take the foundation's side, shared paths merge by hand, README section 'Start a project from this foundation': clone at a tag, create a branch, rename the remote, run the command, add origin, rebuild the graph, mark inherited rows existing, commit, record first results, Take a later foundation release: git fetch foundation --tags, git merge foundation-vX.Y.Z, keep the product's side on product owned paths, rebuild the graph, run every check, Tradeoff: every merge of a foundation release reports conflicts on product owned paths, resolved by hand until the sync command exists, Premise: four coupled decisions in one spec (which names change, how a copy is made, what happens to inherited records, how updates arrive) (+5 more)

### Community 29 - "iOS App Shell"
Cohesion: 0.18
Nodes (9): App, MobileFoundationApp, .body, GreetingScreen, .body, String, Scene, SwiftUI (+1 more)

### Community 30 - "Kotlin Rust Call Status"
Cohesion: 0.23
Nodes (7): E, uniffiCheckCallStatus(), UniffiForeignFutureCompleteVoid, uniffiRustCall(), UniffiRustCallStatusErrorHandler, uniffiRustCallWithError(), U

### Community 31 - "Mobile Contract Extension Conventions"
Cohesion: 0.25
Nodes (11): Explicit application records and enums; private core/transport shapes mapped at the adapter, Async and cancellation conventions for future exports, Conventions for extending the mobile contract, Native capability callback interfaces limited to operations the core requires, Typed UniFFI errors with stable variants; user-facing messages translated natively, Deferred: a contract beyond one string (record, typed error, async call), Records, typed errors, async calls and native callbacks have no caller or test yet, One string in, one string out greeting contract (+3 more)

### Community 32 - "Native Token Mapping and Text Scaling"
Cohesion: 0.35
Nodes (11): System text scaling via generated text styles, Native token mapping, Compose sp mapping of logical text units, Jetpack Compose token projection (FoundationTokens), Dynamic Type mapping of headline and reading scales, Logical spacing units adapt to display density, spacingPage role, SwiftUI token projection (FoundationTokens) (+3 more)

### Community 33 - "Design Principles and Token Conventions"
Cohesion: 0.27
Nodes (11): Design principles, Canonical JSON propagates through code generation, Design definitions compile independently of Cargo and UniFFI, Semantic names for decisions both apps share, Token conventions, Canonical token sources (colors, typography, spacing, radius, motion JSON), References are group-local and point directly to primitives, Token naming convention (lower camel case, #RRGGBB) (+3 more)

### Community 34 - "Localization Schema"
Cohesion: 0.18
Nodes (10): greeting_recipient, additionalProperties, minLength, type, propertyNames, pattern, required, $schema (+2 more)

### Community 35 - "Kotlin Handle Map and Lifting"
Cohesion: 0.42
Nodes (4): InternalException, T, UniffiHandleMap, UniffiNullRustCallStatusErrorHandler

### Community 36 - "Scope 010 and Token Generation Script"
Cohesion: 0.36
Nodes (8): Canonical token schema (tokens.schema.json), 010 - Schemas free of sample names (planned, needs a decision), Done when (010): the localization schema asks for at least one key and names none, the typography role is named for its purpose, native themes and generator tests follow, and a greeting-free catalog and token set pass generate-design-tokens.sh --check, Replace the greeting with a first feature without editing a foundation schema, Foundation schemas require sample names: the greeting_recipient key in the localization schema and the greeting typography role in the token schema, Follow-up: two foundation schemas still require sample names (greeting_recipient, the greeting role); this deserves its own scope row, PYTHONPATH, generate-design-tokens.sh script

### Community 37 - "Android App Shell"
Cohesion: 0.43
Nodes (4): MainActivity, FoundationTheme(), Bundle, ComponentActivity

### Community 38 - "Design System Accessibility"
Cohesion: 0.38
Nodes (6): Accessibility (design system), Status conveyed by text or semantics, not color alone, Honor platform reduced-motion setting, Text contrast check (4.5:1 minimum), W3C WCAG 2.2 contrast minimum guidance, Light and dark text meet the documented contrast threshold

### Community 39 - "Design System and Shared Resource Rules"
Cohesion: 0.43
Nodes (7): Stable role names or same-change migration, Design system rules, Public role name changes require migrating both consumers, Draft 7 schema and native mappings updated together, Draft 7 schemas in shared/specifications, Incompatible source format changes treated as migrations, R16: a breaking change is a migration (token role, resource format, versioned contract)

### Community 40 - "Native Component Guidelines"
Cohesion: 0.33
Nodes (6): Per-target reading order and screen-reader review, Native components guidelines, Greeting as a single text element, Native controls styled with semantic tokens, Reusable native component (introduced on demand), Layout, text measurement, gestures and focus stay in presentation

### Community 41 - "iOS Greeting UI Tests"
Cohesion: 0.50
Nodes (3): UInt8, CIContext, XCUIScreenshot

### Community 42 - "Kotlin FFI Integrity Checks"
Cohesion: 0.60
Nodes (3): IntegrityCheckingUniffiLib, uniffiCheckApiChecksums(), uniffiCheckContractApiVersion()

### Community 43 - "Hosted Build Verification Scopes"
Cohesion: 0.40
Nodes (5): 006 - Hosted build verification (done), Android hosted job installs the supported SDK packages, Three hosted jobs (foundation, iOS, Android) on the same revision, 008 - Hosted results in the verification record (done), Follow-up: verification.md says hosted jobs have not run while the scope index records a passing run

### Community 44 - "Android Rust Build Script"
Cohesion: 0.40
Nodes (4): CARGO_TARGET_AARCH64_LINUX_ANDROID_LINKER, CARGO_TARGET_X86_64_LINUX_ANDROID_LINKER, PATH, build-android-rust.sh script

### Community 45 - "Android Gradle Wrapper"
Cohesion: 0.83
Nodes (3): gradlew script, die(), warn()

### Community 46 - "iOS Rust Build Script"
Cohesion: 0.50
Nodes (3): CARGO_TARGET_DIR, PATH, build-ios-rust.sh script

## Knowledge Gaps
- **64 isolated node(s):** `NoHandle`, `UniffiWithHandle`, `Explicit application records and enums; private core/transport shapes mapped at the adapter`, `apiChecksumMismatch`, `contractVersionMismatch` (+59 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `.body` connect `iOS App Shell` to `Swift UniFFI Bindings`?**
  _High betweenness centrality (0.125) - this node is a cross-community bridge._
- **Why does `hello()` connect `Swift UniFFI Bindings` to `iOS App Shell`?**
  _High betweenness centrality (0.118) - this node is a cross-community bridge._
- **Why does `GreetingScreen` connect `iOS App Shell` to `Native Component Guidelines`, `Platform Rules and Anti-Duplication`?**
  _High betweenness centrality (0.114) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Foundation verification 2026-11-15` (e.g. with `Record separately what compiled and what ran` and `tooling/derive/verification-record.md (empty verification record template for a derived product)`) actually correct?**
  _`Foundation verification 2026-11-15` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `NoHandle`, `UniffiWithHandle`, `Explicit application records and enums; private core/transport shapes mapped at the adapter` to the rest of the system?**
  _64 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Swift UniFFI Bindings` be split into smaller, more focused modules?**
  _Cohesion score 0.05444596443228454 - nodes in this community are weakly interconnected._
- **Should `Ownership Matrix and Shared Resources` be split into smaller, more focused modules?**
  _Cohesion score 0.05583308845136644 - nodes in this community are weakly interconnected._