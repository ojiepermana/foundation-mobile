# Graph Report - mobile  (2026-11-15)

## Corpus Check
- 2 files · ~75,614 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1238 nodes · 3375 edges · 59 communities (57 shown, 2 thin omitted)
- Extraction: 78% EXTRACTED · 22% INFERRED · 0% AMBIGUOUS · INFERRED: 757 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

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
- Architecture Overview and Crate Owners
- Derivation Test Checkout Fixture
- Ownership Matrix and Repository Structure
- Init Command and Identity Files
- Spec 0003 Decision History
- Spec 0003 Acceptance Criteria
- Kotlin FFI Converters
- Spec 0001 Ownership Rules
- Workspace Scopes and Greeting Contract Scope
- Schemas and Sample Names
- Design System and Shared Resource Rules
- Empty Verification Record and Refusals
- Generated Native Tokens
- Real Checkout and Outside Git Tests
- Supported OS and Large Text Scopes
- Generator Tests and Accessibility Checks
- Design Principles and Token Conventions
- Config Schema
- Native Token Mapping and Text Scaling
- iOS App Shell
- Android App Shell
- Kotlin Rust Call Status
- Identity Value Sourcing
- Architecture Boundaries
- Derivation State Check Tests
- Native Greeting Scopes and Deferred Device Work
- Repository States and Default Identity
- Kotlin Handle Map and Lifting
- Design System Guide and Token Commands
- Origin Line and Identity Model
- README and Path Ownership
- Command Line Wrapper Tests
- Generated File and Drift Rules
- Kotlin FFI Integrity Checks
- Foundation Release Tags
- Android Rust Build Script
- Derivation Write Failure Tests
- Android Gradle Wrapper
- iOS Rust Build Script
- Documented Paths Test

## God Nodes (most connected - your core abstractions)
1. `Spec 0002: One planning path: a scope row first, then a spec` - 60 edges
2. `Foundation verification 2026-11-15` - 60 edges
3. `Spec 0001: One owner per responsibility, with rules kept beside the code` - 56 edges
4. `Spec 0003: A new project from the foundation: product identity in two files, one init command, updates by merge (Accepted)` - 55 edges
5. `UniffiLib` - 54 edges
6. `DerivationTests` - 46 edges
7. `Mobile foundation scope (index)` - 45 edges
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
- `Tokens, configuration and localization check` --references--> `GenerationTests`  [INFERRED]
  docs/quality/architecture-compliance.md → tooling/codegen/test_generation.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Coordination records of scope 009: the log, the general brief rules and the manual steps list, all tied to the scope row** — docs_scope_coordination_009_a_new_project_from_the_foundation_log, docs_scope_coordination_009_a_new_project_from_the_foundation_brief_umum, docs_scope_coordination_009_a_new_project_from_the_foundation_manual, docs_scope_root_009_a_new_project_from_the_foundation [EXTRACTED 1.00]
- **Wave 1 ownership split: developer on the verification record, checker on the verify.md ticks, tester on the derivation tests, with no overlap** — docs_scope_coordination_009_a_new_project_from_the_foundation_log_dev_f009_m3, docs_scope_coordination_009_a_new_project_from_the_foundation_log_chk_f009_verify, docs_scope_coordination_009_a_new_project_from_the_foundation_log_tst_f009_test, docs_quality_verification, docs_specs_root_0003_new_project_from_foundation_verify, tooling_derive_test_init_project, docs_scope_coordination_009_a_new_project_from_the_foundation_log_parallel_start [EXTRACTED 1.00]
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
- **One init command turns a foundation clone into a derived product: identity files, README origin line, empty verification record, removed knowledge graph** — scripts_init_project, tooling_derive_init_project, apps_ios_config_identity, apps_android_identity, docs_specs_root_0003_new_project_from_foundation_index_readme_origin_line, docs_specs_root_0003_new_project_from_foundation_index_empty_verification_record, tooling_derive_verification_record, docs_specs_root_0003_new_project_from_foundation_index_init_write_set, docs_specs_root_0003_new_project_from_foundation_index_repository_states_foundation_derived_mixed [EXTRACTED 1.00]
- **One planning path: a scope row first, then a spec before code, named by the agent instructions, the development rules and the repository structure** — docs_specs_root_0002_one_planning_path_decision_scope_row_then_spec, docs_specs_root_0002_one_planning_path_canonical_planning_pattern, docs_rules_development_rules_scope_row_then_spec, agents_scope_row_and_spec_before_code, docs_scope_root_007_one_planning_path, docs_scope_index, docs_architecture_repository_structure_docs_record_homes, docs_specs_root_0001_ownership_development_rules_r10_scope_row_and_spec_for_capability_spec_for_material_decision [EXTRACTED 1.00]
- **Spec triggers kept in their owner files: when a smaller change needs a spec** — docs_specs_root_0002_one_planning_path_trigger_owner_files, docs_rules_development_rules_spec_triggers_for_smaller_changes, docs_rules_service_rules_spec_for_new_crate_or_boundary, docs_quality_architecture_compliance_spec_for_architecture_change, docs_architecture_dependency_rules_new_edge_proposal, docs_contracts_ffi_conventions_compatibility_versioning, docs_decisions_adr_0001_foundation_revisit_conditions, docs_specs_root_0001_ownership_development_rules_spec_triggers [EXTRACTED 1.00]
- **Proof that derivation still works: --check state test, derivation unit test on a temporary copy in scripts/test.sh, CI identity comparison in both native jobs, manual workflow run with derived set** — docs_specs_root_0003_new_project_from_foundation_index_check_form, docs_specs_root_0003_new_project_from_foundation_index_test_form, docs_specs_root_0003_new_project_from_foundation_index_derivation_test, docs_specs_root_0003_new_project_from_foundation_index_ci_identity_comparison, docs_specs_root_0003_new_project_from_foundation_index_workflow_derived_input, scripts_test, github_workflows_foundation, github_workflows_foundation_derived_input, github_workflows_foundation_derive_sample_product_step, github_workflows_foundation_ios_identity_comparison_step, github_workflows_foundation_android_identity_comparison_step [INFERRED 0.85]
- **Design token pipeline from canonical JSON to native projections** — docs_design_system_token_conventions_canonical_token_sources, design_system_schemas_tokens_schema, scripts_generate_design_tokens, docs_design_system_platform_mapping_swiftui_token_projection, docs_design_system_platform_mapping_compose_token_projection, docs_quality_architecture_compliance_tokens_config_localization_check [INFERRED 0.85]
- **Neutral JSON sources validated and generated into native theme and string resources** — design_system_readme_token_files, design_system_readme_tokens_schema, shared_config_readme_foundation_json, shared_localization_readme_catalog_format, design_system_readme_generate_design_tokens_modes, tooling_codegen_requirements_fastjsonschema, design_system_readme_generated_semantic_api, shared_localization_readme_generated_native_strings [INFERRED 0.85]
- **Regenerate derived outputs with their canonical source, never hand-edit** — docs_rules_development_rules_regenerate_derived_files, docs_rules_design_system_rules_regenerate_projections, docs_quality_architecture_compliance_generated_drift_remediation, docs_rules_rust_rules_regenerate_after_signature_change, docs_rules_shared_resources_rules_generated_native_strings, docs_rules_anti_duplication_ffi_shapes_in_rust_export [INFERRED 0.85]
- **Manual step flow: a sub-session reports a manual step, the lead lists it, the user runs it and the checker ticks verify.md from the result** — docs_scope_coordination_009_a_new_project_from_the_foundation_brief_umum_manual_steps_rule, docs_scope_coordination_009_a_new_project_from_the_foundation_manual, docs_scope_coordination_009_a_new_project_from_the_foundation_manual_summary, docs_scope_coordination_009_a_new_project_from_the_foundation_manual_result_routing, docs_scope_coordination_009_a_new_project_from_the_foundation_log_chk_f009_verify, docs_specs_root_0003_new_project_from_foundation_verify, docs_scope_coordination_009_a_new_project_from_the_foundation_manual_f009_1, docs_scope_coordination_009_a_new_project_from_the_foundation_manual_f009_2 [INFERRED 0.85]
- **Tracer bullet greeting path from shared core to both native screens** — docs_scope_index_tracer_bullet_build_approach, docs_scope_root_002_shared_greeting_contract, docs_scope_root_002_shared_greeting_contract_one_string_in_one_string_out_contract, docs_scope_ios_001_native_ios_greeting, docs_scope_android_001_native_android_greeting, docs_scope_root_006_hosted_build_verification [INFERRED 0.85]
- **Verification evidence chain: local checks, hosted jobs and the verification record** — docs_scope_root_005_reproducible_local_builds_and_checks, docs_scope_root_006_hosted_build_verification, docs_scope_root_008_hosted_results_in_the_verification_record, docs_scope_root_008_hosted_results_in_the_verification_record_single_list_of_unverified_targets [INFERRED 0.85]
- **Coordination templates (brief, general rules, log, manual, report) and the scope 009 records filled from them** — claude_skills_coordinate_templates_brief, claude_skills_coordinate_templates_brief_umum, claude_skills_coordinate_templates_log, claude_skills_coordinate_templates_manual, claude_skills_coordinate_templates_report, docs_scope_coordination_009_a_new_project_from_the_foundation_brief_umum, docs_scope_coordination_009_a_new_project_from_the_foundation_log, docs_scope_coordination_009_a_new_project_from_the_foundation_manual [INFERRED 0.95]
- **Derived hosted run 43701289339 as evidence for AC-10: the workflow input, the derive step and both identity comparisons ran on hosted runners** — docs_quality_verification_hosted_run_43701289339, docs_quality_verification_derived_hosted_foundation_job_result, docs_quality_verification_derived_hosted_ios_job_result, docs_quality_verification_derived_hosted_android_job_result, github_workflows_foundation_derived_input, github_workflows_foundation_derive_sample_product_step, github_workflows_foundation_ios_identity_comparison_step, github_workflows_foundation_android_identity_comparison_step, docs_specs_root_0003_new_project_from_foundation_index_ac_10, docs_scope_coordination_009_a_new_project_from_the_foundation_log_hosted_run_43701289339 [INFERRED 0.95]

## Communities (59 total, 2 thin omitted)

### Community 0 - "Verification Record, CI Workflow and Policy Checks"
Cohesion: 0.05
Nodes (85): GreetingTest, GreetingUITests, UInt8, CIContext, Pass representative values through both generated languages, Android linkage and UI check (Linux CI job, emulator instrumentation), Cargo dependency and governance check, Limits of CI checks (+77 more)

### Community 1 - "Swift UniFFI Bindings"
Cohesion: 0.05
Nodes (64): Array, createReader(), createWriter(), Data, FfiConverter, FfiConverterPrimitive, FfiConverterRustBuffer, FfiConverterString (+56 more)

### Community 2 - "Coordinate Skill"
Cohesion: 0.07
Nodes (66): Agent workflow: before commit (run /graphify . --update, stage graphify-out with the change), Knowledge graph (graphify-out/, kept current with /graphify . --update), Role architect: closes a (spec) box or updates a spec so a developer can build without asking again; owns the feature's docs/specs/<NNNN-slug>/ folder; all code and docs/scope are forbidden, Accept this spec? handoff: the architect never answers it itself; it sends the spec path, Decision, key tradeoff and decisions taken to the lead, ends the turn with STATUS: needs-decision and continues after accept, Proposed scope block (blok scope usulan): Pointer line, Design it ticked, Build it with 2 to 5 nested milestones naming Build plan tasks and ACs, and closing boxes by tier, reported for the lead to paste into the scope, Role checker: two modes set by the brief, verify and review; ticks only the verify.md steps it ran or writes a file in docs/reviews; never fixes what it finds, Checker review mode: senior code review of a GA feature with fresh eyes, ranked findings in docs/reviews; only in a new session that has not written, verified or discussed the implementation, Checker verify mode: proves a milestone or feature behaves per spec by running the verify.md steps, scoped to the milestone section and the AC IDs in the brief, and sends failures to the owning developer (+58 more)

### Community 3 - "Kotlin FFI Library Loading"
Cohesion: 0.06
Nodes (34): Disposable, NoHandle, UniffiByValue, UniffiCallbackInterfaceClone, UniffiCallbackInterfaceFree, UniffiForeignFutureCompleteF32, UniffiForeignFutureCompleteF64, UniffiForeignFutureCompleteI16 (+26 more)

### Community 4 - "Scope 009 Coordination Records"
Cohesion: 0.08
Nodes (60): Report field 'Tafsiran AC' (developer, checker, tester): the reading taken for an ambiguous AC and its reason from the AC text or rationale.md, General brief rules (Aturan umum brief) for the sub-sessions of the scope 009 coordination: the fixed part of every brief; the brief wins where it differs, Always forbidden for sub-sessions: docs/scope/, AGENTS.md, graphify-out/, spec content other than the Status line and the verify.md ticks (checker only), other specs, and files outside the brief's allowed list, Decisions in auto mode: for an ambiguous AC read the spec's rationale.md, take the reading closest to the AC text and record it under Tafsiran AC; needs-decision goes to the lead only when the AC text or a spec decision must change, Commit rule for sub-sessions: one commit per step, an imperative English subject without prefix like the repository history, plus the Co-Authored-By trailer, Disk rule: 32 GiB free at the start; only the checker runs full native builds, one at a time; below 10 GiB free stop and report blocked; remove target/, build/ and apps/android/**/build and the temporary clone before reporting done, Hosted run 43701281055 (push trigger, on revision 4a153fe), Lead address: Mobile Foundation Scaffold [f5cda4]; full reports, questions and needs-decision go there through SendMessage (+52 more)

### Community 5 - "Kotlin UniFFI Library Calls"
Cohesion: 0.06
Nodes (3): UniffiLib, UniffiRustCallStatus, UniffiRustFutureContinuationCallback

### Community 6 - "Planning Path and Spec 0002"
Cohesion: 0.11
Nodes (45): Deferred work beyond Hello World, 007 - One planning path (done), The list of deferred work lives in one file, Former split planning path: docs/plans guide versus docs/scope (before this change), Follow-up (settled by spec 0002): R10 sent a new capability to docs/plans while features are tracked in docs/scope, Follow-up (settled by spec 0002): record keeping (ADR and plan naming, REQUIRED_DOCS membership, superseding, whether a spec satisfies R10), Premise: rule files stay authoritative; the spec records the decision, rule set and enforcement, not a second copy, Spec 0002: One planning path: a scope row first, then a spec (+37 more)

### Community 7 - "Rule Set and Platform Rules"
Cohesion: 0.08
Nodes (40): Generators consume neutral sources and never recover canonical values from native output, target/, build/ and Gradle build directories excluded from source control, Decision: keep generated source snapshots in version control and compare against fresh regeneration, Android rules, Checked-in Gradle wrapper, New ABI requires Rust cross-build and runtime test, Anti-duplication rules, Application code displays the binding's return value (+32 more)

### Community 8 - "Rust Core and Greeting Contract"
Cohesion: 0.11
Nodes (29): hello(), preserves_empty_names_and_whitespace(), String, main(), hello(), String, tests/contracts: Cargo integration tests for exported behavior, Core and FFI contract tests (locked Cargo tests) (+21 more)

### Community 9 - "Derivation Command"
Cohesion: 0.12
Nodes (30): Exception, check(), derive(), foundation_ref(), foundation_url(), git(), identity_text(), in_git() (+22 more)

### Community 10 - "Derivation Refusal and Write Set Tests"
Cohesion: 0.09
Nodes (15): DerivationTests, AC-6, AC-7: every accepted remote form becomes https without credentials; the…, AC-7: a local path remote, or no remote, is no usable foundation URL., AC-7: each input that breaks its rule is refused with exit 2, one line and no…, AC-7: a remote URL that is not UTF-8 is no usable foundation URL., AC-7: the in git test compares folders, not path spellings., AC-7: a derived checkout is refused., AC-5: the template on disk, filled with the sample values, is the empty record… (+7 more)

### Community 11 - "Derivation Run and Origin Line Tests"
Cohesion: 0.10
Nodes (13): AC-3, AC-5, AC-6, AC-8: the happy path writes every file and the checkout then…, AC-3: each override reaches only its own identity file, and --version reaches…, AC-3: with one override the other platform keeps --app-id., AC-3, AC-7: a value that starts with a hyphen is refused, and its equals form…, AC-6: without the flags the origin line takes the remote, HEAD and today., AC-6: the foundation remote wins over origin, and the highest release tag wins., AC-3: the example of the criterion, with no other flag, writes 0.1.0 and build…, AC-4: each file is replaced in the documented order, and graphify-out/ goes… (+5 more)

### Community 12 - "Development Rules and Spec Triggers"
Cohesion: 0.22
Nodes (27): Agent workflow: during implementation (place change in owning layer), Plan a new capability in the scope and write its spec under docs/specs before code, Dependency rules, New dependency edge needs an owning module, a use case and a test, Mobile contract (FFI conventions), Explicit application records and enums; private core/transport shapes mapped at the adapter, Async and cancellation conventions for future exports, Compatibility: version breaking contracts and coordinate regeneration, both apps and release (+19 more)

### Community 13 - "Resource Generator"
Cohesion: 0.14
Nodes (19): check_schema(), generate(), load(), projections(), Validate authoritative sources, then materialize or check their projections., unique_members(), validator(), native_text() (+11 more)

### Community 14 - "Kotlin RustBuffer Handling"
Cohesion: 0.14
Nodes (9): ByReference, ByValue, ForeignBytes, `hello`(), RustBuffer, uniffiTraitInterfaceCall(), uniffiTraitInterfaceCallWithError(), kotlin (+1 more)

### Community 15 - "Shared Settings and Localization"
Cohesion: 0.17
Nodes (20): Build-time generation: token JSON and locale JSON -> native theme inputs and localization resources, shared/config, shared/localization, shared/assets: owner of public settings, locale content and brand masters, Decision: neutral JSON tokens and validated shared sources generate native theme inputs and localization, Shared resources owner (build configuration, localization, brand assets), Deferred: a second language end to end, 004 - Shared settings, text and brand assets (done), shared/assets/ owns future brand artwork and its exports, Greeting sentence 'Hello, {name}!' formed in English by the core (+12 more)

### Community 16 - "Architecture Overview and Crate Owners"
Cohesion: 0.19
Nodes (22): Workspace edge: mobile-ffi depends on foundation-core (std-only core), Proc-macro exports define the cross-language API; bindgen feature gates host CLI deps, Architecture overview, foundation_core::hello (sole greeting formatter), Greeting call flow: SwiftUI/Compose -> generated binding -> C ABI/JNA -> mobile-ffi -> foundation-core, Color selection, font scaling, layout and accessibility run natively (no shared renderer), bindings/swift and bindings/kotlin: generated FFI source snapshots, crates/core: owner of shared behavior, domain rules and application validation (+14 more)

### Community 17 - "Derivation Test Checkout Fixture"
Cohesion: 0.14
Nodes (10): Checkout, AC-7: a modified or untracked file is refused, even when git status hides…, AC-4: a graph removal that fails names every changed path and the way back., AC-7: a mixed checkout is refused., AC-4: a checkout that has no graph changes only the two identity files,…, AC-6: a README.md of one line without a newline still ends with the title,…, AC-6: only a foundation-v tag that points exactly at HEAD names the ref;…, AC-7: a change only in the index, and a deleted tracked file, both make the… (+2 more)

### Community 18 - "Ownership Matrix and Repository Structure"
Cohesion: 0.22
Nodes (21): AGENTS.md: Working in the mobile foundation, Agent workflow: before editing (locate owner, contract, callers, tests), Agent workflow: before handoff (run checks, report commands and unverified targets), App trees do not import one another; core never calls platform UI, Ownership matrix, apps/android: owner of Android UI, presentation state and OS APIs, apps/ios: owner of Apple UI, presentation state and OS APIs, design-system/tokens and schemas: owner of canonical visual values and semantic roles (+13 more)

### Community 19 - "Init Command and Identity Files"
Cohesion: 0.19
Nodes (20): apps/android/identity.properties (Android identity file: applicationId, displayName, versionName, versionCode), apps/ios/Config/Identity.xcconfig (iOS identity file: APP_BUNDLE_IDENTIFIER, APP_DISPLAY_NAME, MARKETING_VERSION, CURRENT_PROJECT_VERSION), Product identity (display name, application IDs, app version): owned by apps/ios/Config/Identity.xcconfig and apps/android/identity.properties; consumed by the Xcode and Gradle builds and scripts/init-project.sh, Derivation only on a copy: init-project.sh with --name rewrites README.md and the verification record and removes graphify-out/, so that form runs only in a temporary clone in the session scratchpad; --check and --test are safe in the worktree, Init write set: the two identity files, the README title and origin line, the empty verification record and the removal of graphify-out/, Safe write order: nothing is written until every check passes, contents are built in memory, each file moves into place with os.replace, graphify-out/ is removed last, git restore . is the way back, Force: shared/config/README.md keeps bundle and application IDs in Xcode or Gradle, not in the shared config schema, Recommendation: the identity files stay native (+12 more)

### Community 20 - "Spec 0003 Decision History"
Cohesion: 0.19
Nodes (21): apps/ios/MobileFoundation.xcodeproj/project.pbxproj (Xcode project file), Decision: a product is a clone that changes only its display name, application ID and version through scripts/init-project.sh, keeps every other name, starts with an empty verification record and merges foundation-v tags, Names the foundation keeps: MobileFoundation project, targets and scheme, rootProject.name, crates foundation-core and mobile-ffi, mobile_ffi namespace, Kotlin packages, FoundationTokens, FoundationTheme, foundation_strings.xml, foundation.json, the workflow file, Tradeoff: later foundation scope rows and specs do not flow into products; the reason behind a new foundation rule is read in the foundation repository, Tradeoff: the Linux proof builds nothing, so a change that breaks a derived native build can sit on main until the next manual derived run, Spec 0003 rationale: decision history of the new project spec (context, options considered, rationale), Recommendation: the command does not edit scope rows, Force: foundation fixes must reach products (a fix typed again in each product will not be applied) (+13 more)

### Community 21 - "Spec 0003 Acceptance Criteria"
Cohesion: 0.21
Nodes (21): Ticked in wave 1: 009 Test it, from the tst-f009-test report done (21 to 50 tests, AC-3 to AC-9 each have a test carrying its ID, commit dc9a8d9, merged in 0aa1d5c); on main with the merge staged there were no conflict markers and scripts/test.sh exited 0, Build steps (009): identity file per platform (AC-1, AC-2, done), init command with state check and unit tests (AC-3 to AC-9, done), workflow derived input and identity comparison (AC-10, done), README path and document updates (AC-11, AC-12, done), Spec 0003: A new project from the foundation: product identity in two files, one init command, updates by merge (Accepted), AC-1: both apps carry the same default identity, read from Identity.xcconfig and identity.properties, stated nowhere else under apps/, AC-11: README.md has a section with the full path from clone to first results, path ownership, taking a later release and foundation tagging, AC-2: with the default identity scripts/test.sh passes, both apps build and the greeting tests pass in both appearances, AC-3: init-project.sh --name --app-id writes name, ID, version 0.1.0 and build 1 into both identity files, with per-value overrides, AC-4: the write set is exactly the two identity files, README.md, the verification record and the removed graphify-out/ files; nothing is renamed (+13 more)

### Community 22 - "Kotlin FFI Converters"
Cohesion: 0.21
Nodes (7): FfiConverter, FfiConverterRustBuffer, FfiConverterString, FfiType, ByteBuffer, KotlinType, ULong

### Community 23 - "Spec 0001 Ownership Rules"
Cohesion: 0.23
Nodes (20): Deferred: a contract beyond one string (record, typed error, async call), Spec 0001: One owner per responsibility, with rules kept beside the code, Decision: one owner per responsibility in an ownership matrix, topic-sized rule files, short AGENTS.md entry point, automated checks only where a machine is reliable, An exact dependency list, not a deny list, Follow-up: decide whether checks must pass before a change reaches main (branch rule or local hook), Follow-up: confirm or correct the inferred rationale, Force: coding agents are regular contributors and act on what they load, Force: generated files sit beside hand-written code (edits there are lost or hide a mismatch) (+12 more)

### Community 24 - "Workspace Scopes and Greeting Contract Scope"
Cohesion: 0.20
Nodes (18): Progress is recorded in the scope row; what ran is recorded in the verification record, Android scope, Android app owns its screen, appearance changes and native localization lookup, Mobile foundation scope (index), Beta workflow (/check verify, then /test), Scope status legend and file numbering convention, Tracer Bullet build approach, Workspace completion at a glance: shared foundation 9 of 10 (open 010), iOS 1 of 2, Android 1 of 2 (+10 more)

### Community 25 - "Schemas and Sample Names"
Cohesion: 0.15
Nodes (17): Canonical token schema (tokens.schema.json), Draft 7 schema and native mappings updated together, Draft 7 schemas in shared/specifications, 010 - Schemas free of sample names (planned, needs a decision), Replace the greeting with a first feature without editing a foundation schema, Foundation schemas require sample names: the greeting_recipient key in the localization schema and the greeting typography role in the token schema, Follow-up: two foundation schemas still require sample names (greeting_recipient, the greeting role); this deserves its own scope row, greeting_recipient (+9 more)

### Community 26 - "Design System and Shared Resource Rules"
Cohesion: 0.20
Nodes (17): Stable role names or same-change migration, Generated drift remediation, Tokens, configuration and localization check, Shared visual decisions and translations are generator inputs, Design system rules, Drift check plus verification in both appearances and larger text sizes, Regenerate native projections in the same change, Public role name changes require migrating both consumers (+9 more)

### Community 27 - "Empty Verification Record and Refusals"
Cohesion: 0.14
Nodes (16): A new product would carry the foundation's verification record, scope rows, hosted run links and knowledge graph as its own, Empty verification record: names the product, foundation URL and ref, lists every target as still unverified, holds no hosted run link, Positive: products install side by side under their own name and ID, a foundation fix reaches every product by one merge, a half derived checkout fails scripts/test.sh, records start empty, the identity mismatch is gone, every native run proves the built identity, Refusals: one line naming the input and the rule, exit 2, nothing written, User stories: one command names a clone, foundation releases arrive by merge, the verification record lists only what ran here, every push proves the command still works, Recommendation: --check does not look for hosted run links, Recommendation: the command refuses to run on a derived checkout, Force: a copy inherits claims it never earned (the verification record and the scope index name a hosted run in the foundation repository) (+8 more)

### Community 28 - "Generated Native Tokens"
Cohesion: 0.17
Nodes (12): FoundationTokens, Palette, FoundationTokens, Palette, CGFloat, Color, ColorScheme, 003 - Shared visual definitions (done) (+4 more)

### Community 29 - "Real Checkout and Outside Git Tests"
Cohesion: 0.14
Nodes (9): Unit tests create their own repository in a temporary folder with isolated git configuration; no test touches the real checkout, OutsideGitTests, Checks for the derivation command: every write, every refusal and both clean…, AC-9: the derivation proof is skipped, with its reason, in a checkout that is…, AC-7: outside git both foundation values are required., AC-7: a folder inside another repository counts as outside git., Run the checked in command on a temporary copy of this checkout. The checkout…, AC-9: the copy's own command derives the copy, which then reads derived and… (+1 more)

### Community 30 - "Supported OS and Large Text Scopes"
Cohesion: 0.23
Nodes (12): CoreImage, Android 002 - Lowest supported Android and large text (planned), Declared Android minimum API 24 not yet exercised, Android largest font scale check, Native text style supporting Dynamic Type, iOS simulator results (iPhone 17 on iOS 27.0 local, iOS 26.5 hosted), iOS 002 - Lowest supported iOS and large text (planned), Declared iOS 17 deployment target not yet exercised (+4 more)

### Community 31 - "Generator Tests and Accessibility Checks"
Cohesion: 0.18
Nodes (8): Accessibility (design system), Status conveyed by text or semantics, not color alone, Honor platform reduced-motion setting, Text contrast check (4.5:1 minimum), W3C WCAG 2.2 contrast minimum guidance, Design system and resources result (seven generator tests), Light and dark text meet the documented contrast threshold, GenerationTests

### Community 32 - "Design Principles and Token Conventions"
Cohesion: 0.21
Nodes (14): Per-target reading order and screen-reader review, Native controls styled with semantic tokens, Design principles, Canonical JSON propagates through code generation, Design definitions compile independently of Cargo and UniFFI, Layout, text measurement, gestures and focus stay in presentation, Semantic names for decisions both apps share, Token conventions (+6 more)

### Community 33 - "Config Schema"
Cohesion: 0.14
Nodes (13): defaultLocale, schemaVersion, additionalProperties, const, properties, defaultLocale, schemaVersion, required (+5 more)

### Community 34 - "Native Token Mapping and Text Scaling"
Cohesion: 0.29
Nodes (13): System text scaling via generated text styles, Native token mapping, Compose sp mapping of logical text units, Jetpack Compose token projection (FoundationTokens), Dynamic Type mapping of headline and reading scales, Logical spacing units adapt to display density, spacingPage role, SwiftUI token projection (FoundationTokens) (+5 more)

### Community 35 - "iOS App Shell"
Cohesion: 0.18
Nodes (9): App, MobileFoundationApp, .body, GreetingScreen, .body, String, Scene, SwiftUI (+1 more)

### Community 36 - "Android App Shell"
Cohesion: 0.23
Nodes (8): MainActivity, FoundationTheme(), GreetingScreen(), Bundle, ComponentActivity, Native components guidelines, Greeting as a single text element, Reusable native component (introduced on demand)

### Community 37 - "Kotlin Rust Call Status"
Cohesion: 0.23
Nodes (7): E, uniffiCheckCallStatus(), UniffiForeignFutureCompleteVoid, uniffiRustCall(), UniffiRustCallStatusErrorHandler, uniffiRustCallWithError(), U

### Community 38 - "Identity Value Sourcing"
Cohesion: 0.29
Nodes (9): apps/android/app/src/main/AndroidManifest.xml, apps/android/app/src/main/res/values/app.xml (the app_name string leaves this file; the label comes from the appLabel manifest placeholder), apps/ios/Config/App.xcconfig (iOS app build settings), apps/ios/Config/Project.xcconfig (iOS project build settings), Android build reads identity.properties: app/build.gradle.kts loads applicationId, versionName and versionCode, the label reaches the manifest as the appLabel placeholder, namespace stays foundation.mobile, iOS build reads Identity.xcconfig: Project.xcconfig includes it, App.xcconfig maps the bundle ID and display name, the UI test bundle ID is derived as $(APP_BUNDLE_IDENTIFIER).uitests, Force: identity is spread over files the foundation keeps editing (App.xcconfig, Project.xcconfig, project.pbxproj, app/build.gradle.kts, res/values/app.xml), Recommendation: one identity file per platform that the foundation never edits again (+1 more)

### Community 39 - "Architecture Boundaries"
Cohesion: 0.24
Nodes (11): Architecture boundaries, Documented capability boundary; adapters need an actual caller, Layer: design system (generated Swift/Kotlin values as shared visual vocabulary), Layer: native platform integration (Swift owns Apple services, Kotlin owns Android services), Layer: native presentation (views render, adapt to appearance, handle events), Layer: resources and tooling (build-host validation and generation), Layer: shared Rust (core owns behavior, FFI crate maps exports), Create a platform adapter directory only when a feature needs an OS capability (+3 more)

### Community 40 - "Derivation State Check Tests"
Cohesion: 0.18
Nodes (5): AC-8: every departure from the exact form is a mismatch that names the file and…, AC-8: a derived checkout that lost one signal names that signal., AC-8: an identity file that is not UTF-8, and a missing README.md, are…, AC-8: changing only applicationId names that file and key against a foundation…, AC-8: default IDs under an origin line, and a second origin line, each make a…

### Community 41 - "Native Greeting Scopes and Deferred Device Work"
Cohesion: 0.27
Nodes (10): Android 001 - Native Android greeting (existing), API 36 emulator results (arm64 local, x86_64 hosted) in light and dark, Android app packages both supported CPU architectures, Android physical device coverage unverified, 16 KiB memory page packaging, Deferred: signing, physical device runs and store delivery, iOS 001 - Native iOS greeting (existing), Greeting exposed to accessibility in light and dark appearance (+2 more)

### Community 42 - "Repository States and Default Identity"
Cohesion: 0.29
Nodes (10): The two apps disagree on their own identity (iOS dev.foundation.mobile / Mobile Foundation / 1.0, Android foundation.mobile / Foundation / 0.1.0), init-project.sh --check: prints foundation or derived (exit 0) or names each mismatch in a mixed state (exit 1), Default foundation identity: dev.foundation.mobile, Mobile Foundation, version 0.1.0, build 1, Follow-up: decide in the release path spec whether the iOS and Android versions must match, and add that test to --check if they must, Key invariants: a checkout is foundation or derived, each identity value has one home per platform, the command renames nothing, never runs on a derived or mixed checkout, never changes git state, and foundation tags match foundation-v*, Neutral: the iOS version moves from 1.0 to 0.1.0 to match Android; the Cargo workspace version is not an app version and is left alone, Repository states: foundation (both IDs default, no origin line), derived (neither ID default, valid origin line), mixed (anything else), Tradeoff: the Android application ID changes from foundation.mobile to dev.foundation.mobile, leaving an old debug build as a separate app (+2 more)

### Community 43 - "Kotlin Handle Map and Lifting"
Cohesion: 0.42
Nodes (4): InternalException, T, UniffiHandleMap, UniffiNullRustCallStatusErrorHandler

### Community 44 - "Design System Guide and Token Commands"
Cohesion: 0.36
Nodes (8): Design system guide, generate-design-tokens.sh modes: write, --check (drift), --test (failure cases), Generated semantic token API consumed by native apps, Five canonical token JSON files (primitives and semantic aliases), tokens.schema.json: single Draft 7 document keyed by filename stem, SHA-pinned GitHub Actions with read-only contents permission, Shared build and generation commands, fastjsonschema==2.21.2 (sha256 hash-pinned schema validator)

### Community 45 - "Origin Line and Identity Model"
Cohesion: 0.28
Nodes (9): Done when (009): one recorded decision, one command, a hosted check on a temporary copy, clean inherited records, recorded foundation revision, Follow-up: allow a localized display name when a product needs one (it would move from the identity files to the catalogs), Foundation URL sourcing and normalization: --foundation-url, else the foundation remote, else origin; https, http, ssh and user@host:path forms written as https without user, token, .git or trailing slash, Input validation rules (re.ASCII patterns for app ID, platform overrides, display name of 1 to 30 code points, version, build, foundation URL, ref and date), Product identity data model: application ID, display name, version and build in two identity files, one origin line, two repository states, README origin line on line 3: Started from the [mobile foundation](<URL>) at `<ref>` on <date>., Security model: reads and writes only inside the checkout, no network and no secret, credentials stripped from the remote URL, inputs checked before any write, signing material stays out of the repository (R12), Tradeoff: display names are limited to letters, digits, space, period, hyphen and apostrophe until a product needs more (+1 more)

### Community 46 - "README and Path Ownership"
Cohesion: 0.39
Nodes (9): Follow-up: build the command that takes a foundation release (fetch, merge, apply the ownership table) when the first release is merged into a product, Follow-up: decide where dependency update bots run (a bot in every product changes foundation owned files and will conflict with merges), Path ownership after derivation: product owned paths keep the product's side, foundation owned paths take the foundation's side, shared paths merge by hand, README section 'Start a project from this foundation': clone at a tag, create a branch, rename the remote, run the command, add origin, rebuild the graph, mark inherited rows existing, commit, record first results, Take a later foundation release: git fetch foundation --tags, git merge foundation-vX.Y.Z, keep the product's side on product owned paths, rebuild the graph, run every check, Tradeoff: every merge of a foundation release reports conflicts on product owned paths, resolved by hand until the sync command exists, Premise: four coupled decisions in one spec (which names change, how a copy is made, what happens to inherited records, how updates arrive), Take a later foundation release (git fetch foundation --tags, git merge foundation-vX.Y.Z, keep the product's side on product owned paths) (+1 more)

### Community 47 - "Command Line Wrapper Tests"
Cohesion: 0.31
Nodes (5): CommandLineTests, Run the copied scripts/init-project.sh from another folder, as a person or CI…, AC-3, AC-8: the wrapper finds its own checkout, prints the five changed paths,…, AC-7: through the wrapper a refusal exits 2, prints one line on stderr only,…, AC-8: through the wrapper --check exits 1 and names the mismatch on stderr.

### Community 48 - "Generated File and Drift Rules"
Cohesion: 0.60
Nodes (5): Never hand-edit generated files, Derived file rule: change the canonical input and regenerate every output in the same review, Regenerated token files match the checked in copies, Drift detection for checked-in bindings and resources (stale, edited and missing generated files), R5: a generated file is never edited by hand; change the source and regenerate every output

### Community 49 - "Kotlin FFI Integrity Checks"
Cohesion: 0.60
Nodes (3): IntegrityCheckingUniffiLib, uniffiCheckApiChecksums(), uniffiCheckContractApiVersion()

### Community 50 - "Foundation Release Tags"
Cohesion: 0.50
Nodes (5): Foundation ref resolution: --foundation-ref, else the highest foundation-v* tag exactly at HEAD, else the full HEAD commit ID, Neutral: /develop moves the spec to In Progress and Accepted with scope row 009; creating the first tag foundation-v0.1.0 is the maintainer's step, Release the foundation: run the workflow by hand with derived set, then push an annotated foundation-vMAJOR.MINOR.PATCH tag on main, Recommendation: tags are named foundation-vMAJOR.MINOR.PATCH, Release the foundation (foundation repository only): run the workflow by hand with derived set, then create and push an annotated tag foundation-vMAJOR.MINOR.PATCH on main

### Community 51 - "Android Rust Build Script"
Cohesion: 0.40
Nodes (4): CARGO_TARGET_AARCH64_LINUX_ANDROID_LINKER, CARGO_TARGET_X86_64_LINUX_ANDROID_LINKER, PATH, build-android-rust.sh script

### Community 53 - "Android Gradle Wrapper"
Cohesion: 0.83
Nodes (3): gradlew script, die(), warn()

### Community 54 - "iOS Rust Build Script"
Cohesion: 0.50
Nodes (3): CARGO_TARGET_DIR, PATH, build-ios-rust.sh script

## Knowledge Gaps
- **66 isolated node(s):** `NoHandle`, `UniffiWithHandle`, `Explicit application records and enums; private core/transport shapes mapped at the adapter`, `apiChecksumMismatch`, `contractVersionMismatch` (+61 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Foundation verification 2026-11-15` connect `Verification Record, CI Workflow and Policy Checks` to `Scope 009 Coordination Records`, `Planning Path and Spec 0002`, `Rule Set and Platform Rules`, `Rust Core and Greeting Contract`, `Native Greeting Scopes and Deferred Device Work`, `Development Rules and Spec Triggers`, `README and Path Ownership`, `Shared Settings and Localization`, `Ownership Matrix and Repository Structure`, `Init Command and Identity Files`, `Spec 0003 Acceptance Criteria`, `Workspace Scopes and Greeting Contract Scope`, `Empty Verification Record and Refusals`, `Generated Native Tokens`, `Generator Tests and Accessibility Checks`?**
  _High betweenness centrality (0.116) - this node is a cross-community bridge._
- **Why does `.body` connect `iOS App Shell` to `Swift UniFFI Bindings`?**
  _High betweenness centrality (0.099) - this node is a cross-community bridge._
- **Why does `hello()` connect `Swift UniFFI Bindings` to `iOS App Shell`?**
  _High betweenness centrality (0.099) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Foundation verification 2026-11-15` (e.g. with `Record separately what compiled and what ran` and `tooling/derive/verification-record.md (empty verification record template for a derived product)`) actually correct?**
  _`Foundation verification 2026-11-15` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `NoHandle`, `UniffiWithHandle`, `Explicit application records and enums; private core/transport shapes mapped at the adapter` to the rest of the system?**
  _66 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Verification Record, CI Workflow and Policy Checks` be split into smaller, more focused modules?**
  _Cohesion score 0.05490734385724091 - nodes in this community are weakly interconnected._
- **Should `Swift UniFFI Bindings` be split into smaller, more focused modules?**
  _Cohesion score 0.05444596443228454 - nodes in this community are weakly interconnected._