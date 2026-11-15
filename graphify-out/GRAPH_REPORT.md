# Graph Report - mobile  (2026-11-15)

## Corpus Check
- 11 files · ~72,299 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1131 nodes · 3087 edges · 58 communities
- Extraction: 77% EXTRACTED · 23% INFERRED · 0% AMBIGUOUS · INFERRED: 718 edges (avg confidence: 0.89)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Swift UniFFI Bindings
- Kotlin FFI Library Loading
- Kotlin UniFFI Library Calls
- Planning Path and Scope Index
- Derivation Command Tests
- Spec 0001 Ownership Rules
- Verification Record and UI Tests
- Rust Core and Greeting Contract
- Derivation Command
- Scope 009 Coordination Records
- Development Rules and Spec Triggers
- Spec 0003 Acceptance Criteria
- CI Workflow and Derived Run
- Resource Generator
- Kotlin RustBuffer Handling
- Architecture Overview and Founding Decision
- Ownership Matrix and Repository Structure
- Spec 0003 Decision History
- Shared Settings and Localization
- Init Command and Identity Files
- Kotlin FFI Converters
- Coordinate Skill Lead Flow
- Visual Definitions and Accessibility Checks
- Coordinate Roles and Tick Gates
- Schemas and Sample Names
- Design Principles and Token Conventions
- Architecture Policy Checks
- Coordinate Decision Modes and Log
- Anti-Duplication and Review-Only Rules
- README and Starting a Product
- Config Schema
- iOS App Shell and Native Components
- Architecture Boundaries and Real Callers
- Native Token Mapping and Text Scaling
- Empty Verification Record and Value Sourcing
- Generated Native Tokens
- Kotlin Rust Call Status
- Generator Tests and Drift Checks
- Identity Value Sourcing
- Pinned Toolchain and Gradle Wrapper
- Supported OS and Large Text Scopes
- Repository States and Default Identity
- iOS Greeting Scope and Sources
- Android Greeting Scope
- Android App Shell
- Kotlin Handle Map and Lifting
- Design System Guide and Token Commands
- test.sh and Derivation Test
- Configuration Guide
- Knowledge Graph Update Rules
- Kotlin FFI Integrity Checks
- Review Gate and Reviewer Rule
- Scope 009 Manual Steps
- Android Rust Build Script
- iOS Rust Build Script

## God Nodes (most connected - your core abstractions)
1. `Spec 0002: One planning path: a scope row first, then a spec` - 60 edges
2. `Spec 0001: One owner per responsibility, with rules kept beside the code` - 56 edges
3. `UniffiLib` - 54 edges
4. `Foundation verification 2026-11-15` - 54 edges
5. `Spec 0003: A new project from the foundation: product identity in two files, one init command, updates by merge (In Progress)` - 53 edges
6. `Mobile foundation scope (index)` - 44 edges
7. `Decision: a new capability is planned as a scope row and designed in a spec before code; docs/plans and new ADRs are retired in a single change` - 38 edges
8. `Spec 0003 rationale: decision history of the new project spec (context, options considered, rationale)` - 35 edges
9. `Rollout: one change in fifteen ordered steps (rules, AGENTS.md, architecture docs, README, validator, delete docs/plans, scope files, spec 0001, knowledge graph)` - 33 edges
10. `Ownership matrix` - 30 edges

## Surprising Connections (you probably didn't know these)
- `Product identity result (2026-11-15: test.sh passed with --check printing foundation and --test passing 21 unit tests; both apps carried dev.foundation.mobile, Mobile Foundation, 0.1.0, build 1; a copy derived as Zoë's Proof built and matched its identity file)` --references--> `GreetingTest`  [INFERRED]
  docs/quality/verification.md → apps/android/app/src/androidTest/kotlin/foundation/mobile/GreetingTest.kt
- `Product identity result (2026-11-15: test.sh passed with --check printing foundation and --test passing 21 unit tests; both apps carried dev.foundation.mobile, Mobile Foundation, 0.1.0, build 1; a copy derived as Zoë's Proof built and matched its identity file)` --references--> `GreetingUITests`  [INFERRED]
  docs/quality/verification.md → apps/ios/UITests/GreetingUITests.swift
- `Tokens, configuration and localization check` --references--> `GenerationTests`  [INFERRED]
  docs/quality/architecture-compliance.md → tooling/codegen/test_generation.py
- `Design system and resources result (seven generator tests)` --references--> `GenerationTests`  [INFERRED]
  docs/quality/verification.md → tooling/codegen/test_generation.py
- `Trace screen, generated binding, FFI export and core function before changing shared behavior` --references--> `GreetingScreen`  [INFERRED]
  docs/rules/development-rules.md → apps/ios/Presentation/GreetingScreen.swift

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **The five sub-session roles of /coordinate, each with its own goal, ownership, message paths and model** — claude_skills_coordinate_roles_architect, claude_skills_coordinate_roles_developer, claude_skills_coordinate_roles_checker, claude_skills_coordinate_roles_tester, claude_skills_coordinate_roles_debugger, claude_skills_coordinate_skill_sub_session, claude_skills_coordinate_skill_model_per_role [EXTRACTED 1.00]
- **Tick gates of /coordinate: what must be true on main before the lead ticks each kind of scope box** — claude_skills_coordinate_skill_step_6_tick_gate_and_merge, claude_skills_coordinate_skill_gate_design_it, claude_skills_coordinate_skill_gate_milestone, claude_skills_coordinate_skill_gate_build_it_and_verify_it, claude_skills_coordinate_skill_gate_test_it, claude_skills_coordinate_skill_gate_review_it, claude_skills_coordinate_skill_gate_document_it, claude_skills_coordinate_skill_red_gate_cycle [EXTRACTED 1.00]
- **Coordination templates (brief, general rules, log, manual, report) and the scope 009 records filled from them** — claude_skills_coordinate_templates_brief, claude_skills_coordinate_templates_brief_umum, claude_skills_coordinate_templates_log, claude_skills_coordinate_templates_manual, claude_skills_coordinate_templates_report, docs_scope_coordination_009_a_new_project_from_the_foundation_brief_umum, docs_scope_coordination_009_a_new_project_from_the_foundation_log, docs_scope_coordination_009_a_new_project_from_the_foundation_manual [INFERRED 0.95]
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
- **Coordination records of scope 009: the log, the general brief rules and the manual steps list, all tied to the scope row** — docs_scope_coordination_009_a_new_project_from_the_foundation_log, docs_scope_coordination_009_a_new_project_from_the_foundation_brief_umum, docs_scope_coordination_009_a_new_project_from_the_foundation_manual, docs_scope_root_009_a_new_project_from_the_foundation [EXTRACTED 1.00]
- **Wave 1 ownership split: developer on the verification record, checker on the verify.md ticks, tester on the derivation tests, with no overlap** — docs_scope_coordination_009_a_new_project_from_the_foundation_log_dev_f009_m3, docs_scope_coordination_009_a_new_project_from_the_foundation_log_chk_f009_verify, docs_scope_coordination_009_a_new_project_from_the_foundation_log_tst_f009_test, docs_quality_verification, docs_specs_root_0003_new_project_from_foundation_verify, tooling_derive_test_init_project, docs_scope_coordination_009_a_new_project_from_the_foundation_log_parallel_start [EXTRACTED 1.00]
- **Spec triggers kept in their owner files: when a smaller change needs a spec** — docs_specs_root_0002_one_planning_path_trigger_owner_files, docs_rules_development_rules_spec_triggers_for_smaller_changes, docs_rules_service_rules_spec_for_new_crate_or_boundary, docs_quality_architecture_compliance_spec_for_architecture_change, docs_architecture_dependency_rules_new_edge_proposal, docs_contracts_ffi_conventions_compatibility_versioning, docs_decisions_adr_0001_foundation_revisit_conditions, docs_specs_root_0001_ownership_development_rules_spec_triggers [EXTRACTED 1.00]
- **Design token pipeline from canonical JSON to native projections** — docs_design_system_token_conventions_canonical_token_sources, design_system_schemas_tokens_schema, scripts_generate_design_tokens, docs_design_system_platform_mapping_swiftui_token_projection, docs_design_system_platform_mapping_compose_token_projection, docs_quality_architecture_compliance_tokens_config_localization_check [INFERRED 0.85]
- **Neutral JSON sources validated and generated into native theme and string resources** — design_system_readme_token_files, design_system_readme_tokens_schema, shared_config_readme_foundation_json, shared_localization_readme_catalog_format, design_system_readme_generate_design_tokens_modes, tooling_codegen_requirements_fastjsonschema, design_system_readme_generated_semantic_api, shared_localization_readme_generated_native_strings [INFERRED 0.85]
- **Regenerate derived outputs with their canonical source, never hand-edit** — docs_rules_development_rules_regenerate_derived_files, docs_rules_design_system_rules_regenerate_projections, docs_quality_architecture_compliance_generated_drift_remediation, docs_rules_rust_rules_regenerate_after_signature_change, docs_rules_shared_resources_rules_generated_native_strings, docs_rules_anti_duplication_ffi_shapes_in_rust_export [INFERRED 0.85]
- **Manual step flow: a sub-session reports a manual step, the lead lists it, the user runs it and the checker ticks verify.md from the result** — docs_scope_coordination_009_a_new_project_from_the_foundation_brief_umum_manual_steps_rule, docs_scope_coordination_009_a_new_project_from_the_foundation_manual, docs_scope_coordination_009_a_new_project_from_the_foundation_manual_summary, docs_scope_coordination_009_a_new_project_from_the_foundation_manual_result_routing, docs_scope_coordination_009_a_new_project_from_the_foundation_log_chk_f009_verify, docs_specs_root_0003_new_project_from_foundation_verify [INFERRED 0.85]
- **Verification evidence chain: local checks, hosted jobs and the verification record** — docs_scope_root_005_reproducible_local_builds_and_checks, docs_scope_root_006_hosted_build_verification, docs_scope_root_008_hosted_results_in_the_verification_record, docs_scope_root_008_hosted_results_in_the_verification_record_single_list_of_unverified_targets [INFERRED 0.85]

## Communities (58 total, 0 thin omitted)

### Community 0 - "Swift UniFFI Bindings"
Cohesion: 0.05
Nodes (64): Array, createReader(), createWriter(), Data, FfiConverter, FfiConverterPrimitive, FfiConverterRustBuffer, FfiConverterString (+56 more)

### Community 1 - "Kotlin FFI Library Loading"
Cohesion: 0.06
Nodes (34): Disposable, NoHandle, UniffiByValue, UniffiCallbackInterfaceClone, UniffiCallbackInterfaceFree, UniffiForeignFutureCompleteF32, UniffiForeignFutureCompleteF64, UniffiForeignFutureCompleteI16 (+26 more)

### Community 2 - "Kotlin UniFFI Library Calls"
Cohesion: 0.06
Nodes (3): UniffiLib, UniffiRustCallStatus, UniffiRustFutureContinuationCallback

### Community 3 - "Planning Path and Scope Index"
Cohesion: 0.10
Nodes (50): Progress is recorded in the scope row; what ran is recorded in the verification record, Mobile foundation scope (index), Beta workflow (/check verify, then /test), Deferred work beyond Hello World, Scope status legend and file numbering convention, Tracer Bullet build approach, Workspace completion at a glance: shared foundation 8 of 10 (open 009, 010), iOS 1 of 2, Android 1 of 2, iOS scope (+42 more)

### Community 4 - "Derivation Command Tests"
Cohesion: 0.12
Nodes (8): Unit tests create their own repository in a temporary folder with isolated git configuration; no test touches the real checkout, Checkout, DerivationTests, OutsideGitTests, Checks for the derivation command: every write, every refusal and both clean…, Run the checked in command on a temporary copy of this checkout. The checkout…, A small foundation checkout in a temporary folder, in git unless a test says…, RealCheckoutTests

### Community 5 - "Spec 0001 Ownership Rules"
Cohesion: 0.11
Nodes (39): AGENTS.md: Working in the mobile foundation, Android rules, New ABI requires Rust cross-build and runtime test, Record separately what compiled and what ran, iOS rules, Deferred: a contract beyond one string (record, typed error, async call), 001 - Ownership and development rules (done), One owner per shared responsibility (ten responsibilities in the ownership matrix) (+31 more)

### Community 6 - "Verification Record and UI Tests"
Cohesion: 0.10
Nodes (35): GreetingTest, GreetingUITests, UInt8, CIContext, Android linkage and UI check (Linux CI job, emulator instrumentation), GitHub Actions CI jobs (macOS and Linux), iOS linkage and UI check (macOS CI job, XCTest), Physical hardware verification for simulator-inaccessible capabilities (+27 more)

### Community 7 - "Rust Core and Greeting Contract"
Cohesion: 0.10
Nodes (33): hello(), preserves_empty_names_and_whitespace(), String, main(), hello(), String, tests/contracts: Cargo integration tests for exported behavior, Core and FFI contract tests (locked Cargo tests) (+25 more)

### Community 8 - "Derivation Command"
Cohesion: 0.12
Nodes (31): Exception, check(), derive(), foundation_ref(), foundation_url(), git(), identity_text(), in_git() (+23 more)

### Community 9 - "Scope 009 Coordination Records"
Cohesion: 0.10
Nodes (32): Skill panel answers in the general rules: AskUserQuestion does not wake the lead, so every skill panel is answered from a fixed list or sent to the lead as needs-decision, General brief rules (Aturan umum brief) for the sub-sessions of the scope 009 coordination: the fixed part of every brief; the brief wins where it differs, Always forbidden for sub-sessions: docs/scope/, AGENTS.md, graphify-out/, spec content other than the Status line and the verify.md ticks (checker only), other specs, and files outside the brief's allowed list, Commit rule for sub-sessions: one commit per step, an imperative English subject without prefix like the repository history, plus the Co-Authored-By trailer, Disk rule: 32 GiB free at the start; only the checker runs full native builds, one at a time; below 10 GiB free stop and report blocked; remove target/, build/ and apps/android/**/build and the temporary clone before reporting done, Lead address: Mobile Foundation Scaffold [f5cda4]; full reports, questions and needs-decision go there through SendMessage, Process rule: stop only the processes, simulators and emulators you started, name them F009-<session> and delete them afterwards; suites longer than 10 minutes run detached with nohup, Project adjustments: the role files were written for another Rust project; cargo xtask, stackly_testkit, clients/swift, evidence/, prd.md and test-preferences.json do not exist here; evidence is the commands and output in the report (+24 more)

### Community 10 - "Development Rules and Spec Triggers"
Cohesion: 0.20
Nodes (29): Agent workflow: during implementation (place change in owning layer), Plan a new capability in the scope and write its spec under docs/specs before code, Dependency rules, New dependency edge needs an owning module, a use case and a test, Mobile contract (FFI conventions), Explicit application records and enums; private core/transport shapes mapped at the adapter, Async and cancellation conventions for future exports, Compatibility: version breaking contracts and coordinate regeneration, both apps and release (+21 more)

### Community 11 - "Spec 0003 Acceptance Criteria"
Cohesion: 0.13
Nodes (28): Build steps (009): identity file per platform (AC-1, AC-2, done), init command with state check and unit tests (AC-3 to AC-9, done), workflow derived input and identity comparison (AC-10, open), README path and document updates (AC-11, AC-12, done), Spec 0003: A new project from the foundation: product identity in two files, one init command, updates by merge (In Progress), AC-11: README.md has a section with the full path from clone to first results, path ownership, taking a later release and foundation tagging, AC-2: with the default identity scripts/test.sh passes, both apps build and the greeting tests pass in both appearances, AC-4: the write set is exactly the two identity files, README.md, the verification record and the removed graphify-out/ files; nothing is renamed, AC-5: the verification record becomes the empty record naming the product, foundation URL and revision, with every target unverified, AC-6: README.md has the product name as title on line 1 and the origin line on line 3 followed by one blank line, AC-7: the command refuses, changes nothing and exits 2 with a one line reason (bad input, default ID, dirty tree, derived or mixed checkout, missing foundation URL or ref) (+20 more)

### Community 12 - "CI Workflow and Derived Run"
Cohesion: 0.19
Nodes (26): Project identity state check (init-project.sh --check and --test, CI identity comparison), Unverified: the workflow with the derived input and the identity comparison steps has not run on a hosted runner; no run with derived set has happened yet, Hosted run 43701281055 (push trigger, on revision 4a153fe), Scope 009 specifics: main at the start is 4a153fe, equal to origin/main; Build plan steps 1 to 10 of spec 0003 are on main; no sub-session triggers, repeats or cancels a hosted run; each of verification.md, verify.md and test_init_project.py has exactly one sub-session that may change it, Sub-session dev-f009-m3 (developer, opus-5-5 medium): scope 009 milestone 3, Build plan step 11 for AC-10; owns docs/quality/verification.md, Hosted run 43701289339 (workflow_dispatch with derived active, on revision 4a153fe): already running when coordination began and not triggered by the lead; the developer waits for it and records it, no second run is triggered, Decision: reconciliation with main: Build plan step 8 (derived input and identity comparison in both native jobs) already landed in 4a153fe, so milestone 3 has only step 11 left: the hosted run with derived and its note in the verification record, AC-10: the workflow accepts a manual run with the derived input, and every native job compares the built app's ID and display name with the identity file (+18 more)

### Community 13 - "Resource Generator"
Cohesion: 0.14
Nodes (19): check_schema(), generate(), load(), projections(), Validate authoritative sources, then materialize or check their projections., unique_members(), validator(), native_text() (+11 more)

### Community 14 - "Kotlin RustBuffer Handling"
Cohesion: 0.14
Nodes (9): ByReference, ByValue, ForeignBytes, `hello`(), RustBuffer, uniffiTraitInterfaceCall(), uniffiTraitInterfaceCallWithError(), kotlin (+1 more)

### Community 15 - "Architecture Overview and Founding Decision"
Cohesion: 0.19
Nodes (23): Layer: shared Rust (core owns behavior, FFI crate maps exports), Workspace edge: mobile-ffi depends on foundation-core (std-only core), Proc-macro exports define the cross-language API; bindgen feature gates host CLI deps, Architecture overview, Build-time generation: token JSON and locale JSON -> native theme inputs and localization resources, foundation_core::hello (sole greeting formatter), Greeting call flow: SwiftUI/Compose -> generated binding -> C ABI/JNA -> mobile-ffi -> foundation-core, Color selection, font scaling, layout and accessibility run natively (no shared renderer) (+15 more)

### Community 16 - "Ownership Matrix and Repository Structure"
Cohesion: 0.21
Nodes (21): Agent workflow: before editing (locate owner, contract, callers, tests), App trees do not import one another; core never calls platform UI, Ownership matrix, apps/android: owner of Android UI, presentation state and OS APIs, apps/ios: owner of Apple UI, presentation state and OS APIs, Derived file rule: change the canonical input and regenerate every output in the same review, design-system/tokens and schemas: owner of canonical visual values and semantic roles, docs/ and root AGENTS.md: architecture, decision records, scope and agent workflow (+13 more)

### Community 17 - "Spec 0003 Decision History"
Cohesion: 0.20
Nodes (21): Decision: a product is a clone that changes only its display name, application ID and version through scripts/init-project.sh, keeps every other name, starts with an empty verification record and merges foundation-v tags, Spec 0003 rationale: decision history of the new project spec (context, options considered, rationale), Recommendation: --check does not look for hosted run links, Recommendation: the command does not edit scope rows, Recommendation: the command refuses to run on a derived checkout, Force: foundation fixes must reach products (a fix typed again in each product will not be applied), Force: one maintainer, and real caller first (R8): an unchecked step rests on one person and no tool may exist before something calls it, Force: stable names make a merge clean (31 code and config files and 13 paths carry the foundation name) (+13 more)

### Community 18 - "Shared Settings and Localization"
Cohesion: 0.18
Nodes (19): Never hand-edit generated files, Generators consume neutral sources and never recover canonical values from native output, Decision: keep generated source snapshots in version control and compare against fresh regeneration, Shared resource ownership rules, Shared resources owner (build configuration, localization, brand assets), Deferred: a second language end to end, 004 - Shared settings, text and brand assets (done), shared/assets/ owns future brand artwork and its exports (+11 more)

### Community 19 - "Init Command and Identity Files"
Cohesion: 0.22
Nodes (19): apps/android/identity.properties (Android identity file: applicationId, displayName, versionName, versionCode), apps/ios/Config/Identity.xcconfig (iOS identity file: APP_BUNDLE_IDENTIFIER, APP_DISPLAY_NAME, MARKETING_VERSION, CURRENT_PROJECT_VERSION), Product identity (display name, application IDs, app version): owned by apps/ios/Config/Identity.xcconfig and apps/android/identity.properties; consumed by the Xcode and Gradle builds and scripts/init-project.sh, Derivation only on a copy: init-project.sh with --name rewrites README.md and the verification record and removes graphify-out/, so that form runs only in a temporary clone in the session scratchpad; --check and --test are safe in the worktree, Decision: the tester installs no new tool and test-preferences.json is not created; the framework is the existing Python unittest run through scripts/init-project.sh --test, Sub-session tst-f009-test (tester, opus-5-5 high): Test it for scope 009 over range 44b585b..4a153fe; owns tooling/derive/test_init_project.py and new test files in tooling/derive/, AC-1: both apps carry the same default identity, read from Identity.xcconfig and identity.properties, stated nowhere else under apps/, AC-3: init-project.sh --name --app-id writes name, ID, version 0.1.0 and build 1 into both identity files, with per-value overrides (+11 more)

### Community 20 - "Kotlin FFI Converters"
Cohesion: 0.21
Nodes (7): FfiConverter, FfiConverterRustBuffer, FfiConverterString, FfiType, ByteBuffer, KotlinType, ULong

### Community 21 - "Coordinate Skill Lead Flow"
Cohesion: 0.16
Nodes (20): /coordinate skill: finish one scope with parallel sub-sessions (architect, developer, checker, tester, debugger) while the invoking session acts as lead, Gate Build it and Verify it: closed together by one checker running a full /check verify after the last milestone is merged, Item and ownership: one item is one box or part of a milestone's Build plan steps; ownership is written as file paths, and two items share a wave only when no file is in both ownerships, Lead session: stays on main in the main checkout, picks the SCOPE, splits items, guards the tick gates, merges green branches and writes the log; writes no production code, Limits (Batasan): only the lead edits scope files and merges to main; the lead pushes main only in step 9 and never with force; sub-sessions commit on their own branch and never push or open a PR; some choices always wait for the user, Manual steps (Langkah manual): steps needing the user's eyes, hands, account, device or permission; no session runs them; the box is still ticked when the rest passes and the step is recorded NOT_RUN; a FAIL reopens it, Run defaults of /coordinate: parallel sub-sessions for non-overlapping ownership, wave plan shown then run, debugger on a red gate, decisions follow the decision mode, user-only steps go to the manual file, a feature is marked done at its last box, Standby first turn: all sessions the queue needs are started on the user's turn; reserve sessions and sessions whose item is not ready end their first turn with STATUS: standby until the lead sends start (+12 more)

### Community 22 - "Visual Definitions and Accessibility Checks"
Cohesion: 0.13
Nodes (13): Accessibility (design system), Status conveyed by text or semantics, not color alone, Honor platform reduced-motion setting, Text contrast check (4.5:1 minimum), W3C WCAG 2.2 contrast minimum guidance, 003 - Shared visual definitions (done), Light and dark text meet the documented contrast threshold, Shared named visual values (color, type, spacing, corners, motion) (+5 more)

### Community 23 - "Coordinate Roles and Tick Gates"
Cohesion: 0.25
Nodes (19): Role architect: closes a (spec) box or updates a spec so a developer can build without asking again; owns the feature's docs/specs/<NNNN-slug>/ folder; all code and docs/scope are forbidden, Proposed scope block (blok scope usulan): Pointer line, Design it ticked, Build it with 2 to 5 nested milestones naming Build plan tasks and ACs, and closing boxes by tier, reported for the lead to paste into the scope, Role checker: two modes set by the brief, verify and review; ticks only the verify.md steps it ran or writes a file in docs/reviews; never fixes what it finds, Checker verify mode: proves a milestone or feature behaves per spec by running the verify.md steps, scoped to the milestone section and the AC IDs in the brief, and sends failures to the owning developer, Role debugger: finds and proves the root cause of a failure the lead forwards and proposes a minimal fix to the file owner; never edits others' files; its branch is never merged directly, Role developer: builds one milestone, one Build it box or the named Build plan steps on the files in its ownership; one commit per Build plan step; reports Pointer code in and finished steps to the lead, verify.md milestone section: written by the developer at 'Save verify steps?' (UI / manual, Commands, Acceptance-criteria coverage); with the Status line the only spec content a developer may change, Role tester: writes tests that lock a newly built milestone or feature, runs them and records evidence; owns test files and evidence only; failures go straight to the owning developer (+11 more)

### Community 24 - "Schemas and Sample Names"
Cohesion: 0.15
Nodes (17): Canonical token schema (tokens.schema.json), Draft 7 schema and native mappings updated together, Draft 7 schemas in shared/specifications, 010 - Schemas free of sample names (planned, needs a decision), Replace the greeting with a first feature without editing a foundation schema, Foundation schemas require sample names: the greeting_recipient key in the localization schema and the greeting typography role in the token schema, Follow-up: two foundation schemas still require sample names (greeting_recipient, the greeting role); this deserves its own scope row, greeting_recipient (+9 more)

### Community 25 - "Design Principles and Token Conventions"
Cohesion: 0.17
Nodes (18): Per-target reading order and screen-reader review, Native controls styled with semantic tokens, Design principles, Canonical JSON propagates through code generation, Design definitions compile independently of Cargo and UniFFI, Layout, text measurement, gestures and focus stay in presentation, Semantic names for decisions both apps share, Token conventions (+10 more)

### Community 26 - "Architecture Policy Checks"
Cohesion: 0.24
Nodes (16): Cargo dependency and governance check, Architecture policy result (dependency and required-document checks), 007 - One planning path (done), Required document check covers the scope index, An exact dependency list, not a deny list, Follow-up (settled by spec 0002): record keeping (ADR and plan naming, REQUIRED_DOCS membership, superseding, whether a spec satisfies R10), Follow-up (settled by spec 0002): docs/specs and docs/scope were named by neither repository-structure.md nor REQUIRED_DOCS, R13: the governing documents exist and are not empty (REQUIRED_DOCS) (+8 more)

### Community 27 - "Coordinate Decision Modes and Log"
Cohesion: 0.17
Nodes (16): Accept this spec? handoff: the architect never answers it itself; it sends the spec path, Decision, key tradeoff and decisions taken to the lead, ends the turn with STATUS: needs-decision and continues after accept, Decision mode (Mode keputusan): governs only decisions, the choices that change spec content; an ambiguous AC reading is not a decision, Heavy decision (keputusan berat): expensive to reverse once built (on-disk data format or migration, contract break, security model, licensing, existing user data, changes to an Accepted spec), Mode auto (default): the recommended option is taken for ordinary and heavy decisions, heavy ones flagged berat, Mode tanya: the user decides every decision, Mode tanya berat: the recommended option for ordinary decisions, the user decides heavy ones, Recommended option: the architect takes its own recommendation and writes reason and runner-up in rationale.md; the lead accepts after three checks; every decision is recorded with its runner-up and how to undo it, Lead step 8: end of wave (summary led by heavy delegated decisions and new manual steps, run sync over the wave range, record the next wave's start hash) (+8 more)

### Community 28 - "Anti-Duplication and Review-Only Rules"
Cohesion: 0.18
Nodes (15): Limits of CI checks, Reviewers trace changed behavior from owner into each client, Anti-duplication rules, Locate the owner before adding a constant, rule, DTO, translation or asset, OS-specific capability stays in its own app, Reviewers assess semantic duplication, Trace screen, generated binding, FFI export and core function before changing shared behavior, Native permissions, UIKit delegates and device lifecycle stay in the Apple adapter (+7 more)

### Community 29 - "README and Starting a Product"
Cohesion: 0.24
Nodes (13): Agent workflow: before handoff (run checks, report commands and unverified targets), Pass representative values through both generated languages, Verification before reporting: scripts/test.sh must exit 0; build-ios.sh simulator, device and test in light and dark when apps/ios/ changed; build-android.sh assemble and connectedDebugAndroidTest in both night modes when apps/android/ changed; git status clean and the diff against main limited to ownership files, Follow-up: build the command that takes a foundation release (fetch, merge, apply the ownership table) when the first release is merged into a product, Path ownership after derivation: product owned paths keep the product's side, foundation owned paths take the foundation's side, shared paths merge by hand, README section 'Start a project from this foundation': clone at a tag, create a branch, rename the remote, run the command, add origin, rebuild the graph, mark inherited rows existing, commit, record first results, Take a later foundation release: git fetch foundation --tags, git merge foundation-vX.Y.Z, keep the product's side on product owned paths, rebuild the graph, run every check, Tradeoff: every merge of a foundation release reports conflicts on product owned paths, resolved by hand until the sync command exists (+5 more)

### Community 30 - "Config Schema"
Cohesion: 0.14
Nodes (13): defaultLocale, schemaVersion, additionalProperties, const, properties, defaultLocale, schemaVersion, required (+5 more)

### Community 31 - "iOS App Shell and Native Components"
Cohesion: 0.15
Nodes (13): App, MobileFoundationApp, .body, GreetingScreen, .body, String, Native components guidelines, Greeting as a single text element (+5 more)

### Community 32 - "Architecture Boundaries and Real Callers"
Cohesion: 0.22
Nodes (13): Architecture boundaries, Documented capability boundary; adapters need an actual caller, Layer: design system (generated Swift/Kotlin values as shared visual vocabulary), Layer: native platform integration (Swift owns Apple services, Kotlin owns Android services), Layer: native presentation (views render, adapt to appearance, handle events), Layer: resources and tooling (build-host validation and generation), Create a platform adapter directory only when a feature needs an OS capability, Introduce presentation state or a ViewModel only when needed (+5 more)

### Community 33 - "Native Token Mapping and Text Scaling"
Cohesion: 0.29
Nodes (13): System text scaling via generated text styles, Native token mapping, Compose sp mapping of logical text units, Jetpack Compose token projection (FoundationTokens), Dynamic Type mapping of headline and reading scales, Logical spacing units adapt to display density, spacingPage role, SwiftUI token projection (FoundationTokens) (+5 more)

### Community 34 - "Empty Verification Record and Value Sourcing"
Cohesion: 0.22
Nodes (13): Done when (009): one recorded decision, one command, a hosted check on a temporary copy, clean inherited records, recorded foundation revision, A new product would carry the foundation's verification record, scope rows, hosted run links and knowledge graph as its own, Empty verification record: names the product, foundation URL and ref, lists every target as still unverified, holds no hosted run link, Foundation ref resolution: --foundation-ref, else the highest foundation-v* tag exactly at HEAD, else the full HEAD commit ID, Foundation URL sourcing and normalization: --foundation-url, else the foundation remote, else origin; https, http, ssh and user@host:path forms written as https without user, token, .git or trailing slash, README origin line on line 3: Started from the [mobile foundation](<URL>) at `<ref>` on <date>., User stories: one command names a clone, foundation releases arrive by merge, the verification record lists only what ran here, every push proves the command still works, Force: a copy inherits claims it never earned (the verification record and the scope index name a hosted run in the foundation repository) (+5 more)

### Community 35 - "Generated Native Tokens"
Cohesion: 0.20
Nodes (9): FoundationTokens, Palette, FoundationTokens, Palette, CGFloat, Color, ColorScheme, Font (+1 more)

### Community 36 - "Kotlin Rust Call Status"
Cohesion: 0.23
Nodes (7): E, uniffiCheckCallStatus(), UniffiForeignFutureCompleteVoid, uniffiRustCall(), UniffiRustCallStatusErrorHandler, uniffiRustCallWithError(), U

### Community 37 - "Generator Tests and Drift Checks"
Cohesion: 0.24
Nodes (11): Generated drift remediation, Tokens, configuration and localization check, Design system and resources result (seven generator tests), Shared visual decisions and translations are generator inputs, Drift check plus verification in both appearances and larger text sizes, Regenerate native projections in the same change, Regenerate derived files alongside canonical inputs, Generated native strings owned by the resource generator (+3 more)

### Community 38 - "Identity Value Sourcing"
Cohesion: 0.27
Nodes (9): apps/android/app/src/main/AndroidManifest.xml, apps/android/app/src/main/res/values/app.xml (the app_name string leaves this file; the label comes from the appLabel manifest placeholder), apps/ios/Config/App.xcconfig (iOS app build settings), apps/ios/Config/Project.xcconfig (iOS project build settings), apps/ios/MobileFoundation.xcodeproj/project.pbxproj (Xcode project file), Android build reads identity.properties: app/build.gradle.kts loads applicationId, versionName and versionCode, the label reaches the manifest as the appLabel placeholder, namespace stays foundation.mobile, iOS build reads Identity.xcconfig: Project.xcconfig includes it, App.xcconfig maps the bundle ID and display name, the UI test bundle ID is derived as $(APP_BUNDLE_IDENTIFIER).uitests, Force: identity is spread over files the foundation keeps editing (App.xcconfig, Project.xcconfig, project.pbxproj, app/build.gradle.kts, res/values/app.xml) (+1 more)

### Community 39 - "Pinned Toolchain and Gradle Wrapper"
Cohesion: 0.24
Nodes (9): gradlew script, die(), warn(), target/, build/ and Gradle build directories excluded from source control, Checked-in Gradle wrapper, Binaries, signing material, SDK paths and IDE data stay outside the repository, Exceptions: test literal for the greeting, derived file beside its consumer, Gradle wrapper JAR, OS-specific capability stays in its app, R12: binaries, signing material, SDK paths and IDE data stay out; compiler and dependencies pinned, builds use --locked (+1 more)

### Community 40 - "Supported OS and Large Text Scopes"
Cohesion: 0.25
Nodes (10): CoreImage, Declared Android minimum API 24 not yet exercised, Android largest font scale check, iOS simulator results (iPhone 17 on iOS 27.0 local, iOS 26.5 hosted), iOS 002 - Lowest supported iOS and large text (planned), Declared iOS 17 deployment target not yet exercised, iOS largest accessibility text size check, iOS simulator boots in each system appearance before XCTest (+2 more)

### Community 41 - "Repository States and Default Identity"
Cohesion: 0.25
Nodes (11): The two apps disagree on their own identity (iOS dev.foundation.mobile / Mobile Foundation / 1.0, Android foundation.mobile / Foundation / 0.1.0), init-project.sh --check: prints foundation or derived (exit 0) or names each mismatch in a mixed state (exit 1), Default foundation identity: dev.foundation.mobile, Mobile Foundation, version 0.1.0, build 1, Key invariants: a checkout is foundation or derived, each identity value has one home per platform, the command renames nothing, never runs on a derived or mixed checkout, never changes git state, and foundation tags match foundation-v*, Positive: products install side by side under their own name and ID, a foundation fix reaches every product by one merge, a half derived checkout fails scripts/test.sh, records start empty, the identity mismatch is gone, every native run proves the built identity, Refusals: one line naming the input and the rule, exit 2, nothing written, Repository states: foundation (both IDs default, no origin line), derived (neither ID default, valid origin line), mixed (anything else), Tradeoff: the Android application ID changes from foundation.mobile to dev.foundation.mobile, leaving an old debug build as a separate app (+3 more)

### Community 42 - "iOS Greeting Scope and Sources"
Cohesion: 0.27
Nodes (8): Android physical device coverage unverified, Deferred: signing, physical device runs and store delivery, iOS 001 - Native iOS greeting (existing), Native text style supporting Dynamic Type, Greeting exposed to accessibility in light and dark appearance, iOS physical device coverage unverified, Unsigned iOS device build linked successfully, SwiftUI

### Community 43 - "Android Greeting Scope"
Cohesion: 0.33
Nodes (8): Android 001 - Native Android greeting (existing), API 36 emulator results (arm64 local, x86_64 hosted) in light and dark, Android app packages both supported CPU architectures, Android 002 - Lowest supported Android and large text (planned), 16 KiB memory page packaging, Android scope, Android app owns its screen, appearance changes and native localization lookup, Apple app owns its screen, appearance changes and native localization lookup

### Community 44 - "Android App Shell"
Cohesion: 0.33
Nodes (5): MainActivity, FoundationTheme(), GreetingScreen(), Bundle, ComponentActivity

### Community 45 - "Kotlin Handle Map and Lifting"
Cohesion: 0.42
Nodes (4): InternalException, T, UniffiHandleMap, UniffiNullRustCallStatusErrorHandler

### Community 46 - "Design System Guide and Token Commands"
Cohesion: 0.36
Nodes (8): Design system guide, generate-design-tokens.sh modes: write, --check (drift), --test (failure cases), Generated semantic token API consumed by native apps, Five canonical token JSON files (primitives and semantic aliases), tokens.schema.json: single Draft 7 document keyed by filename stem, SHA-pinned GitHub Actions with read-only contents permission, Shared build and generation commands, fastjsonschema==2.21.2 (sha256 hash-pinned schema validator)

### Community 47 - "test.sh and Derivation Test"
Cohesion: 0.42
Nodes (8): Product identity result (2026-11-15: test.sh passed with --check printing foundation and --test passing 21 unit tests; both apps carried dev.foundation.mobile, Mobile Foundation, 0.1.0, build 1; a copy derived as Zoë's Proof built and matched its identity file), Enforcement: scripts/test.sh runs format, lint, tests and three policy checks; CI runs the same script plus iOS and Android jobs, AC-9: init-project.sh --test runs the unit tests including the derivation on a temporary copy; scripts/test.sh runs it so the foundation CI job proves the command on every push, Derivation test: copies the files git lists to a temporary folder, runs the copy's own command with sample values, requires --check to print derived and check-architecture.py to pass, then removes the copy, The Linux proof runs on every push; the native proof runs by hand before a foundation tag, The Linux proof is one unit test, not a second run of scripts/test.sh, CI job: foundation (locked Rust build + scripts/test.sh on ubuntu-24.04), test.sh script

### Community 48 - "Configuration Guide"
Cohesion: 0.39
Nodes (7): Force: shared/config/README.md keeps bundle and application IDs in Xcode or Gradle, not in the shared config schema, Recommendation: the identity files stay native, Configuration guide, foundation.json: public build-time configuration (v1 schema), Native build settings stay in Xcode or Gradle (deployment targets, bundle and application IDs, entitlements, manifest entries); product identity lives in Identity.xcconfig and identity.properties, Only public settings in shared config; secrets via native credential store or CI secret store, Unknown keys and unsupported schema versions fail the build check; version schema for incompatible changes

### Community 49 - "Knowledge Graph Update Rules"
Cohesion: 0.48
Nodes (7): Agent workflow: before commit (run /graphify . --update, stage graphify-out with the change), Knowledge graph (graphify-out/, kept current with /graphify . --update), Token saving: graph first, files later: lead and sub-sessions ask graphify query and explain before reading files, and open files only where the graph points, Token saving: graph only for changed files: each graph update processes only the files of the commit being prepared; code through graphify update, documents through a restricted /graphify --update whose manifest is stamped for those files only, Graph and commit: the lead fulfils the AGENTS.md /graphify . --update rule when merging to main; sub-sessions never run graphify update and never stage anything under graphify-out/, Main checkout and knowledge graph: run graphify query and graphify explain against the main checkout's graphify-out/graph.json before reading files, and never change a file in the main checkout, Decision: the knowledge graph is updated once per gate event: merged files, scope ticks and the log go into one graph update and one commit, so the AGENTS.md rule is met without repeated extraction

### Community 50 - "Kotlin FFI Integrity Checks"
Cohesion: 0.60
Nodes (3): IntegrityCheckingUniffiLib, uniffiCheckApiChecksums(), uniffiCheckContractApiVersion()

### Community 51 - "Review Gate and Reviewer Rule"
Cohesion: 0.50
Nodes (5): Checker review mode: senior code review of a GA feature with fresh eyes, ranked findings in docs/reviews; only in a new session that has not written, verified or discussed the implementation, Gate Review it (GA features): review by a new checker session that has not seen the implementation, file in docs/reviews; Blocker or Major findings start a fix item; ticked when none remain open, Token saving: reuse a finished sub-session for the next item of the same feature after clearing its context; never for Review it, Reviewer rule: the reviewer must be a different model family from every author in the change range, Sub-session status values in the log: standby, aktif, peer, done, blocked, failed, merged, dipakai ulang, diarsipkan, tidak di-merge

### Community 52 - "Scope 009 Manual Steps"
Cohesion: 0.50
Nodes (5): Manual steps rule: GUI apps, GitHub web pages, physical devices, signing, installing tools, repository settings, push and triggering or repeating workflows are done only by the user or the lead; gh is read-only; headless simulators and emulators are allowed; a failed or flaky step is reported failed, not manual, Manual steps (Langkah manual) for scope 009 - A new project from the foundation: steps that need the user's eyes, hands, account, device or permission and that no session runs, Manual steps of feature 009 A new project from the foundation (spec 0003): no step yet, Manual step summary (Ringkasan) for scope 009 (ID, step, AC, boxes ticked while the step is NOT_RUN, runnable after, result): no step yet; the lead adds rows when a sub-session report contains manual steps, Values from the user (Nilai dari user): values only the user knows; the waiting AC stays BLOCKED until the value exists; none yet

### Community 53 - "Android Rust Build Script"
Cohesion: 0.40
Nodes (4): CARGO_TARGET_AARCH64_LINUX_ANDROID_LINKER, CARGO_TARGET_X86_64_LINUX_ANDROID_LINKER, PATH, build-android-rust.sh script

### Community 54 - "iOS Rust Build Script"
Cohesion: 0.50
Nodes (3): CARGO_TARGET_DIR, PATH, build-ios-rust.sh script

## Knowledge Gaps
- **66 isolated node(s):** `NoHandle`, `UniffiWithHandle`, `Explicit application records and enums; private core/transport shapes mapped at the adapter`, `apiChecksumMismatch`, `contractVersionMismatch` (+61 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `GreetingScreen` connect `iOS App Shell and Native Components` to `Native Token Mapping and Text Scaling`, `iOS Greeting Scope and Sources`, `Anti-Duplication and Review-Only Rules`?**
  _High betweenness centrality (0.141) - this node is a cross-community bridge._
- **Why does `.body` connect `iOS App Shell and Native Components` to `Swift UniFFI Bindings`?**
  _High betweenness centrality (0.131) - this node is a cross-community bridge._
- **Why does `hello()` connect `Swift UniFFI Bindings` to `iOS App Shell and Native Components`?**
  _High betweenness centrality (0.124) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Foundation verification 2026-11-15` (e.g. with `Record separately what compiled and what ran` and `tooling/derive/verification-record.md (empty verification record template for a derived product)`) actually correct?**
  _`Foundation verification 2026-11-15` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `NoHandle`, `UniffiWithHandle`, `Explicit application records and enums; private core/transport shapes mapped at the adapter` to the rest of the system?**
  _66 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Swift UniFFI Bindings` be split into smaller, more focused modules?**
  _Cohesion score 0.05444596443228454 - nodes in this community are weakly interconnected._
- **Should `Kotlin FFI Library Loading` be split into smaller, more focused modules?**
  _Cohesion score 0.055288461538461536 - nodes in this community are weakly interconnected._