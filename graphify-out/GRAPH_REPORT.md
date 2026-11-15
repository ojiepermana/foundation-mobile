# Graph Report - mobile  (2026-11-15)

## Corpus Check
- 4 files · ~74,891 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1224 nodes · 3297 edges · 66 communities (65 shown, 1 thin omitted)
- Extraction: 78% EXTRACTED · 22% INFERRED · 0% AMBIGUOUS · INFERRED: 738 edges (avg confidence: 0.89)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Planning Path, Scope Index and Policy Checks
- Swift UniFFI Bindings
- Verification Record and CI Workflow
- Kotlin FFI Library Loading
- Kotlin UniFFI Library Calls
- Derivation Command
- Derivation Refusal Tests
- Rust Core and Greeting Contract
- Derivation Run and Origin Line Tests
- Architecture Compliance and Spec Triggers
- Spec 0001 Ownership Rules
- Init Command and Identity Files
- Coordinate Skill Lead Flow
- Resource Generator
- Derivation Test Checkout Fixture
- Kotlin RustBuffer Handling
- Shared Settings and Localization
- Spec 0003 Acceptance Criteria
- Spec 0003 Decision History
- Rule Set and Contract Rules
- Kotlin FFI Converters
- Visual Definitions and Accessibility Checks
- Schemas and Sample Names
- Architecture Overview and Founding Decision
- Ownership Matrix and Repository Structure
- Coordinate Roles and Report Template
- Generator Tests and Drift Checks
- Real Checkout and Outside Git Tests
- Design Principles and Token Conventions
- test.sh and Derivation Test
- Scope 009 Coordination Log
- Empty Verification Record and Value Sourcing
- Config Schema
- Generated Files and Shared Sources Rules
- iOS Greeting Scope and Unverified Devices
- Scope 009 General Brief Rules
- Native Token Mapping and Text Scaling
- Scope 009 Row and Verify Steps
- iOS App Shell
- Android Greeting and Supported OS Scopes
- Kotlin Rust Call Status
- Architecture Boundaries and Real Callers
- README and Starting a Product
- Identity Value Sourcing
- Coordinate Decision Modes and Log
- Contract Extension and Deferred Work
- Derivation State Check Tests
- Android App Shell
- Kotlin Handle Map and Lifting
- Design System Guide and Token Commands
- Command Line Wrapper Tests
- Knowledge Graph Update Rules
- Coordinate Tick Gates and Manual Steps
- Refusals and Input Validation
- Generated Swift Tokens
- Generated Kotlin Tokens
- Kotlin FFI Integrity Checks
- Scope 009 Manual Steps
- Android Rust Build Script
- Derivation Write Failure Tests
- Android Gradle Wrapper
- Native Component Guidelines
- iOS Rust Build Script

## God Nodes (most connected - your core abstractions)
1. `Spec 0002: One planning path: a scope row first, then a spec` - 60 edges
2. `Foundation verification 2026-11-15` - 59 edges
3. `Spec 0001: One owner per responsibility, with rules kept beside the code` - 56 edges
4. `UniffiLib` - 54 edges
5. `Spec 0003: A new project from the foundation: product identity in two files, one init command, updates by merge (In Progress)` - 53 edges
6. `DerivationTests` - 46 edges
7. `Mobile foundation scope (index)` - 44 edges
8. `Decision: a new capability is planned as a scope row and designed in a spec before code; docs/plans and new ADRs are retired in a single change` - 38 edges
9. `Spec 0003 rationale: decision history of the new project spec (context, options considered, rationale)` - 35 edges
10. `Rollout: one change in fifteen ordered steps (rules, AGENTS.md, architecture docs, README, validator, delete docs/plans, scope files, spec 0001, knowledge graph)` - 33 edges

## Surprising Connections (you probably didn't know these)
- `Greeting as a single text element` --references--> `GreetingScreen`  [INFERRED]
  docs/design-system/component-guidelines.md → apps/ios/Presentation/GreetingScreen.swift
- `Trace screen, generated binding, FFI export and core function before changing shared behavior` --references--> `GreetingScreen`  [INFERRED]
  docs/rules/development-rules.md → apps/ios/Presentation/GreetingScreen.swift
- `Render the returned Rust string verbatim` --references--> `GreetingScreen`  [INFERRED]
  docs/rules/ios-rules.md → apps/ios/Presentation/GreetingScreen.swift
- `SwiftUI presentation with Dynamic Type and adaptive appearance` --references--> `GreetingScreen`  [INFERRED]
  docs/rules/ios-rules.md → apps/ios/Presentation/GreetingScreen.swift
- `Product identity result (2026-11-15: test.sh passed with --check printing foundation and --test passing 21 unit tests; both apps carried dev.foundation.mobile, Mobile Foundation, 0.1.0, build 1; a copy derived as Zoë's Proof built and matched its identity file)` --references--> `GreetingTest`  [INFERRED]
  docs/quality/verification.md → apps/android/app/src/androidTest/kotlin/foundation/mobile/GreetingTest.kt

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Coordination records of scope 009: the log, the general brief rules and the manual steps list, all tied to the scope row** — docs_scope_coordination_009_a_new_project_from_the_foundation_log, docs_scope_coordination_009_a_new_project_from_the_foundation_brief_umum, docs_scope_coordination_009_a_new_project_from_the_foundation_manual, docs_scope_root_009_a_new_project_from_the_foundation [EXTRACTED 1.00]
- **Wave 1 ownership split: developer on the verification record, checker on the verify.md ticks, tester on the derivation tests, with no overlap** — docs_scope_coordination_009_a_new_project_from_the_foundation_log_dev_f009_m3, docs_scope_coordination_009_a_new_project_from_the_foundation_log_chk_f009_verify, docs_scope_coordination_009_a_new_project_from_the_foundation_log_tst_f009_test, docs_quality_verification, docs_specs_root_0003_new_project_from_foundation_verify, tooling_derive_test_init_project, docs_scope_coordination_009_a_new_project_from_the_foundation_log_parallel_start [EXTRACTED 1.00]
- **Derived hosted run 43701289339 as evidence for AC-10: the workflow input, the derive step and both identity comparisons ran on hosted runners** — docs_quality_verification_hosted_run_43701289339, docs_quality_verification_derived_hosted_foundation_job_result, docs_quality_verification_derived_hosted_ios_job_result, docs_quality_verification_derived_hosted_android_job_result, github_workflows_foundation_derived_input, github_workflows_foundation_derive_sample_product_step, github_workflows_foundation_ios_identity_comparison_step, github_workflows_foundation_android_identity_comparison_step, docs_specs_root_0003_new_project_from_foundation_index_ac_10, docs_scope_coordination_009_a_new_project_from_the_foundation_log_hosted_run_43701289339 [INFERRED 0.95]
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
- **The five sub-session roles of /coordinate, each with its own goal, ownership, message paths and model** — claude_skills_coordinate_roles_architect, claude_skills_coordinate_roles_developer, claude_skills_coordinate_roles_checker, claude_skills_coordinate_roles_tester, claude_skills_coordinate_roles_debugger, claude_skills_coordinate_skill_sub_session, claude_skills_coordinate_skill_model_per_role [EXTRACTED 1.00]
- **Tick gates of /coordinate: what must be true on main before the lead ticks each kind of scope box** — claude_skills_coordinate_skill_step_6_tick_gate_and_merge, claude_skills_coordinate_skill_gate_design_it, claude_skills_coordinate_skill_gate_milestone, claude_skills_coordinate_skill_gate_build_it_and_verify_it, claude_skills_coordinate_skill_gate_test_it, claude_skills_coordinate_skill_gate_review_it, claude_skills_coordinate_skill_gate_document_it, claude_skills_coordinate_skill_red_gate_cycle [EXTRACTED 1.00]
- **Greeting vertical slice: localized recipient through UniFFI to the Rust formatter** — readme_hello_world_greeting, shared_localization_readme_greeting_recipient, docs_architecture_overview_greeting_call_flow, docs_contracts_ffi_conventions_hello_contract, docs_architecture_overview_foundation_core_hello, docs_architecture_ownership_matrix_crates_mobile_ffi, docs_architecture_ownership_matrix_bindings, readme_uniffi [EXTRACTED 1.00]
- **One planning path: a scope row first, then a spec before code, named by the agent instructions, the development rules and the repository structure** — docs_specs_root_0002_one_planning_path_decision_scope_row_then_spec, docs_specs_root_0002_one_planning_path_canonical_planning_pattern, docs_rules_development_rules_scope_row_then_spec, agents_scope_row_and_spec_before_code, docs_scope_root_007_one_planning_path, docs_scope_index, docs_architecture_repository_structure_docs_record_homes, docs_specs_root_0001_ownership_development_rules_r10_scope_row_and_spec_for_capability_spec_for_material_decision [EXTRACTED 1.00]
- **Spec triggers kept in their owner files: when a smaller change needs a spec** — docs_specs_root_0002_one_planning_path_trigger_owner_files, docs_rules_development_rules_spec_triggers_for_smaller_changes, docs_rules_service_rules_spec_for_new_crate_or_boundary, docs_quality_architecture_compliance_spec_for_architecture_change, docs_architecture_dependency_rules_new_edge_proposal, docs_contracts_ffi_conventions_compatibility_versioning, docs_decisions_adr_0001_foundation_revisit_conditions, docs_specs_root_0001_ownership_development_rules_spec_triggers [EXTRACTED 1.00]
- **Design token pipeline from canonical JSON to native projections** — docs_design_system_token_conventions_canonical_token_sources, design_system_schemas_tokens_schema, scripts_generate_design_tokens, docs_design_system_platform_mapping_swiftui_token_projection, docs_design_system_platform_mapping_compose_token_projection, docs_quality_architecture_compliance_tokens_config_localization_check [INFERRED 0.85]
- **Neutral JSON sources validated and generated into native theme and string resources** — design_system_readme_token_files, design_system_readme_tokens_schema, shared_config_readme_foundation_json, shared_localization_readme_catalog_format, design_system_readme_generate_design_tokens_modes, tooling_codegen_requirements_fastjsonschema, design_system_readme_generated_semantic_api, shared_localization_readme_generated_native_strings [INFERRED 0.85]
- **Regenerate derived outputs with their canonical source, never hand-edit** — docs_rules_development_rules_regenerate_derived_files, docs_rules_design_system_rules_regenerate_projections, docs_quality_architecture_compliance_generated_drift_remediation, docs_rules_rust_rules_regenerate_after_signature_change, docs_rules_shared_resources_rules_generated_native_strings, docs_rules_anti_duplication_ffi_shapes_in_rust_export [INFERRED 0.85]
- **Manual step flow: a sub-session reports a manual step, the lead lists it, the user runs it and the checker ticks verify.md from the result** — docs_scope_coordination_009_a_new_project_from_the_foundation_brief_umum_manual_steps_rule, docs_scope_coordination_009_a_new_project_from_the_foundation_manual, docs_scope_coordination_009_a_new_project_from_the_foundation_manual_summary, docs_scope_coordination_009_a_new_project_from_the_foundation_manual_result_routing, docs_scope_coordination_009_a_new_project_from_the_foundation_log_chk_f009_verify, docs_specs_root_0003_new_project_from_foundation_verify [INFERRED 0.85]
- **Verification evidence chain: local checks, hosted jobs and the verification record** — docs_scope_root_005_reproducible_local_builds_and_checks, docs_scope_root_006_hosted_build_verification, docs_scope_root_008_hosted_results_in_the_verification_record, docs_scope_root_008_hosted_results_in_the_verification_record_single_list_of_unverified_targets [INFERRED 0.85]
- **Coordination templates (brief, general rules, log, manual, report) and the scope 009 records filled from them** — claude_skills_coordinate_templates_brief, claude_skills_coordinate_templates_brief_umum, claude_skills_coordinate_templates_log, claude_skills_coordinate_templates_manual, claude_skills_coordinate_templates_report, docs_scope_coordination_009_a_new_project_from_the_foundation_brief_umum, docs_scope_coordination_009_a_new_project_from_the_foundation_log, docs_scope_coordination_009_a_new_project_from_the_foundation_manual [INFERRED 0.95]

## Communities (66 total, 1 thin omitted)

### Community 0 - "Planning Path, Scope Index and Policy Checks"
Cohesion: 0.07
Nodes (90): AGENTS.md: Working in the mobile foundation, Agent workflow: before handoff (run checks, report commands and unverified targets), Agent workflow: during implementation (place change in owning layer), Plan a new capability in the scope and write its spec under docs/specs before code, Architecture overview, docs/ and root AGENTS.md: architecture, decision records, scope and agent workflow, docs/ record homes: docs/scope (what to build and its status), docs/specs (design and decision records), docs/decisions (the founding decision), ADR 0001: Native apps with a shared Rust core (+82 more)

### Community 1 - "Swift UniFFI Bindings"
Cohesion: 0.05
Nodes (64): Array, createReader(), createWriter(), Data, FfiConverter, FfiConverterPrimitive, FfiConverterRustBuffer, FfiConverterString (+56 more)

### Community 2 - "Verification Record and CI Workflow"
Cohesion: 0.07
Nodes (65): GreetingTest, GreetingUITests, UInt8, CIContext, Pass representative values through both generated languages, Android linkage and UI check (Linux CI job, emulator instrumentation), GitHub Actions CI jobs (macOS and Linux), iOS linkage and UI check (macOS CI job, XCTest) (+57 more)

### Community 3 - "Kotlin FFI Library Loading"
Cohesion: 0.06
Nodes (34): Disposable, NoHandle, UniffiByValue, UniffiCallbackInterfaceClone, UniffiCallbackInterfaceFree, UniffiForeignFutureCompleteF32, UniffiForeignFutureCompleteF64, UniffiForeignFutureCompleteI16 (+26 more)

### Community 4 - "Kotlin UniFFI Library Calls"
Cohesion: 0.06
Nodes (3): UniffiLib, UniffiRustCallStatus, UniffiRustFutureContinuationCallback

### Community 5 - "Derivation Command"
Cohesion: 0.12
Nodes (30): Exception, check(), derive(), foundation_ref(), foundation_url(), git(), identity_text(), in_git() (+22 more)

### Community 6 - "Derivation Refusal Tests"
Cohesion: 0.09
Nodes (15): DerivationTests, AC-6, AC-7: every accepted remote form becomes https without credentials; the…, AC-7: a local path remote, or no remote, is no usable foundation URL., AC-7: each input that breaks its rule is refused with exit 2, one line and no…, AC-7: a remote URL that is not UTF-8 is no usable foundation URL., AC-7: the in git test compares folders, not path spellings., AC-7: a derived checkout is refused., AC-5: the template on disk, filled with the sample values, is the empty record… (+7 more)

### Community 7 - "Rust Core and Greeting Contract"
Cohesion: 0.13
Nodes (24): hello(), preserves_empty_names_and_whitespace(), String, hello(), String, tests/contracts: Cargo integration tests for exported behavior, Core and FFI contract tests (locked Cargo tests), UniFFI generated files drift check (+16 more)

### Community 8 - "Derivation Run and Origin Line Tests"
Cohesion: 0.10
Nodes (13): AC-3, AC-5, AC-6, AC-8: the happy path writes every file and the checkout then…, AC-3: each override reaches only its own identity file, and --version reaches…, AC-3: with one override the other platform keeps --app-id., AC-3, AC-7: a value that starts with a hyphen is refused, and its equals form…, AC-6: without the flags the origin line takes the remote, HEAD and today., AC-6: the foundation remote wins over origin, and the highest release tag wins., AC-3: the example of the criterion, with no other flag, writes 0.1.0 and build…, AC-4: each file is replaced in the documented order, and graphify-out/ goes… (+5 more)

### Community 9 - "Architecture Compliance and Spec Triggers"
Cohesion: 0.19
Nodes (25): Dependency rules, New dependency edge needs an owning module, a use case and a test, Compatibility: version breaking contracts and coordinate regeneration, both apps and release, Revisit conditions: dependency direction change, async native boundary, independently versioned clients, new shared crate or service, Architecture compliance, Limits of CI checks, Physical hardware verification for simulator-inaccessible capabilities, Reviewers trace changed behavior from owner into each client (+17 more)

### Community 10 - "Spec 0001 Ownership Rules"
Cohesion: 0.16
Nodes (25): Color selection, font scaling, layout and accessibility run natively (no shared renderer), Rejected alternative: shared UI runtime, One owner per shared responsibility (ten responsibilities in the ownership matrix), Spec 0001: One owner per responsibility, with rules kept beside the code, Automate only what a machine can judge, Decision: one owner per responsibility in an ownership matrix, topic-sized rule files, short AGENTS.md entry point, automated checks only where a machine is reliable, Enforcement: scripts/test.sh runs format, lint, tests and three policy checks; CI runs the same script plus iOS and Android jobs, An exact dependency list, not a deny list (+17 more)

### Community 11 - "Init Command and Identity Files"
Cohesion: 0.18
Nodes (23): apps/android/identity.properties (Android identity file: applicationId, displayName, versionName, versionCode), apps/ios/Config/Identity.xcconfig (iOS identity file: APP_BUNDLE_IDENTIFIER, APP_DISPLAY_NAME, MARKETING_VERSION, CURRENT_PROJECT_VERSION), Product identity (display name, application IDs, app version): owned by apps/ios/Config/Identity.xcconfig and apps/android/identity.properties; consumed by the Xcode and Gradle builds and scripts/init-project.sh, Derivation only on a copy: init-project.sh with --name rewrites README.md and the verification record and removes graphify-out/, so that form runs only in a temporary clone in the session scratchpad; --check and --test are safe in the worktree, init-project.sh --check: prints foundation or derived (exit 0) or names each mismatch in a mixed state (exit 1), Init write set: the two identity files, the README title and origin line, the empty verification record and the removal of graphify-out/, Key invariants: a checkout is foundation or derived, each identity value has one home per platform, the command renames nothing, never runs on a derived or mixed checkout, never changes git state, and foundation tags match foundation-v*, Product identity data model: application ID, display name, version and build in two identity files, one origin line, two repository states (+15 more)

### Community 12 - "Coordinate Skill Lead Flow"
Cohesion: 0.14
Nodes (24): Checker review mode: senior code review of a GA feature with fresh eyes, ranked findings in docs/reviews; only in a new session that has not written, verified or discussed the implementation, /coordinate skill: finish one scope with parallel sub-sessions (architect, developer, checker, tester, debugger) while the invoking session acts as lead, Gate Review it (GA features): review by a new checker session that has not seen the implementation, file in docs/reviews; Blocker or Major findings start a fix item; ticked when none remain open, Item and ownership: one item is one box or part of a milestone's Build plan steps; ownership is written as file paths, and two items share a wave only when no file is in both ownerships, Lead session: stays on main in the main checkout, picks the SCOPE, splits items, guards the tick gates, merges green branches and writes the log; writes no production code, Limits (Batasan): only the lead edits scope files and merges to main; the lead pushes main only in step 9 and never with force; sub-sessions commit on their own branch and never push or open a PR; some choices always wait for the user, Token saving: reuse a finished sub-session for the next item of the same feature after clearing its context; never for Review it, Reviewer rule: the reviewer must be a different model family from every author in the change range (+16 more)

### Community 13 - "Resource Generator"
Cohesion: 0.14
Nodes (19): check_schema(), generate(), load(), projections(), Validate authoritative sources, then materialize or check their projections., unique_members(), validator(), native_text() (+11 more)

### Community 14 - "Derivation Test Checkout Fixture"
Cohesion: 0.13
Nodes (11): Checkout, AC-4: git sees changes in exactly the documented paths, and no rename., AC-7: a modified or untracked file is refused, even when git status hides…, AC-4: a graph removal that fails names every changed path and the way back., AC-7: a mixed checkout is refused., AC-4: a checkout that has no graph changes only the two identity files,…, AC-6: a README.md of one line without a newline still ends with the title,…, AC-6: only a foundation-v tag that points exactly at HEAD names the ref;… (+3 more)

### Community 15 - "Kotlin RustBuffer Handling"
Cohesion: 0.14
Nodes (9): ByReference, ByValue, ForeignBytes, `hello`(), RustBuffer, uniffiTraitInterfaceCall(), uniffiTraitInterfaceCallWithError(), kotlin (+1 more)

### Community 16 - "Shared Settings and Localization"
Cohesion: 0.16
Nodes (21): Build-time generation: token JSON and locale JSON -> native theme inputs and localization resources, Shared resource ownership rules, Shared resources owner (build configuration, localization, brand assets), Deferred: a second language end to end, 004 - Shared settings, text and brand assets (done), shared/assets/ owns future brand artwork and its exports, Greeting sentence 'Hello, {name}!' formed in English by the core, Invalid settings, resource keys and mismatched translation placeholders are rejected (+13 more)

### Community 17 - "Spec 0003 Acceptance Criteria"
Cohesion: 0.20
Nodes (23): Ticked in wave 1: 009 Test it, from the tst-f009-test report done (21 to 50 tests, AC-3 to AC-9 each have a test carrying its ID, commit dc9a8d9); on main with the merge staged there were no conflict markers and scripts/test.sh exited 0, Build steps (009): identity file per platform (AC-1, AC-2, done), init command with state check and unit tests (AC-3 to AC-9, done), workflow derived input and identity comparison (AC-10, open), README path and document updates (AC-11, AC-12, done), The two apps disagree on their own identity (iOS dev.foundation.mobile / Mobile Foundation / 1.0, Android foundation.mobile / Foundation / 0.1.0), Spec 0003: A new project from the foundation: product identity in two files, one init command, updates by merge (In Progress), AC-1: both apps carry the same default identity, read from Identity.xcconfig and identity.properties, stated nowhere else under apps/, AC-11: README.md has a section with the full path from clone to first results, path ownership, taking a later release and foundation tagging, AC-2: with the default identity scripts/test.sh passes, both apps build and the greeting tests pass in both appearances, AC-3: init-project.sh --name --app-id writes name, ID, version 0.1.0 and build 1 into both identity files, with per-value overrides (+15 more)

### Community 18 - "Spec 0003 Decision History"
Cohesion: 0.18
Nodes (22): Decision: a product is a clone that changes only its display name, application ID and version through scripts/init-project.sh, keeps every other name, starts with an empty verification record and merges foundation-v tags, Follow-up: revisit keeping MobileFoundation as the Xcode project and scheme name if it confuses contributors to a product, Names the foundation keeps: MobileFoundation project, targets and scheme, rootProject.name, crates foundation-core and mobile-ffi, mobile_ffi namespace, Kotlin packages, FoundationTokens, FoundationTheme, foundation_strings.xml, foundation.json, the workflow file, Tradeoff: a command and its unit tests are kept for a job that runs once per product, Tradeoff: foundation names stay in product code (MobileFoundation project, scheme and bundle, Foundation-prefixed types and packages); users see only the display name, Tradeoff: later foundation scope rows and specs do not flow into products; the reason behind a new foundation rule is read in the foundation repository, Tradeoff: a product carries the foundation's commit history and its foundation-v tags, Spec 0003 rationale: decision history of the new project spec (context, options considered, rationale) (+14 more)

### Community 19 - "Rule Set and Contract Rules"
Cohesion: 0.14
Nodes (20): main(), target/, build/ and Gradle build directories excluded from source control, Mobile contract (FFI conventions), UniFFI derives native functions, buffer handling and contract checks; no raw pointers or hand-maintained C ABI declarations, Checked-in Gradle wrapper, Application code displays the binding's return value, OS-specific capability stays in its own app, Binaries, signing material, SDK paths and IDE data stay outside the repository (+12 more)

### Community 20 - "Kotlin FFI Converters"
Cohesion: 0.21
Nodes (7): FfiConverter, FfiConverterRustBuffer, FfiConverterString, FfiType, ByteBuffer, KotlinType, ULong

### Community 21 - "Visual Definitions and Accessibility Checks"
Cohesion: 0.14
Nodes (14): Accessibility (design system), Status conveyed by text or semantics, not color alone, Honor platform reduced-motion setting, Text contrast check (4.5:1 minimum), W3C WCAG 2.2 contrast minimum guidance, Tokens, configuration and localization check, Design system and resources result (seven generator tests), 003 - Shared visual definitions (done) (+6 more)

### Community 22 - "Schemas and Sample Names"
Cohesion: 0.15
Nodes (17): Canonical token schema (tokens.schema.json), Draft 7 schema and native mappings updated together, Draft 7 schemas in shared/specifications, 010 - Schemas free of sample names (planned, needs a decision), Replace the greeting with a first feature without editing a foundation schema, Foundation schemas require sample names: the greeting_recipient key in the localization schema and the greeting typography role in the token schema, Follow-up: two foundation schemas still require sample names (greeting_recipient, the greeting role); this deserves its own scope row, greeting_recipient (+9 more)

### Community 23 - "Architecture Overview and Founding Decision"
Cohesion: 0.23
Nodes (16): Workspace edge: mobile-ffi depends on foundation-core (std-only core), Proc-macro exports define the cross-language API; bindgen feature gates host CLI deps, foundation_core::hello (sole greeting formatter), Greeting call flow: SwiftUI/Compose -> generated binding -> C ABI/JNA -> mobile-ffi -> foundation-core, crates/core: owner of shared behavior, domain rules and application validation, crates/mobile-ffi: owner of cross-language API, records and typed errors (UniFFI), Public contract: hello(name: String) -> String in crates/mobile-ffi, Decision: two Cargo workspace members; dependency-free core exported through UniFFI to native apps (+8 more)

### Community 24 - "Ownership Matrix and Repository Structure"
Cohesion: 0.30
Nodes (16): Agent workflow: before editing (locate owner, contract, callers, tests), App trees do not import one another; core never calls platform UI, Ownership matrix, apps/android: owner of Android UI, presentation state and OS APIs, apps/ios: owner of Apple UI, presentation state and OS APIs, design-system/tokens and schemas: owner of canonical visual values and semantic roles, scripts/ and .github/workflows/: build and verification orchestration, shared/config, shared/localization, shared/assets: owner of public settings, locale content and brand masters (+8 more)

### Community 25 - "Coordinate Roles and Report Template"
Cohesion: 0.30
Nodes (15): Role architect: closes a (spec) box or updates a spec so a developer can build without asking again; owns the feature's docs/specs/<NNNN-slug>/ folder; all code and docs/scope are forbidden, Proposed scope block (blok scope usulan): Pointer line, Design it ticked, Build it with 2 to 5 nested milestones naming Build plan tasks and ACs, and closing boxes by tier, reported for the lead to paste into the scope, Role checker: two modes set by the brief, verify and review; ticks only the verify.md steps it ran or writes a file in docs/reviews; never fixes what it finds, Role debugger: finds and proves the root cause of a failure the lead forwards and proposes a minimal fix to the file owner; never edits others' files; its branch is never merged directly, Role developer: builds one milestone, one Build it box or the named Build plan steps on the files in its ownership; one commit per Build plan step; reports Pointer code in and finished steps to the lead, Role tester: writes tests that lock a newly built milestone or feature, runs them and records evidence; owns test files and evidence only; failures go straight to the owning developer, Evidence labels: fixture or native, with native only for a run with a real binary; a fixture pass is not native proof, and missing hardware, binary or signing is recorded BLOCKED, Gate Design it (spec): spec accepted per decision mode, architect branch merged, spec has Requirements with AC IDs, Decision, Build plan and Consequences; the lead then adds the Pointer line and milestones to the scope (+7 more)

### Community 26 - "Generator Tests and Drift Checks"
Cohesion: 0.20
Nodes (14): Stable role names or same-change migration, Generated drift remediation, Shared visual decisions and translations are generator inputs, Design system rules, Drift check plus verification in both appearances and larger text sizes, Regenerate native projections in the same change, Public role name changes require migrating both consumers, Regenerate derived files alongside canonical inputs (+6 more)

### Community 27 - "Real Checkout and Outside Git Tests"
Cohesion: 0.14
Nodes (9): Unit tests create their own repository in a temporary folder with isolated git configuration; no test touches the real checkout, OutsideGitTests, Checks for the derivation command: every write, every refusal and both clean…, AC-9: the derivation proof is skipped, with its reason, in a checkout that is…, AC-7: outside git both foundation values are required., AC-7: a folder inside another repository counts as outside git., Run the checked in command on a temporary copy of this checkout. The checkout…, AC-9: the copy's own command derives the copy, which then reads derived and… (+1 more)

### Community 28 - "Design Principles and Token Conventions"
Cohesion: 0.21
Nodes (14): Per-target reading order and screen-reader review, Native controls styled with semantic tokens, Design principles, Canonical JSON propagates through code generation, Design definitions compile independently of Cargo and UniFFI, Layout, text measurement, gestures and focus stay in presentation, Semantic names for decisions both apps share, Token conventions (+6 more)

### Community 29 - "test.sh and Derivation Test"
Cohesion: 0.26
Nodes (13): Project identity state check (init-project.sh --check and --test, CI identity comparison), Rust format and lint check (rustfmt, Clippy warnings denied), Derived hosted run foundation job result (locked build and scripts/test.sh passed: three Rust tests, 21 derivation tests, seven generator tests; this job does not derive), Product identity result (2026-11-15: test.sh passed with --check printing foundation and --test passing 21 unit tests; both apps carried dev.foundation.mobile, Mobile Foundation, 0.1.0, build 1; a copy derived as Zoë's Proof built and matched its identity file), Rust workspace result (Rust 1.100.0, locked build, three tests passed), AC-9: init-project.sh --test runs the unit tests including the derivation on a temporary copy; scripts/test.sh runs it so the foundation CI job proves the command on every push, Derivation test: copies the files git lists to a temporary folder, runs the copy's own command with sample values, requires --check to print derived and check-architecture.py to pass, then removes the copy, init-project.sh --test: runs the unit tests under tooling/derive/ (+5 more)

### Community 30 - "Scope 009 Coordination Log"
Cohesion: 0.22
Nodes (14): Session model per role: developer claude-opus-5-5 medium, tester claude-opus-5-5 high, checker verify claude-fable-5-2 high, debugger claude-fable-5-2 medium, Sub-session flow: read the brief, the general rules, then the role file in the main checkout, call the skill the brief names, and only then work in the existing worktree and branch; a reused session runs git merge main first, Coordination log (Log koordinasi) for scope 009 - A new project from the foundation (wave 1 active, decision mode auto, start hash 4a153fe, updated 2026-11-15 17:55), Decision (user): 'Ya, commit': .claude/skills/coordinate entered main as ed84a93; rust-async-patterns and rust-best-practices were not asked about and stay untracked, Decision: the .claude/skills/coordinate folder is not committed on main, so sub-sessions read role files and templates from the main checkout by absolute path; the user is asked to decide on committing it, Decision: scope 009 has no Review it and Document it boxes (Beta flow), so no backup review session is reserved, Open blocker: .claude/skills/rust-async-patterns/ and .claude/skills/rust-best-practices/ are untracked in the main checkout; at the push of step 9 both are treated as a known exception unless the user asks for a commit, Decision: checker and tester start together with the developer, because Build plan steps 1 to 10 are complete on main and the three ownerships do not overlap; ticks still wait for the gate (+6 more)

### Community 31 - "Empty Verification Record and Value Sourcing"
Cohesion: 0.20
Nodes (14): Empty verification record: names the product, foundation URL and ref, lists every target as still unverified, holds no hosted run link, Foundation ref resolution: --foundation-ref, else the highest foundation-v* tag exactly at HEAD, else the full HEAD commit ID, Foundation URL sourcing and normalization: --foundation-url, else the foundation remote, else origin; https, http, ssh and user@host:path forms written as https without user, token, .git or trailing slash, README origin line on line 3: Started from the [mobile foundation](<URL>) at `<ref>` on <date>., User stories: one command names a clone, foundation releases arrive by merge, the verification record lists only what ran here, every push proves the command still works, Recommendation: --check does not look for hosted run links, Force: a copy inherits claims it never earned (the verification record and the scope index name a hosted run in the foundation repository), Inherited scope rows and specs stay as history (+6 more)

### Community 32 - "Config Schema"
Cohesion: 0.14
Nodes (13): defaultLocale, schemaVersion, additionalProperties, const, properties, defaultLocale, schemaVersion, required (+5 more)

### Community 33 - "Generated Files and Shared Sources Rules"
Cohesion: 0.21
Nodes (13): Never hand-edit generated files, Generators consume neutral sources and never recover canonical values from native output, bindings/swift and bindings/kotlin: generated FFI source snapshots, Derived file rule: change the canonical input and regenerate every output in the same review, Decision: keep generated source snapshots in version control and compare against fresh regeneration, Rejected alternative: implementing application behavior independently in both apps, Follow-up: a small import scan in check-architecture.py for R3, Force: generated files sit beside hand-written code (edits there are lost or hide a mismatch) (+5 more)

### Community 34 - "iOS Greeting Scope and Unverified Devices"
Cohesion: 0.19
Nodes (12): CoreImage, Android physical device coverage unverified, Deferred: signing, physical device runs and store delivery, iOS 001 - Native iOS greeting (existing), Native text style supporting Dynamic Type, Greeting exposed to accessibility in light and dark appearance, iOS physical device coverage unverified, iOS simulator results (iPhone 17 on iOS 27.0 local, iOS 26.5 hosted) (+4 more)

### Community 35 - "Scope 009 General Brief Rules"
Cohesion: 0.15
Nodes (13): Skill panel answers in the general rules: AskUserQuestion does not wake the lead, so every skill panel is answered from a fixed list or sent to the lead as needs-decision, Report field 'Tafsiran AC' (developer, checker, tester): the reading taken for an ambiguous AC and its reason from the AC text or rationale.md, General brief rules (Aturan umum brief) for the sub-sessions of the scope 009 coordination: the fixed part of every brief; the brief wins where it differs, Always forbidden for sub-sessions: docs/scope/, AGENTS.md, graphify-out/, spec content other than the Status line and the verify.md ticks (checker only), other specs, and files outside the brief's allowed list, Decisions in auto mode: for an ambiguous AC read the spec's rationale.md, take the reading closest to the AC text and record it under Tafsiran AC; needs-decision goes to the lead only when the AC text or a spec decision must change, Commit rule for sub-sessions: one commit per step, an imperative English subject without prefix like the repository history, plus the Co-Authored-By trailer, Disk rule: 32 GiB free at the start; only the checker runs full native builds, one at a time; below 10 GiB free stop and report blocked; remove target/, build/ and apps/android/**/build and the temporary clone before reporting done, Lead address: Mobile Foundation Scaffold [f5cda4]; full reports, questions and needs-decision go there through SendMessage (+5 more)

### Community 36 - "Native Token Mapping and Text Scaling"
Cohesion: 0.29
Nodes (13): System text scaling via generated text styles, Native token mapping, Compose sp mapping of logical text units, Jetpack Compose token projection (FoundationTokens), Dynamic Type mapping of headline and reading scales, Logical spacing units adapt to display density, spacingPage role, SwiftUI token projection (FoundationTokens) (+5 more)

### Community 37 - "Scope 009 Row and Verify Steps"
Cohesion: 0.21
Nodes (13): Project adjustments: the role files were written for another Rust project; cargo xtask, stackly_testkit, clients/swift, evidence/, prd.md and test-preferences.json do not exist here; evidence is the commands and output in the report, Sub-session chk-f009-verify (checker verify, fable-5-2 high): full verify of AC-1 to AC-12, closing milestone 3, Build it and Verify it; owns the ticks in verify.md of spec 0003, Decision: lead gate on main after each merge: no conflict markers, scripts/test.sh exits 0, native build per platform only when apps/ changed (the skill gate commands cargo xtask and swift test do not exist in this repo), Decision: the milestone verify is folded into one full verify, because milestone 3 is the last milestone and verify.md of spec 0003 has no per-milestone sections, Manual step results go to the lead (step ID, PASS or FAIL, output on FAIL); the lead forwards them to the checker who ticks verify.md; a FAIL reopens the box, 009 - A new project from the foundation (in-progress), Closing boxes (009): Verify it is open, Test it is ticked, Done when (009): one recorded decision, one command, a hosted check on a temporary copy, clean inherited records, recorded foundation revision (+5 more)

### Community 38 - "iOS App Shell"
Cohesion: 0.18
Nodes (9): App, MobileFoundationApp, .body, GreetingScreen, .body, String, Scene, SwiftUI (+1 more)

### Community 39 - "Android Greeting and Supported OS Scopes"
Cohesion: 0.30
Nodes (11): Android 001 - Native Android greeting (existing), API 36 emulator results (arm64 local, x86_64 hosted) in light and dark, Android app packages both supported CPU architectures, Android 002 - Lowest supported Android and large text (planned), 16 KiB memory page packaging, Declared Android minimum API 24 not yet exercised, Android largest font scale check, iOS 002 - Lowest supported iOS and large text (planned) (+3 more)

### Community 40 - "Kotlin Rust Call Status"
Cohesion: 0.23
Nodes (7): E, uniffiCheckCallStatus(), UniffiForeignFutureCompleteVoid, uniffiRustCall(), UniffiRustCallStatusErrorHandler, uniffiRustCallWithError(), U

### Community 41 - "Architecture Boundaries and Real Callers"
Cohesion: 0.27
Nodes (12): Architecture boundaries, Documented capability boundary; adapters need an actual caller, Layer: design system (generated Swift/Kotlin values as shared visual vocabulary), Layer: native platform integration (Swift owns Apple services, Kotlin owns Android services), Layer: native presentation (views render, adapt to appearance, handle events), Layer: resources and tooling (build-host validation and generation), Layer: shared Rust (core owns behavior, FFI crate maps exports), Create a platform adapter directory only when a feature needs an OS capability (+4 more)

### Community 42 - "README and Starting a Product"
Cohesion: 0.27
Nodes (12): Follow-up: build the command that takes a foundation release (fetch, merge, apply the ownership table) when the first release is merged into a product, Follow-up: decide where dependency update bots run (a bot in every product changes foundation owned files and will conflict with merges), Neutral: /develop moves the spec to In Progress and Accepted with scope row 009; creating the first tag foundation-v0.1.0 is the maintainer's step, Path ownership after derivation: product owned paths keep the product's side, foundation owned paths take the foundation's side, shared paths merge by hand, README section 'Start a project from this foundation': clone at a tag, create a branch, rename the remote, run the command, add origin, rebuild the graph, mark inherited rows existing, commit, record first results, Release the foundation: run the workflow by hand with derived set, then push an annotated foundation-vMAJOR.MINOR.PATCH tag on main, Take a later foundation release: git fetch foundation --tags, git merge foundation-vX.Y.Z, keep the product's side on product owned paths, rebuild the graph, run every check, Tradeoff: every merge of a foundation release reports conflicts on product owned paths, resolved by hand until the sync command exists (+4 more)

### Community 43 - "Identity Value Sourcing"
Cohesion: 0.27
Nodes (9): apps/android/app/src/main/AndroidManifest.xml, apps/android/app/src/main/res/values/app.xml (the app_name string leaves this file; the label comes from the appLabel manifest placeholder), apps/ios/Config/App.xcconfig (iOS app build settings), apps/ios/Config/Project.xcconfig (iOS project build settings), apps/ios/MobileFoundation.xcodeproj/project.pbxproj (Xcode project file), Android build reads identity.properties: app/build.gradle.kts loads applicationId, versionName and versionCode, the label reaches the manifest as the appLabel placeholder, namespace stays foundation.mobile, iOS build reads Identity.xcconfig: Project.xcconfig includes it, App.xcconfig maps the bundle ID and display name, the UI test bundle ID is derived as $(APP_BUNDLE_IDENTIFIER).uitests, Force: identity is spread over files the foundation keeps editing (App.xcconfig, Project.xcconfig, project.pbxproj, app/build.gradle.kts, res/values/app.xml) (+1 more)

### Community 44 - "Coordinate Decision Modes and Log"
Cohesion: 0.25
Nodes (11): Accept this spec? handoff: the architect never answers it itself; it sends the spec path, Decision, key tradeoff and decisions taken to the lead, ends the turn with STATUS: needs-decision and continues after accept, Decision mode (Mode keputusan): governs only decisions, the choices that change spec content; an ambiguous AC reading is not a decision, Heavy decision (keputusan berat): expensive to reverse once built (on-disk data format or migration, contract break, security model, licensing, existing user data, changes to an Accepted spec), Mode auto (default): the recommended option is taken for ordinary and heavy decisions, heavy ones flagged berat, Mode tanya: the user decides every decision, Mode tanya berat: the recommended option for ordinary decisions, the user decides heavy ones, Recommended option: the architect takes its own recommendation and writes reason and runner-up in rationale.md; the lead accepts after three checks; every decision is recorded with its runner-up and how to undo it, Values only the user knows (email address, account, handle, legal name, price) are not decisions in any mode: they go to the manual file and the dependent AC is BLOCKED with owner user (+3 more)

### Community 45 - "Contract Extension and Deferred Work"
Cohesion: 0.24
Nodes (11): Explicit application records and enums; private core/transport shapes mapped at the adapter, Async and cancellation conventions for future exports, Conventions for extending the mobile contract, Native capability callback interfaces limited to operations the core requires, Typed UniFFI errors with stable variants; user-facing messages translated natively, Deferred: a contract beyond one string (record, typed error, async call), Records, typed errors, async calls and native callbacks have no caller or test yet, One string in, one string out greeting contract (+3 more)

### Community 46 - "Derivation State Check Tests"
Cohesion: 0.18
Nodes (5): AC-8: every departure from the exact form is a mismatch that names the file and…, AC-8: a derived checkout that lost one signal names that signal., AC-8: an identity file that is not UTF-8, and a missing README.md, are…, AC-8: changing only applicationId names that file and key against a foundation…, AC-8: default IDs under an origin line, and a second origin line, each make a…

### Community 47 - "Android App Shell"
Cohesion: 0.33
Nodes (5): MainActivity, FoundationTheme(), GreetingScreen(), Bundle, ComponentActivity

### Community 48 - "Kotlin Handle Map and Lifting"
Cohesion: 0.42
Nodes (4): InternalException, T, UniffiHandleMap, UniffiNullRustCallStatusErrorHandler

### Community 49 - "Design System Guide and Token Commands"
Cohesion: 0.36
Nodes (8): Design system guide, generate-design-tokens.sh modes: write, --check (drift), --test (failure cases), Generated semantic token API consumed by native apps, Five canonical token JSON files (primitives and semantic aliases), tokens.schema.json: single Draft 7 document keyed by filename stem, SHA-pinned GitHub Actions with read-only contents permission, Shared build and generation commands, fastjsonschema==2.21.2 (sha256 hash-pinned schema validator)

### Community 50 - "Command Line Wrapper Tests"
Cohesion: 0.31
Nodes (5): CommandLineTests, Run the copied scripts/init-project.sh from another folder, as a person or CI…, AC-3, AC-8: the wrapper finds its own checkout, prints the five changed paths,…, AC-7: through the wrapper a refusal exits 2, prints one line on stderr only,…, AC-8: through the wrapper --check exits 1 and names the mismatch on stderr.

### Community 51 - "Knowledge Graph Update Rules"
Cohesion: 0.46
Nodes (8): Agent workflow: before commit (run /graphify . --update, stage graphify-out with the change), Knowledge graph (graphify-out/, kept current with /graphify . --update), Token saving: graph first, files later: lead and sub-sessions ask graphify query and explain before reading files, and open files only where the graph points, Token saving: graph only for changed files: each graph update processes only the files of the commit being prepared; code through graphify update, documents through a restricted /graphify --update whose manifest is stamped for those files only, Graph and commit: the lead fulfils the AGENTS.md /graphify . --update rule when merging to main; sub-sessions never run graphify update and never stage anything under graphify-out/, Main checkout and knowledge graph: run graphify query and graphify explain against the main checkout's graphify-out/graph.json before reading files, and never change a file in the main checkout, Decision: the knowledge graph is updated once per gate event: merged files, scope ticks and the log go into one graph update and one commit, so the AGENTS.md rule is met without repeated extraction, Decision: the restricted graph update stamped _origin semantic directly in graph.json for nodes and edges of the 14 coordination and skill documents, because the library guesses the tier from the shape of the location; later restricted updates stamp the chunk before the merge

### Community 52 - "Coordinate Tick Gates and Manual Steps"
Cohesion: 0.32
Nodes (8): Checker verify mode: proves a milestone or feature behaves per spec by running the verify.md steps, scoped to the milestone section and the AC IDs in the brief, and sends failures to the owning developer, verify.md milestone section: written by the developer at 'Save verify steps?' (UI / manual, Commands, Acceptance-criteria coverage); with the Status line the only spec content a developer may change, Gate Build it and Verify it: closed together by one checker running a full /check verify after the last milestone is merged, Gate Document it: the lead runs the document skill with changelog over the feature's merge range and commits CHANGELOG.md, Gate milestone: developer branch merged and the checker verify reports done for that milestone's section of verify.md, Manual steps (Langkah manual): steps needing the user's eyes, hands, account, device or permission; no session runs them; the box is still ticked when the rest passes and the step is recorded NOT_RUN; a FAIL reopens it, Run defaults of /coordinate: parallel sub-sessions for non-overlapping ownership, wave plan shown then run, debugger on a red gate, decisions follow the decision mode, user-only steps go to the manual file, a feature is marked done at its last box, Lead step 6: tick gate and merge (only the lead edits scope files; clean worktree, diff limited to ownership, merge --no-ff --no-commit, checks on main, commit, then tick one box per edit)

### Community 53 - "Refusals and Input Validation"
Cohesion: 0.25
Nodes (8): Follow-up: allow a localized display name when a product needs one (it would move from the identity files to the catalogs), Input validation rules (re.ASCII patterns for app ID, platform overrides, display name of 1 to 30 code points, version, build, foundation URL, ref and date), Positive: products install side by side under their own name and ID, a foundation fix reaches every product by one merge, a half derived checkout fails scripts/test.sh, records start empty, the identity mismatch is gone, every native run proves the built identity, Refusals: one line naming the input and the rule, exit 2, nothing written, Tradeoff: display names are limited to letters, digits, space, period, hyphen and apostrophe until a product needs more, Recommendation: the command refuses to run on a derived checkout, Force: two copies of the foundation carry the same ID, so one installs over the other, Refusal steps (AC-7): eight bad inputs, an untracked file, a second run on a derived clone, a run outside git and a local path remote each exit 2 with one line and leave git status unchanged

### Community 54 - "Generated Swift Tokens"
Cohesion: 0.33
Nodes (6): FoundationTokens, Palette, CGFloat, ColorScheme, Font, TimeInterval

### Community 55 - "Generated Kotlin Tokens"
Cohesion: 0.50
Nodes (3): FoundationTokens, Palette, Color

### Community 56 - "Kotlin FFI Integrity Checks"
Cohesion: 0.60
Nodes (3): IntegrityCheckingUniffiLib, uniffiCheckApiChecksums(), uniffiCheckContractApiVersion()

### Community 57 - "Scope 009 Manual Steps"
Cohesion: 0.50
Nodes (5): Manual steps rule: GUI apps, GitHub web pages, physical devices, signing, installing tools, repository settings, push and triggering or repeating workflows are done only by the user or the lead; gh is read-only; headless simulators and emulators are allowed; a failed or flaky step is reported failed, not manual, Manual steps (Langkah manual) for scope 009 - A new project from the foundation: steps that need the user's eyes, hands, account, device or permission and that no session runs, Manual steps of feature 009 A new project from the foundation (spec 0003): no step yet, Manual step summary (Ringkasan) for scope 009 (ID, step, AC, boxes ticked while the step is NOT_RUN, runnable after, result): no step yet; the lead adds rows when a sub-session report contains manual steps, Values from the user (Nilai dari user): values only the user knows; the waiting AC stays BLOCKED until the value exists; none yet

### Community 58 - "Android Rust Build Script"
Cohesion: 0.40
Nodes (4): CARGO_TARGET_AARCH64_LINUX_ANDROID_LINKER, CARGO_TARGET_X86_64_LINUX_ANDROID_LINKER, PATH, build-android-rust.sh script

### Community 60 - "Android Gradle Wrapper"
Cohesion: 0.83
Nodes (3): gradlew script, die(), warn()

### Community 61 - "Native Component Guidelines"
Cohesion: 0.50
Nodes (4): Native components guidelines, Greeting as a single text element, Reusable native component (introduced on demand), Introduce presentation state or a ViewModel only when needed

### Community 62 - "iOS Rust Build Script"
Cohesion: 0.50
Nodes (3): CARGO_TARGET_DIR, PATH, build-ios-rust.sh script

## Knowledge Gaps
- **66 isolated node(s):** `NoHandle`, `UniffiWithHandle`, `Explicit application records and enums; private core/transport shapes mapped at the adapter`, `Values from the user (Nilai dari user): values only the user knows; the waiting AC stays BLOCKED until the value exists; none yet`, `Commit rule for sub-sessions: one commit per step, an imperative English subject without prefix like the repository history, plus the Co-Authored-By trailer` (+61 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `.body` connect `iOS App Shell` to `Swift UniFFI Bindings`?**
  _High betweenness centrality (0.129) - this node is a cross-community bridge._
- **Why does `hello()` connect `Swift UniFFI Bindings` to `iOS App Shell`?**
  _High betweenness centrality (0.127) - this node is a cross-community bridge._
- **Why does `Foundation verification 2026-11-15` connect `Verification Record and CI Workflow` to `Planning Path, Scope Index and Policy Checks`, `iOS Greeting Scope and Unverified Devices`, `Scope 009 Row and Verify Steps`, `Rust Core and Greeting Contract`, `Android Greeting and Supported OS Scopes`, `Architecture Compliance and Spec Triggers`, `README and Starting a Product`, `Init Command and Identity Files`, `Shared Settings and Localization`, `Spec 0003 Acceptance Criteria`, `Visual Definitions and Accessibility Checks`, `test.sh and Derivation Test`, `Empty Verification Record and Value Sourcing`?**
  _High betweenness centrality (0.122) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Foundation verification 2026-11-15` (e.g. with `Record separately what compiled and what ran` and `tooling/derive/verification-record.md (empty verification record template for a derived product)`) actually correct?**
  _`Foundation verification 2026-11-15` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `NoHandle`, `UniffiWithHandle`, `Explicit application records and enums; private core/transport shapes mapped at the adapter` to the rest of the system?**
  _66 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Planning Path, Scope Index and Policy Checks` be split into smaller, more focused modules?**
  _Cohesion score 0.06999522216913522 - nodes in this community are weakly interconnected._
- **Should `Swift UniFFI Bindings` be split into smaller, more focused modules?**
  _Cohesion score 0.05444596443228454 - nodes in this community are weakly interconnected._