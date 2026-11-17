# Graph Report - mobile  (2026-11-17)

## Corpus Check
- 113 files · ~58,726 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1326 nodes · 4091 edges · 57 communities (56 shown, 1 thin omitted)
- Extraction: 77% EXTRACTED · 23% INFERRED · 0% AMBIGUOUS · INFERRED: 933 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `1cb94819`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Foundation verification 2026-11-15
- mobile_ffi.swift
- Sub-session dev-f010-m1 (developer, opus-5-5 medium, archived): scope 010 Build it, all three milestones, Build plan steps 1 to 5 of spec 0004, all finished; owns both schemas, typography.json, the generated token files, three app files, the codegen fixtures and tests, five documents and verify.md; branch claude/dev-f010-m1-6599c9
- mobile_ffi.kt
- Coordination log (Log koordinasi) for scope 009 - A new project from the foundation (wave 1 finished, no active wave, decision mode auto, start hash 4a153fe, updated 2026-11-15 19:05)
- UniffiLib
- 0002. One planning path: a scope row first, then a spec
- Spec 0001: One owner per responsibility, with rules kept beside the code
- CI job: android (JDK 17, API 36 emulator, optional sample derivation, identity comparison, Kotlin binding + Compose UI)
- init_project.py
- .assert_refused
- .run_command
- Architecture compliance
- generate.py
- RustBuffer
- config.schema.json
- Mobile foundation scope (index)
- .git
- Ownership matrix
- apps/ios/Config/Identity.xcconfig (iOS identity file: APP_BUNDLE_IDENTIFIER, APP_DISPLAY_NAME, MARKETING_VERSION, CURRENT_PROJECT_VERSION)
- Spec 0003 rationale: decision history of the new project spec (context, options considered, rationale)
- Spec 0003: A new project from the foundation: product identity in two files, one init command, updates by merge (Accepted)
- FfiConverter
- Spec 0004: Schemas free of sample names: one key of any name, a heading role, generator tests on their own sources (Status: Accepted, 2026-11-15); removes the two sample names (greeting_recipient, the greeting role) that the foundation schemas still require
- 002 - Shared greeting contract (done)
- localization.schema.json
- test_generation.py
- 003 - Shared visual definitions (done)
- GreetingScreen
- test_init_project.py
- FoundationTokens
- R4: shared behavior lives in the core, the export stays thin, both clients stay on one contract
- AGENTS.md
- test.sh
- Native token mapping
- iOS 001 - Native iOS greeting (existing)
- README: Native mobile foundation
- uniffiCheckCallStatus
- DerivationTests
- Accessibility (design system)
- .assert_mixed
- ADR 0001 · Native apps with a shared Rust core
- InternalException
- Spec 0004 rationale: decision history of the schemas free of sample names spec (context, options considered, rationale)
- Shared resource ownership rules
- Path ownership after derivation: product owned paths keep the product's side, foundation owned paths take the foundation's side, shared paths merge by hand
- CommandLineTests
- IntegrityCheckingUniffiLib
- General brief rules (Aturan umum brief) for the sub-sessions of the scope 010 coordination: the fixed part of every brief; the brief the lead sends points to this file, and the brief wins where the two differ
- build-android-rust.sh
- .test_a_write_that_fails_leaves_the_later_files_and_no_temporary_file
- build-ios-rust.sh
- FoundationTokens
- generate-design-tokens.sh
- gradlew

## God Nodes (most connected - your core abstractions)
1. `Foundation verification 2026-11-15` - 76 edges
2. `Spec 0004: Schemas free of sample names: one key of any name, a heading role, generator tests on their own sources (Status: Accepted, 2026-11-15); removes the two sample names (greeting_recipient, the greeting role) that the foundation schemas still require` - 75 edges
3. `Spec 0003: A new project from the foundation: product identity in two files, one init command, updates by merge (Accepted)` - 66 edges
4. `Coordination log (Log koordinasi) for scope 010 - Schemas free of sample names (wave 1 finished 2026-11-15, no active wave, decision mode auto, start hash 7b6ca4f, updated 2026-11-15 21:25)` - 62 edges
5. `UniffiLib` - 54 edges
6. `Spec 0001: One owner per responsibility, with rules kept beside the code` - 49 edges
7. `DerivationTests` - 47 edges
8. `Sub-session dev-f010-m1 (developer, opus-5-5 medium, archived): scope 010 Build it, all three milestones, Build plan steps 1 to 5 of spec 0004, all finished; owns both schemas, typography.json, the generated token files, three app files, the codegen fixtures and tests, five documents and verify.md; branch claude/dev-f010-m1-6599c9` - 41 edges
9. `010 - Schemas free of sample names (done)` - 37 edges
10. `Mobile foundation scope (index)` - 36 edges

## Surprising Connections (you probably didn't know these)
- `Derived hosted run android job result (same derive command; Gradle 9.3.1 assembled the derived debug app; identity file and built app matched; two instrumentation tests passed with night mode off and on)` --references--> `GreetingTest`  [INFERRED]
  docs/quality/verification.md → apps/android/app/src/androidTest/kotlin/foundation/mobile/GreetingTest.kt
- `Hosted run 43723923953 android job result (Gradle 9.3.1 with Temurin 17.0.21 assembled the debug app and instrumentation APK; derive step skipped; the comparison step printed the same two identity lines; two instrumentation tests passed with night mode off and on, on an API 36 x86_64 emulator)` --references--> `GreetingTest`  [INFERRED]
  docs/quality/verification.md → apps/android/app/src/androidTest/kotlin/foundation/mobile/GreetingTest.kt
- `Product identity result (2026-11-15: test.sh passed with --check printing foundation and --test passing 21 unit tests; both apps carried dev.foundation.mobile, Mobile Foundation, 0.1.0, build 1; a copy derived as Zoë's Proof built and matched its identity file)` --references--> `GreetingTest`  [INFERRED]
  docs/quality/verification.md → apps/android/app/src/androidTest/kotlin/foundation/mobile/GreetingTest.kt
- `Schemas free of sample names result (2026-11-15: test.sh passed with nine generator tests on Python 3.9.6 and --check passed; both apps built and passed the greeting tests in light and dark after the rename to typographyHeading; a scratch clone with the single key welcome_title generated, checked and tested)` --references--> `GreetingTest`  [INFERRED]
  docs/quality/verification.md → apps/android/app/src/androidTest/kotlin/foundation/mobile/GreetingTest.kt
- `Greeting as a single text element` --references--> `GreetingScreen()`  [INFERRED]
  docs/design-system/component-guidelines.md → apps/android/presentation/src/main/kotlin/foundation/presentation/GreetingScreen.kt

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Hosted run 43593365100 as runtime evidence for the greeting contract, visual definitions, shared text and reproducible builds** — docs_scope_root_002_shared_greeting_contract, docs_scope_root_003_shared_visual_definitions, docs_scope_root_004_shared_settings_text_and_brand_assets, docs_scope_root_005_reproducible_local_builds_and_checks, docs_quality_verification_hosted_run_43593365100, docs_quality_verification [EXTRACTED 1.00]
- **Forces that motivate the one-owner-per-responsibility decision** — docs_specs_root_0001_ownership_development_rules_force_two_languages_downstream_of_one_source, docs_specs_root_0001_ownership_development_rules_force_generated_files_beside_handwritten_code, docs_specs_root_0001_ownership_development_rules_force_coding_agents_as_regular_contributors, docs_specs_root_0001_ownership_development_rules_force_one_maintainer, docs_specs_root_0001_ownership_development_rules_force_small_codebase, docs_specs_root_0001_ownership_development_rules_decision_one_owner_per_responsibility [EXTRACTED 1.00]
- **Machine enforcement chain: test.sh runs the validator and both generator drift checks, mirrored by the CI foundation job** — docs_specs_root_0001_ownership_development_rules_enforcement_test_script_and_three_policy_checks, scripts_test, tooling_validation_check_architecture, scripts_generate_bindings, scripts_generate_design_tokens, github_workflows_foundation_foundation_job [EXTRACTED 1.00]
- **Rules that rest on review alone with no automated check** — docs_specs_root_0001_ownership_development_rules_r1_one_authoritative_owner, docs_specs_root_0001_ownership_development_rules_r3_app_trees_do_not_import_one_another, docs_specs_root_0001_ownership_development_rules_r8_real_caller_first, docs_specs_root_0001_ownership_development_rules_r9_search_before_adding, docs_specs_root_0001_ownership_development_rules_r11_handoff_reports_compiled_and_ran_separately, docs_specs_root_0001_ownership_development_rules_r14_bindgen_feature_host_only, docs_specs_root_0001_ownership_development_rules_r15_library_change_transitive_and_size_review, docs_specs_root_0001_ownership_development_rules_r16_breaking_change_is_a_migration, docs_specs_root_0001_ownership_development_rules_r18_service_proposal_requirements [EXTRACTED 1.00]
- **Regenerate and compare checks that keep generated tokens, catalogs and bindings equal to their sources** — docs_scope_root_003_shared_visual_definitions_token_drift_check, docs_scope_root_004_shared_settings_text_and_brand_assets_single_english_catalog, docs_scope_root_005_reproducible_local_builds_and_checks_generated_output_drift_detection, scripts_test [INFERRED 0.85]
- **Automated architecture compliance checks** — docs_quality_architecture_compliance_rust_format_and_lint, docs_quality_architecture_compliance_core_and_ffi_contract_tests, docs_quality_architecture_compliance_cargo_dependency_and_governance_check, docs_quality_architecture_compliance_project_identity_state_check, docs_quality_architecture_compliance_uniffi_generated_files_check, docs_quality_architecture_compliance_tokens_config_localization_check, docs_quality_architecture_compliance_ios_linkage_and_ui_check, docs_quality_architecture_compliance_android_linkage_and_ui_check [EXTRACTED 1.00]
- **Build plan of spec 0004: five steps that together satisfy AC-1 to AC-7** — docs_specs_root_0004_schemas_free_of_sample_names_index_build_plan, docs_specs_root_0004_schemas_free_of_sample_names_index_build_plan_step_1, docs_specs_root_0004_schemas_free_of_sample_names_index_build_plan_step_2, docs_specs_root_0004_schemas_free_of_sample_names_index_build_plan_step_3, docs_specs_root_0004_schemas_free_of_sample_names_index_build_plan_step_4, docs_specs_root_0004_schemas_free_of_sample_names_index_build_plan_step_5, docs_specs_root_0004_schemas_free_of_sample_names_index_ac_1, docs_specs_root_0004_schemas_free_of_sample_names_index_ac_2, docs_specs_root_0004_schemas_free_of_sample_names_index_ac_3, docs_specs_root_0004_schemas_free_of_sample_names_index_ac_4, docs_specs_root_0004_schemas_free_of_sample_names_index_ac_5, docs_specs_root_0004_schemas_free_of_sample_names_index_ac_6, docs_specs_root_0004_schemas_free_of_sample_names_index_ac_7 [EXTRACTED 1.00]
- **Rename path of the typography role greeting to heading: token schema, typography.json, both generated token files and the three readers, changed in one commit** — design_system_schemas_tokens_schema, docs_specs_root_0004_schemas_free_of_sample_names_index_token_schema_required_heading_and_body, docs_specs_root_0004_schemas_free_of_sample_names_index_typography_json_heading_role, docs_design_system_token_conventions_canonical_token_sources, docs_specs_root_0004_schemas_free_of_sample_names_index_typographyheading_generated_property, apps_ios_designsystem_generated_foundationtokens, apps_android_designsystem_src_main_kotlin_foundation_designsystem_foundationtokens, apps_ios_presentation_greetingscreen, apps_android_designsystem_src_main_kotlin_foundation_designsystem_foundationtheme, apps_android_app_src_androidtest_kotlin_foundation_mobile_greetingtest, docs_specs_root_0004_schemas_free_of_sample_names_index_build_plan_step_2 [EXTRACTED 1.00]
- **One init command turns a foundation clone into a derived product: identity files, README origin line, empty verification record, removed knowledge graph** — scripts_init_project, tooling_derive_init_project, apps_ios_config_identity, apps_android_identity, docs_specs_root_0003_new_project_from_foundation_index_readme_origin_line, docs_specs_root_0003_new_project_from_foundation_index_empty_verification_record, tooling_derive_verification_record, docs_specs_root_0003_new_project_from_foundation_index_init_write_set, docs_specs_root_0003_new_project_from_foundation_index_repository_states_foundation_derived_mixed [EXTRACTED 1.00]
- **Coordination records of scope 009: the log, the general brief rules and the manual steps list, all tied to the scope row** — docs_scope_coordination_009_a_new_project_from_the_foundation_log, docs_scope_coordination_009_a_new_project_from_the_foundation_brief_umum, docs_scope_coordination_009_a_new_project_from_the_foundation_manual, docs_scope_root_009_a_new_project_from_the_foundation [EXTRACTED 1.00]
- **Wave 1 ownership split: developer on the verification record, checker on the verify.md ticks, tester on the derivation tests, with no overlap** — docs_scope_coordination_009_a_new_project_from_the_foundation_log_dev_f009_m3, docs_scope_coordination_009_a_new_project_from_the_foundation_log_chk_f009_verify, docs_scope_coordination_009_a_new_project_from_the_foundation_log_tst_f009_test, docs_quality_verification, docs_specs_root_0003_new_project_from_foundation_verify, tooling_derive_test_init_project, docs_scope_coordination_009_a_new_project_from_the_foundation_log_parallel_start [EXTRACTED 1.00]
- **Box list of scope 010: Design it, Build it with three milestones, Verify it and Test it, all ticked** — docs_scope_root_010_schemas_free_of_sample_names_design_it, docs_scope_root_010_schemas_free_of_sample_names_build_it, docs_scope_root_010_schemas_free_of_sample_names_milestone_1_one_key_rule_and_heading_role, docs_scope_root_010_schemas_free_of_sample_names_milestone_2_generator_tests_on_own_sources, docs_scope_root_010_schemas_free_of_sample_names_milestone_3_document_updates_and_verification_record, docs_scope_root_010_schemas_free_of_sample_names_verify_it, docs_scope_root_010_schemas_free_of_sample_names_test_it [EXTRACTED 1.00]
- **Coordination records of scope 010 (log, general brief rules, manual steps) tied to the scope 010 file** — docs_scope_coordination_010_schemas_free_of_sample_names_log, docs_scope_coordination_010_schemas_free_of_sample_names_brief_umum, docs_scope_coordination_010_schemas_free_of_sample_names_manual, docs_scope_root_010_schemas_free_of_sample_names [EXTRACTED 1.00]
- **Scope 010 decisions carried over from the scope 009 coordination log (lead gate, session and disk limit, Beta flow boxes, one graph update per gate)** — docs_scope_coordination_010_schemas_free_of_sample_names_log_lead_gate_on_main, docs_scope_coordination_010_schemas_free_of_sample_names_log_session_and_disk_limit, docs_scope_coordination_010_schemas_free_of_sample_names_log_no_review_or_document_box, docs_scope_coordination_010_schemas_free_of_sample_names_log_one_graph_update_per_gate, docs_scope_coordination_009_a_new_project_from_the_foundation_log [EXTRACTED 1.00]
- **The nine delegated decisions of spec 0004 taken in auto mode for scope 010 (one heavy: the role name heading)** — docs_scope_coordination_010_schemas_free_of_sample_names_log_delegated_decisions, docs_scope_coordination_010_schemas_free_of_sample_names_log_delegated_heading_role_name, docs_scope_coordination_010_schemas_free_of_sample_names_log_delegated_required_roles_heading_body, docs_scope_coordination_010_schemas_free_of_sample_names_log_delegated_no_alias_for_typography_greeting, docs_scope_coordination_010_schemas_free_of_sample_names_log_delegated_min_properties_rule, docs_scope_coordination_010_schemas_free_of_sample_names_log_delegated_greeting_recipient_stays_sample_content, docs_scope_coordination_010_schemas_free_of_sample_names_log_delegated_fixture_source_tree, docs_scope_coordination_010_schemas_free_of_sample_names_log_delegated_done_when_4_proof, docs_scope_coordination_010_schemas_free_of_sample_names_log_delegated_scope_two_sample_names_only, docs_scope_coordination_010_schemas_free_of_sample_names_log_delegated_cross_check_findings_applied, docs_specs_root_0004_schemas_free_of_sample_names_index [EXTRACTED 1.00]
- **Proof that derivation still works: --check state test, derivation unit test on a temporary copy in scripts/test.sh, CI identity comparison in both native jobs, manual workflow run with derived set** — docs_specs_root_0003_new_project_from_foundation_index_check_form, docs_specs_root_0003_new_project_from_foundation_index_test_form, docs_specs_root_0003_new_project_from_foundation_index_derivation_test, docs_specs_root_0003_new_project_from_foundation_index_ci_identity_comparison, docs_specs_root_0003_new_project_from_foundation_index_workflow_derived_input, scripts_test, github_workflows_foundation, github_workflows_foundation_derived_input, github_workflows_foundation_derive_sample_product_step, github_workflows_foundation_ios_identity_comparison_step, github_workflows_foundation_android_identity_comparison_step [INFERRED 0.85]
- **Design token pipeline from canonical JSON to native projections** — docs_design_system_token_conventions_canonical_token_sources, design_system_schemas_tokens_schema, scripts_generate_design_tokens, docs_design_system_platform_mapping_swiftui_token_projection, docs_design_system_platform_mapping_compose_token_projection, docs_quality_architecture_compliance_tokens_config_localization_check [INFERRED 0.85]
- **Generator tests on their own sources: the fixture tree, the nine tests, the --test form and the invariants that keep them independent of a product's catalog and tokens** — docs_specs_root_0004_schemas_free_of_sample_names_index_fixture_source_tree, docs_specs_root_0004_schemas_free_of_sample_names_index_nine_generator_tests, docs_specs_root_0004_schemas_free_of_sample_names_index_test_form, docs_specs_root_0004_schemas_free_of_sample_names_index_test_module_names, docs_specs_root_0004_schemas_free_of_sample_names_index_invariant_tests_read_fixture_only, docs_specs_root_0004_schemas_free_of_sample_names_index_invariant_fixture_satisfies_schemas, docs_specs_root_0004_schemas_free_of_sample_names_index_test_sources_without_a_sample_name_generate_and_check, docs_specs_root_0004_schemas_free_of_sample_names_index_ac_5, docs_specs_root_0004_schemas_free_of_sample_names_index_ac_6, tooling_codegen_test_generation [INFERRED 0.85]
- **Regenerate derived outputs with their canonical source, never hand-edit** — docs_rules_development_rules_regenerate_derived_files, docs_rules_design_system_rules_regenerate_projections, docs_quality_architecture_compliance_generated_drift_remediation, docs_rules_rust_rules_regenerate_after_signature_change, docs_rules_shared_resources_rules_generated_native_strings, docs_rules_anti_duplication_ffi_shapes_in_rust_export [INFERRED 0.85]
- **Manual step flow: a sub-session reports a manual step, the lead lists it, the user runs it and the checker ticks verify.md from the result** — docs_scope_coordination_009_a_new_project_from_the_foundation_brief_umum_manual_steps_rule, docs_scope_coordination_009_a_new_project_from_the_foundation_manual, docs_scope_coordination_009_a_new_project_from_the_foundation_manual_summary, docs_scope_coordination_009_a_new_project_from_the_foundation_manual_result_routing, docs_scope_coordination_009_a_new_project_from_the_foundation_log_chk_f009_verify, docs_specs_root_0003_new_project_from_foundation_verify, docs_scope_coordination_009_a_new_project_from_the_foundation_manual_f009_1, docs_scope_coordination_009_a_new_project_from_the_foundation_manual_f009_2 [INFERRED 0.85]
- **Tracer bullet greeting path from shared core to both native screens** — docs_scope_index_tracer_bullet_build_approach, docs_scope_root_002_shared_greeting_contract, docs_scope_root_002_shared_greeting_contract_one_string_in_one_string_out_contract, docs_scope_ios_001_native_ios_greeting, docs_scope_android_001_native_android_greeting, docs_scope_root_006_hosted_build_verification [INFERRED 0.85]
- **Verification evidence chain: local checks, hosted jobs and the verification record** — docs_scope_root_005_reproducible_local_builds_and_checks, docs_scope_root_006_hosted_build_verification, docs_scope_root_008_hosted_results_in_the_verification_record, docs_scope_root_008_hosted_results_in_the_verification_record_single_list_of_unverified_targets [INFERRED 0.85]
- **Documents that follow spec 0004 (AC-7): the typographyHeading mapping, the required roles and naming rule, the README rule that the schema names no key, the checks row naming the fixture tree, and the two verification record rows** — docs_specs_root_0004_schemas_free_of_sample_names_index_ac_7, docs_design_system_platform_mapping_typographyheading, docs_design_system_token_conventions_required_roles_and_naming_rule, shared_localization_readme_schema_names_no_key, docs_quality_architecture_compliance_tokens_config_localization_check, docs_quality_verification_design_system_and_resources_result, docs_quality_verification_schemas_free_of_sample_names_result [INFERRED 0.95]
- **Derived hosted run 43701289339 as evidence for AC-10: the workflow input, the derive step and both identity comparisons ran on hosted runners** — docs_quality_verification_hosted_run_43701289339, docs_quality_verification_derived_hosted_foundation_job_result, docs_quality_verification_derived_hosted_ios_job_result, docs_quality_verification_derived_hosted_android_job_result, github_workflows_foundation_derived_input, github_workflows_foundation_derive_sample_product_step, github_workflows_foundation_ios_identity_comparison_step, github_workflows_foundation_android_identity_comparison_step, docs_specs_root_0003_new_project_from_foundation_index_ac_10, docs_scope_coordination_009_a_new_project_from_the_foundation_log_hosted_run_43701289339 [INFERRED 0.95]

## Communities (57 total, 1 thin omitted)

### Community 0 - "Foundation verification 2026-11-15"
Cohesion: 0.08
Nodes (50): GreetingTest, GreetingUITests, UInt8, CIContext, Android linkage and UI check (Linux CI job, emulator instrumentation), GitHub Actions CI jobs (macOS and Linux), iOS linkage and UI check (macOS CI job, XCTest), Physical hardware verification for simulator-inaccessible capabilities (+42 more)

### Community 1 - "mobile_ffi.swift"
Cohesion: 0.05
Nodes (64): Array, createReader(), createWriter(), Data, FfiConverter, FfiConverterPrimitive, FfiConverterRustBuffer, FfiConverterString (+56 more)

### Community 2 - "Sub-session dev-f010-m1 (developer, opus-5-5 medium, archived): scope 010 Build it, all three milestones, Build plan steps 1 to 5 of spec 0004, all finished; owns both schemas, typography.json, the generated token files, three app files, the codegen fixtures and tests, five documents and verify.md; branch claude/dev-f010-m1-6599c9"
Cohesion: 0.13
Nodes (42): Schemas free of sample names result (2026-11-15: test.sh passed with nine generator tests on Python 3.9.6 and --check passed; both apps built and passed the greeting tests in light and dark after the rename to typographyHeading; a scratch clone with the single key welcome_title generated, checked and tested), Disk rule: 22 GiB free at the start; one full native build at a time (the developer for the platform it touches, then the checker); the tester builds only if the brief asks; run df -g . first; below 10 GiB free stop and report blocked; remove target/, build/ and scratchpad clones before done, Sample removal only on a copy: proof that the catalog and token set pass without the greeting names runs on test fixtures or a temporary scratchpad clone, never by leaving the worktree with the samples deleted; scripts/init-project.sh --name only in a temporary clone, --check and --test are safe, Decision (lead): checker and tester started together from the developer branch (git merge claude/dev-f010-m1-6599c9 in each worktree), before the build merge was committed, Checker note, not a blocker: verify.md does not ask for --rerun-tasks for the second night mode on Android as the hosted workflow does; without that flag the test task still ran again (Starting 2 tests, new timestamp), Sub-session chk-f010-verify (checker verify, fable-5-2 high, archived): scope 010 full verify of AC-1 to AC-7 from the developer branch, closing the three milestones, Build it and Verify it; owns the verify.md ticks of spec 0004; branch claude/chk-f010-verify-59dbd8, Delegated decision (spec 0004, AC-3, not heavy, in force): no alias for the old name typographyGreeting, one change; runner-up greeting kept for one release; undo via architect (update) of spec 0004, rebuilding Build plan step 2, Sub-session dev-f010-m1 (developer, opus-5-5 medium, archived): scope 010 Build it, all three milestones, Build plan steps 1 to 5 of spec 0004, all finished; owns both schemas, typography.json, the generated token files, three app files, the codegen fixtures and tests, five documents and verify.md; branch claude/dev-f010-m1-6599c9 (+34 more)

### Community 3 - "mobile_ffi.kt"
Cohesion: 0.06
Nodes (34): Disposable, NoHandle, UniffiByValue, UniffiCallbackInterfaceClone, UniffiCallbackInterfaceFree, UniffiForeignFutureCompleteF32, UniffiForeignFutureCompleteF64, UniffiForeignFutureCompleteI16 (+26 more)

### Community 4 - "Coordination log (Log koordinasi) for scope 009 - A new project from the foundation (wave 1 finished, no active wave, decision mode auto, start hash 4a153fe, updated 2026-11-15 19:05)"
Cohesion: 0.08
Nodes (63): General brief rules (Aturan umum brief) for the sub-sessions of the scope 009 coordination: the fixed part of every brief; the brief wins where it differs, Always forbidden for sub-sessions: docs/scope/, AGENTS.md, graphify-out/, spec content other than the Status line and the verify.md ticks (checker only), other specs, and files outside the brief's allowed list, Decisions in auto mode: for an ambiguous AC read the spec's rationale.md, take the reading closest to the AC text and record it under Tafsiran AC; needs-decision goes to the lead only when the AC text or a spec decision must change, Commit rule for sub-sessions: one commit per step, an imperative English subject without prefix like the repository history, plus the Co-Authored-By trailer, Disk rule: 32 GiB free at the start; only the checker runs full native builds, one at a time; below 10 GiB free stop and report blocked; remove target/, build/ and apps/android/**/build and the temporary clone before reporting done, Main checkout and knowledge graph: run graphify query and graphify explain against the main checkout's graphify-out/graph.json before reading files, and never change a file in the main checkout, Hosted run 43701281055 (push trigger, on revision 4a153fe), Lead address: Mobile Foundation Scaffold [f5cda4]; full reports, questions and needs-decision go there through SendMessage (+55 more)

### Community 5 - "UniffiLib"
Cohesion: 0.06
Nodes (3): UniffiLib, UniffiRustCallStatus, UniffiRustFutureContinuationCallback

### Community 6 - "0002. One planning path: a scope row first, then a spec"
Cohesion: 0.17
Nodes (12): 0002. One planning path: a scope row first, then a spec, Consequences, Context, Decision, Follow-up, Option 1: Scope row first, then a spec, in one change, Option 2: The plans folder is the path, Option 3: Keep every home, with a written split (+4 more)

### Community 7 - "Spec 0001: One owner per responsibility, with rules kept beside the code"
Cohesion: 0.13
Nodes (35): Boundaries, Limits of CI checks, Reviewers assess semantic duplication, Spec 0001: One owner per responsibility, with rules kept beside the code, Automate only what a machine can judge, Decision: one owner per responsibility in an ownership matrix, topic-sized rule files, short AGENTS.md entry point, automated checks only where a machine is reliable, Enforcement: scripts/test.sh runs format, lint, tests and three policy checks; CI runs the same script plus iOS and Android jobs, An exact dependency list, not a deny list (+27 more)

### Community 8 - "CI job: android (JDK 17, API 36 emulator, optional sample derivation, identity comparison, Kotlin binding + Compose UI)"
Cohesion: 0.26
Nodes (20): Derived hosted run android job result (same derive command; Gradle 9.3.1 assembled the derived debug app; identity file and built app matched; two instrumentation tests passed with night mode off and on), Derived hosted run ios job result (derive step ran init-project.sh as Zoë's Proof with dev.example.derived; Xcode 26.5 built the derived app; identity file and built app matched; greeting test passed in light and dark on iOS 26.5), Hosted run 43701281055 on the push of revision 4a153fe (all three jobs passed; the derive step was skipped; both comparison steps passed with dev.foundation.mobile and Mobile Foundation), Hosted run 43701289339 on revision 4a153fe (2026-11-15, started by hand through workflow_dispatch with the derived input set; all three jobs passed), Hosted run 43723923953 android job result (Gradle 9.3.1 with Temurin 17.0.21 assembled the debug app and instrumentation APK; derive step skipped; the comparison step printed the same two identity lines; two instrumentation tests passed with night mode off and on, on an API 36 x86_64 emulator), Hosted run 43723923953 ios job result (Xcode 26.5 built the simulator app and linked the unsigned device build; derive step skipped; identity file and built app both dev.foundation.mobile, Mobile Foundation; greeting test passed in light and dark on an iPhone 17 simulator on iOS 26.5), AC-10: the workflow accepts a manual run with the derived input, and every native job compares the built app's ID and display name with the identity file, CI identity comparison: each native job compares the built app's ID and display name (PlistBuddy on Info.plist, aapt2 dump badging on the debug APK) with its identity file and fails on a difference (+12 more)

### Community 9 - "init_project.py"
Cohesion: 0.12
Nodes (31): Exception, check(), derive(), foundation_ref(), foundation_url(), git(), identity_text(), in_git() (+23 more)

### Community 10 - ".assert_refused"
Cohesion: 0.11
Nodes (9): AC-7: a local path remote, or no remote, is no usable foundation URL., AC-7: each input that breaks its rule is refused with exit 2, one line and no…, AC-7: a remote URL that is not UTF-8 is no usable foundation URL., AC-7: a derived checkout is refused., AC-7: each name outside the rule is refused on its own, with exit 2, one line…, AC-7: each application ID outside the rule of its flag is refused on its own., AC-7: each version, date, foundation URL and ref outside its rule is refused on…, AC-7: the foundation remote is read first; when it exists and is unusable,… (+1 more)

### Community 11 - ".run_command"
Cohesion: 0.11
Nodes (12): AC-3, AC-5, AC-6, AC-8: the happy path writes every file and the checkout then…, AC-3: each override reaches only its own identity file, and --version reaches…, AC-3: with one override the other platform keeps --app-id., AC-3, AC-7: a value that starts with a hyphen is refused, and its equals form…, AC-6: without the flags the origin line takes the remote, HEAD and today., AC-6: the foundation remote wins over origin, and the highest release tag wins., AC-3: the example of the criterion, with no other flag, writes 0.1.0 and build…, AC-5, AC-6: the remote's user and token are dropped before the URL is written… (+4 more)

### Community 12 - "Architecture compliance"
Cohesion: 0.19
Nodes (19): Dependency rules, Architecture, Architecture compliance, Rust format and lint check (rustfmt, Clippy warnings denied), Spec under docs/specs and policy update for a new dependency or material architecture change, Development rules, Capability spec checklist: user outcome, scope, acceptance criteria, existing owner, public contract, dependency direction, platform specific work, verification matrix, /scope and /architect: the usual commands for writing the scope row and the spec (+11 more)

### Community 13 - "generate.py"
Cohesion: 0.12
Nodes (23): Neutral: tooling/codegen/generate.py, tokens.py and resources.py are not edited, Security model: nothing new; the generator reads and writes inside the checkout, the tests inside a temporary folder that they remove; no network beyond the existing download of the pinned validator wheel on first use, and no secret, Recommendation: the generator code is left alone; the property name already comes from the role name, so the rename needs no code change, SHA-pinned GitHub Actions with read-only contents permission, check_schema(), generate(), load(), projections() (+15 more)

### Community 14 - "RustBuffer"
Cohesion: 0.13
Nodes (9): ByReference, ByValue, ForeignBytes, `hello`(), RustBuffer, uniffiTraitInterfaceCall(), uniffiTraitInterfaceCallWithError(), kotlin (+1 more)

### Community 15 - "config.schema.json"
Cohesion: 0.10
Nodes (18): Draft 7 schema and native mappings updated together, Draft 7 schemas in shared/specifications, Fixture shared/config/foundation.json: schemaVersion 1, defaultLocale en, defaultLocale, schemaVersion, foundation.json: public build-time configuration (v1 schema), Unknown keys and unsupported schema versions fail the build check; version schema for incompatible changes, additionalProperties (+10 more)

### Community 16 - "Mobile foundation scope (index)"
Cohesion: 0.13
Nodes (26): docs/ and root AGENTS.md: architecture, decision records, scope and agent workflow, docs/ record homes: docs/scope (what to build and its status), docs/specs (design and decision records), docs/decisions (the founding decision), Cargo dependency and governance check, Architecture policy result (dependency and required-document checks), Progress is recorded in the scope row; what ran is recorded in the verification record, Mobile foundation scope (index), Deferred: a contract beyond one string (record, typed error, async call), Deferred: a second language end to end (+18 more)

### Community 17 - ".git"
Cohesion: 0.16
Nodes (9): Checkout, AC-7: a modified or untracked file is refused, even when git status hides…, AC-7: a mixed checkout is refused., AC-4: a checkout that has no graph changes only the two identity files,…, AC-6: a README.md of one line without a newline still ends with the title,…, AC-6: only a foundation-v tag that points exactly at HEAD names the ref;…, AC-7: a change only in the index, and a deleted tracked file, both make the…, AC-7: git status leaves ignored files out, so an ignored local file is no… (+1 more)

### Community 18 - "Ownership matrix"
Cohesion: 0.24
Nodes (21): Ownership matrix, apps/android: owner of Android UI, presentation state and OS APIs, apps/ios: owner of Apple UI, presentation state and OS APIs, bindings/swift and bindings/kotlin: generated FFI source snapshots, crates/core: owner of shared behavior, domain rules and application validation, crates/mobile-ffi: owner of cross-language API, records and typed errors (UniFFI), Derived file rule: change the canonical input and regenerate every output in the same review, design-system/tokens and schemas: owner of canonical visual values and semantic roles (+13 more)

### Community 19 - "apps/ios/Config/Identity.xcconfig (iOS identity file: APP_BUNDLE_IDENTIFIER, APP_DISPLAY_NAME, MARKETING_VERSION, CURRENT_PROJECT_VERSION)"
Cohesion: 0.14
Nodes (29): apps/android/app/src/main/AndroidManifest.xml, apps/android/app/src/main/res/values/app.xml (the app_name string leaves this file; the label comes from the appLabel manifest placeholder), apps/android/identity.properties (Android identity file: applicationId, displayName, versionName, versionCode), apps/ios/Config/App.xcconfig (iOS app build settings), apps/ios/Config/Identity.xcconfig (iOS identity file: APP_BUNDLE_IDENTIFIER, APP_DISPLAY_NAME, MARKETING_VERSION, CURRENT_PROJECT_VERSION), apps/ios/Config/Project.xcconfig (iOS project build settings), apps/ios/MobileFoundation.xcodeproj/project.pbxproj (Xcode project file), Product identity (display name, application IDs, app version): owned by apps/ios/Config/Identity.xcconfig and apps/android/identity.properties; consumed by the Xcode and Gradle builds and scripts/init-project.sh (+21 more)

### Community 20 - "Spec 0003 rationale: decision history of the new project spec (context, options considered, rationale)"
Cohesion: 0.13
Nodes (30): Decision: a product is a clone that changes only its display name, application ID and version through scripts/init-project.sh, keeps every other name, starts with an empty verification record and merges foundation-v tags, Tradeoff: a command and its unit tests are kept for a job that runs once per product, Tradeoff: later foundation scope rows and specs do not flow into products; the reason behind a new foundation rule is read in the foundation repository, Tradeoff: a product carries the foundation's commit history and its foundation-v tags, Spec 0003 rationale: decision history of the new project spec (context, options considered, rationale), Recommendation: --check does not look for hosted run links, Recommendation: the command does not edit scope rows, Recommendation: the command refuses to run on a derived checkout (+22 more)

### Community 21 - "Spec 0003: A new project from the foundation: product identity in two files, one init command, updates by merge (Accepted)"
Cohesion: 0.15
Nodes (29): Ticked in wave 1: 009 Test it, from the tst-f009-test report done (21 to 50 tests, AC-3 to AC-9 each have a test carrying its ID, commit dc9a8d9, merged in 0aa1d5c); on main with the merge staged there were no conflict markers and scripts/test.sh exited 0, Build steps (009): identity file per platform (AC-1, AC-2, done), init command with state check and unit tests (AC-3 to AC-9, done), workflow derived input and identity comparison (AC-10, done), README path and document updates (AC-11, AC-12, done), The two apps disagree on their own identity (iOS dev.foundation.mobile / Mobile Foundation / 1.0, Android foundation.mobile / Foundation / 0.1.0), Spec 0003: A new project from the foundation: product identity in two files, one init command, updates by merge (Accepted), AC-1: both apps carry the same default identity, read from Identity.xcconfig and identity.properties, stated nowhere else under apps/, AC-2: with the default identity scripts/test.sh passes, both apps build and the greeting tests pass in both appearances, AC-3: init-project.sh --name --app-id writes name, ID, version 0.1.0 and build 1 into both identity files, with per-value overrides, AC-4: the write set is exactly the two identity files, README.md, the verification record and the removed graphify-out/ files; nothing is renamed (+21 more)

### Community 22 - "FfiConverter"
Cohesion: 0.22
Nodes (7): FfiConverter, FfiConverterRustBuffer, FfiConverterString, FfiType, ByteBuffer, KotlinType, ULong

### Community 23 - "Spec 0004: Schemas free of sample names: one key of any name, a heading role, generator tests on their own sources (Status: Accepted, 2026-11-15); removes the two sample names (greeting_recipient, the greeting role) that the foundation schemas still require"
Cohesion: 0.12
Nodes (53): Decision rule (mode auto): the architect still sends an 'Accept this spec?' summary to the lead and waits for accept; other roles read rationale.md for an ambiguous AC, take the reading closest to the AC text and record it in 'Tafsiran AC'; needs-decision only if AC text or a spec decision must change, Scope 010 specifics: main at start = 7b6ca4f, equal to origin/main; one feature with one open box, Design it (spec); spec number 0004; source is the spec 0003 Follow-up on greeting_recipient and the greeting role; Beta flow closes with Verify it and Test it; one developer until the lead splits ownership, Coordination log (Log koordinasi) for scope 010 - Schemas free of sample names (wave 1 finished 2026-11-15, no active wave, decision mode auto, start hash 7b6ca4f, updated 2026-11-15 21:25), Sub-session arc-f010-spec (architect, fable-5-2 high, archived): scope 010 Design it (spec), spec 0004; owns docs/specs/_root/0004-schemas-free-of-sample-names/ plus one Follow-up line in the spec 0003 index.md; branch claude/arc-f010-spec-6c76d1, Closing (Penutupan) of the scope 010 coordination: every green branch merged on 2026-11-15 (arc-f010-spec in 7c906fb, dev-f010-m1 in 8c8caf8, tst-f010-test and chk-f010-verify in b64055a), no Document step, closing commit b64055a, nothing kept, no blocker left, Cleanup at closing: for each of the four coordination branches (arc-f010-spec, dev-f010-m1, chk-f010-verify, tst-f010-test) the session was archived, the worktree removed and the branch deleted, /sync at closing (2026-11-15, range 7b6ca4f..b64055a): the changed sources (the two schemas, typography.json, GreetingScreen.swift, FoundationTheme.kt) change no command, convention or dependency that AGENTS.md records, so nothing was changed; no tick was rejected, Decision (lead): spec cross check = Another model (the default for Beta) (+45 more)

### Community 24 - "002 - Shared greeting contract (done)"
Cohesion: 0.15
Nodes (18): hello(), preserves_empty_names_and_whitespace(), String, hello(), String, tests/contracts: Cargo integration tests for exported behavior, Core and FFI contract tests (locked Cargo tests), Reviewers trace changed behavior from owner into each client (+10 more)

### Community 25 - "localization.schema.json"
Cohesion: 0.16
Nodes (28): Delegated decision (spec 0004, AC-4, not heavy, in force): the key greeting_recipient stays as sample content in the catalog and both apps, and the schema no longer names it; runner-up the neutral key recipient_name; undo via architect (update) of spec 0004, Build plan step 2 grows by 7 files, Delegated decision (spec 0004, AC-1, not heavy, in force): the 'at least one key' rule is "minProperties": 1 with no required and no properties; runner-up an empty catalog is allowed; undo via architect (update) of spec 0004, rebuilding Build plan step 1, AC-1: localization.schema.json holds "minProperties": 1 with no required and no properties member; an empty default catalog {} makes --check exit 1 with 'en.json: data must contain at least 1 properties'; any single key that fits the key pattern is accepted, AC-4: the sample app behaves as before: scripts/test.sh exits 0, both apps build, the greeting tests pass in light and dark on both platforms, and greeting_recipient stays in en.json, both generated string files and both app entry points, Build plan step 1: in shared/specifications/localization.schema.json replace the line "required": ["greeting_recipient"], with "minProperties": 1, and run scripts/generate-design-tokens.sh --check (AC-1), Text for shared/localization/README.md: a catalog needs at least one key, the schema names none so the keys are yours to choose, and the sample key greeting_recipient is replaced together with the greeting screen when the first feature arrives, One-key rule: the localization schema after the change is a Draft 7 object with minProperties 1, the key pattern ^[a-z][a-z0-9]*(_[a-z0-9]+)*$ and non-empty string values; it has no required member and names no key at all, Sample content that stays on purpose: the key greeting_recipient in en.json and both generated string files, MobileFoundationApp.swift, MainActivity.kt, GreetingTest.kt, the GreetingScreen screens and the accessibility identifier greeting; a product replaces these together (+20 more)

### Community 26 - "test_generation.py"
Cohesion: 0.12
Nodes (33): Tokens, configuration and localization check (generate-design-tokens.sh --check validates canonical data and compares native outputs; --test runs failure and regeneration cases on the tests' own source tree tooling/codegen/fixtures/sources/), Design system and resources result (nine generator tests, which read tooling/codegen/fixtures/sources/ and not the checkout's own sources), Delegated decision (spec 0004, AC-5, not heavy, in force): the generator tests read the fixture tree tooling/codegen/fixtures/sources/ (7 files); runner-up the tests keep reading the checkout sources generically; undo via architect (update) of spec 0004, rebuilding Build plan step 3, Decision (lead): the spec, verify.md and the verification record say 'nine generator tests', so the tester is asked to close AC gaps by strengthening the nine existing tests; a new test function only if there is no other way, with the new count reported to the lead, Ticked in wave 1: 010 Test it, from the tst-f010-test report done (9 tests before and after; AC-1, AC-2, AC-3, AC-5 and AC-6 locked through subTest and exact error messages; five mutations, each in its own clone, were caught; commits 87ec624, 1c67e0d, 16b8e60); branch merged in b64055a, AC-5: no test under tooling/codegen/ reads the checkout's design-system/tokens/, shared/config/ or shared/localization/; tests read tooling/codegen/fixtures/sources/ and the checkout's schemas; --test still passes with en.json and typography.json replaced by {}, Text for docs/quality/architecture-compliance.md: the generator tests read their own source tree under tooling/codegen/fixtures/sources/, so they pass whatever the tokens and catalogs of the checkout hold, Build plan step 3: add the seven fixture files under tooling/codegen/fixtures/sources/ and change tooling/codegen/test_generation.py to the nine tests, then run scripts/generate-design-tokens.sh --test (AC-5, AC-6) (+25 more)

### Community 27 - "003 - Shared visual definitions (done)"
Cohesion: 0.23
Nodes (11): Design system, Android scope, Android app owns its screen, appearance changes and native localization lookup, Tracer Bullet build approach, iOS scope, Apple app owns its screen, appearance changes and native localization lookup, 003 - Shared visual definitions (done), Shared named visual values (color, type, spacing, corners, motion) (+3 more)

### Community 28 - "GreetingScreen"
Cohesion: 0.17
Nodes (11): App, MobileFoundationApp, .body, GreetingScreen, .body, String, Native components guidelines, Greeting as a single text element (+3 more)

### Community 29 - "test_init_project.py"
Cohesion: 0.14
Nodes (9): Unit tests create their own repository in a temporary folder with isolated git configuration; no test touches the real checkout, OutsideGitTests, Checks for the derivation command: every write, every refusal and both clean…, AC-9: the derivation proof is skipped, with its reason, in a checkout that is…, AC-7: outside git both foundation values are required., AC-7: a folder inside another repository counts as outside git., Run the checked in command on a temporary copy of this checkout. The checkout…, AC-9: the copy's own command derives the copy, which then reads derived and… (+1 more)

### Community 30 - "FoundationTokens"
Cohesion: 0.29
Nodes (6): MainActivity, FoundationTokens, Palette, GreetingScreen(), Bundle, ComponentActivity

### Community 31 - "R4: shared behavior lives in the core, the export stays thin, both clients stay on one contract"
Cohesion: 0.15
Nodes (20): main(), target/, build/ and Gradle build directories excluded from source control, Extending the contract, Mobile contract, Design definitions compile independently of Cargo and UniFFI, UniFFI generated files drift check, ABI generation result (UniFFI 0.31.2, identical regenerated tree), FFI shapes change in the annotated Rust export (+12 more)

### Community 32 - "AGENTS.md"
Cohesion: 0.13
Nodes (22): Before editing, Before handoff, During implementation, Working in the mobile foundation, Android rules, Checked-in Gradle wrapper, New ABI requires Rust cross-build and runtime test, Anti-duplication rules (+14 more)

### Community 33 - "test.sh"
Cohesion: 0.16
Nodes (20): Derived hosted run foundation job result (locked build and scripts/test.sh passed: three Rust tests, 21 derivation tests, seven generator tests; this job does not derive), Hosted run 43723923953 foundation job result (ubuntu-24.04; locked build and scripts/test.sh passed with Rust 1.100.0 and Python 3.12: three Rust tests, 50 derivation tests, nine generator tests), Derivation only on a copy: init-project.sh with --name rewrites README.md and the verification record and removes graphify-out/, so that form runs only in a temporary clone in the session scratchpad; --check and --test are safe in the worktree, Decision: the tester installs no new tool and test-preferences.json is not created; the framework is the existing Python unittest run through scripts/init-project.sh --test, Done when (009): one recorded decision, one command, a hosted check on a temporary copy, clean inherited records, recorded foundation revision, init-project.sh --check: prints foundation or derived (exit 0) or names each mismatch in a mixed state (exit 1), Derivation test: copies the files git lists to a temporary folder, runs the copy's own command with sample values, requires --check to print derived and check-architecture.py to pass, then removes the copy, Key invariants: a checkout is foundation or derived, each identity value has one home per platform, the command renames nothing, never runs on a derived or mixed checkout, never changes git state, and foundation tags match foundation-v* (+12 more)

### Community 34 - "Native token mapping"
Cohesion: 0.27
Nodes (15): System text scaling via generated text styles, Native token mapping, Compose sp mapping of logical text units, Jetpack Compose token projection (FoundationTokens), Dynamic Type mapping of headline and reading scales, Logical spacing units adapt to display density, spacingPage role, SwiftUI token projection (FoundationTokens) (+7 more)

### Community 35 - "iOS 001 - Native iOS greeting (existing)"
Cohesion: 0.15
Nodes (22): CoreImage, Android 001 - Native Android greeting (existing), API 36 emulator results (arm64 local, x86_64 hosted) in light and dark, Android app packages both supported CPU architectures, Android physical device coverage unverified, Android 002 - Lowest supported Android and large text (planned), 16 KiB memory page packaging, Declared Android minimum API 24 not yet exercised (+14 more)

### Community 36 - "README: Native mobile foundation"
Cohesion: 0.27
Nodes (11): AC-11: README.md has a section with the full path from clone to first results, path ownership, taking a later release and foundation tagging, Neutral: /develop moves the spec to In Progress and Accepted with scope row 009; creating the first tag foundation-v0.1.0 is the maintainer's step, README section 'Start a project from this foundation': clone at a tag, create a branch, rename the remote, run the command, add origin, rebuild the graph, mark inherited rows existing, commit, record first results, Release the foundation: run the workflow by hand with derived set, then push an annotated foundation-vMAJOR.MINOR.PATCH tag on main, Recommendation: tags are named foundation-vMAJOR.MINOR.PATCH, README: Native mobile foundation, Finish the start by hand: rebuild the knowledge graph (/graphify .), mark inherited scope rows existing (/scope), commit, run scripts/test.sh and both native builds, push, record the first local and hosted results, Hello, World! greeting shown by SwiftUI and Compose apps (+3 more)

### Community 37 - "uniffiCheckCallStatus"
Cohesion: 0.23
Nodes (7): E, uniffiCheckCallStatus(), UniffiForeignFutureCompleteVoid, uniffiRustCall(), UniffiRustCallStatusErrorHandler, uniffiRustCallWithError(), U

### Community 38 - "DerivationTests"
Cohesion: 0.12
Nodes (9): DerivationTests, AC-4: git sees changes in exactly the documented paths, and no rename., AC-6, AC-7: every accepted remote form becomes https without credentials; the…, AC-7: the in git test compares folders, not path spellings., AC-4: a graph removal that fails names every changed path and the way back., AC-4: each file is replaced in the documented order, and graphify-out/ goes…, AC-5: the template on disk, filled with the sample values, is the empty record…, AC-7: letters from any script, digits 0 to 9, single spaces, periods, hyphens… (+1 more)

### Community 39 - "Accessibility (design system)"
Cohesion: 0.24
Nodes (9): Accessibility (design system), Per-target reading order and screen-reader review, Status conveyed by text or semantics, not color alone, Honor platform reduced-motion setting, Text contrast check (4.5:1 minimum), W3C WCAG 2.2 contrast minimum guidance, Native controls styled with semantic tokens, Layout, text measurement, gestures and focus stay in presentation (+1 more)

### Community 40 - ".assert_mixed"
Cohesion: 0.18
Nodes (5): AC-8: every departure from the exact form is a mismatch that names the file and…, AC-8: a derived checkout that lost one signal names that signal., AC-8: an identity file that is not UTF-8, and a missing README.md, are…, AC-8: changing only applicationId names that file and key against a foundation…, AC-8: default IDs under an origin line, and a second origin line, each make a…

### Community 41 - "ADR 0001 · Native apps with a shared Rust core"
Cohesion: 0.40
Nodes (5): ADR 0001 · Native apps with a shared Rust core, Consequences, Context, Decision, Revisit when

### Community 43 - "InternalException"
Cohesion: 0.42
Nodes (4): InternalException, T, UniffiHandleMap, UniffiNullRustCallStatusErrorHandler

### Community 44 - "Spec 0004 rationale: decision history of the schemas free of sample names spec (context, options considered, rationale)"
Cohesion: 0.15
Nodes (30): FoundationTheme(), Stable role names or same-change migration, Public role name changes require migrating both consumers, Incompatible source format changes treated as migrations, Decision: Option 1, fix the two schemas in place (one key of any name through minProperties), rename the required typography role greeting to heading in one change across the source, both generated files and three readers, and give the generator tests their own source tree, Invariant: a consumed role is renamed in one change with every reader on both platforms; no alias is kept, Tradeoff: typographyGreeting is gone with no alias; a product derived before this release renames its uses when it merges the release (the compiler names each place, and the generator rewrites the generated files), Spec 0004 rationale: decision history of the schemas free of sample names spec (context, options considered, rationale) (+22 more)

### Community 45 - "Shared resource ownership rules"
Cohesion: 0.17
Nodes (16): Generated drift remediation, Design system rules, Drift check plus verification in both appearances and larger text sizes, Regenerate native projections in the same change, Shared visual values live in design-system/tokens, Regenerate derived files alongside canonical inputs, Shared resource ownership rules, Generated native strings owned by the resource generator (+8 more)

### Community 46 - "Path ownership after derivation: product owned paths keep the product's side, foundation owned paths take the foundation's side, shared paths merge by hand"
Cohesion: 0.22
Nodes (15): Replace the greeting with a first feature without editing a foundation schema, Follow-up: build the command that takes a foundation release (fetch, merge, apply the ownership table) when the first release is merged into a product, Follow-up: decide where dependency update bots run (a bot in every product changes foundation owned files and will conflict with merges), Follow-up: revisit keeping MobileFoundation as the Xcode project and scheme name if it confuses contributors to a product, Names the foundation keeps: MobileFoundation project, targets and scheme, rootProject.name, crates foundation-core and mobile-ffi, mobile_ffi namespace, Kotlin packages, FoundationTokens, FoundationTheme, foundation_strings.xml, foundation.json, the workflow file, Path ownership after derivation: product owned paths keep the product's side, foundation owned paths take the foundation's side, shared paths merge by hand, Take a later foundation release: git fetch foundation --tags, git merge foundation-vX.Y.Z, keep the product's side on product owned paths, rebuild the graph, run every check, Tradeoff: foundation names stay in product code (MobileFoundation project, scheme and bundle, Foundation-prefixed types and packages); users see only the display name (+7 more)

### Community 47 - "CommandLineTests"
Cohesion: 0.31
Nodes (5): CommandLineTests, Run the copied scripts/init-project.sh from another folder, as a person or CI…, AC-3, AC-8: the wrapper finds its own checkout, prints the five changed paths,…, AC-7: through the wrapper a refusal exits 2, prints one line on stderr only,…, AC-8: through the wrapper --check exits 1 and names the mismatch on stderr.

### Community 49 - "IntegrityCheckingUniffiLib"
Cohesion: 0.60
Nodes (3): IntegrityCheckingUniffiLib, uniffiCheckApiChecksums(), uniffiCheckContractApiVersion()

### Community 50 - "General brief rules (Aturan umum brief) for the sub-sessions of the scope 010 coordination: the fixed part of every brief; the brief the lead sends points to this file, and the brief wins where the two differ"
Cohesion: 0.09
Nodes (29): Before commit, Graph and commit: the lead fulfils the AGENTS.md /graphify . --update rule when merging to main; sub-sessions never run graphify update and never stage anything under graphify-out/, Decision: the knowledge graph is updated once per gate event: merged files, scope ticks and the log go into one graph update and one commit, so the AGENTS.md rule is met without repeated extraction, Decision: the restricted graph update stamped _origin semantic directly in graph.json for nodes and edges of the 14 coordination and skill documents, because the library guesses the tier from the shape of the location; later restricted updates stamp the chunk before the merge, General brief rules (Aturan umum brief) for the sub-sessions of the scope 010 coordination: the fixed part of every brief; the brief the lead sends points to this file, and the brief wins where the two differ, Additional user conditions (Ketentuan tambahan user) for the scope 010 coordination: none, Always forbidden: docs/scope/, AGENTS.md, graphify-out/, spec content other than the **Status** line and verify.md ticks (except the architect on its own spec), other specs, and files outside 'File yang BOLEH diubah'; changes outside ownership are requested from the owner or the lead, Commit rule: one commit per step, an English imperative subject without a prefix like this repo's history (e.g. 'Plan and specify a new project from the foundation'), plus the Co-Authored-By trailer from the session's system reminder; the developer moves the spec **Status** from Proposed to In Progress (+21 more)

### Community 51 - "build-android-rust.sh"
Cohesion: 0.40
Nodes (4): CARGO_TARGET_AARCH64_LINUX_ANDROID_LINKER, CARGO_TARGET_X86_64_LINUX_ANDROID_LINKER, PATH, build-android-rust.sh script

### Community 54 - "build-ios-rust.sh"
Cohesion: 0.50
Nodes (3): CARGO_TARGET_DIR, PATH, build-ios-rust.sh script

### Community 55 - "FoundationTokens"
Cohesion: 0.29
Nodes (7): FoundationTokens, Palette, CGFloat, Color, ColorScheme, Font, TimeInterval

### Community 63 - "generate-design-tokens.sh"
Cohesion: 0.14
Nodes (28): Canonical token schema (tokens.schema.json), Canonical JSON propagates through code generation, Semantic names for decisions both apps share, Token conventions, Canonical token sources (colors, typography, spacing, radius, motion JSON), References are group-local and point directly to primitives, Token naming convention (lower camel case, #RRGGBB), Primitive token (names a value) (+20 more)

### Community 68 - "gradlew"
Cohesion: 0.83
Nodes (3): gradlew script, die(), warn()

## Knowledge Gaps
- **88 isolated node(s):** `.body`, `CoreImage`, `XCTest`, `UniffiWithHandle`, `NoHandle` (+83 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `DerivationTests` connect `DerivationTests` to `test.sh`, `.assert_mixed`, `.assert_refused`, `.run_command`, `.git`, `.test_a_write_that_fails_leaves_the_later_files_and_no_temporary_file`, `test_init_project.py`?**
  _High betweenness centrality (0.146) - this node is a cross-community bridge._
- **Why does `Foundation verification 2026-11-15` connect `Foundation verification 2026-11-15` to `AGENTS.md`, `test.sh`, `Sub-session dev-f010-m1 (developer, opus-5-5 medium, archived): scope 010 Build it, all three milestones, Build plan steps 1 to 5 of spec 0004, all finished; owns both schemas, typography.json, the generated token files, three app files, the codegen fixtures and tests, five documents and verify.md; branch claude/dev-f010-m1-6599c9`, `iOS 001 - Native iOS greeting (existing)`, `Coordination log (Log koordinasi) for scope 009 - A new project from the foundation (wave 1 finished, no active wave, decision mode auto, start hash 4a153fe, updated 2026-11-15 19:05)`, `README: Native mobile foundation`, `CI job: android (JDK 17, API 36 emulator, optional sample derivation, identity comparison, Kotlin binding + Compose UI)`, `Architecture compliance`, `Path ownership after derivation: product owned paths keep the product's side, foundation owned paths take the foundation's side, shared paths merge by hand`, `Mobile foundation scope (index)`, `apps/ios/Config/Identity.xcconfig (iOS identity file: APP_BUNDLE_IDENTIFIER, APP_DISPLAY_NAME, MARKETING_VERSION, CURRENT_PROJECT_VERSION)`, `Spec 0003: A new project from the foundation: product identity in two files, one init command, updates by merge (Accepted)`, `002 - Shared greeting contract (done)`, `test_generation.py`, `003 - Shared visual definitions (done)`, `R4: shared behavior lives in the core, the export stays thin, both clients stay on one contract`?**
  _High betweenness centrality (0.113) - this node is a cross-community bridge._
- **Why does `Hosted run 43723923953 foundation job result (ubuntu-24.04; locked build and scripts/test.sh passed with Rust 1.100.0 and Python 3.12: three Rust tests, 50 derivation tests, nine generator tests)` connect `test.sh` to `Foundation verification 2026-11-15`, `test_generation.py`, `DerivationTests`?**
  _High betweenness centrality (0.105) - this node is a cross-community bridge._
- **Are the 5 inferred relationships involving `Foundation verification 2026-11-15` (e.g. with `Record separately what compiled and what ran` and `Sub-session dev-f010-m1 (developer, opus-5-5 medium, archived): scope 010 Build it, all three milestones, Build plan steps 1 to 5 of spec 0004, all finished; owns both schemas, typography.json, the generated token files, three app files, the codegen fixtures and tests, five documents and verify.md; branch claude/dev-f010-m1-6599c9`) actually correct?**
  _`Foundation verification 2026-11-15` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `Spec 0004: Schemas free of sample names: one key of any name, a heading role, generator tests on their own sources (Status: Accepted, 2026-11-15); removes the two sample names (greeting_recipient, the greeting role) that the foundation schemas still require` (e.g. with `Hosted run 43723923953 on revision b64055a (pushed to main on 2026-11-15; the first hosted run after the localization schema stopped naming a key and the typography role greeting became heading; all three jobs passed)` and `Schemas free of sample names result (2026-11-15: test.sh passed with nine generator tests on Python 3.9.6 and --check passed; both apps built and passed the greeting tests in light and dark after the rename to typographyHeading; a scratch clone with the single key welcome_title generated, checked and tested)`) actually correct?**
  _`Spec 0004: Schemas free of sample names: one key of any name, a heading role, generator tests on their own sources (Status: Accepted, 2026-11-15); removes the two sample names (greeting_recipient, the greeting role) that the foundation schemas still require` has 7 INFERRED edges - model-reasoned connections that need verification._
- **What connects `.body`, `CoreImage`, `XCTest` to the rest of the system?**
  _88 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Foundation verification 2026-11-15` be split into smaller, more focused modules?**
  _Cohesion score 0.0803633822501747 - nodes in this community are weakly interconnected._