# Graph Report - mobile  (2026-11-15)

## Corpus Check
- 1 files · ~88,219 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1444 nodes · 4630 edges · 59 communities (58 shown, 1 thin omitted)
- Extraction: 75% EXTRACTED · 25% INFERRED · 0% AMBIGUOUS · INFERRED: 1157 edges (avg confidence: 0.9)
- Token cost: 106,301 input · 6,307 output

## Community Hubs (Navigation)
- Verification Record, CI Workflow and Policy Checks
- Swift UniFFI Bindings
- Coordinate Skill
- Kotlin FFI Library Loading
- Scope 009 Coordination Records
- Kotlin UniFFI Library Calls
- Planning Path and Spec 0002
- Spec 0001 Ownership Decision and Forces
- Rust Rules and Bridge Hygiene
- Derivation Command
- Derivation Refusal and Write Set Tests
- Derivation Run and Origin Line Tests
- Development Rules and Spec Triggers
- Resource Generator
- Kotlin RustBuffer Handling
- Shared Settings, Localization and Config Schema
- Architecture Check and Planning Rules
- Derivation Test Checkout Fixture
- Ownership Matrix and Repository Structure
- Init Command and Identity Files
- Spec 0003 Decision History
- Spec 0003 Path Ownership and Kept Names
- Kotlin FFI Converters
- Scope 010 Coordination Records
- Empty Verification Record
- Spec 0004 Rationale and Token Schema
- Generator Tests and Fixture Sources
- Shared Greeting Contract and FFI Export
- Contract Extension Conventions
- Real Checkout and Outside Git Tests
- Android App Shell
- Rust Core and Greeting Contract
- Platform Rules and Agent Workflow
- Scope 010 Build, Verify and Verification Matrix
- Token Conventions and Native Token Mapping
- Native Greeting and Supported OS Scopes
- Greeting Screens and iOS App Shell
- Kotlin Rust Call Status
- Identity Value Sourcing
- Architecture Boundaries
- Derivation State Check Tests
- UniFFI Generator on Host Tooling
- Localization Schema One-Key Rule
- Kotlin Handle Map and Lifting
- Spec 0004 and Heading Role Rename
- Regeneration and Drift Remediation
- Command Line Wrapper Tests
- Rule Set R1 to R19 and Generated File Rules
- Kotlin FFI Integrity Checks
- Android Rust Build Script
- Derivation Write Failure Tests
- iOS Rust Build Script
- iOS Greeting UI Test Pixel Check
- Token Command and Spec 0004 API Surface
- Android Gradle Wrapper
- Derivation Tests and Documented Paths

## God Nodes (most connected - your core abstractions)
1. `Spec 0004: Schemas free of sample names: one key of any name, a heading role, generator tests on their own sources (Status: Accepted, 2026-11-15); removes the two sample names (greeting_recipient, the greeting role) that the foundation schemas still require` - 74 edges
2. `Foundation verification 2026-11-15` - 71 edges
3. `Spec 0003: A new project from the foundation: product identity in two files, one init command, updates by merge (Accepted)` - 66 edges
4. `Spec 0002: One planning path: a scope row first, then a spec` - 61 edges
5. `Coordination log (Log koordinasi) for scope 010 - Schemas free of sample names (wave 1 finished 2026-11-15, no active wave, decision mode auto, start hash 7b6ca4f, updated 2026-11-15 21:25)` - 60 edges
6. `Spec 0001: One owner per responsibility, with rules kept beside the code` - 57 edges
7. `UniffiLib` - 54 edges
8. `Mobile foundation scope (index)` - 48 edges
9. `DerivationTests` - 46 edges
10. `Sub-session dev-f010-m1 (developer, opus-5-5 medium, archived): scope 010 Build it, all three milestones, Build plan steps 1 to 5 of spec 0004, all finished; owns both schemas, typography.json, the generated token files, three app files, the codegen fixtures and tests, five documents and verify.md; branch claude/dev-f010-m1-6599c9` - 42 edges

## Surprising Connections (you probably didn't know these)
- `Product identity result (2026-11-15: test.sh passed with --check printing foundation and --test passing 21 unit tests; both apps carried dev.foundation.mobile, Mobile Foundation, 0.1.0, build 1; a copy derived as Zoë's Proof built and matched its identity file)` --references--> `GreetingUITests`  [INFERRED]
  docs/quality/verification.md → apps/ios/UITests/GreetingUITests.swift
- `Schemas free of sample names result (2026-11-15: test.sh passed with nine generator tests on Python 3.9.6 and --check passed; both apps built and passed the greeting tests in light and dark after the rename to typographyHeading; a scratch clone with the single key welcome_title generated, checked and tested)` --references--> `GreetingUITests`  [INFERRED]
  docs/quality/verification.md → apps/ios/UITests/GreetingUITests.swift
- `Product identity result (2026-11-15: test.sh passed with --check printing foundation and --test passing 21 unit tests; both apps carried dev.foundation.mobile, Mobile Foundation, 0.1.0, build 1; a copy derived as Zoë's Proof built and matched its identity file)` --references--> `GreetingTest`  [INFERRED]
  docs/quality/verification.md → apps/android/app/src/androidTest/kotlin/foundation/mobile/GreetingTest.kt
- `Schemas free of sample names result (2026-11-15: test.sh passed with nine generator tests on Python 3.9.6 and --check passed; both apps built and passed the greeting tests in light and dark after the rename to typographyHeading; a scratch clone with the single key welcome_title generated, checked and tested)` --references--> `GreetingTest`  [INFERRED]
  docs/quality/verification.md → apps/android/app/src/androidTest/kotlin/foundation/mobile/GreetingTest.kt
- `Trace screen, generated binding, FFI export and core function before changing shared behavior` --references--> `GreetingScreen`  [INFERRED]
  docs/rules/development-rules.md → apps/ios/Presentation/GreetingScreen.swift

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Coordination records of scope 010 (log, general brief rules, manual steps) tied to the scope 010 file** — docs_scope_coordination_010_schemas_free_of_sample_names_log, docs_scope_coordination_010_schemas_free_of_sample_names_brief_umum, docs_scope_coordination_010_schemas_free_of_sample_names_manual, docs_scope_root_010_schemas_free_of_sample_names [EXTRACTED 1.00]
- **Scope 010 decisions carried over from the scope 009 coordination log (lead gate, session and disk limit, Beta flow boxes, one graph update per gate)** — docs_scope_coordination_010_schemas_free_of_sample_names_log_lead_gate_on_main, docs_scope_coordination_010_schemas_free_of_sample_names_log_session_and_disk_limit, docs_scope_coordination_010_schemas_free_of_sample_names_log_no_review_or_document_box, docs_scope_coordination_010_schemas_free_of_sample_names_log_one_graph_update_per_gate, docs_scope_coordination_009_a_new_project_from_the_foundation_log [EXTRACTED 1.00]
- **The nine delegated decisions of spec 0004 taken in auto mode for scope 010 (one heavy: the role name heading)** — docs_scope_coordination_010_schemas_free_of_sample_names_log_delegated_decisions, docs_scope_coordination_010_schemas_free_of_sample_names_log_delegated_heading_role_name, docs_scope_coordination_010_schemas_free_of_sample_names_log_delegated_required_roles_heading_body, docs_scope_coordination_010_schemas_free_of_sample_names_log_delegated_no_alias_for_typography_greeting, docs_scope_coordination_010_schemas_free_of_sample_names_log_delegated_min_properties_rule, docs_scope_coordination_010_schemas_free_of_sample_names_log_delegated_greeting_recipient_stays_sample_content, docs_scope_coordination_010_schemas_free_of_sample_names_log_delegated_fixture_source_tree, docs_scope_coordination_010_schemas_free_of_sample_names_log_delegated_done_when_4_proof, docs_scope_coordination_010_schemas_free_of_sample_names_log_delegated_scope_two_sample_names_only, docs_scope_coordination_010_schemas_free_of_sample_names_log_delegated_cross_check_findings_applied, docs_specs_root_0004_schemas_free_of_sample_names_index [EXTRACTED 1.00]
- **Wave 1 sub-sessions of the scope 010 coordination with their coordinate role files** — docs_scope_coordination_010_schemas_free_of_sample_names_log_arc_f010_spec, docs_scope_coordination_010_schemas_free_of_sample_names_log_dev_f010_m1, docs_scope_coordination_010_schemas_free_of_sample_names_log_chk_f010_verify, docs_scope_coordination_010_schemas_free_of_sample_names_log_tst_f010_test, claude_skills_coordinate_roles_architect, claude_skills_coordinate_roles_developer, claude_skills_coordinate_roles_checker, claude_skills_coordinate_roles_tester [EXTRACTED 1.00]
- **Hosted run 43593365100 as runtime evidence for the greeting contract, visual definitions, shared text and reproducible builds** — docs_scope_root_002_shared_greeting_contract, docs_scope_root_003_shared_visual_definitions, docs_scope_root_004_shared_settings_text_and_brand_assets, docs_scope_root_005_reproducible_local_builds_and_checks, docs_quality_verification_hosted_run_43593365100, docs_quality_verification [EXTRACTED 1.00]
- **Forces that motivate the one-owner-per-responsibility decision** — docs_specs_root_0001_ownership_development_rules_force_two_languages_downstream_of_one_source, docs_specs_root_0001_ownership_development_rules_force_generated_files_beside_handwritten_code, docs_specs_root_0001_ownership_development_rules_force_coding_agents_as_regular_contributors, docs_specs_root_0001_ownership_development_rules_force_one_maintainer, docs_specs_root_0001_ownership_development_rules_force_small_codebase, docs_specs_root_0001_ownership_development_rules_decision_one_owner_per_responsibility [EXTRACTED 1.00]
- **Machine enforcement chain: test.sh runs the validator and both generator drift checks, mirrored by the CI foundation job** — docs_specs_root_0001_ownership_development_rules_enforcement_test_script_and_three_policy_checks, scripts_test, tooling_validation_check_architecture, scripts_generate_bindings, scripts_generate_design_tokens, github_workflows_foundation_foundation_job [EXTRACTED 1.00]
- **Rules that rest on review alone with no automated check** — docs_specs_root_0001_ownership_development_rules_r1_one_authoritative_owner, docs_specs_root_0001_ownership_development_rules_r3_app_trees_do_not_import_one_another, docs_specs_root_0001_ownership_development_rules_r8_real_caller_first, docs_specs_root_0001_ownership_development_rules_r9_search_before_adding, docs_specs_root_0001_ownership_development_rules_r11_handoff_reports_compiled_and_ran_separately, docs_specs_root_0001_ownership_development_rules_r14_bindgen_feature_host_only, docs_specs_root_0001_ownership_development_rules_r15_library_change_transitive_and_size_review, docs_specs_root_0001_ownership_development_rules_r16_breaking_change_is_a_migration, docs_specs_root_0001_ownership_development_rules_r18_service_proposal_requirements [EXTRACTED 1.00]
- **Canonical source over generated output: edit sources, regenerate, compare snapshots** — agents_never_hand_edit_generated_files, docs_architecture_ownership_matrix_derived_file_rule, docs_architecture_dependency_rules_one_way_generation, docs_decisions_adr_0001_foundation_checked_in_source_snapshots [INFERRED 0.85]
- **Regenerate and compare checks that keep generated tokens, catalogs and bindings equal to their sources** — docs_scope_root_003_shared_visual_definitions_token_drift_check, docs_scope_root_004_shared_settings_text_and_brand_assets_single_english_catalog, docs_scope_root_005_reproducible_local_builds_and_checks_generated_output_drift_detection, scripts_test [INFERRED 0.85]
- **Automated architecture compliance checks** — docs_quality_architecture_compliance_rust_format_and_lint, docs_quality_architecture_compliance_core_and_ffi_contract_tests, docs_quality_architecture_compliance_cargo_dependency_and_governance_check, docs_quality_architecture_compliance_project_identity_state_check, docs_quality_architecture_compliance_uniffi_generated_files_check, docs_quality_architecture_compliance_tokens_config_localization_check, docs_quality_architecture_compliance_ios_linkage_and_ui_check, docs_quality_architecture_compliance_android_linkage_and_ui_check [EXTRACTED 1.00]
- **The five sub-session roles of /coordinate, each with its own goal, ownership, message paths and model** — claude_skills_coordinate_roles_architect, claude_skills_coordinate_roles_developer, claude_skills_coordinate_roles_checker, claude_skills_coordinate_roles_tester, claude_skills_coordinate_roles_debugger, claude_skills_coordinate_skill_sub_session, claude_skills_coordinate_skill_model_per_role [EXTRACTED 1.00]
- **Tick gates of /coordinate: what must be true on main before the lead ticks each kind of scope box** — claude_skills_coordinate_skill_step_6_tick_gate_and_merge, claude_skills_coordinate_skill_gate_design_it, claude_skills_coordinate_skill_gate_milestone, claude_skills_coordinate_skill_gate_build_it_and_verify_it, claude_skills_coordinate_skill_gate_test_it, claude_skills_coordinate_skill_gate_review_it, claude_skills_coordinate_skill_gate_document_it, claude_skills_coordinate_skill_red_gate_cycle [EXTRACTED 1.00]
- **Build plan of spec 0004: five steps that together satisfy AC-1 to AC-7** — docs_specs_root_0004_schemas_free_of_sample_names_index_build_plan, docs_specs_root_0004_schemas_free_of_sample_names_index_build_plan_step_1, docs_specs_root_0004_schemas_free_of_sample_names_index_build_plan_step_2, docs_specs_root_0004_schemas_free_of_sample_names_index_build_plan_step_3, docs_specs_root_0004_schemas_free_of_sample_names_index_build_plan_step_4, docs_specs_root_0004_schemas_free_of_sample_names_index_build_plan_step_5, docs_specs_root_0004_schemas_free_of_sample_names_index_ac_1, docs_specs_root_0004_schemas_free_of_sample_names_index_ac_2, docs_specs_root_0004_schemas_free_of_sample_names_index_ac_3, docs_specs_root_0004_schemas_free_of_sample_names_index_ac_4, docs_specs_root_0004_schemas_free_of_sample_names_index_ac_5, docs_specs_root_0004_schemas_free_of_sample_names_index_ac_6, docs_specs_root_0004_schemas_free_of_sample_names_index_ac_7 [EXTRACTED 1.00]
- **Rename path of the typography role greeting to heading: token schema, typography.json, both generated token files and the three readers, changed in one commit** — design_system_schemas_tokens_schema, docs_specs_root_0004_schemas_free_of_sample_names_index_token_schema_required_heading_and_body, docs_specs_root_0004_schemas_free_of_sample_names_index_typography_json_heading_role, docs_design_system_token_conventions_canonical_token_sources, docs_specs_root_0004_schemas_free_of_sample_names_index_typographyheading_generated_property, apps_ios_designsystem_generated_foundationtokens, apps_android_designsystem_src_main_kotlin_foundation_designsystem_foundationtokens, apps_ios_presentation_greetingscreen, apps_android_designsystem_src_main_kotlin_foundation_designsystem_foundationtheme, apps_android_app_src_androidtest_kotlin_foundation_mobile_greetingtest, docs_specs_root_0004_schemas_free_of_sample_names_index_build_plan_step_2 [EXTRACTED 1.00]
- **Greeting vertical slice: localized recipient through UniFFI to the Rust formatter** — readme_hello_world_greeting, shared_localization_readme_greeting_recipient, docs_architecture_overview_greeting_call_flow, docs_contracts_ffi_conventions_hello_contract, docs_architecture_overview_foundation_core_hello, docs_architecture_ownership_matrix_crates_mobile_ffi, docs_architecture_ownership_matrix_bindings, readme_uniffi [EXTRACTED 1.00]
- **One init command turns a foundation clone into a derived product: identity files, README origin line, empty verification record, removed knowledge graph** — scripts_init_project, tooling_derive_init_project, apps_ios_config_identity, apps_android_identity, docs_specs_root_0003_new_project_from_foundation_index_readme_origin_line, docs_specs_root_0003_new_project_from_foundation_index_empty_verification_record, tooling_derive_verification_record, docs_specs_root_0003_new_project_from_foundation_index_init_write_set, docs_specs_root_0003_new_project_from_foundation_index_repository_states_foundation_derived_mixed [EXTRACTED 1.00]
- **One planning path: a scope row first, then a spec before code, named by the agent instructions, the development rules and the repository structure** — docs_specs_root_0002_one_planning_path_decision_scope_row_then_spec, docs_specs_root_0002_one_planning_path_canonical_planning_pattern, docs_rules_development_rules_scope_row_then_spec, agents_scope_row_and_spec_before_code, docs_scope_root_007_one_planning_path, docs_scope_index, docs_architecture_repository_structure_docs_record_homes, docs_specs_root_0001_ownership_development_rules_r10_scope_row_and_spec_for_capability_spec_for_material_decision [EXTRACTED 1.00]
- **Coordination records of scope 009: the log, the general brief rules and the manual steps list, all tied to the scope row** — docs_scope_coordination_009_a_new_project_from_the_foundation_log, docs_scope_coordination_009_a_new_project_from_the_foundation_brief_umum, docs_scope_coordination_009_a_new_project_from_the_foundation_manual, docs_scope_root_009_a_new_project_from_the_foundation [EXTRACTED 1.00]
- **Wave 1 ownership split: developer on the verification record, checker on the verify.md ticks, tester on the derivation tests, with no overlap** — docs_scope_coordination_009_a_new_project_from_the_foundation_log_dev_f009_m3, docs_scope_coordination_009_a_new_project_from_the_foundation_log_chk_f009_verify, docs_scope_coordination_009_a_new_project_from_the_foundation_log_tst_f009_test, docs_quality_verification, docs_specs_root_0003_new_project_from_foundation_verify, tooling_derive_test_init_project, docs_scope_coordination_009_a_new_project_from_the_foundation_log_parallel_start [EXTRACTED 1.00]
- **Box list of scope 010: Design it, Build it with three milestones, Verify it and Test it, all ticked** — docs_scope_root_010_schemas_free_of_sample_names_design_it, docs_scope_root_010_schemas_free_of_sample_names_build_it, docs_scope_root_010_schemas_free_of_sample_names_milestone_1_one_key_rule_and_heading_role, docs_scope_root_010_schemas_free_of_sample_names_milestone_2_generator_tests_on_own_sources, docs_scope_root_010_schemas_free_of_sample_names_milestone_3_document_updates_and_verification_record, docs_scope_root_010_schemas_free_of_sample_names_verify_it, docs_scope_root_010_schemas_free_of_sample_names_test_it [EXTRACTED 1.00]
- **Spec triggers kept in their owner files: when a smaller change needs a spec** — docs_specs_root_0002_one_planning_path_trigger_owner_files, docs_rules_development_rules_spec_triggers_for_smaller_changes, docs_rules_service_rules_spec_for_new_crate_or_boundary, docs_quality_architecture_compliance_spec_for_architecture_change, docs_architecture_dependency_rules_new_edge_proposal, docs_contracts_ffi_conventions_compatibility_versioning, docs_decisions_adr_0001_foundation_revisit_conditions, docs_specs_root_0001_ownership_development_rules_spec_triggers [EXTRACTED 1.00]
- **Proof that derivation still works: --check state test, derivation unit test on a temporary copy in scripts/test.sh, CI identity comparison in both native jobs, manual workflow run with derived set** — docs_specs_root_0003_new_project_from_foundation_index_check_form, docs_specs_root_0003_new_project_from_foundation_index_test_form, docs_specs_root_0003_new_project_from_foundation_index_derivation_test, docs_specs_root_0003_new_project_from_foundation_index_ci_identity_comparison, docs_specs_root_0003_new_project_from_foundation_index_workflow_derived_input, scripts_test, github_workflows_foundation, github_workflows_foundation_derived_input, github_workflows_foundation_derive_sample_product_step, github_workflows_foundation_ios_identity_comparison_step, github_workflows_foundation_android_identity_comparison_step [INFERRED 0.85]
- **Design token pipeline from canonical JSON to native projections** — docs_design_system_token_conventions_canonical_token_sources, design_system_schemas_tokens_schema, scripts_generate_design_tokens, docs_design_system_platform_mapping_swiftui_token_projection, docs_design_system_platform_mapping_compose_token_projection, docs_quality_architecture_compliance_tokens_config_localization_check [INFERRED 0.85]
- **Generator tests on their own sources: the fixture tree, the nine tests, the --test form and the invariants that keep them independent of a product's catalog and tokens** — docs_specs_root_0004_schemas_free_of_sample_names_index_fixture_source_tree, docs_specs_root_0004_schemas_free_of_sample_names_index_nine_generator_tests, docs_specs_root_0004_schemas_free_of_sample_names_index_test_form, docs_specs_root_0004_schemas_free_of_sample_names_index_test_module_names, docs_specs_root_0004_schemas_free_of_sample_names_index_invariant_tests_read_fixture_only, docs_specs_root_0004_schemas_free_of_sample_names_index_invariant_fixture_satisfies_schemas, docs_specs_root_0004_schemas_free_of_sample_names_index_test_sources_without_a_sample_name_generate_and_check, docs_specs_root_0004_schemas_free_of_sample_names_index_ac_5, docs_specs_root_0004_schemas_free_of_sample_names_index_ac_6, tooling_codegen_test_generation [INFERRED 0.85]
- **Neutral JSON sources validated and generated into native theme and string resources** — design_system_readme_token_files, design_system_readme_tokens_schema, shared_config_readme_foundation_json, shared_localization_readme_catalog_format, design_system_readme_generate_design_tokens_modes, tooling_codegen_requirements_fastjsonschema, design_system_readme_generated_semantic_api, shared_localization_readme_generated_native_strings [INFERRED 0.85]
- **Regenerate derived outputs with their canonical source, never hand-edit** — docs_rules_development_rules_regenerate_derived_files, docs_rules_design_system_rules_regenerate_projections, docs_quality_architecture_compliance_generated_drift_remediation, docs_rules_rust_rules_regenerate_after_signature_change, docs_rules_shared_resources_rules_generated_native_strings, docs_rules_anti_duplication_ffi_shapes_in_rust_export [INFERRED 0.85]
- **Manual step flow: a sub-session reports a manual step, the lead lists it, the user runs it and the checker ticks verify.md from the result** — docs_scope_coordination_009_a_new_project_from_the_foundation_brief_umum_manual_steps_rule, docs_scope_coordination_009_a_new_project_from_the_foundation_manual, docs_scope_coordination_009_a_new_project_from_the_foundation_manual_summary, docs_scope_coordination_009_a_new_project_from_the_foundation_manual_result_routing, docs_scope_coordination_009_a_new_project_from_the_foundation_log_chk_f009_verify, docs_specs_root_0003_new_project_from_foundation_verify, docs_scope_coordination_009_a_new_project_from_the_foundation_manual_f009_1, docs_scope_coordination_009_a_new_project_from_the_foundation_manual_f009_2 [INFERRED 0.85]
- **Tracer bullet greeting path from shared core to both native screens** — docs_scope_index_tracer_bullet_build_approach, docs_scope_root_002_shared_greeting_contract, docs_scope_root_002_shared_greeting_contract_one_string_in_one_string_out_contract, docs_scope_ios_001_native_ios_greeting, docs_scope_android_001_native_android_greeting, docs_scope_root_006_hosted_build_verification [INFERRED 0.85]
- **Verification evidence chain: local checks, hosted jobs and the verification record** — docs_scope_root_005_reproducible_local_builds_and_checks, docs_scope_root_006_hosted_build_verification, docs_scope_root_008_hosted_results_in_the_verification_record, docs_scope_root_008_hosted_results_in_the_verification_record_single_list_of_unverified_targets [INFERRED 0.85]
- **Coordination templates (brief, general rules, log, manual, report) and the scope 009 records filled from them** — claude_skills_coordinate_templates_brief, claude_skills_coordinate_templates_brief_umum, claude_skills_coordinate_templates_log, claude_skills_coordinate_templates_manual, claude_skills_coordinate_templates_report, docs_scope_coordination_009_a_new_project_from_the_foundation_brief_umum, docs_scope_coordination_009_a_new_project_from_the_foundation_log, docs_scope_coordination_009_a_new_project_from_the_foundation_manual [INFERRED 0.95]
- **Documents that follow spec 0004 (AC-7): the typographyHeading mapping, the required roles and naming rule, the README rule that the schema names no key, the checks row naming the fixture tree, and the two verification record rows** — docs_specs_root_0004_schemas_free_of_sample_names_index_ac_7, docs_design_system_platform_mapping_typographyheading, docs_design_system_token_conventions_required_roles_and_naming_rule, shared_localization_readme_schema_names_no_key, docs_quality_architecture_compliance_tokens_config_localization_check, docs_quality_verification_design_system_and_resources_result, docs_quality_verification_schemas_free_of_sample_names_result [INFERRED 0.95]
- **Derived hosted run 43701289339 as evidence for AC-10: the workflow input, the derive step and both identity comparisons ran on hosted runners** — docs_quality_verification_hosted_run_43701289339, docs_quality_verification_derived_hosted_foundation_job_result, docs_quality_verification_derived_hosted_ios_job_result, docs_quality_verification_derived_hosted_android_job_result, github_workflows_foundation_derived_input, github_workflows_foundation_derive_sample_product_step, github_workflows_foundation_ios_identity_comparison_step, github_workflows_foundation_android_identity_comparison_step, docs_specs_root_0003_new_project_from_foundation_index_ac_10, docs_scope_coordination_009_a_new_project_from_the_foundation_log_hosted_run_43701289339 [INFERRED 0.95]

## Communities (59 total, 1 thin omitted)

### Community 0 - "Verification Record, CI Workflow and Policy Checks"
Cohesion: 0.08
Nodes (67): GreetingTest, GreetingUITests, Pass representative values through both generated languages, Android linkage and UI check (Linux CI job, emulator instrumentation), GitHub Actions CI jobs (macOS and Linux), iOS linkage and UI check (macOS CI job, XCTest), Rust format and lint check (rustfmt, Clippy warnings denied), Foundation verification 2026-11-15 (+59 more)

### Community 1 - "Swift UniFFI Bindings"
Cohesion: 0.05
Nodes (64): Array, createReader(), createWriter(), Data, FfiConverter, FfiConverterPrimitive, FfiConverterRustBuffer, FfiConverterString (+56 more)

### Community 2 - "Coordinate Skill"
Cohesion: 0.05
Nodes (90): Agent workflow: before commit (run /graphify . --update, stage graphify-out with the change), Knowledge graph (graphify-out/, kept current with /graphify . --update), Role architect: closes a (spec) box or updates a spec so a developer can build without asking again; owns the feature's docs/specs/<NNNN-slug>/ folder; all code and docs/scope are forbidden, Accept this spec? handoff: the architect never answers it itself; it sends the spec path, Decision, key tradeoff and decisions taken to the lead, ends the turn with STATUS: needs-decision and continues after accept, Proposed scope block (blok scope usulan): Pointer line, Design it ticked, Build it with 2 to 5 nested milestones naming Build plan tasks and ACs, and closing boxes by tier, reported for the lead to paste into the scope, Role checker: two modes set by the brief, verify and review; ticks only the verify.md steps it ran or writes a file in docs/reviews; never fixes what it finds, Checker review mode: senior code review of a GA feature with fresh eyes, ranked findings in docs/reviews; only in a new session that has not written, verified or discussed the implementation, Checker verify mode: proves a milestone or feature behaves per spec by running the verify.md steps, scoped to the milestone section and the AC IDs in the brief, and sends failures to the owning developer (+82 more)

### Community 3 - "Kotlin FFI Library Loading"
Cohesion: 0.06
Nodes (34): Disposable, NoHandle, UniffiByValue, UniffiCallbackInterfaceClone, UniffiCallbackInterfaceFree, UniffiForeignFutureCompleteF32, UniffiForeignFutureCompleteF64, UniffiForeignFutureCompleteI16 (+26 more)

### Community 4 - "Scope 009 Coordination Records"
Cohesion: 0.10
Nodes (36): General brief rules (Aturan umum brief) for the sub-sessions of the scope 009 coordination: the fixed part of every brief; the brief wins where it differs, Always forbidden for sub-sessions: docs/scope/, AGENTS.md, graphify-out/, spec content other than the Status line and the verify.md ticks (checker only), other specs, and files outside the brief's allowed list, Commit rule for sub-sessions: one commit per step, an imperative English subject without prefix like the repository history, plus the Co-Authored-By trailer, Disk rule: 32 GiB free at the start; only the checker runs full native builds, one at a time; below 10 GiB free stop and report blocked; remove target/, build/ and apps/android/**/build and the temporary clone before reporting done, Lead address: Mobile Foundation Scaffold [f5cda4]; full reports, questions and needs-decision go there through SendMessage, Manual steps rule: GUI apps, GitHub web pages, physical devices, signing, installing tools, repository settings, push and triggering or repeating workflows are done only by the user or the lead; gh is read-only; headless simulators and emulators are allowed; a failed or flaky step is reported failed, not manual, Process rule: stop only the processes, simulators and emulators you started, name them F009-<session> and delete them afterwards; suites longer than 10 minutes run detached with nohup, Report rule: one final report per item through SendMessage following the coordinate skill's report template; done is valid only when everything is committed, the working tree is clean and the last git merge main was run; the first line is STATUS (+28 more)

### Community 5 - "Kotlin UniFFI Library Calls"
Cohesion: 0.06
Nodes (3): UniffiLib, UniffiRustCallStatus, UniffiRustFutureContinuationCallback

### Community 6 - "Planning Path and Spec 0002"
Cohesion: 0.10
Nodes (54): Plan a new capability in the scope and write its spec under docs/specs before code, Development rules, Capability spec checklist: user outcome, scope, acceptance criteria, existing owner, public contract, dependency direction, platform specific work, verification matrix, Progress is recorded in the scope row; what ran is recorded in the verification record, /scope and /architect: the usual commands for writing the scope row and the spec, Plan a new capability as a scope row (the brief), then write a spec under docs/specs before code, Smallest slice exercisable through its real caller, Mobile foundation scope (index) (+46 more)

### Community 7 - "Spec 0001 Ownership Decision and Forces"
Cohesion: 0.19
Nodes (22): Single greeting as the minimal exercise of interop, linking, resources and display, Spec 0001: One owner per responsibility, with rules kept beside the code, Automate only what a machine can judge, Decision: one owner per responsibility in an ownership matrix, topic-sized rule files, short AGENTS.md entry point, automated checks only where a machine is reliable, An exact dependency list, not a deny list, Follow-up: decide whether checks must pass before a change reaches main (branch rule or local hook), Follow-up: confirm or correct the inferred rationale, Follow-up: record reviewers per owner (CODEOWNERS) when a second contributor joins (+14 more)

### Community 8 - "Rust Rules and Bridge Hygiene"
Cohesion: 0.38
Nodes (10): Mobile contract (FFI conventions), UniFFI generated files drift check, ABI generation result (UniFFI 0.31.2, identical regenerated tree), FFI shapes change in the annotated Rust export, Rust rules, Regenerate both languages and run both apps after a signature or UniFFI upgrade, Thin FFI exports with public contract tests, R17: bridge hygiene (bindings match the library revision, no raw pointers, no hand-maintained C declarations) (+2 more)

### Community 9 - "Derivation Command"
Cohesion: 0.12
Nodes (30): Exception, check(), derive(), foundation_ref(), foundation_url(), git(), identity_text(), in_git() (+22 more)

### Community 10 - "Derivation Refusal and Write Set Tests"
Cohesion: 0.09
Nodes (12): OutsideGitTests, AC-7: a local path remote, or no remote, is no usable foundation URL., AC-7: each input that breaks its rule is refused with exit 2, one line and no…, AC-7: a remote URL that is not UTF-8 is no usable foundation URL., AC-7: a derived checkout is refused., AC-7: each name outside the rule is refused on its own, with exit 2, one line…, AC-7: each application ID outside the rule of its flag is refused on its own., AC-7: each version, date, foundation URL and ref outside its rule is refused on… (+4 more)

### Community 11 - "Derivation Run and Origin Line Tests"
Cohesion: 0.11
Nodes (12): AC-3, AC-5, AC-6, AC-8: the happy path writes every file and the checkout then…, AC-3: each override reaches only its own identity file, and --version reaches…, AC-3: with one override the other platform keeps --app-id., AC-3, AC-7: a value that starts with a hyphen is refused, and its equals form…, AC-6: without the flags the origin line takes the remote, HEAD and today., AC-6: the foundation remote wins over origin, and the highest release tag wins., AC-3: the example of the criterion, with no other flag, writes 0.1.0 and build…, AC-5, AC-6: the remote's user and token are dropped before the URL is written… (+4 more)

### Community 12 - "Development Rules and Spec Triggers"
Cohesion: 0.38
Nodes (16): Dependency rules, New dependency edge needs an owning module, a use case and a test, Generators consume neutral sources and never recover canonical values from native output, Compatibility: version breaking contracts and coordinate regeneration, both apps and release, ADR 0001: Native apps with a shared Rust core, Decision: keep generated source snapshots in version control and compare against fresh regeneration, Revisit conditions: dependency direction change, async native boundary, independently versioned clients, new shared crate or service, Architecture compliance (+8 more)

### Community 13 - "Resource Generator"
Cohesion: 0.06
Nodes (46): FoundationTokens, Palette, CGFloat, Color, ColorScheme, Design system guide, generate-design-tokens.sh modes: write, --check (drift), --test (failure cases), Generated semantic token API consumed by native apps (+38 more)

### Community 14 - "Kotlin RustBuffer Handling"
Cohesion: 0.14
Nodes (9): ByReference, ByValue, ForeignBytes, `hello`(), RustBuffer, uniffiTraitInterfaceCall(), uniffiTraitInterfaceCallWithError(), kotlin (+1 more)

### Community 15 - "Shared Settings, Localization and Config Schema"
Cohesion: 0.06
Nodes (51): Build-time generation: token JSON and locale JSON -> native theme inputs and localization resources, Stable role names or same-change migration, Design system rules, Public role name changes require migrating both consumers, Draft 7 schema and native mappings updated together, Shared visual values live in design-system/tokens, Shared resource ownership rules, Draft 7 schemas in shared/specifications (+43 more)

### Community 16 - "Architecture Check and Planning Rules"
Cohesion: 0.19
Nodes (19): Cargo dependency and governance check, Architecture policy result (dependency and required-document checks), Specs are numbered NNNN-kebab-title.md in the folder mirroring the scope workspace; a replaced record is marked superseded; ADR 0001 stays the founding record, Deferred: a contract beyond one string (record, typed error, async call), Scope status legend and file numbering convention, 007 - One planning path (done), Required document check covers the scope index, Follow-up (settled by spec 0002): record keeping (ADR and plan naming, REQUIRED_DOCS membership, superseding, whether a spec satisfies R10) (+11 more)

### Community 17 - "Derivation Test Checkout Fixture"
Cohesion: 0.16
Nodes (9): Checkout, AC-7: a modified or untracked file is refused, even when git status hides…, AC-7: a mixed checkout is refused., AC-4: a checkout that has no graph changes only the two identity files,…, AC-6: a README.md of one line without a newline still ends with the title,…, AC-6: only a foundation-v tag that points exactly at HEAD names the ref;…, AC-7: a change only in the index, and a deleted tracked file, both make the…, AC-7: git status leaves ignored files out, so an ignored local file is no… (+1 more)

### Community 18 - "Ownership Matrix and Repository Structure"
Cohesion: 0.14
Nodes (35): Agent workflow: before editing (locate owner, contract, callers, tests), App trees do not import one another; core never calls platform UI, Workspace edge: mobile-ffi depends on foundation-core (std-only core), Proc-macro exports define the cross-language API; bindgen feature gates host CLI deps, Architecture overview, foundation_core::hello (sole greeting formatter), Greeting call flow: SwiftUI/Compose -> generated binding -> C ABI/JNA -> mobile-ffi -> foundation-core, Color selection, font scaling, layout and accessibility run natively (no shared renderer) (+27 more)

### Community 19 - "Init Command and Identity Files"
Cohesion: 0.15
Nodes (21): Project identity state check (init-project.sh --check and --test, CI identity comparison), Product identity result (2026-11-15: test.sh passed with --check printing foundation and --test passing 21 unit tests; both apps carried dev.foundation.mobile, Mobile Foundation, 0.1.0, build 1; a copy derived as Zoë's Proof built and matched its identity file), Derivation only on a copy: init-project.sh with --name rewrites README.md and the verification record and removes graphify-out/, so that form runs only in a temporary clone in the session scratchpad; --check and --test are safe in the worktree, Done when (009): one recorded decision, one command, a hosted check on a temporary copy, clean inherited records, recorded foundation revision, AC-9: init-project.sh --test runs the unit tests including the derivation on a temporary copy; scripts/test.sh runs it so the foundation CI job proves the command on every push, init-project.sh --check: prints foundation or derived (exit 0) or names each mismatch in a mixed state (exit 1), Derivation test: copies the files git lists to a temporary folder, runs the copy's own command with sample values, requires --check to print derived and check-architecture.py to pass, then removes the copy, Foundation ref resolution: --foundation-ref, else the highest foundation-v* tag exactly at HEAD, else the full HEAD commit ID (+13 more)

### Community 20 - "Spec 0003 Decision History"
Cohesion: 0.12
Nodes (35): Decision: a product is a clone that changes only its display name, application ID and version through scripts/init-project.sh, keeps every other name, starts with an empty verification record and merges foundation-v tags, Follow-up: build the command that takes a foundation release (fetch, merge, apply the ownership table) when the first release is merged into a product, Follow-up: decide where dependency update bots run (a bot in every product changes foundation owned files and will conflict with merges), Neutral: /develop moves the spec to In Progress and Accepted with scope row 009; creating the first tag foundation-v0.1.0 is the maintainer's step, Path ownership after derivation: product owned paths keep the product's side, foundation owned paths take the foundation's side, shared paths merge by hand, README section 'Start a project from this foundation': clone at a tag, create a branch, rename the remote, run the command, add origin, rebuild the graph, mark inherited rows existing, commit, record first results, Release the foundation: run the workflow by hand with derived set, then push an annotated foundation-vMAJOR.MINOR.PATCH tag on main, Take a later foundation release: git fetch foundation --tags, git merge foundation-vX.Y.Z, keep the product's side on product owned paths, rebuild the graph, run every check (+27 more)

### Community 21 - "Spec 0003 Path Ownership and Kept Names"
Cohesion: 0.10
Nodes (31): Checker note, not a blocker: the iOS icon caption reads MobileFoundation without a space although CFBundleDisplayName is Mobile Foundation; SpringBoard shortens long names (Acme Notes shows its space); a spaced caption needs a shorter name, which is a product decision, The two apps disagree on their own identity (iOS dev.foundation.mobile / Mobile Foundation / 1.0, Android foundation.mobile / Foundation / 0.1.0), Spec 0003: A new project from the foundation: product identity in two files, one init command, updates by merge (Accepted), AC-7: the command refuses, changes nothing and exits 2 with a one line reason (bad input, default ID, dirty tree, derived or mixed checkout, missing foundation URL or ref), Default foundation identity: dev.foundation.mobile, Mobile Foundation, version 0.1.0, build 1, Follow-up: decide in the release path spec whether the iOS and Android versions must match, and add that test to --check if they must, Follow-up: allow a localized display name when a product needs one (it would move from the identity files to the catalogs), Follow-up: record where /graphify and /scope come from, with a way to do each step by hand (+23 more)

### Community 22 - "Kotlin FFI Converters"
Cohesion: 0.21
Nodes (7): FfiConverter, FfiConverterRustBuffer, FfiConverterString, FfiType, ByteBuffer, KotlinType, ULong

### Community 23 - "Scope 010 Coordination Records"
Cohesion: 0.11
Nodes (62): Android scope, Android app owns its screen, appearance changes and native localization lookup, Scope 010 specifics: main at start = 7b6ca4f, equal to origin/main; one feature with one open box, Design it (spec); spec number 0004; source is the spec 0003 Follow-up on greeting_recipient and the greeting role; Beta flow closes with Verify it and Test it; one developer until the lead splits ownership, Coordination log (Log koordinasi) for scope 010 - Schemas free of sample names (wave 1 finished 2026-11-15, no active wave, decision mode auto, start hash 7b6ca4f, updated 2026-11-15 21:25), Sub-session arc-f010-spec (architect, fable-5-2 high, archived): scope 010 Design it (spec), spec 0004; owns docs/specs/_root/0004-schemas-free-of-sample-names/ plus one Follow-up line in the spec 0003 index.md; branch claude/arc-f010-spec-6c76d1, Decision (lead): checker and tester started together from the developer branch (git merge claude/dev-f010-m1-6599c9 in each worktree), before the build merge was committed, Sub-session chk-f010-verify (checker verify, fable-5-2 high, archived): scope 010 full verify of AC-1 to AC-7 from the developer branch, closing the three milestones, Build it and Verify it; owns the verify.md ticks of spec 0004; branch claude/chk-f010-verify-59dbd8, Closing (Penutupan) of the scope 010 coordination: every green branch merged on 2026-11-15 (arc-f010-spec in 7c906fb, dev-f010-m1 in 8c8caf8, tst-f010-test and chk-f010-verify in b64055a), no Document step, closing commit b64055a, nothing kept, no blocker left (+54 more)

### Community 24 - "Empty Verification Record"
Cohesion: 0.24
Nodes (10): A new product would carry the foundation's verification record, scope rows, hosted run links and knowledge graph as its own, AC-5: the verification record becomes the empty record naming the product, foundation URL and revision, with every target unverified, Empty verification record: names the product, foundation URL and ref, lists every target as still unverified, holds no hosted run link, User stories: one command names a clone, foundation releases arrive by merge, the verification record lists only what ran here, every push proves the command still works, Force: a copy inherits claims it never earned (the verification record and the scope index name a hosted run in the foundation repository), Force: the knowledge graph is tied to this checkout (74 tracked cache files under a path-named folder, one owner specific string), tooling/derive/verification-record.md (empty verification record template for a derived product), Nothing has run in the derived repository yet; the foundation's own results live in the foundation repository and are not results for the project (+2 more)

### Community 25 - "Spec 0004 Rationale and Token Schema"
Cohesion: 0.17
Nodes (29): Canonical token schema (tokens.schema.json), Delegated decision (spec 0004, AC-2, not heavy, in force): the token schema keeps required typography roles, required: ["heading", "body"]; runner-up no required role (minProperties); undo via architect (update) of spec 0004, rebuilding Build plan step 2, Reconciliation (lead): git branch --no-merged main is empty, there is no other worktree, and none of the 32 peer sessions works in this repo; nothing was done outside the coordination; no feature 010 artifact is on main yet, both schemas still name the sample names, Foundation schemas require sample names: the greeting_recipient key in the localization schema and the greeting typography role in the token schema, Decision: Option 1, fix the two schemas in place (one key of any name through minProperties), rename the required typography role greeting to heading in one change across the source, both generated files and three readers, and give the generator tests their own source tree, Follow-up: decide whether the token schema should require fewer roles once a product shows which ones it does not use, Tradeoff: the token schema still requires seventeen role names; a product that wants no heading or no feedback role still has to keep it, since this spec removes the sample name, not the idea of required roles, Spec 0004 rationale: decision history of the schemas free of sample names spec (context, options considered, rationale) (+21 more)

### Community 26 - "Generator Tests and Fixture Sources"
Cohesion: 0.10
Nodes (42): Tokens, configuration and localization check (generate-design-tokens.sh --check validates canonical data and compares native outputs; --test runs failure and regeneration cases on the tests' own source tree tooling/codegen/fixtures/sources/), Design system and resources result (nine generator tests, which read tooling/codegen/fixtures/sources/ and not the checkout's own sources), Schemas free of sample names result (2026-11-15: test.sh passed with nine generator tests on Python 3.9.6 and --check passed; both apps built and passed the greeting tests in light and dark after the rename to typographyHeading; a scratch clone with the single key welcome_title generated, checked and tested), Sample removal only on a copy: proof that the catalog and token set pass without the greeting names runs on test fixtures or a temporary scratchpad clone, never by leaving the worktree with the samples deleted; scripts/init-project.sh --name only in a temporary clone, --check and --test are safe, Delegated decision (spec 0004, AC-6, not heavy, in force): Done when clause (4) is proven by a unit test on the fixture plus a temporary clone step with the real script; runner-up a --root generator flag with stored output; undo via architect (update) of spec 0004, rebuilding Build plan steps 3 and 5, Build plan steps finished by dev-f010-m1: 1, 2, 3, 4 and 5 in commits 6b92beb, 861bc7d, eba5c48, efb0a6c and db8fe2f; 6efe3c4 moves the spec Status line and e874293 adds verify.md; code pointers: design-system/, shared/specifications/, tooling/codegen/, Decision (lead): the spec, verify.md and the verification record say 'nine generator tests', so the tester is asked to close AC gaps by strengthening the nine existing tests; a new test function only if there is no other way, with the new count reported to the lead, Ticked in wave 1: 010 Test it, from the tst-f010-test report done (9 tests before and after; AC-1, AC-2, AC-3, AC-5 and AC-6 locked through subTest and exact error messages; five mutations, each in its own clone, were caught; commits 87ec624, 1c67e0d, 16b8e60); branch merged in b64055a (+34 more)

### Community 27 - "Shared Greeting Contract and FFI Export"
Cohesion: 0.39
Nodes (7): hello(), String, 002 - Shared greeting contract (done), Generated bindings (code that carries values between languages), One string in, one string out greeting contract, Neither app screen has shown a Unicode name, Unicode round trip through both generated bindings (Android emulator, iOS host executable)

### Community 28 - "Contract Extension Conventions"
Cohesion: 0.47
Nodes (6): Explicit application records and enums; private core/transport shapes mapped at the adapter, Async and cancellation conventions for future exports, Conventions for extending the mobile contract, Native capability callback interfaces limited to operations the core requires, Typed UniFFI errors with stable variants; user-facing messages translated natively, Records, typed errors, async calls and native callbacks have no caller or test yet

### Community 29 - "Real Checkout and Outside Git Tests"
Cohesion: 0.33
Nodes (4): AC-9: the derivation proof is skipped, with its reason, in a checkout that is…, Run the checked in command on a temporary copy of this checkout. The checkout…, AC-9: the copy's own command derives the copy, which then reads derived and…, RealCheckoutTests

### Community 30 - "Android App Shell"
Cohesion: 0.60
Nodes (3): MainActivity, Bundle, ComponentActivity

### Community 31 - "Rust Core and Greeting Contract"
Cohesion: 0.22
Nodes (10): hello(), preserves_empty_names_and_whitespace(), String, tests/contracts: Cargo integration tests for exported behavior, Core and FFI contract tests (locked Cargo tests), Shared computations and validation belong in the core, Greeting accepts the caller's complete Unicode string, Shared algorithms implemented in crates/core (+2 more)

### Community 32 - "Platform Rules and Agent Workflow"
Cohesion: 0.14
Nodes (22): AGENTS.md: Working in the mobile foundation, Agent workflow: before handoff (run checks, report commands and unverified targets), Agent workflow: during implementation (place change in owning layer), target/, build/ and Gradle build directories excluded from source control, Android rules, Checked-in Gradle wrapper, Compose presentation with native Material semantics, New ABI requires Rust cross-build and runtime test (+14 more)

### Community 33 - "Scope 010 Build, Verify and Verification Matrix"
Cohesion: 0.24
Nodes (15): Verification before reporting: scripts/test.sh must exit 0; build-ios.sh simulator, device and test in light and dark when apps/ios/ changed; build-android.sh assemble and connectedDebugAndroidTest in both night modes when apps/android/ changed; git status clean and the diff against main limited to ownership files, Disk rule: 22 GiB free at the start; one full native build at a time (the developer for the platform it touches, then the checker); the tester builds only if the brief asks; run df -g . first; below 10 GiB free stop and report blocked; remove target/, build/ and scratchpad clones before done, Verification before reporting: scripts/test.sh must exit 0; if apps/ios/ changed run scripts/build-ios.sh simulator, device and test light and dark; if apps/android/ changed run scripts/build-android.sh assemble and connected tests in both night modes; git status clean, diff only ownership files, Checker note, not a blocker: verify.md does not ask for --rerun-tasks for the second night mode on Android as the hosted workflow does; without that flag the test task still ran again (Starting 2 tests, new timestamp), Disk note: free disk fell from 26 to 15 GiB during verify and rose again to 25 GiB, Decision (lead): the lead gate for the developer branch on main is scripts/test.sh and scripts/generate-design-tokens.sh --check; the native builds of both platforms, which the gate asks for when apps/ changed, are proven by the checker on the same tree; the milestones are ticked only after the checker reports done, Decision (lead, carried over from the scope 009 log): the lead gate on main after a merge is no conflict markers, scripts/test.sh exits 0, and a native build per platform when apps/ changed, Decision (lead, carried over from the scope 009 log): the 4-session limit is counted per coordination; busy sessions of other projects on the same Mac (tablet, desktop, pool, Stackly) are not counted; 22 GiB free disk limits native builds to one session at a time (+7 more)

### Community 34 - "Token Conventions and Native Token Mapping"
Cohesion: 0.14
Nodes (30): System text scaling via generated text styles, Native token mapping, Compose sp mapping of logical text units, Jetpack Compose token projection (FoundationTokens), Dynamic Type mapping of headline and reading scales, Logical spacing units adapt to display density, spacingPage role, SwiftUI token projection (FoundationTokens) (+22 more)

### Community 35 - "Native Greeting and Supported OS Scopes"
Cohesion: 0.14
Nodes (22): CoreImage, Android 001 - Native Android greeting (existing), API 36 emulator results (arm64 local, x86_64 hosted) in light and dark, Android app packages both supported CPU architectures, Android physical device coverage unverified, Android 002 - Lowest supported Android and large text (planned), 16 KiB memory page packaging, Declared Android minimum API 24 not yet exercised (+14 more)

### Community 36 - "Greeting Screens and iOS App Shell"
Cohesion: 0.13
Nodes (14): App, MobileFoundationApp, .body, GreetingScreen, .body, String, Per-target reading order and screen-reader review, Native components guidelines (+6 more)

### Community 37 - "Kotlin Rust Call Status"
Cohesion: 0.23
Nodes (7): E, uniffiCheckCallStatus(), UniffiForeignFutureCompleteVoid, uniffiRustCall(), UniffiRustCallStatusErrorHandler, uniffiRustCallWithError(), U

### Community 38 - "Identity Value Sourcing"
Cohesion: 0.12
Nodes (43): apps/android/app/src/main/AndroidManifest.xml, apps/android/app/src/main/res/values/app.xml (the app_name string leaves this file; the label comes from the appLabel manifest placeholder), apps/android/identity.properties (Android identity file: applicationId, displayName, versionName, versionCode), apps/ios/Config/App.xcconfig (iOS app build settings), apps/ios/Config/Identity.xcconfig (iOS identity file: APP_BUNDLE_IDENTIFIER, APP_DISPLAY_NAME, MARKETING_VERSION, CURRENT_PROJECT_VERSION), apps/ios/Config/Project.xcconfig (iOS project build settings), apps/ios/MobileFoundation.xcodeproj/project.pbxproj (Xcode project file), Product identity (display name, application IDs, app version): owned by apps/ios/Config/Identity.xcconfig and apps/android/identity.properties; consumed by the Xcode and Gradle builds and scripts/init-project.sh (+35 more)

### Community 39 - "Architecture Boundaries"
Cohesion: 0.24
Nodes (13): Architecture boundaries, Documented capability boundary; adapters need an actual caller, Layer: design system (generated Swift/Kotlin values as shared visual vocabulary), Layer: native platform integration (Swift owns Apple services, Kotlin owns Android services), Layer: native presentation (views render, adapt to appearance, handle events), Layer: resources and tooling (build-host validation and generation), Layer: shared Rust (core owns behavior, FFI crate maps exports), Create a platform adapter directory only when a feature needs an OS capability (+5 more)

### Community 40 - "Derivation State Check Tests"
Cohesion: 0.18
Nodes (5): AC-8: every departure from the exact form is a mismatch that names the file and…, AC-8: a derived checkout that lost one signal names that signal., AC-8: an identity file that is not UTF-8, and a missing README.md, are…, AC-8: changing only applicationId names that file and key against a foundation…, AC-8: default IDs under an origin line, and a second origin line, each make a…

### Community 41 - "UniFFI Generator on Host Tooling"
Cohesion: 0.50
Nodes (4): main(), Design definitions compile independently of Cargo and UniFFI, UniFFI generator feature restricted to host tooling, R14: the UniFFI generator feature (bindgen) stays on host tooling

### Community 42 - "Localization Schema One-Key Rule"
Cohesion: 0.21
Nodes (16): Delegated decision (spec 0004, AC-1, not heavy, in force): the 'at least one key' rule is "minProperties": 1 with no required and no properties; runner-up an empty catalog is allowed; undo via architect (update) of spec 0004, rebuilding Build plan step 1, Replace the greeting with a first feature without editing a foundation schema, AC-1: localization.schema.json holds "minProperties": 1 with no required and no properties member; an empty default catalog {} makes --check exit 1 with 'en.json: data must contain at least 1 properties'; any single key that fits the key pattern is accepted, Build plan step 1: in shared/specifications/localization.schema.json replace the line "required": ["greeting_recipient"], with "minProperties": 1, and run scripts/generate-design-tokens.sh --check (AC-1), One-key rule: the localization schema after the change is a Draft 7 object with minProperties 1, the key pattern ^[a-z][a-z0-9]*(_[a-z0-9]+)*$ and non-empty string values; it has no required member and names no key at all, Positive: a product replaces the greeting without editing design-system/schemas/, shared/specifications/ or tooling/; the generator tests pass in every product; the large text style fits any screen; an empty catalog is still refused; one more test proves sample-free sources on every push, User stories: a product maintainer replaces the greeting by editing only the catalog, token values and app sources; the foundation maintainer's generator tests pass whatever a product holds; a contributor gets a large text style named for its use, additionalProperties (+8 more)

### Community 43 - "Kotlin Handle Map and Lifting"
Cohesion: 0.42
Nodes (4): InternalException, T, UniffiHandleMap, UniffiNullRustCallStatusErrorHandler

### Community 44 - "Spec 0004 and Heading Role Rename"
Cohesion: 0.16
Nodes (26): FoundationTheme(), FoundationTokens, Palette, Delegated decisions (Keputusan delegasi) for scope 010: spec decisions taken from the recommended option on the user's behalf, heavy (berat) rows on top; nine rows for spec 0004, all in force, one heavy (the role name heading), Delegated decision (spec 0004, AC-4, not heavy, in force): the key greeting_recipient stays as sample content in the catalog and both apps, and the schema no longer names it; runner-up the neutral key recipient_name; undo via architect (update) of spec 0004, Build plan step 2 grows by 7 files, Delegated decision (spec 0004, AC-2 and AC-3, heavy, in force): the typography role replacing greeting is named heading; runner-up title; undo via architect (update) of spec 0004, rebuilding Build plan steps 2 and 3, the fixture content and the step 4 document texts, Delegated decision (spec 0004, AC-3, not heavy, in force): no alias for the old name typographyGreeting, one change; runner-up greeting kept for one release; undo via architect (update) of spec 0004, rebuilding Build plan step 2, Spec 0004: Schemas free of sample names: one key of any name, a heading role, generator tests on their own sources (Status: Accepted, 2026-11-15); removes the two sample names (greeting_recipient, the greeting role) that the foundation schemas still require (+18 more)

### Community 45 - "Regeneration and Drift Remediation"
Cohesion: 1.00
Nodes (3): Generated drift remediation, Regenerate native projections in the same change, Regenerate derived files alongside canonical inputs

### Community 47 - "Command Line Wrapper Tests"
Cohesion: 0.31
Nodes (5): CommandLineTests, Run the copied scripts/init-project.sh from another folder, as a person or CI…, AC-3, AC-8: the wrapper finds its own checkout, prints the five changed paths,…, AC-7: through the wrapper a refusal exits 2, prints one line on stderr only,…, AC-8: through the wrapper --check exits 1 and names the mismatch on stderr.

### Community 48 - "Rule Set R1 to R19 and Generated File Rules"
Cohesion: 0.12
Nodes (27): Never hand-edit generated files, GreetingScreen(), Derived file rule: change the canonical input and regenerate every output in the same review, Rejected alternative: implementing application behavior independently in both apps, Limits of CI checks, Reviewers trace changed behavior from owner into each client, Anti-duplication rules, Locate the owner before adding a constant, rule, DTO, translation or asset (+19 more)

### Community 49 - "Kotlin FFI Integrity Checks"
Cohesion: 0.60
Nodes (3): IntegrityCheckingUniffiLib, uniffiCheckApiChecksums(), uniffiCheckContractApiVersion()

### Community 51 - "Android Rust Build Script"
Cohesion: 0.40
Nodes (4): CARGO_TARGET_AARCH64_LINUX_ANDROID_LINKER, CARGO_TARGET_X86_64_LINUX_ANDROID_LINKER, PATH, build-android-rust.sh script

### Community 54 - "iOS Rust Build Script"
Cohesion: 0.50
Nodes (3): CARGO_TARGET_DIR, PATH, build-ios-rust.sh script

### Community 62 - "iOS Greeting UI Test Pixel Check"
Cohesion: 0.50
Nodes (3): UInt8, CIContext, XCUIScreenshot

### Community 63 - "Token Command and Spec 0004 API Surface"
Cohesion: 0.18
Nodes (15): Generated files rule: never hand-edit generator output; change the source (design-system/tokens/, design-system/schemas/, shared/localization/, shared/specifications/, tooling/codegen/), run scripts/generate-design-tokens.sh and the generators scripts/test.sh checks, commit output with its source, Delegated decision (spec 0004, AC-5, not heavy, in force): the generator tests read the fixture tree tooling/codegen/fixtures/sources/ (7 files); runner-up the tests keep reading the checkout sources generically; undo via architect (update) of spec 0004, rebuilding Build plan step 3, Tester note: the 'no file contains the word' parts of AC-2, AC-3 and AC-5 are deliberately not locked by a test and stay guarded by git grep in verify.md; exit code 1 of the shell wrapper for an empty catalog is not locked by a test either, only its message, AC-5: no test under tooling/codegen/ reads the checkout's design-system/tokens/, shared/config/ or shared/localization/; tests read tooling/codegen/fixtures/sources/ and the checkout's schemas; --test still passes with en.json and typography.json replaced by {}, API surface: the existing command scripts/generate-design-tokens.sh; its forms, flags and output paths do not change, and tooling/codegen/generate.py, tokens.py and resources.py are not edited, scripts/generate-design-tokens.sh --check: the same two rules; an empty catalog and a token set without heading are refused with the messages in AC-1 and AC-2; exit 0 clean, 1 invalid or drifted, Invariant: the fixture tree satisfies the schemas; when a schema gains a required name the fixture gains it in the same change, and a failing --test is the signal that it did not, Invariant: a generator test reads the fixture tree and the schemas, never the checkout's own catalog, configuration or tokens; --check is the one proof that the checkout's own sources are valid (+7 more)

### Community 68 - "Android Gradle Wrapper"
Cohesion: 0.83
Nodes (3): gradlew script, die(), warn()

### Community 70 - "Derivation Tests and Documented Paths"
Cohesion: 0.12
Nodes (9): DerivationTests, AC-4: git sees changes in exactly the documented paths, and no rename., AC-6, AC-7: every accepted remote form becomes https without credentials; the…, AC-7: the in git test compares folders, not path spellings., AC-4: a graph removal that fails names every changed path and the way back., AC-4: each file is replaced in the documented order, and graphify-out/ goes…, AC-5: the template on disk, filled with the sample values, is the empty record…, AC-7: letters from any script, digits 0 to 9, single spaces, periods, hyphens… (+1 more)

## Knowledge Gaps
- **68 isolated node(s):** `NoHandle`, `UniffiWithHandle`, `Explicit application records and enums; private core/transport shapes mapped at the adapter`, `additionalProperties`, `const` (+63 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Spec 0003: A new project from the foundation: product identity in two files, one init command, updates by merge (Accepted)` connect `Spec 0003 Path Ownership and Kept Names` to `Verification Record, CI Workflow and Policy Checks`, `Scope 009 Coordination Records`, `Identity Value Sourcing`, `Spec 0001 Ownership Decision and Forces`, `Planning Path and Spec 0002`, `Localization Schema One-Key Rule`, `Development Rules and Spec Triggers`, `Spec 0004 and Heading Role Rename`, `Shared Settings, Localization and Config Schema`, `Rule Set R1 to R19 and Generated File Rules`, `Architecture Check and Planning Rules`, `Ownership Matrix and Repository Structure`, `Init Command and Identity Files`, `Spec 0003 Decision History`, `Scope 010 Coordination Records`, `Empty Verification Record`, `Spec 0004 Rationale and Token Schema`?**
  _High betweenness centrality (0.098) - this node is a cross-community bridge._
- **Why does `DerivationTests` connect `Derivation Tests and Documented Paths` to `Derivation State Check Tests`, `Derivation Refusal and Write Set Tests`, `Derivation Run and Origin Line Tests`, `Derivation Test Checkout Fixture`, `Init Command and Identity Files`, `Derivation Write Failure Tests`, `Real Checkout and Outside Git Tests`?**
  _High betweenness centrality (0.092) - this node is a cross-community bridge._
- **Why does `GreetingScreen` connect `Greeting Screens and iOS App Shell` to `Rule Set R1 to R19 and Generated File Rules`, `Platform Rules and Agent Workflow`, `Spec 0004 and Heading Role Rename`?**
  _High betweenness centrality (0.077) - this node is a cross-community bridge._
- **Are the 6 inferred relationships involving `Spec 0004: Schemas free of sample names: one key of any name, a heading role, generator tests on their own sources (Status: Accepted, 2026-11-15); removes the two sample names (greeting_recipient, the greeting role) that the foundation schemas still require` (e.g. with `Schemas free of sample names result (2026-11-15: test.sh passed with nine generator tests on Python 3.9.6 and --check passed; both apps built and passed the greeting tests in light and dark after the rename to typographyHeading; a scratch clone with the single key welcome_title generated, checked and tested)` and `Design it (spec) (010): ticked; command /architect schemas free of sample names`) actually correct?**
  _`Spec 0004: Schemas free of sample names: one key of any name, a heading role, generator tests on their own sources (Status: Accepted, 2026-11-15); removes the two sample names (greeting_recipient, the greeting role) that the foundation schemas still require` has 6 INFERRED edges - model-reasoned connections that need verification._
- **Are the 5 inferred relationships involving `Foundation verification 2026-11-15` (e.g. with `Record separately what compiled and what ran` and `Sub-session dev-f010-m1 (developer, opus-5-5 medium, archived): scope 010 Build it, all three milestones, Build plan steps 1 to 5 of spec 0004, all finished; owns both schemas, typography.json, the generated token files, three app files, the codegen fixtures and tests, five documents and verify.md; branch claude/dev-f010-m1-6599c9`) actually correct?**
  _`Foundation verification 2026-11-15` has 5 INFERRED edges - model-reasoned connections that need verification._
- **What connects `NoHandle`, `UniffiWithHandle`, `Explicit application records and enums; private core/transport shapes mapped at the adapter` to the rest of the system?**
  _68 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Verification Record, CI Workflow and Policy Checks` be split into smaller, more focused modules?**
  _Cohesion score 0.0792838874680307 - nodes in this community are weakly interconnected._