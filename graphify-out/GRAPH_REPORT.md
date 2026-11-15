# Graph Report - mobile  (2026-11-15)

## Corpus Check
- 6 files · ~85,066 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1420 nodes · 4336 edges · 63 communities (62 shown, 1 thin omitted)
- Extraction: 76% EXTRACTED · 24% INFERRED · 0% AMBIGUOUS · INFERRED: 1033 edges (avg confidence: 0.9)
- Token cost: 211,509 input · 118,354 output

## Community Hubs (Navigation)
- Verification Record, CI Workflow and Policy Checks
- Swift UniFFI Bindings
- Coordinate Skill
- Kotlin FFI Library Loading
- Scope 009 Coordination Records
- Kotlin UniFFI Library Calls
- Planning Path and Spec 0002
- Rule Set and Platform Rules
- Rust Core and Greeting Contract
- Derivation Command
- Derivation Refusal and Write Set Tests
- Derivation Run and Origin Line Tests
- Development Rules and Spec Triggers
- Resource Generator
- Kotlin RustBuffer Handling
- Shared Settings and Localization
- Architecture Check and Planning Rules
- Derivation Test Checkout Fixture
- Ownership Matrix and Repository Structure
- Init Command and Identity Files
- Spec 0003 Decision History
- Spec 0003 Acceptance Criteria
- Kotlin FFI Converters
- Scope 010 Coordination and Spec 0004
- Workspace Scopes and Greeting Contract Scope
- Spec 0004 Rationale and Schemas
- Generator Tests and Fixture Sources
- Coordinate Roles and Report Template
- Generated Native Tokens
- Real Checkout and Outside Git Tests
- Supported OS and Large Text Scopes
- Generator Tests and Accessibility Checks
- Token Conventions and Spec 0004 Document Updates
- Spec 0004 Verification Matrix and Token Command
- Native Token Mapping and Text Scaling
- iOS App Shell
- Android App Shell
- Kotlin Rust Call Status
- Identity Value Sourcing
- Architecture Boundaries and Mobile Contract
- Derivation State Check Tests
- Hosted Build Verification and iOS UI Tests
- Scope 010 General Brief Rules
- Kotlin Handle Map and Lifting
- Heading Role Rename and Design System Guide
- Knowledge Graph Update Rules
- README and Path Ownership
- Command Line Wrapper Tests
- Generated File and Drift Rules
- Kotlin FFI Integrity Checks
- CI Workflow and Spec 0003 Build Plan
- Android Rust Build Script
- Derivation Write Failure Tests
- Greeting Screens, Platform Rules and Gradle Wrapper
- iOS Rust Build Script
- Coordinate Wave Plan and Ownership
- Scope 010 Manual Steps
- Verification Before Reporting and Native Builds
- Decision Mode Auto
- iOS Greeting UI Test Pixel Check

## God Nodes (most connected - your core abstractions)
1. `Spec 0004: Schemas free of sample names: one key of any name, a heading role, generator tests on their own sources (Status: Proposed, 2026-11-15); removes the two sample names (greeting_recipient, the greeting role) that the foundation schemas still require` - 67 edges
2. `Foundation verification 2026-11-15` - 66 edges
3. `Spec 0003: A new project from the foundation: product identity in two files, one init command, updates by merge (Accepted)` - 66 edges
4. `Spec 0002: One planning path: a scope row first, then a spec` - 61 edges
5. `Spec 0001: One owner per responsibility, with rules kept beside the code` - 57 edges
6. `UniffiLib` - 54 edges
7. `DerivationTests` - 46 edges
8. `Mobile foundation scope (index)` - 46 edges
9. `Coordination log (Log koordinasi) for scope 010 - Schemas free of sample names (wave 1 active, decision mode auto, start hash 7b6ca4f)` - 42 edges
10. `Decision: a new capability is planned as a scope row and designed in a spec before code; docs/plans and new ADRs are retired in a single change` - 38 edges

## Surprising Connections (you probably didn't know these)
- `Derived hosted run android job result (same derive command; Gradle 9.3.1 assembled the derived debug app; identity file and built app matched; two instrumentation tests passed with night mode off and on)` --references--> `GreetingTest`  [INFERRED]
  docs/quality/verification.md → apps/android/app/src/androidTest/kotlin/foundation/mobile/GreetingTest.kt
- `Product identity result (2026-11-15: test.sh passed with --check printing foundation and --test passing 21 unit tests; both apps carried dev.foundation.mobile, Mobile Foundation, 0.1.0, build 1; a copy derived as Zoë's Proof built and matched its identity file)` --references--> `GreetingTest`  [INFERRED]
  docs/quality/verification.md → apps/android/app/src/androidTest/kotlin/foundation/mobile/GreetingTest.kt
- `Derived hosted run ios job result (derive step ran init-project.sh as Zoë's Proof with dev.example.derived; Xcode 26.5 built the derived app; identity file and built app matched; greeting test passed in light and dark on iOS 26.5)` --references--> `GreetingUITests`  [INFERRED]
  docs/quality/verification.md → apps/ios/UITests/GreetingUITests.swift
- `Product identity result (2026-11-15: test.sh passed with --check printing foundation and --test passing 21 unit tests; both apps carried dev.foundation.mobile, Mobile Foundation, 0.1.0, build 1; a copy derived as Zoë's Proof built and matched its identity file)` --references--> `GreetingUITests`  [INFERRED]
  docs/quality/verification.md → apps/ios/UITests/GreetingUITests.swift
- `Tokens, configuration and localization check` --references--> `GenerationTests`  [INFERRED]
  docs/quality/architecture-compliance.md → tooling/codegen/test_generation.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Rename path of the typography role greeting to heading: token schema, typography.json, both generated token files and the three readers, changed in one commit** — design_system_schemas_tokens_schema, docs_specs_root_0004_schemas_free_of_sample_names_index_token_schema_required_heading_and_body, docs_specs_root_0004_schemas_free_of_sample_names_index_typography_json_heading_role, docs_design_system_token_conventions_canonical_token_sources, docs_specs_root_0004_schemas_free_of_sample_names_index_typographyheading_generated_property, apps_ios_designsystem_generated_foundationtokens, apps_android_designsystem_src_main_kotlin_foundation_designsystem_foundationtokens, apps_ios_presentation_greetingscreen, apps_android_designsystem_src_main_kotlin_foundation_designsystem_foundationtheme, apps_android_app_src_androidtest_kotlin_foundation_mobile_greetingtest, docs_specs_root_0004_schemas_free_of_sample_names_index_build_plan_step_2 [EXTRACTED 1.00]
- **Build plan of spec 0004: five steps that together satisfy AC-1 to AC-7** — docs_specs_root_0004_schemas_free_of_sample_names_index_build_plan, docs_specs_root_0004_schemas_free_of_sample_names_index_build_plan_step_1, docs_specs_root_0004_schemas_free_of_sample_names_index_build_plan_step_2, docs_specs_root_0004_schemas_free_of_sample_names_index_build_plan_step_3, docs_specs_root_0004_schemas_free_of_sample_names_index_build_plan_step_4, docs_specs_root_0004_schemas_free_of_sample_names_index_build_plan_step_5, docs_specs_root_0004_schemas_free_of_sample_names_index_ac_1, docs_specs_root_0004_schemas_free_of_sample_names_index_ac_2, docs_specs_root_0004_schemas_free_of_sample_names_index_ac_3, docs_specs_root_0004_schemas_free_of_sample_names_index_ac_4, docs_specs_root_0004_schemas_free_of_sample_names_index_ac_5, docs_specs_root_0004_schemas_free_of_sample_names_index_ac_6, docs_specs_root_0004_schemas_free_of_sample_names_index_ac_7 [EXTRACTED 1.00]
- **Generator tests on their own sources: the fixture tree, the nine tests, the --test form and the invariants that keep them independent of a product's catalog and tokens** — docs_specs_root_0004_schemas_free_of_sample_names_index_fixture_source_tree, docs_specs_root_0004_schemas_free_of_sample_names_index_nine_generator_tests, docs_specs_root_0004_schemas_free_of_sample_names_index_test_form, docs_specs_root_0004_schemas_free_of_sample_names_index_test_module_names, docs_specs_root_0004_schemas_free_of_sample_names_index_invariant_tests_read_fixture_only, docs_specs_root_0004_schemas_free_of_sample_names_index_invariant_fixture_satisfies_schemas, docs_specs_root_0004_schemas_free_of_sample_names_index_test_sources_without_a_sample_name_generate_and_check, docs_specs_root_0004_schemas_free_of_sample_names_index_ac_5, docs_specs_root_0004_schemas_free_of_sample_names_index_ac_6, tooling_codegen_test_generation [INFERRED 0.85]
- **One init command turns a foundation clone into a derived product: identity files, README origin line, empty verification record, removed knowledge graph** — scripts_init_project, tooling_derive_init_project, apps_ios_config_identity, apps_android_identity, docs_specs_root_0003_new_project_from_foundation_index_readme_origin_line, docs_specs_root_0003_new_project_from_foundation_index_empty_verification_record, tooling_derive_verification_record, docs_specs_root_0003_new_project_from_foundation_index_init_write_set, docs_specs_root_0003_new_project_from_foundation_index_repository_states_foundation_derived_mixed [EXTRACTED 1.00]
- **Coordination records of scope 010 (log, general brief rules, manual steps) tied to the scope 010 file** — docs_scope_coordination_010_schemas_free_of_sample_names_log, docs_scope_coordination_010_schemas_free_of_sample_names_brief_umum, docs_scope_coordination_010_schemas_free_of_sample_names_manual, docs_scope_root_010_schemas_free_of_sample_names [EXTRACTED 1.00]
- **Scope 010 decisions carried over from the scope 009 coordination log (lead gate, session and disk limit, Beta flow boxes, one graph update per gate)** — docs_scope_coordination_010_schemas_free_of_sample_names_log_lead_gate_on_main, docs_scope_coordination_010_schemas_free_of_sample_names_log_session_and_disk_limit, docs_scope_coordination_010_schemas_free_of_sample_names_log_no_review_or_document_box, docs_scope_coordination_010_schemas_free_of_sample_names_log_one_graph_update_per_gate, docs_scope_coordination_009_a_new_project_from_the_foundation_log [EXTRACTED 1.00]
- **Wave 1 sub-sessions of the scope 010 coordination with their coordinate role files** — docs_scope_coordination_010_schemas_free_of_sample_names_log_arc_f010_spec, docs_scope_coordination_010_schemas_free_of_sample_names_log_dev_f010_m1, docs_scope_coordination_010_schemas_free_of_sample_names_log_chk_f010_verify, docs_scope_coordination_010_schemas_free_of_sample_names_log_tst_f010_test, claude_skills_coordinate_roles_architect, claude_skills_coordinate_roles_developer, claude_skills_coordinate_roles_checker, claude_skills_coordinate_roles_tester [EXTRACTED 1.00]
- **Proof that derivation still works: --check state test, derivation unit test on a temporary copy in scripts/test.sh, CI identity comparison in both native jobs, manual workflow run with derived set** — docs_specs_root_0003_new_project_from_foundation_index_check_form, docs_specs_root_0003_new_project_from_foundation_index_test_form, docs_specs_root_0003_new_project_from_foundation_index_derivation_test, docs_specs_root_0003_new_project_from_foundation_index_ci_identity_comparison, docs_specs_root_0003_new_project_from_foundation_index_workflow_derived_input, scripts_test, github_workflows_foundation, github_workflows_foundation_derived_input, github_workflows_foundation_derive_sample_product_step, github_workflows_foundation_ios_identity_comparison_step, github_workflows_foundation_android_identity_comparison_step [INFERRED 0.85]
- **Box list of scope 010: Design it (ticked), Build it with three milestones, Verify it and Test it (open)** — docs_scope_root_010_schemas_free_of_sample_names_design_it, docs_scope_root_010_schemas_free_of_sample_names_build_it, docs_scope_root_010_schemas_free_of_sample_names_milestone_1_one_key_rule_and_heading_role, docs_scope_root_010_schemas_free_of_sample_names_milestone_2_generator_tests_on_own_sources, docs_scope_root_010_schemas_free_of_sample_names_milestone_3_document_updates_and_verification_record, docs_scope_root_010_schemas_free_of_sample_names_verify_it, docs_scope_root_010_schemas_free_of_sample_names_test_it [EXTRACTED 1.00]
- **The nine delegated decisions of spec 0004 taken in auto mode for scope 010 (one heavy: the role name heading)** — docs_scope_coordination_010_schemas_free_of_sample_names_log_delegated_decisions, docs_scope_coordination_010_schemas_free_of_sample_names_log_delegated_heading_role_name, docs_scope_coordination_010_schemas_free_of_sample_names_log_delegated_required_roles_heading_body, docs_scope_coordination_010_schemas_free_of_sample_names_log_delegated_no_alias_for_typography_greeting, docs_scope_coordination_010_schemas_free_of_sample_names_log_delegated_min_properties_rule, docs_scope_coordination_010_schemas_free_of_sample_names_log_delegated_greeting_recipient_stays_sample_content, docs_scope_coordination_010_schemas_free_of_sample_names_log_delegated_fixture_source_tree, docs_scope_coordination_010_schemas_free_of_sample_names_log_delegated_done_when_4_proof, docs_scope_coordination_010_schemas_free_of_sample_names_log_delegated_scope_two_sample_names_only, docs_scope_coordination_010_schemas_free_of_sample_names_log_delegated_cross_check_findings_applied, docs_specs_root_0004_schemas_free_of_sample_names_index [EXTRACTED 1.00]
- **Automated architecture compliance checks** — docs_quality_architecture_compliance_rust_format_and_lint, docs_quality_architecture_compliance_core_and_ffi_contract_tests, docs_quality_architecture_compliance_cargo_dependency_and_governance_check, docs_quality_architecture_compliance_project_identity_state_check, docs_quality_architecture_compliance_uniffi_generated_files_check, docs_quality_architecture_compliance_tokens_config_localization_check, docs_quality_architecture_compliance_ios_linkage_and_ui_check, docs_quality_architecture_compliance_android_linkage_and_ui_check [EXTRACTED 1.00]
- **Hosted run 43593365100 as runtime evidence for the greeting contract, visual definitions, shared text and reproducible builds** — docs_scope_root_002_shared_greeting_contract, docs_scope_root_003_shared_visual_definitions, docs_scope_root_004_shared_settings_text_and_brand_assets, docs_scope_root_005_reproducible_local_builds_and_checks, docs_quality_verification_hosted_run_43593365100, docs_quality_verification [EXTRACTED 1.00]
- **Forces that motivate the one-owner-per-responsibility decision** — docs_specs_root_0001_ownership_development_rules_force_two_languages_downstream_of_one_source, docs_specs_root_0001_ownership_development_rules_force_generated_files_beside_handwritten_code, docs_specs_root_0001_ownership_development_rules_force_coding_agents_as_regular_contributors, docs_specs_root_0001_ownership_development_rules_force_one_maintainer, docs_specs_root_0001_ownership_development_rules_force_small_codebase, docs_specs_root_0001_ownership_development_rules_decision_one_owner_per_responsibility [EXTRACTED 1.00]
- **Machine enforcement chain: test.sh runs the validator and both generator drift checks, mirrored by the CI foundation job** — docs_specs_root_0001_ownership_development_rules_enforcement_test_script_and_three_policy_checks, scripts_test, tooling_validation_check_architecture, scripts_generate_bindings, scripts_generate_design_tokens, github_workflows_foundation_foundation_job [EXTRACTED 1.00]
- **Rules that rest on review alone with no automated check** — docs_specs_root_0001_ownership_development_rules_r1_one_authoritative_owner, docs_specs_root_0001_ownership_development_rules_r3_app_trees_do_not_import_one_another, docs_specs_root_0001_ownership_development_rules_r8_real_caller_first, docs_specs_root_0001_ownership_development_rules_r9_search_before_adding, docs_specs_root_0001_ownership_development_rules_r11_handoff_reports_compiled_and_ran_separately, docs_specs_root_0001_ownership_development_rules_r14_bindgen_feature_host_only, docs_specs_root_0001_ownership_development_rules_r15_library_change_transitive_and_size_review, docs_specs_root_0001_ownership_development_rules_r16_breaking_change_is_a_migration, docs_specs_root_0001_ownership_development_rules_r18_service_proposal_requirements [EXTRACTED 1.00]
- **Canonical source over generated output: edit sources, regenerate, compare snapshots** — agents_never_hand_edit_generated_files, docs_architecture_ownership_matrix_derived_file_rule, docs_architecture_dependency_rules_one_way_generation, docs_decisions_adr_0001_foundation_checked_in_source_snapshots [INFERRED 0.85]
- **Regenerate and compare checks that keep generated tokens, catalogs and bindings equal to their sources** — docs_scope_root_003_shared_visual_definitions_token_drift_check, docs_scope_root_004_shared_settings_text_and_brand_assets_single_english_catalog, docs_scope_root_005_reproducible_local_builds_and_checks_generated_output_drift_detection, scripts_test [INFERRED 0.85]
- **The five sub-session roles of /coordinate, each with its own goal, ownership, message paths and model** — claude_skills_coordinate_roles_architect, claude_skills_coordinate_roles_developer, claude_skills_coordinate_roles_checker, claude_skills_coordinate_roles_tester, claude_skills_coordinate_roles_debugger, claude_skills_coordinate_skill_sub_session, claude_skills_coordinate_skill_model_per_role [EXTRACTED 1.00]
- **Tick gates of /coordinate: what must be true on main before the lead ticks each kind of scope box** — claude_skills_coordinate_skill_step_6_tick_gate_and_merge, claude_skills_coordinate_skill_gate_design_it, claude_skills_coordinate_skill_gate_milestone, claude_skills_coordinate_skill_gate_build_it_and_verify_it, claude_skills_coordinate_skill_gate_test_it, claude_skills_coordinate_skill_gate_review_it, claude_skills_coordinate_skill_gate_document_it, claude_skills_coordinate_skill_red_gate_cycle [EXTRACTED 1.00]
- **Greeting vertical slice: localized recipient through UniFFI to the Rust formatter** — readme_hello_world_greeting, shared_localization_readme_greeting_recipient, docs_architecture_overview_greeting_call_flow, docs_contracts_ffi_conventions_hello_contract, docs_architecture_overview_foundation_core_hello, docs_architecture_ownership_matrix_crates_mobile_ffi, docs_architecture_ownership_matrix_bindings, readme_uniffi [EXTRACTED 1.00]
- **One planning path: a scope row first, then a spec before code, named by the agent instructions, the development rules and the repository structure** — docs_specs_root_0002_one_planning_path_decision_scope_row_then_spec, docs_specs_root_0002_one_planning_path_canonical_planning_pattern, docs_rules_development_rules_scope_row_then_spec, agents_scope_row_and_spec_before_code, docs_scope_root_007_one_planning_path, docs_scope_index, docs_architecture_repository_structure_docs_record_homes, docs_specs_root_0001_ownership_development_rules_r10_scope_row_and_spec_for_capability_spec_for_material_decision [EXTRACTED 1.00]
- **Coordination records of scope 009: the log, the general brief rules and the manual steps list, all tied to the scope row** — docs_scope_coordination_009_a_new_project_from_the_foundation_log, docs_scope_coordination_009_a_new_project_from_the_foundation_brief_umum, docs_scope_coordination_009_a_new_project_from_the_foundation_manual, docs_scope_root_009_a_new_project_from_the_foundation [EXTRACTED 1.00]
- **Wave 1 ownership split: developer on the verification record, checker on the verify.md ticks, tester on the derivation tests, with no overlap** — docs_scope_coordination_009_a_new_project_from_the_foundation_log_dev_f009_m3, docs_scope_coordination_009_a_new_project_from_the_foundation_log_chk_f009_verify, docs_scope_coordination_009_a_new_project_from_the_foundation_log_tst_f009_test, docs_quality_verification, docs_specs_root_0003_new_project_from_foundation_verify, tooling_derive_test_init_project, docs_scope_coordination_009_a_new_project_from_the_foundation_log_parallel_start [EXTRACTED 1.00]
- **Spec triggers kept in their owner files: when a smaller change needs a spec** — docs_specs_root_0002_one_planning_path_trigger_owner_files, docs_rules_development_rules_spec_triggers_for_smaller_changes, docs_rules_service_rules_spec_for_new_crate_or_boundary, docs_quality_architecture_compliance_spec_for_architecture_change, docs_architecture_dependency_rules_new_edge_proposal, docs_contracts_ffi_conventions_compatibility_versioning, docs_decisions_adr_0001_foundation_revisit_conditions, docs_specs_root_0001_ownership_development_rules_spec_triggers [EXTRACTED 1.00]
- **Design token pipeline from canonical JSON to native projections** — docs_design_system_token_conventions_canonical_token_sources, design_system_schemas_tokens_schema, scripts_generate_design_tokens, docs_design_system_platform_mapping_swiftui_token_projection, docs_design_system_platform_mapping_compose_token_projection, docs_quality_architecture_compliance_tokens_config_localization_check [INFERRED 0.85]
- **Neutral JSON sources validated and generated into native theme and string resources** — design_system_readme_token_files, design_system_readme_tokens_schema, shared_config_readme_foundation_json, shared_localization_readme_catalog_format, design_system_readme_generate_design_tokens_modes, tooling_codegen_requirements_fastjsonschema, design_system_readme_generated_semantic_api, shared_localization_readme_generated_native_strings [INFERRED 0.85]
- **Regenerate derived outputs with their canonical source, never hand-edit** — docs_rules_development_rules_regenerate_derived_files, docs_rules_design_system_rules_regenerate_projections, docs_quality_architecture_compliance_generated_drift_remediation, docs_rules_rust_rules_regenerate_after_signature_change, docs_rules_shared_resources_rules_generated_native_strings, docs_rules_anti_duplication_ffi_shapes_in_rust_export [INFERRED 0.85]
- **Manual step flow: a sub-session reports a manual step, the lead lists it, the user runs it and the checker ticks verify.md from the result** — docs_scope_coordination_009_a_new_project_from_the_foundation_brief_umum_manual_steps_rule, docs_scope_coordination_009_a_new_project_from_the_foundation_manual, docs_scope_coordination_009_a_new_project_from_the_foundation_manual_summary, docs_scope_coordination_009_a_new_project_from_the_foundation_manual_result_routing, docs_scope_coordination_009_a_new_project_from_the_foundation_log_chk_f009_verify, docs_specs_root_0003_new_project_from_foundation_verify, docs_scope_coordination_009_a_new_project_from_the_foundation_manual_f009_1, docs_scope_coordination_009_a_new_project_from_the_foundation_manual_f009_2 [INFERRED 0.85]
- **Tracer bullet greeting path from shared core to both native screens** — docs_scope_index_tracer_bullet_build_approach, docs_scope_root_002_shared_greeting_contract, docs_scope_root_002_shared_greeting_contract_one_string_in_one_string_out_contract, docs_scope_ios_001_native_ios_greeting, docs_scope_android_001_native_android_greeting, docs_scope_root_006_hosted_build_verification [INFERRED 0.85]
- **Verification evidence chain: local checks, hosted jobs and the verification record** — docs_scope_root_005_reproducible_local_builds_and_checks, docs_scope_root_006_hosted_build_verification, docs_scope_root_008_hosted_results_in_the_verification_record, docs_scope_root_008_hosted_results_in_the_verification_record_single_list_of_unverified_targets [INFERRED 0.85]
- **Coordination templates (brief, general rules, log, manual, report) and the scope 009 records filled from them** — claude_skills_coordinate_templates_brief, claude_skills_coordinate_templates_brief_umum, claude_skills_coordinate_templates_log, claude_skills_coordinate_templates_manual, claude_skills_coordinate_templates_report, docs_scope_coordination_009_a_new_project_from_the_foundation_brief_umum, docs_scope_coordination_009_a_new_project_from_the_foundation_log, docs_scope_coordination_009_a_new_project_from_the_foundation_manual [INFERRED 0.95]
- **Derived hosted run 43701289339 as evidence for AC-10: the workflow input, the derive step and both identity comparisons ran on hosted runners** — docs_quality_verification_hosted_run_43701289339, docs_quality_verification_derived_hosted_foundation_job_result, docs_quality_verification_derived_hosted_ios_job_result, docs_quality_verification_derived_hosted_android_job_result, github_workflows_foundation_derived_input, github_workflows_foundation_derive_sample_product_step, github_workflows_foundation_ios_identity_comparison_step, github_workflows_foundation_android_identity_comparison_step, docs_specs_root_0003_new_project_from_foundation_index_ac_10, docs_scope_coordination_009_a_new_project_from_the_foundation_log_hosted_run_43701289339 [INFERRED 0.95]

## Communities (63 total, 1 thin omitted)

### Community 0 - "Verification Record, CI Workflow and Policy Checks"
Cohesion: 0.12
Nodes (32): GreetingTest, GreetingUITests, Android linkage and UI check (Linux CI job, emulator instrumentation), GitHub Actions CI jobs (macOS and Linux), iOS linkage and UI check (macOS CI job, XCTest), Physical hardware verification for simulator-inaccessible capabilities, Foundation verification 2026-11-15, Android compilation result (Gradle 9.3.1, AGP 9.1.0, Temurin 17) (+24 more)

### Community 1 - "Swift UniFFI Bindings"
Cohesion: 0.05
Nodes (64): Array, createReader(), createWriter(), Data, FfiConverter, FfiConverterPrimitive, FfiConverterRustBuffer, FfiConverterString (+56 more)

### Community 2 - "Coordinate Skill"
Cohesion: 0.14
Nodes (23): Checker review mode: senior code review of a GA feature with fresh eyes, ranked findings in docs/reviews; only in a new session that has not written, verified or discussed the implementation, /coordinate skill: finish one scope with parallel sub-sessions (architect, developer, checker, tester, debugger) while the invoking session acts as lead, Gate Review it (GA features): review by a new checker session that has not seen the implementation, file in docs/reviews; Blocker or Major findings start a fix item; ticked when none remain open, Lead session: stays on main in the main checkout, picks the SCOPE, splits items, guards the tick gates, merges green branches and writes the log; writes no production code, Limits (Batasan): only the lead edits scope files and merges to main; the lead pushes main only in step 9 and never with force; sub-sessions commit on their own branch and never push or open a PR; some choices always wait for the user, Token saving: reuse a finished sub-session for the next item of the same feature after clearing its context; never for Review it, Reviewer rule: the reviewer must be a different model family from every author in the change range, Standby first turn: all sessions the queue needs are started on the user's turn; reserve sessions and sessions whose item is not ready end their first turn with STATUS: standby until the lead sends start (+15 more)

### Community 3 - "Kotlin FFI Library Loading"
Cohesion: 0.06
Nodes (34): Disposable, NoHandle, UniffiByValue, UniffiCallbackInterfaceClone, UniffiCallbackInterfaceFree, UniffiForeignFutureCompleteF32, UniffiForeignFutureCompleteF64, UniffiForeignFutureCompleteI16 (+26 more)

### Community 4 - "Scope 009 Coordination Records"
Cohesion: 0.08
Nodes (57): General brief rules (Aturan umum brief) for the sub-sessions of the scope 009 coordination: the fixed part of every brief; the brief wins where it differs, Always forbidden for sub-sessions: docs/scope/, AGENTS.md, graphify-out/, spec content other than the Status line and the verify.md ticks (checker only), other specs, and files outside the brief's allowed list, Commit rule for sub-sessions: one commit per step, an imperative English subject without prefix like the repository history, plus the Co-Authored-By trailer, Disk rule: 32 GiB free at the start; only the checker runs full native builds, one at a time; below 10 GiB free stop and report blocked; remove target/, build/ and apps/android/**/build and the temporary clone before reporting done, Lead address: Mobile Foundation Scaffold [f5cda4]; full reports, questions and needs-decision go there through SendMessage, Manual steps rule: GUI apps, GitHub web pages, physical devices, signing, installing tools, repository settings, push and triggering or repeating workflows are done only by the user or the lead; gh is read-only; headless simulators and emulators are allowed; a failed or flaky step is reported failed, not manual, Process rule: stop only the processes, simulators and emulators you started, name them F009-<session> and delete them afterwards; suites longer than 10 minutes run detached with nohup, Project adjustments: the role files were written for another Rust project; cargo xtask, stackly_testkit, clients/swift, evidence/, prd.md and test-preferences.json do not exist here; evidence is the commands and output in the report (+49 more)

### Community 5 - "Kotlin UniFFI Library Calls"
Cohesion: 0.06
Nodes (3): UniffiLib, UniffiRustCallStatus, UniffiRustFutureContinuationCallback

### Community 6 - "Planning Path and Spec 0002"
Cohesion: 0.10
Nodes (58): Agent workflow: during implementation (place change in owning layer), Plan a new capability in the scope and write its spec under docs/specs before code, Architecture overview, Development rules, Capability spec checklist: user outcome, scope, acceptance criteria, existing owner, public contract, dependency direction, platform specific work, verification matrix, Progress is recorded in the scope row; what ran is recorded in the verification record, /scope and /architect: the usual commands for writing the scope row and the spec, Plan a new capability as a scope row (the brief), then write a spec under docs/specs before code (+50 more)

### Community 7 - "Rule Set and Platform Rules"
Cohesion: 0.12
Nodes (39): Rejected alternative: implementing application behavior independently in both apps, Android rules, Locate the owner before adding a constant, rule, DTO, translation or asset, Spec 0001: One owner per responsibility, with rules kept beside the code, Automate only what a machine can judge, Decision: one owner per responsibility in an ownership matrix, topic-sized rule files, short AGENTS.md entry point, automated checks only where a machine is reliable, An exact dependency list, not a deny list, Follow-up: decide whether checks must pass before a change reaches main (branch rule or local hook) (+31 more)

### Community 8 - "Rust Core and Greeting Contract"
Cohesion: 0.10
Nodes (30): hello(), preserves_empty_names_and_whitespace(), String, main(), hello(), String, target/, build/ and Gradle build directories excluded from source control, tests/contracts: Cargo integration tests for exported behavior (+22 more)

### Community 9 - "Derivation Command"
Cohesion: 0.12
Nodes (31): Exception, check(), derive(), foundation_ref(), foundation_url(), git(), identity_text(), in_git() (+23 more)

### Community 10 - "Derivation Refusal and Write Set Tests"
Cohesion: 0.09
Nodes (15): DerivationTests, AC-6, AC-7: every accepted remote form becomes https without credentials; the…, AC-7: a local path remote, or no remote, is no usable foundation URL., AC-7: each input that breaks its rule is refused with exit 2, one line and no…, AC-7: a remote URL that is not UTF-8 is no usable foundation URL., AC-7: the in git test compares folders, not path spellings., AC-7: a derived checkout is refused., AC-5: the template on disk, filled with the sample values, is the empty record… (+7 more)

### Community 11 - "Derivation Run and Origin Line Tests"
Cohesion: 0.10
Nodes (13): AC-3, AC-5, AC-6, AC-8: the happy path writes every file and the checkout then…, AC-3: each override reaches only its own identity file, and --version reaches…, AC-3: with one override the other platform keeps --app-id., AC-3, AC-7: a value that starts with a hyphen is refused, and its equals form…, AC-6: without the flags the origin line takes the remote, HEAD and today., AC-6: the foundation remote wins over origin, and the highest release tag wins., AC-3: the example of the criterion, with no other flag, writes 0.1.0 and build…, AC-4: each file is replaced in the documented order, and graphify-out/ goes… (+5 more)

### Community 12 - "Development Rules and Spec Triggers"
Cohesion: 0.27
Nodes (19): Agent workflow: before editing (locate owner, contract, callers, tests), Dependency rules, New dependency edge needs an owning module, a use case and a test, Generators consume neutral sources and never recover canonical values from native output, Compatibility: version breaking contracts and coordinate regeneration, both apps and release, ADR 0001: Native apps with a shared Rust core, Decision: keep generated source snapshots in version control and compare against fresh regeneration, Revisit conditions: dependency direction change, async native boundary, independently versioned clients, new shared crate or service (+11 more)

### Community 13 - "Resource Generator"
Cohesion: 0.13
Nodes (23): Shared visual decisions and translations are generator inputs, Generated native strings owned by the resource generator, Neutral: tooling/codegen/generate.py, tokens.py and resources.py are not edited, Test module names added to tooling/codegen/test_generation.py: FIXTURE (fixtures/sources beside the module), TOKEN_SCHEMA and LOCALIZATION_SCHEMA (relative strings that generate.check_schema joins to the checkout root) and token_groups(), which loads the fixture token files by stem, Recommendation: the generator code is left alone; the property name already comes from the role name, so the rename needs no code change, check_schema(), generate(), load() (+15 more)

### Community 14 - "Kotlin RustBuffer Handling"
Cohesion: 0.16
Nodes (7): ByReference, ByValue, ForeignBytes, `hello`(), RustBuffer, kotlin, Pointer

### Community 15 - "Shared Settings and Localization"
Cohesion: 0.08
Nodes (35): Shared resource ownership rules, Shared resources owner (build configuration, localization, brand assets), Deferred: a second language end to end, 004 - Shared settings, text and brand assets (done), shared/assets/ owns future brand artwork and its exports, Greeting sentence 'Hello, {name}!' formed in English by the core, Invalid settings, resource keys and mismatched translation placeholders are rejected, Single English localization catalog and public fallback locale (+27 more)

### Community 16 - "Architecture Check and Planning Rules"
Cohesion: 0.17
Nodes (22): AGENTS.md: Working in the mobile foundation, Cargo dependency and governance check, Architecture policy result (dependency and required-document checks), Specs are numbered NNNN-kebab-title.md in the folder mirroring the scope workspace; a replaced record is marked superseded; ADR 0001 stays the founding record, Deferred: a contract beyond one string (record, typed error, async call), Scope status legend and file numbering convention, 001 - Ownership and development rules (done), One owner per shared responsibility (ten responsibilities in the ownership matrix) (+14 more)

### Community 17 - "Derivation Test Checkout Fixture"
Cohesion: 0.13
Nodes (11): Checkout, AC-4: git sees changes in exactly the documented paths, and no rename., AC-7: a modified or untracked file is refused, even when git status hides…, AC-4: a graph removal that fails names every changed path and the way back., AC-7: a mixed checkout is refused., AC-4: a checkout that has no graph changes only the two identity files,…, AC-6: a README.md of one line without a newline still ends with the title,…, AC-6: only a foundation-v tag that points exactly at HEAD names the ref;… (+3 more)

### Community 18 - "Ownership Matrix and Repository Structure"
Cohesion: 0.22
Nodes (21): App trees do not import one another; core never calls platform UI, Ownership matrix, apps/android: owner of Android UI, presentation state and OS APIs, apps/ios: owner of Apple UI, presentation state and OS APIs, design-system/tokens and schemas: owner of canonical visual values and semantic roles, docs/ and root AGENTS.md: architecture, decision records, scope and agent workflow, scripts/ and .github/workflows/: build and verification orchestration, shared/config, shared/localization, shared/assets: owner of public settings, locale content and brand masters (+13 more)

### Community 19 - "Init Command and Identity Files"
Cohesion: 0.19
Nodes (26): apps/android/identity.properties (Android identity file: applicationId, displayName, versionName, versionCode), apps/ios/Config/Identity.xcconfig (iOS identity file: APP_BUNDLE_IDENTIFIER, APP_DISPLAY_NAME, MARKETING_VERSION, CURRENT_PROJECT_VERSION), Product identity (display name, application IDs, app version): owned by apps/ios/Config/Identity.xcconfig and apps/android/identity.properties; consumed by the Xcode and Gradle builds and scripts/init-project.sh, Project identity state check (init-project.sh --check and --test, CI identity comparison), Product identity result (2026-11-15: test.sh passed with --check printing foundation and --test passing 21 unit tests; both apps carried dev.foundation.mobile, Mobile Foundation, 0.1.0, build 1; a copy derived as Zoë's Proof built and matched its identity file), Derivation only on a copy: init-project.sh with --name rewrites README.md and the verification record and removes graphify-out/, so that form runs only in a temporary clone in the session scratchpad; --check and --test are safe in the worktree, Decision: the tester installs no new tool and test-preferences.json is not created; the framework is the existing Python unittest run through scripts/init-project.sh --test, Done when (009): one recorded decision, one command, a hosted check on a temporary copy, clean inherited records, recorded foundation revision (+18 more)

### Community 20 - "Spec 0003 Decision History"
Cohesion: 0.12
Nodes (33): A new product would carry the foundation's verification record, scope rows, hosted run links and knowledge graph as its own, AC-5: the verification record becomes the empty record naming the product, foundation URL and revision, with every target unverified, Decision: a product is a clone that changes only its display name, application ID and version through scripts/init-project.sh, keeps every other name, starts with an empty verification record and merges foundation-v tags, Empty verification record: names the product, foundation URL and ref, lists every target as still unverified, holds no hosted run link, Positive: products install side by side under their own name and ID, a foundation fix reaches every product by one merge, a half derived checkout fails scripts/test.sh, records start empty, the identity mismatch is gone, every native run proves the built identity, Spec 0003 rationale: decision history of the new project spec (context, options considered, rationale), Recommendation: --check does not look for hosted run links, Recommendation: the command does not edit scope rows (+25 more)

### Community 21 - "Spec 0003 Acceptance Criteria"
Cohesion: 0.11
Nodes (31): Checker note, not a blocker: the iOS icon caption reads MobileFoundation without a space although CFBundleDisplayName is Mobile Foundation; SpringBoard shortens long names (Acme Notes shows its space); a spaced caption needs a shorter name, which is a product decision, Spec 0003: A new project from the foundation: product identity in two files, one init command, updates by merge (Accepted), AC-1: both apps carry the same default identity, read from Identity.xcconfig and identity.properties, stated nowhere else under apps/, AC-6: README.md has the product name as title on line 1 and the origin line on line 3 followed by one blank line, Default foundation identity: dev.foundation.mobile, Mobile Foundation, version 0.1.0, build 1, Follow-up: decide in the release path spec whether the iOS and Android versions must match, and add that test to --check if they must, Follow-up: allow a localized display name when a product needs one (it would move from the identity files to the catalogs), Follow-up: record where /graphify and /scope come from, with a way to do each step by hand (+23 more)

### Community 22 - "Kotlin FFI Converters"
Cohesion: 0.17
Nodes (9): FfiConverter, FfiConverterRustBuffer, FfiConverterString, FfiType, uniffiTraitInterfaceCall(), uniffiTraitInterfaceCallWithError(), ByteBuffer, KotlinType (+1 more)

### Community 23 - "Scope 010 Coordination and Spec 0004"
Cohesion: 0.14
Nodes (43): Coordination log (Log koordinasi) for scope 010 - Schemas free of sample names (wave 1 active, decision mode auto, start hash 7b6ca4f), Sub-session arc-f010-spec (architect, fable-5-2 high, merged): scope 010 Design it (spec), spec 0004; owns docs/specs/_root/0004-schemas-free-of-sample-names/ plus one Follow-up line in the spec 0003 index.md; branch claude/arc-f010-spec-6c76d1, Sub-session chk-f010-verify (checker verify, fable-5-2 high, standby): scope 010 milestone verify and full verify, closing Build it and Verify it; owns the verify.md ticks of spec 0004; branch claude/chk-f010-verify-59dbd8, Closing (Penutupan) of the scope 010 coordination: not closed yet, Decision (lead): spec cross check = Another model (the default for Beta), Delegated decision (spec 0004, Verification matrix, not heavy, in force): every fix the cross check recommended is applied; runner-up leave the findings; undo via architect (update) of spec 0004, Delegated decisions (Keputusan delegasi) for scope 010: spec decisions taken from the recommended option on the user's behalf, heavy (berat) rows on top; nine rows for spec 0004, all in force, one heavy (the role name heading), Delegated decision (spec 0004, AC-3, not heavy, in force): no alias for the old name typographyGreeting, one change; runner-up greeting kept for one release; undo via architect (update) of spec 0004, rebuilding Build plan step 2 (+35 more)

### Community 24 - "Workspace Scopes and Greeting Contract Scope"
Cohesion: 0.18
Nodes (17): Android scope, Android app owns its screen, appearance changes and native localization lookup, Decision (lead, carried over from the scope 009 log): scope 010 follows the Beta flow, so it has no Review it and Document it boxes and no backup review session is reserved, Decision (lead): the lead reads docs/scope/index.md, _root/scope.md and the scope 010 file directly; scope 010 has one open box, Design it (spec), Beta workflow (/check verify, then /test), Tracer Bullet build approach, Workspace completion at a glance: shared foundation 9 of 10 (open 010), iOS 1 of 2, Android 1 of 2, iOS scope (+9 more)

### Community 25 - "Spec 0004 Rationale and Schemas"
Cohesion: 0.11
Nodes (42): Canonical token schema (tokens.schema.json), Scope 010 specifics: main at start = 7b6ca4f, equal to origin/main; one feature with one open box, Design it (spec); spec number 0004; source is the spec 0003 Follow-up on greeting_recipient and the greeting role; Beta flow closes with Verify it and Test it; one developer until the lead splits ownership, Delegated decision (spec 0004, AC-1, not heavy, in force): the 'at least one key' rule is "minProperties": 1 with no required and no properties; runner-up an empty catalog is allowed; undo via architect (update) of spec 0004, rebuilding Build plan step 1, Reconciliation (lead): git branch --no-merged main is empty, there is no other worktree, and none of the 32 peer sessions works in this repo; nothing was done outside the coordination; no feature 010 artifact is on main yet, both schemas still name the sample names, Foundation schemas require sample names: the greeting_recipient key in the localization schema and the greeting typography role in the token schema, Follow-up (done): two foundation schemas still require sample names (greeting_recipient, the greeting role); this deserves its own scope row; designed in spec 0004 (2026-11-15), Build plan step 1: in shared/specifications/localization.schema.json replace the line "required": ["greeting_recipient"], with "minProperties": 1, and run scripts/generate-design-tokens.sh --check (AC-1), Decision: Option 1, fix the two schemas in place (one key of any name through minProperties), rename the required typography role greeting to heading in one change across the source, both generated files and three readers, and give the generator tests their own source tree (+34 more)

### Community 26 - "Generator Tests and Fixture Sources"
Cohesion: 0.15
Nodes (19): Delegated decision (spec 0004, AC-5, not heavy, in force): the generator tests read the fixture tree tooling/codegen/fixtures/sources/ (7 files); runner-up the tests keep reading the checkout sources generically; undo via architect (update) of spec 0004, rebuilding Build plan step 3, Build plan step 3: add the seven fixture files under tooling/codegen/fixtures/sources/ and change tooling/codegen/test_generation.py to the nine tests, then run scripts/generate-design-tokens.sh --test (AC-5, AC-6), Fixture design-system/tokens/colors.json: primitives paper #FFFFFF and coal #000000, with the eleven semantic color roles (brand, primary, secondary, background, surface, textPrimary, textSecondary, border, success, warning, error) aliased to them for light and dark, The scale names headline and reading are kept in the fixture because the generator maps exactly those two names to SwiftUI text styles, Fixture source tree tooling/codegen/fixtures/sources/: seven files mirroring the layout the generator reads (five token files, shared/config/foundation.json, shared/localization/en.json), with names and values that differ from the checkout's own on purpose, Fixture spacing.json, radius.json and motion.json: spacing near 8 and far 20 with roles content and page; radius round 10 with role surface; motion brisk 120 with role feedback, Fixture design-system/tokens/typography.json: scales headline (size 30, lineHeight 36) and reading (15, 22), weights regular 400 and bold 700, roles heading (headline, bold) and body (reading, regular), The only line in the test module that names generate.ROOT is schema = generate.load(generate.ROOT / LOCALIZATION_SCHEMA) in the new localization test; both tests that copy the fixture tree wrap their body in TemporaryDirectory() and redirect_stdout(StringIO()) (+11 more)

### Community 27 - "Coordinate Roles and Report Template"
Cohesion: 0.26
Nodes (21): Role architect: closes a (spec) box or updates a spec so a developer can build without asking again; owns the feature's docs/specs/<NNNN-slug>/ folder; all code and docs/scope are forbidden, Proposed scope block (blok scope usulan): Pointer line, Design it ticked, Build it with 2 to 5 nested milestones naming Build plan tasks and ACs, and closing boxes by tier, reported for the lead to paste into the scope, Role checker: two modes set by the brief, verify and review; ticks only the verify.md steps it ran or writes a file in docs/reviews; never fixes what it finds, Checker verify mode: proves a milestone or feature behaves per spec by running the verify.md steps, scoped to the milestone section and the AC IDs in the brief, and sends failures to the owning developer, Role debugger: finds and proves the root cause of a failure the lead forwards and proposes a minimal fix to the file owner; never edits others' files; its branch is never merged directly, Role developer: builds one milestone, one Build it box or the named Build plan steps on the files in its ownership; one commit per Build plan step; reports Pointer code in and finished steps to the lead, verify.md milestone section: written by the developer at 'Save verify steps?' (UI / manual, Commands, Acceptance-criteria coverage); with the Status line the only spec content a developer may change, Role tester: writes tests that lock a newly built milestone or feature, runs them and records evidence; owns test files and evidence only; failures go straight to the owning developer (+13 more)

### Community 28 - "Generated Native Tokens"
Cohesion: 0.29
Nodes (7): FoundationTokens, Palette, CGFloat, Color, ColorScheme, Font, TimeInterval

### Community 29 - "Real Checkout and Outside Git Tests"
Cohesion: 0.14
Nodes (9): Unit tests create their own repository in a temporary folder with isolated git configuration; no test touches the real checkout, OutsideGitTests, Checks for the derivation command: every write, every refusal and both clean…, AC-9: the derivation proof is skipped, with its reason, in a checkout that is…, AC-7: outside git both foundation values are required., AC-7: a folder inside another repository counts as outside git., Run the checked in command on a temporary copy of this checkout. The checkout…, AC-9: the copy's own command derives the copy, which then reads derived and… (+1 more)

### Community 30 - "Supported OS and Large Text Scopes"
Cohesion: 0.22
Nodes (13): FoundationTokens, Palette, Android 001 - Native Android greeting (existing), API 36 emulator results (arm64 local, x86_64 hosted) in light and dark, Android app packages both supported CPU architectures, Android 002 - Lowest supported Android and large text (planned), 16 KiB memory page packaging, Declared Android minimum API 24 not yet exercised (+5 more)

### Community 31 - "Generator Tests and Accessibility Checks"
Cohesion: 0.25
Nodes (10): Accessibility (design system), Status conveyed by text or semantics, not color alone, Honor platform reduced-motion setting, Text contrast check (4.5:1 minimum), W3C WCAG 2.2 contrast minimum guidance, 003 - Shared visual definitions (done), Light and dark text meet the documented contrast threshold, Shared named visual values (color, type, spacing, corners, motion) (+2 more)

### Community 32 - "Token Conventions and Spec 0004 Document Updates"
Cohesion: 0.16
Nodes (24): Semantic names for decisions both apps share, Token conventions, References are group-local and point directly to primitives, Token naming convention (lower camel case, #RRGGBB), Primitive token (names a value), Stable role names or same-change migration, Semantic role (describes where to use a value), Tokens, configuration and localization check (+16 more)

### Community 33 - "Spec 0004 Verification Matrix and Token Command"
Cohesion: 0.14
Nodes (33): Build-time generation: token JSON and locale JSON -> native theme inputs and localization resources, Sample removal only on a copy: proof that the catalog and token set pass without the greeting names runs on test fixtures or a temporary scratchpad clone, never by leaving the worktree with the samples deleted; scripts/init-project.sh --name only in a temporary clone, --check and --test are safe, Delegated decision (spec 0004, AC-6, not heavy, in force): Done when clause (4) is proven by a unit test on the fixture plus a temporary clone step with the real script; runner-up a --root generator flag with stored output; undo via architect (update) of spec 0004, rebuilding Build plan steps 3 and 5, Delegated decision (spec 0004, AC-4, not heavy, in force): the key greeting_recipient stays as sample content in the catalog and both apps, and the schema no longer names it; runner-up the neutral key recipient_name; undo via architect (update) of spec 0004, Build plan step 2 grows by 7 files, Decision (lead): spec 0004 accepted after three auto-mode checks: the six cross-check gaps (another model, read only) are in the Verification matrix; Done when clauses (1) to (4) are covered by AC-1 to AC-6; no decision conflicts with spec 0001, 0002 or 0003, Done when (010): the localization schema asks for at least one key and names none, the typography role is named for its purpose, native themes and generator tests follow, and a greeting-free catalog and token set pass generate-design-tokens.sh --check, AC-1: localization.schema.json holds "minProperties": 1 with no required and no properties member; an empty default catalog {} makes --check exit 1 with 'en.json: data must contain at least 1 properties'; any single key that fits the key pattern is accepted, AC-4: the sample app behaves as before: scripts/test.sh exits 0, both apps build, the greeting tests pass in light and dark on both platforms, and greeting_recipient stays in en.json, both generated string files and both app entry points (+25 more)

### Community 34 - "Native Token Mapping and Text Scaling"
Cohesion: 0.23
Nodes (16): System text scaling via generated text styles, Native token mapping, Compose sp mapping of logical text units, Jetpack Compose token projection (FoundationTokens), Dynamic Type mapping of headline and reading scales, Logical spacing units adapt to display density, spacingPage role, SwiftUI token projection (FoundationTokens) (+8 more)

### Community 35 - "iOS App Shell"
Cohesion: 0.18
Nodes (12): App, MobileFoundationApp, .body, Android physical device coverage unverified, Deferred: signing, physical device runs and store delivery, iOS 001 - Native iOS greeting (existing), Native text style supporting Dynamic Type, Greeting exposed to accessibility in light and dark appearance (+4 more)

### Community 36 - "Android App Shell"
Cohesion: 0.60
Nodes (3): MainActivity, Bundle, ComponentActivity

### Community 37 - "Kotlin Rust Call Status"
Cohesion: 0.23
Nodes (7): E, uniffiCheckCallStatus(), UniffiForeignFutureCompleteVoid, uniffiRustCall(), UniffiRustCallStatusErrorHandler, uniffiRustCallWithError(), U

### Community 38 - "Identity Value Sourcing"
Cohesion: 0.27
Nodes (10): apps/android/app/src/main/AndroidManifest.xml, apps/android/app/src/main/res/values/app.xml (the app_name string leaves this file; the label comes from the appLabel manifest placeholder), apps/ios/Config/App.xcconfig (iOS app build settings), apps/ios/Config/Project.xcconfig (iOS project build settings), apps/ios/MobileFoundation.xcodeproj/project.pbxproj (Xcode project file), Android build reads identity.properties: app/build.gradle.kts loads applicationId, versionName and versionCode, the label reaches the manifest as the appLabel placeholder, namespace stays foundation.mobile, iOS build reads Identity.xcconfig: Project.xcconfig includes it, App.xcconfig maps the bundle ID and display name, the UI test bundle ID is derived as $(APP_BUNDLE_IDENTIFIER).uitests, Force: identity is spread over files the foundation keeps editing (App.xcconfig, Project.xcconfig, project.pbxproj, app/build.gradle.kts, res/values/app.xml) (+2 more)

### Community 39 - "Architecture Boundaries and Mobile Contract"
Cohesion: 0.13
Nodes (29): Architecture boundaries, Documented capability boundary; adapters need an actual caller, Layer: design system (generated Swift/Kotlin values as shared visual vocabulary), Layer: native platform integration (Swift owns Apple services, Kotlin owns Android services), Layer: native presentation (views render, adapt to appearance, handle events), Layer: resources and tooling (build-host validation and generation), Layer: shared Rust (core owns behavior, FFI crate maps exports), Workspace edge: mobile-ffi depends on foundation-core (std-only core) (+21 more)

### Community 40 - "Derivation State Check Tests"
Cohesion: 0.18
Nodes (5): AC-8: every departure from the exact form is a mismatch that names the file and…, AC-8: a derived checkout that lost one signal names that signal., AC-8: an identity file that is not UTF-8, and a missing README.md, are…, AC-8: changing only applicationId names that file and key against a foundation…, AC-8: default IDs under an origin line, and a second origin line, each make a…

### Community 41 - "Hosted Build Verification and iOS UI Tests"
Cohesion: 0.25
Nodes (7): CoreImage, iOS simulator results (iPhone 17 on iOS 27.0 local, iOS 26.5 hosted), 006 - Hosted build verification (done), Android hosted job installs the supported SDK packages, iOS simulator boots in each system appearance before XCTest, Three hosted jobs (foundation, iOS, Android) on the same revision, XCTest

### Community 42 - "Scope 010 General Brief Rules"
Cohesion: 0.18
Nodes (12): General brief rules (Aturan umum brief) for the sub-sessions of the scope 010 coordination: the fixed part of every brief; the brief the lead sends points to this file, and the brief wins where the two differ, Additional user conditions (Ketentuan tambahan user) for the scope 010 coordination: none, Commit rule: one commit per step, an English imperative subject without a prefix like this repo's history (e.g. 'Plan and specify a new project from the foundation'), plus the Co-Authored-By trailer from the session's system reminder; the developer moves the spec **Status** from Proposed to In Progress, Disk rule: 22 GiB free at the start; one full native build at a time (the developer for the platform it touches, then the checker); the tester builds only if the brief asks; run df -g . first; below 10 GiB free stop and report blocked; remove target/, build/ and scratchpad clones before done, Lead address: the lead session Mobile Foundation Scaffold; full reports, questions and needs-decision go there via SendMessage; other sub-sessions are found in ListAgents by title prefix; sessions of this coordination always use f010, unlike similarly named sessions of other projects on this Mac, Process rule: stop only processes, simulators and emulators you started yourself, name them uniquely (F010-<session name>) and delete them afterwards; a suite longer than 10 minutes runs detached with nohup and a scratchpad log, Project adjustments: the role files were written for another Rust project; this repo has no cargo xtask, stackly_testkit, clients/swift, evidence/, prd.md or test-preferences.json; scope is in docs/scope/_root/, specs in docs/specs/_root/<NNNN-slug>/; evidence is the commands and output in the report, Report rule: one final report per item with no interim messages to the lead, following templates/report.md via SendMessage; done is valid only when all is committed, the tree is clean and the last git merge main ran; then wrap_up with a first line STATUS: ...; the lead reads only the first 400 characters (+4 more)

### Community 43 - "Kotlin Handle Map and Lifting"
Cohesion: 0.42
Nodes (4): InternalException, T, UniffiHandleMap, UniffiNullRustCallStatusErrorHandler

### Community 44 - "Heading Role Rename and Design System Guide"
Cohesion: 0.14
Nodes (26): FoundationTheme(), Design system guide, generate-design-tokens.sh modes: write, --check (drift), --test (failure cases), Generated semantic token API consumed by native apps, Five canonical token JSON files (primitives and semantic aliases), tokens.schema.json: single Draft 7 document keyed by filename stem, Canonical token sources (colors, typography, spacing, radius, motion JSON), Delegated decision (spec 0004, AC-2 and AC-3, heavy, in force): the typography role replacing greeting is named heading; runner-up title; undo via architect (update) of spec 0004, rebuilding Build plan steps 2 and 3, the fixture content and the step 4 document texts (+18 more)

### Community 45 - "Knowledge Graph Update Rules"
Cohesion: 0.32
Nodes (13): Agent workflow: before commit (run /graphify . --update, stage graphify-out with the change), Knowledge graph (graphify-out/, kept current with /graphify . --update), Token saving: graph first, files later: lead and sub-sessions ask graphify query and explain before reading files, and open files only where the graph points, Token saving: graph only for changed files: each graph update processes only the files of the commit being prepared; code through graphify update, documents through a restricted /graphify --update whose manifest is stamped for those files only, Graph and commit: the lead fulfils the AGENTS.md /graphify . --update rule when merging to main; sub-sessions never run graphify update and never stage anything under graphify-out/, Main checkout and knowledge graph: run graphify query and graphify explain against the main checkout's graphify-out/graph.json before reading files, and never change a file in the main checkout, Decision: the knowledge graph is updated once per gate event: merged files, scope ticks and the log go into one graph update and one commit, so the AGENTS.md rule is met without repeated extraction, Decision: the restricted graph update stamped _origin semantic directly in graph.json for nodes and edges of the 14 coordination and skill documents, because the library guesses the tier from the shape of the location; later restricted updates stamp the chunk before the merge (+5 more)

### Community 46 - "README and Path Ownership"
Cohesion: 0.35
Nodes (12): AC-11: README.md has a section with the full path from clone to first results, path ownership, taking a later release and foundation tagging, Follow-up: build the command that takes a foundation release (fetch, merge, apply the ownership table) when the first release is merged into a product, Follow-up: decide where dependency update bots run (a bot in every product changes foundation owned files and will conflict with merges), Path ownership after derivation: product owned paths keep the product's side, foundation owned paths take the foundation's side, shared paths merge by hand, README section 'Start a project from this foundation': clone at a tag, create a branch, rename the remote, run the command, add origin, rebuild the graph, mark inherited rows existing, commit, record first results, Take a later foundation release: git fetch foundation --tags, git merge foundation-vX.Y.Z, keep the product's side on product owned paths, rebuild the graph, run every check, Tradeoff: every merge of a foundation release reports conflicts on product owned paths, resolved by hand until the sync command exists, UI / manual steps: home screen label Mobile Foundation on both apps, Identity.xcconfig listed in Xcode and not a base config, a derived Acme Notes pair installed beside the foundation apps, the derived checkbox on the Actions page, the README section read through (three of the five are ticked; the Xcode file list step and the Actions page step are open) (+4 more)

### Community 47 - "Command Line Wrapper Tests"
Cohesion: 0.31
Nodes (5): CommandLineTests, Run the copied scripts/init-project.sh from another folder, as a person or CI…, AC-3, AC-8: the wrapper finds its own checkout, prints the five changed paths,…, AC-7: through the wrapper a refusal exits 2, prints one line on stderr only,…, AC-8: through the wrapper --check exits 1 and names the mismatch on stderr.

### Community 48 - "Generated File and Drift Rules"
Cohesion: 0.36
Nodes (8): Never hand-edit generated files, Derived file rule: change the canonical input and regenerate every output in the same review, Generated drift remediation, Regenerate native projections in the same change, Regenerate derived files alongside canonical inputs, Generated files rule: never hand-edit generator output; change the source (design-system/tokens/, design-system/schemas/, shared/localization/, shared/specifications/, tooling/codegen/), run scripts/generate-design-tokens.sh and the generators scripts/test.sh checks, commit output with its source, Drift detection for checked-in bindings and resources (stale, edited and missing generated files), R5: a generated file is never edited by hand; change the source and regenerate every output

### Community 49 - "Kotlin FFI Integrity Checks"
Cohesion: 0.60
Nodes (3): IntegrityCheckingUniffiLib, uniffiCheckApiChecksums(), uniffiCheckContractApiVersion()

### Community 50 - "CI Workflow and Spec 0003 Build Plan"
Cohesion: 0.20
Nodes (31): Pass representative values through both generated languages, Derived hosted run android job result (same derive command; Gradle 9.3.1 assembled the derived debug app; identity file and built app matched; two instrumentation tests passed with night mode off and on), Derived hosted run ios job result (derive step ran init-project.sh as Zoë's Proof with dev.example.derived; Xcode 26.5 built the derived app; identity file and built app matched; greeting test passed in light and dark on iOS 26.5), Hosted run 43701281055 on the push of revision 4a153fe (all three jobs passed; the derive step was skipped; both comparison steps passed with dev.foundation.mobile and Mobile Foundation), Hosted run 43701289339 on revision 4a153fe (2026-11-15, started by hand through workflow_dispatch with the derived input set; all three jobs passed), Hosted run 43701281055 (push trigger, on revision 4a153fe), Scope 009 specifics: main at the start is 4a153fe, equal to origin/main; Build plan steps 1 to 10 of spec 0003 are on main; no sub-session triggers, repeats or cancels a hosted run; each of verification.md, verify.md and test_init_project.py has exactly one sub-session that may change it, Sub-session dev-f009-m3 (developer, opus-5-5 medium, archived): scope 009 milestone 3, Build plan step 11 for AC-10; owns docs/quality/verification.md (+23 more)

### Community 51 - "Android Rust Build Script"
Cohesion: 0.40
Nodes (4): CARGO_TARGET_AARCH64_LINUX_ANDROID_LINKER, CARGO_TARGET_X86_64_LINUX_ANDROID_LINKER, PATH, build-android-rust.sh script

### Community 53 - "Greeting Screens, Platform Rules and Gradle Wrapper"
Cohesion: 0.08
Nodes (31): gradlew script, die(), warn(), GreetingScreen(), GreetingScreen, .body, String, Per-target reading order and screen-reader review (+23 more)

### Community 54 - "iOS Rust Build Script"
Cohesion: 0.50
Nodes (3): CARGO_TARGET_DIR, PATH, build-ios-rust.sh script

### Community 55 - "Coordinate Wave Plan and Ownership"
Cohesion: 0.40
Nodes (5): Item and ownership: one item is one box or part of a milestone's Build plan steps; ownership is written as file paths, and two items share a wave only when no file is in both ownerships, Lead step 2: analysis and wave plan (read the scope and the needed spec parts, reconcile with sessions, branches and code already on main, build the dependency graph, mark each open box SIAP or TERBLOKIR), Wave plan: an ordered queue approved once (longest remaining chain first, then items whose merge unblocks most, closing boxes, architects as slot fillers), shown and then run without waiting, Brief field 'File yang BOLEH diubah': the files and folders the item owns; anything else is forbidden or requested from its owner, Always forbidden: docs/scope/, AGENTS.md, graphify-out/, spec content other than the **Status** line and verify.md ticks (except the architect on its own spec), other specs, and files outside 'File yang BOLEH diubah'; changes outside ownership are requested from the owner or the lead

### Community 59 - "Scope 010 Manual Steps"
Cohesion: 0.36
Nodes (8): Manual steps (Langkah manual): steps needing the user's eyes, hands, account, device or permission; no session runs them; the box is still ticked when the rest passes and the step is recorded NOT_RUN; a FAIL reopens it, Template: manual steps file (Langkah manual) for the user: summary table with stable step IDs F<feature>-<n>, values from the user, and per-feature steps with prerequisite, exact command and pass condition, Manual steps rule: GUI apps such as Xcode, GitHub web pages, physical devices, signing, tool installs, repo settings, pushes and workflow triggers are run only by the user or lead and go in the report's 'Langkah manual' field; gh is read-only; headless simulators are allowed; a failed step is not manual, Manual steps (Langkah manual) for scope 010 - Schemas free of sample names: steps that need the user's eyes, hands, account, device or permission and that no session runs; none recorded yet, Feature 010 steps: Schemas free of sample names (spec 0004): no manual steps yet, Result routing for scope 010 manual steps: the user sends the step ID, PASS or FAIL and the output on FAIL to the lead; the lead forwards it to the checker, who ticks verify.md; FAIL reopens the box; decisions taken on the user's behalf are in the log's 'Keputusan delegasi' section, Manual step summary (Ringkasan) for scope 010 (ID, step, AC, boxes ticked while the step is NOT_RUN, runnable after, result): no steps yet, Values from the user (Nilai dari user) for scope 010 (ID, value needed, waiting AC, waiting file): values only the user knows; the waiting AC stays BLOCKED until the value exists; none yet

### Community 60 - "Verification Before Reporting and Native Builds"
Cohesion: 0.18
Nodes (14): Agent workflow: before handoff (run checks, report commands and unverified targets), Rust format and lint check (rustfmt, Clippy warnings denied), Derived hosted run foundation job result (locked build and scripts/test.sh passed: three Rust tests, 21 derivation tests, seven generator tests; this job does not derive), Verification before reporting: scripts/test.sh must exit 0; build-ios.sh simulator, device and test in light and dark when apps/ios/ changed; build-android.sh assemble and connectedDebugAndroidTest in both night modes when apps/android/ changed; git status clean and the diff against main limited to ownership files, Verification before reporting: scripts/test.sh must exit 0; if apps/ios/ changed run scripts/build-ios.sh simulator, device and test light and dark; if apps/android/ changed run scripts/build-android.sh assemble and connected tests in both night modes; git status clean, diff only ownership files, Decision (lead, carried over from the scope 009 log): the lead gate on main after a merge is no conflict markers, scripts/test.sh exits 0, and a native build per platform when apps/ changed, Enforcement: scripts/test.sh runs format, lint, tests and three policy checks; CI runs the same script plus iOS and Android jobs, AC-2: with the default identity scripts/test.sh passes, both apps build and the greeting tests pass in both appearances (+6 more)

### Community 61 - "Decision Mode Auto"
Cohesion: 0.21
Nodes (15): Accept this spec? handoff: the architect never answers it itself; it sends the spec path, Decision, key tradeoff and decisions taken to the lead, ends the turn with STATUS: needs-decision and continues after accept, Decision mode (Mode keputusan): governs only decisions, the choices that change spec content; an ambiguous AC reading is not a decision, Heavy decision (keputusan berat): expensive to reverse once built (on-disk data format or migration, contract break, security model, licensing, existing user data, changes to an Accepted spec), Mode auto (default): the recommended option is taken for ordinary and heavy decisions, heavy ones flagged berat, Mode tanya: the user decides every decision, Mode tanya berat: the recommended option for ordinary decisions, the user decides heavy ones, Recommended option: the architect takes its own recommendation and writes reason and runner-up in rationale.md; the lead accepts after three checks; every decision is recorded with its runner-up and how to undo it, Run defaults of /coordinate: parallel sub-sessions for non-overlapping ownership, wave plan shown then run, debugger on a red gate, decisions follow the decision mode, user-only steps go to the manual file, a feature is marked done at its last box (+7 more)

### Community 62 - "iOS Greeting UI Test Pixel Check"
Cohesion: 0.50
Nodes (3): UInt8, CIContext, XCUIScreenshot

## Knowledge Gaps
- **70 isolated node(s):** `NoHandle`, `UniffiWithHandle`, `Explicit application records and enums; private core/transport shapes mapped at the adapter`, `test.sh script`, `apiChecksumMismatch` (+65 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Spec 0003: A new project from the foundation: product identity in two files, one init command, updates by merge (Accepted)` connect `Spec 0003 Acceptance Criteria` to `Spec 0004 Verification Matrix and Token Command`, `Scope 009 Coordination Records`, `Planning Path and Spec 0002`, `Rule Set and Platform Rules`, `Identity Value Sourcing`, `Development Rules and Spec Triggers`, `README and Path Ownership`, `Architecture Check and Planning Rules`, `CI Workflow and Spec 0003 Build Plan`, `Ownership Matrix and Repository Structure`, `Init Command and Identity Files`, `Spec 0003 Decision History`, `Scope 010 Coordination and Spec 0004`, `Spec 0004 Rationale and Schemas`, `Verification Before Reporting and Native Builds`?**
  _High betweenness centrality (0.122) - this node is a cross-community bridge._
- **Why does `DerivationTests` connect `Derivation Refusal and Write Set Tests` to `Derivation State Check Tests`, `Derivation Run and Origin Line Tests`, `Derivation Test Checkout Fixture`, `Derivation Write Failure Tests`, `Real Checkout and Outside Git Tests`?**
  _High betweenness centrality (0.112) - this node is a cross-community bridge._
- **Why does `.body` connect `iOS App Shell` to `Swift UniFFI Bindings`, `Greeting Screens, Platform Rules and Gradle Wrapper`?**
  _High betweenness centrality (0.098) - this node is a cross-community bridge._
- **Are the 5 inferred relationships involving `Spec 0004: Schemas free of sample names: one key of any name, a heading role, generator tests on their own sources (Status: Proposed, 2026-11-15); removes the two sample names (greeting_recipient, the greeting role) that the foundation schemas still require` (e.g. with `Design it (spec) (010): ticked; command /architect schemas free of sample names` and `Canonical token schema (tokens.schema.json)`) actually correct?**
  _`Spec 0004: Schemas free of sample names: one key of any name, a heading role, generator tests on their own sources (Status: Proposed, 2026-11-15); removes the two sample names (greeting_recipient, the greeting role) that the foundation schemas still require` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `Foundation verification 2026-11-15` (e.g. with `Record separately what compiled and what ran` and `Sub-session dev-f010-m1 (developer, opus-5-5 medium, active): scope 010 Build it, all three milestones, Build plan steps 1 to 5 of spec 0004; owns both schemas, typography.json, the generated token files, three app files, the codegen fixtures and tests, five documents and verify.md; branch claude/dev-f010-m1-6599c9`) actually correct?**
  _`Foundation verification 2026-11-15` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `NoHandle`, `UniffiWithHandle`, `Explicit application records and enums; private core/transport shapes mapped at the adapter` to the rest of the system?**
  _70 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Verification Record, CI Workflow and Policy Checks` be split into smaller, more focused modules?**
  _Cohesion score 0.12477718360071301 - nodes in this community are weakly interconnected._