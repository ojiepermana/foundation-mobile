# Graph Report - mobile  (2026-11-15)

## Corpus Check
- 7 files · ~75,404 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1233 nodes · 3351 edges · 52 communities (51 shown, 1 thin omitted)
- Extraction: 78% EXTRACTED · 22% INFERRED · 0% AMBIGUOUS · INFERRED: 752 edges (avg confidence: 0.89)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Swift UniFFI Bindings
- Planning Path, Scope Index and Policy Checks
- Ownership Matrix, Architecture and Shared Resources
- Design System, Schemas and Generator Checks
- Coordinate Skill
- Kotlin FFI Library Loading
- Kotlin UniFFI Library Calls
- CI Workflow and Derived Run
- test.sh, Init Checks and Verify Steps
- Verification Record and UI Tests
- Scope 009 Coordination Records
- Derivation Command
- Spec 0003 Decision History and Init Command
- Rust Core and Greeting Contract
- Native Greeting and Supported OS Scopes
- Derivation Run and Origin Line Tests
- Platform Rules and Native App Shells
- Spec 0003 and Starting a Product
- Resource Generator
- Derivation Refusal Tests
- Kotlin FFI Converters
- Spec 0001 Ownership Rules
- Kotlin RustBuffer Handling
- Derivation Test Checkout Fixture
- Product Identity Files and Criteria
- Architecture Compliance and Spec Triggers
- Identity Value Sourcing
- Workspace Scopes and Visual Definitions
- Derivation Write Set Tests
- Empty Verification Record and Refusals
- Config Schema
- Generated Native Tokens
- Kotlin Rust Call Status
- Derivation State Check Tests
- Rule Set and Generated File Rules
- Anti-Duplication and Review-Only Rules
- Android App Shell
- Kotlin Handle Map and Lifting
- Command Line Wrapper Tests
- Mobile Contract Extension Conventions
- Real Checkout Derivation Tests
- Shared Greeting Contract Tests
- iOS Greeting UI Test Helpers
- Kotlin FFI Integrity Checks
- Android Rust Build Script
- Derivation Write Failure Tests
- Android Gradle Wrapper
- iOS Rust Build Script
- Hosted Build Verification Scope

## God Nodes (most connected - your core abstractions)
1. `Spec 0002: One planning path: a scope row first, then a spec` - 60 edges
2. `Foundation verification 2026-11-15` - 59 edges
3. `Spec 0001: One owner per responsibility, with rules kept beside the code` - 56 edges
4. `UniffiLib` - 54 edges
5. `Spec 0003: A new project from the foundation: product identity in two files, one init command, updates by merge (Accepted)` - 54 edges
6. `DerivationTests` - 46 edges
7. `Mobile foundation scope (index)` - 45 edges
8. `Decision: a new capability is planned as a scope row and designed in a spec before code; docs/plans and new ADRs are retired in a single change` - 38 edges
9. `Spec 0003 rationale: decision history of the new project spec (context, options considered, rationale)` - 35 edges
10. `Rollout: one change in fifteen ordered steps (rules, AGENTS.md, architecture docs, README, validator, delete docs/plans, scope files, spec 0001, knowledge graph)` - 33 edges

## Surprising Connections (you probably didn't know these)
- `Greeting is a pure function; no application services exist` --references--> `hello()`  [INFERRED]
  docs/rules/service-rules.md → crates/core/src/lib.rs
- `Derived hosted run android job result (same derive command; Gradle 9.3.1 assembled the derived debug app; identity file and built app matched; two instrumentation tests passed with night mode off and on)` --references--> `GreetingTest`  [INFERRED]
  docs/quality/verification.md → apps/android/app/src/androidTest/kotlin/foundation/mobile/GreetingTest.kt
- `Product identity result (2026-11-15: test.sh passed with --check printing foundation and --test passing 21 unit tests; both apps carried dev.foundation.mobile, Mobile Foundation, 0.1.0, build 1; a copy derived as Zoë's Proof built and matched its identity file)` --references--> `GreetingTest`  [INFERRED]
  docs/quality/verification.md → apps/android/app/src/androidTest/kotlin/foundation/mobile/GreetingTest.kt
- `Derived hosted run ios job result (derive step ran init-project.sh as Zoë's Proof with dev.example.derived; Xcode 26.5 built the derived app; identity file and built app matched; greeting test passed in light and dark on iOS 26.5)` --references--> `GreetingUITests`  [INFERRED]
  docs/quality/verification.md → apps/ios/UITests/GreetingUITests.swift
- `Product identity result (2026-11-15: test.sh passed with --check printing foundation and --test passing 21 unit tests; both apps carried dev.foundation.mobile, Mobile Foundation, 0.1.0, build 1; a copy derived as Zoë's Proof built and matched its identity file)` --references--> `GreetingUITests`  [INFERRED]
  docs/quality/verification.md → apps/ios/UITests/GreetingUITests.swift

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **One init command turns a foundation clone into a derived product: identity files, README origin line, empty verification record, removed knowledge graph** — scripts_init_project, tooling_derive_init_project, apps_ios_config_identity, apps_android_identity, docs_specs_root_0003_new_project_from_foundation_index_readme_origin_line, docs_specs_root_0003_new_project_from_foundation_index_empty_verification_record, tooling_derive_verification_record, docs_specs_root_0003_new_project_from_foundation_index_init_write_set, docs_specs_root_0003_new_project_from_foundation_index_repository_states_foundation_derived_mixed [EXTRACTED 1.00]
- **Proof that derivation still works: --check state test, derivation unit test on a temporary copy in scripts/test.sh, CI identity comparison in both native jobs, manual workflow run with derived set** — docs_specs_root_0003_new_project_from_foundation_index_check_form, docs_specs_root_0003_new_project_from_foundation_index_test_form, docs_specs_root_0003_new_project_from_foundation_index_derivation_test, docs_specs_root_0003_new_project_from_foundation_index_ci_identity_comparison, docs_specs_root_0003_new_project_from_foundation_index_workflow_derived_input, scripts_test, github_workflows_foundation, github_workflows_foundation_derived_input, github_workflows_foundation_derive_sample_product_step, github_workflows_foundation_ios_identity_comparison_step, github_workflows_foundation_android_identity_comparison_step [INFERRED 0.85]
- **Tracer bullet greeting path from shared core to both native screens** — docs_scope_index_tracer_bullet_build_approach, docs_scope_root_002_shared_greeting_contract, docs_scope_root_002_shared_greeting_contract_one_string_in_one_string_out_contract, docs_scope_ios_001_native_ios_greeting, docs_scope_android_001_native_android_greeting, docs_scope_root_006_hosted_build_verification [INFERRED 0.85]
- **Coordination records of scope 009: the log, the general brief rules and the manual steps list, all tied to the scope row** — docs_scope_coordination_009_a_new_project_from_the_foundation_log, docs_scope_coordination_009_a_new_project_from_the_foundation_brief_umum, docs_scope_coordination_009_a_new_project_from_the_foundation_manual, docs_scope_root_009_a_new_project_from_the_foundation [EXTRACTED 1.00]
- **Wave 1 ownership split: developer on the verification record, checker on the verify.md ticks, tester on the derivation tests, with no overlap** — docs_scope_coordination_009_a_new_project_from_the_foundation_log_dev_f009_m3, docs_scope_coordination_009_a_new_project_from_the_foundation_log_chk_f009_verify, docs_scope_coordination_009_a_new_project_from_the_foundation_log_tst_f009_test, docs_quality_verification, docs_specs_root_0003_new_project_from_foundation_verify, tooling_derive_test_init_project, docs_scope_coordination_009_a_new_project_from_the_foundation_log_parallel_start [EXTRACTED 1.00]
- **Manual step flow: a sub-session reports a manual step, the lead lists it, the user runs it and the checker ticks verify.md from the result** — docs_scope_coordination_009_a_new_project_from_the_foundation_brief_umum_manual_steps_rule, docs_scope_coordination_009_a_new_project_from_the_foundation_manual, docs_scope_coordination_009_a_new_project_from_the_foundation_manual_summary, docs_scope_coordination_009_a_new_project_from_the_foundation_manual_result_routing, docs_scope_coordination_009_a_new_project_from_the_foundation_log_chk_f009_verify, docs_specs_root_0003_new_project_from_foundation_verify, docs_scope_coordination_009_a_new_project_from_the_foundation_manual_f009_1, docs_scope_coordination_009_a_new_project_from_the_foundation_manual_f009_2 [INFERRED 0.85]
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
- **Spec triggers kept in their owner files: when a smaller change needs a spec** — docs_specs_root_0002_one_planning_path_trigger_owner_files, docs_rules_development_rules_spec_triggers_for_smaller_changes, docs_rules_service_rules_spec_for_new_crate_or_boundary, docs_quality_architecture_compliance_spec_for_architecture_change, docs_architecture_dependency_rules_new_edge_proposal, docs_contracts_ffi_conventions_compatibility_versioning, docs_decisions_adr_0001_foundation_revisit_conditions, docs_specs_root_0001_ownership_development_rules_spec_triggers [EXTRACTED 1.00]
- **Design token pipeline from canonical JSON to native projections** — docs_design_system_token_conventions_canonical_token_sources, design_system_schemas_tokens_schema, scripts_generate_design_tokens, docs_design_system_platform_mapping_swiftui_token_projection, docs_design_system_platform_mapping_compose_token_projection, docs_quality_architecture_compliance_tokens_config_localization_check [INFERRED 0.85]
- **Neutral JSON sources validated and generated into native theme and string resources** — design_system_readme_token_files, design_system_readme_tokens_schema, shared_config_readme_foundation_json, shared_localization_readme_catalog_format, design_system_readme_generate_design_tokens_modes, tooling_codegen_requirements_fastjsonschema, design_system_readme_generated_semantic_api, shared_localization_readme_generated_native_strings [INFERRED 0.85]
- **Regenerate derived outputs with their canonical source, never hand-edit** — docs_rules_development_rules_regenerate_derived_files, docs_rules_design_system_rules_regenerate_projections, docs_quality_architecture_compliance_generated_drift_remediation, docs_rules_rust_rules_regenerate_after_signature_change, docs_rules_shared_resources_rules_generated_native_strings, docs_rules_anti_duplication_ffi_shapes_in_rust_export [INFERRED 0.85]
- **Verification evidence chain: local checks, hosted jobs and the verification record** — docs_scope_root_005_reproducible_local_builds_and_checks, docs_scope_root_006_hosted_build_verification, docs_scope_root_008_hosted_results_in_the_verification_record, docs_scope_root_008_hosted_results_in_the_verification_record_single_list_of_unverified_targets [INFERRED 0.85]
- **Coordination templates (brief, general rules, log, manual, report) and the scope 009 records filled from them** — claude_skills_coordinate_templates_brief, claude_skills_coordinate_templates_brief_umum, claude_skills_coordinate_templates_log, claude_skills_coordinate_templates_manual, claude_skills_coordinate_templates_report, docs_scope_coordination_009_a_new_project_from_the_foundation_brief_umum, docs_scope_coordination_009_a_new_project_from_the_foundation_log, docs_scope_coordination_009_a_new_project_from_the_foundation_manual [INFERRED 0.95]
- **Derived hosted run 43701289339 as evidence for AC-10: the workflow input, the derive step and both identity comparisons ran on hosted runners** — docs_quality_verification_hosted_run_43701289339, docs_quality_verification_derived_hosted_foundation_job_result, docs_quality_verification_derived_hosted_ios_job_result, docs_quality_verification_derived_hosted_android_job_result, github_workflows_foundation_derived_input, github_workflows_foundation_derive_sample_product_step, github_workflows_foundation_ios_identity_comparison_step, github_workflows_foundation_android_identity_comparison_step, docs_specs_root_0003_new_project_from_foundation_index_ac_10, docs_scope_coordination_009_a_new_project_from_the_foundation_log_hosted_run_43701289339 [INFERRED 0.95]

## Communities (52 total, 1 thin omitted)

### Community 0 - "Swift UniFFI Bindings"
Cohesion: 0.05
Nodes (68): App, MobileFoundationApp, .body, Array, createReader(), createWriter(), Data, FfiConverter (+60 more)

### Community 1 - "Planning Path, Scope Index and Policy Checks"
Cohesion: 0.07
Nodes (85): AGENTS.md: Working in the mobile foundation, Agent workflow: before handoff (run checks, report commands and unverified targets), Agent workflow: during implementation (place change in owning layer), Plan a new capability in the scope and write its spec under docs/specs before code, Architecture overview, docs/ and root AGENTS.md: architecture, decision records, scope and agent workflow, docs/ record homes: docs/scope (what to build and its status), docs/specs (design and decision records), docs/decisions (the founding decision), ADR 0001: Native apps with a shared Rust core (+77 more)

### Community 2 - "Ownership Matrix, Architecture and Shared Resources"
Cohesion: 0.06
Nodes (76): Never hand-edit generated files, Design system guide, generate-design-tokens.sh modes: write, --check (drift), --test (failure cases), Generated semantic token API consumed by native apps, Five canonical token JSON files (primitives and semantic aliases), tokens.schema.json: single Draft 7 document keyed by filename stem, Architecture boundaries, Documented capability boundary; adapters need an actual caller (+68 more)

### Community 3 - "Design System, Schemas and Generator Checks"
Cohesion: 0.05
Nodes (64): Canonical token schema (tokens.schema.json), Accessibility (design system), Per-target reading order and screen-reader review, Status conveyed by text or semantics, not color alone, Honor platform reduced-motion setting, System text scaling via generated text styles, Text contrast check (4.5:1 minimum), W3C WCAG 2.2 contrast minimum guidance (+56 more)

### Community 4 - "Coordinate Skill"
Cohesion: 0.07
Nodes (70): Agent workflow: before commit (run /graphify . --update, stage graphify-out with the change), Knowledge graph (graphify-out/, kept current with /graphify . --update), Role architect: closes a (spec) box or updates a spec so a developer can build without asking again; owns the feature's docs/specs/<NNNN-slug>/ folder; all code and docs/scope are forbidden, Accept this spec? handoff: the architect never answers it itself; it sends the spec path, Decision, key tradeoff and decisions taken to the lead, ends the turn with STATUS: needs-decision and continues after accept, Proposed scope block (blok scope usulan): Pointer line, Design it ticked, Build it with 2 to 5 nested milestones naming Build plan tasks and ACs, and closing boxes by tier, reported for the lead to paste into the scope, Role checker: two modes set by the brief, verify and review; ticks only the verify.md steps it ran or writes a file in docs/reviews; never fixes what it finds, Checker review mode: senior code review of a GA feature with fresh eyes, ranked findings in docs/reviews; only in a new session that has not written, verified or discussed the implementation, Checker verify mode: proves a milestone or feature behaves per spec by running the verify.md steps, scoped to the milestone section and the AC IDs in the brief, and sends failures to the owning developer (+62 more)

### Community 5 - "Kotlin FFI Library Loading"
Cohesion: 0.06
Nodes (34): Disposable, NoHandle, UniffiByValue, UniffiCallbackInterfaceClone, UniffiCallbackInterfaceFree, UniffiForeignFutureCompleteF32, UniffiForeignFutureCompleteF64, UniffiForeignFutureCompleteI16 (+26 more)

### Community 6 - "Kotlin UniFFI Library Calls"
Cohesion: 0.06
Nodes (3): UniffiLib, UniffiRustCallStatus, UniffiRustFutureContinuationCallback

### Community 7 - "CI Workflow and Derived Run"
Cohesion: 0.16
Nodes (32): Pass representative values through both generated languages, Derived hosted run android job result (same derive command; Gradle 9.3.1 assembled the derived debug app; identity file and built app matched; two instrumentation tests passed with night mode off and on), Derived hosted run ios job result (derive step ran init-project.sh as Zoë's Proof with dev.example.derived; Xcode 26.5 built the derived app; identity file and built app matched; greeting test passed in light and dark on iOS 26.5), Hosted run 43701281055 on the push of revision 4a153fe (all three jobs passed; the derive step was skipped; both comparison steps passed with dev.foundation.mobile and Mobile Foundation), Hosted run 43701289339 on revision 4a153fe (2026-11-15, started by hand through workflow_dispatch with the derived input set; all three jobs passed), Hosted run 43701281055 (push trigger, on revision 4a153fe), Scope 009 specifics: main at the start is 4a153fe, equal to origin/main; Build plan steps 1 to 10 of spec 0003 are on main; no sub-session triggers, repeats or cancels a hosted run; each of verification.md, verify.md and test_init_project.py has exactly one sub-session that may change it, Verification before reporting: scripts/test.sh must exit 0; build-ios.sh simulator, device and test in light and dark when apps/ios/ changed; build-android.sh assemble and connectedDebugAndroidTest in both night modes when apps/android/ changed; git status clean and the diff against main limited to ownership files (+24 more)

### Community 8 - "test.sh, Init Checks and Verify Steps"
Cohesion: 0.13
Nodes (32): Derivation only on a copy: init-project.sh with --name rewrites README.md and the verification record and removes graphify-out/, so that form runs only in a temporary clone in the session scratchpad; --check and --test are safe in the worktree, Project adjustments: the role files were written for another Rust project; cargo xtask, stackly_testkit, clients/swift, evidence/, prd.md and test-preferences.json do not exist here; evidence is the commands and output in the report, Checker note, not a blocker: the Value sourcing step 'Default application ID for the check' in verify.md names the message 'still the foundation default', while with both IDs at the default --check exits 1 with a message about the origin line; AC-8 is met; the step sentence could be tidied through an architect (update) item, Sub-session chk-f009-verify (checker verify, fable-5-2 high, merged): full verify of AC-1 to AC-12, closing milestone 3, Build it and Verify it; owns the ticks in verify.md of spec 0003, Decision: lead gate on main after each merge: no conflict markers, scripts/test.sh exits 0, native build per platform only when apps/ changed (the skill gate commands cargo xtask and swift test do not exist in this repo), Decision: the milestone verify is folded into one full verify, because milestone 3 is the last milestone and verify.md of spec 0003 has no per-milestone sections, Ticked in wave 1: 009 Build it and Verify it, from the chk-f009-verify report done with verdict PASS: 45 of 47 verify.md steps passed and were ticked, none failed, AC-1 to AC-12 each covered by a passing step (commits 99f2840, 89d0b74); manual NOT_RUN: F009-1, F009-2, Ticked in wave 1: 009 Test it, from the tst-f009-test report done (21 to 50 tests, AC-3 to AC-9 each have a test carrying its ID, commit dc9a8d9, merged in 0aa1d5c); on main with the merge staged there were no conflict markers and scripts/test.sh exited 0 (+24 more)

### Community 9 - "Verification Record and UI Tests"
Cohesion: 0.13
Nodes (31): GreetingTest, GreetingUITests, Android linkage and UI check (Linux CI job, emulator instrumentation), GitHub Actions CI jobs (macOS and Linux), iOS linkage and UI check (macOS CI job, XCTest), Foundation verification 2026-11-15, Android compilation result (Gradle 9.3.1, AGP 9.1.0, Temurin 17), Android packaging 16 KiB alignment result (+23 more)

### Community 10 - "Scope 009 Coordination Records"
Cohesion: 0.10
Nodes (33): Report field 'Tafsiran AC' (developer, checker, tester): the reading taken for an ambiguous AC and its reason from the AC text or rationale.md, General brief rules (Aturan umum brief) for the sub-sessions of the scope 009 coordination: the fixed part of every brief; the brief wins where it differs, Always forbidden for sub-sessions: docs/scope/, AGENTS.md, graphify-out/, spec content other than the Status line and the verify.md ticks (checker only), other specs, and files outside the brief's allowed list, Decisions in auto mode: for an ambiguous AC read the spec's rationale.md, take the reading closest to the AC text and record it under Tafsiran AC; needs-decision goes to the lead only when the AC text or a spec decision must change, Commit rule for sub-sessions: one commit per step, an imperative English subject without prefix like the repository history, plus the Co-Authored-By trailer, Disk rule: 32 GiB free at the start; only the checker runs full native builds, one at a time; below 10 GiB free stop and report blocked; remove target/, build/ and apps/android/**/build and the temporary clone before reporting done, Lead address: Mobile Foundation Scaffold [f5cda4]; full reports, questions and needs-decision go there through SendMessage, Manual steps rule: GUI apps, GitHub web pages, physical devices, signing, installing tools, repository settings, push and triggering or repeating workflows are done only by the user or the lead; gh is read-only; headless simulators and emulators are allowed; a failed or flaky step is reported failed, not manual (+25 more)

### Community 11 - "Derivation Command"
Cohesion: 0.12
Nodes (31): Exception, check(), derive(), foundation_ref(), foundation_url(), git(), identity_text(), in_git() (+23 more)

### Community 12 - "Spec 0003 Decision History and Init Command"
Cohesion: 0.13
Nodes (29): apps/ios/MobileFoundation.xcodeproj/project.pbxproj (Xcode project file), Done when (009): one recorded decision, one command, a hosted check on a temporary copy, clean inherited records, recorded foundation revision, AC-11: README.md has a section with the full path from clone to first results, path ownership, taking a later release and foundation tagging, Decision: a product is a clone that changes only its display name, application ID and version through scripts/init-project.sh, keeps every other name, starts with an empty verification record and merges foundation-v tags, Neutral: /develop moves the spec to In Progress and Accepted with scope row 009; creating the first tag foundation-v0.1.0 is the maintainer's step, README section 'Start a project from this foundation': clone at a tag, create a branch, rename the remote, run the command, add origin, rebuild the graph, mark inherited rows existing, commit, record first results, Release the foundation: run the workflow by hand with derived set, then push an annotated foundation-vMAJOR.MINOR.PATCH tag on main, Tradeoff: the Linux proof builds nothing, so a change that breaks a derived native build can sit on main until the next manual derived run (+21 more)

### Community 13 - "Rust Core and Greeting Contract"
Cohesion: 0.12
Nodes (26): hello(), preserves_empty_names_and_whitespace(), String, main(), hello(), String, Design definitions compile independently of Cargo and UniFFI, Core and FFI contract tests (locked Cargo tests) (+18 more)

### Community 14 - "Native Greeting and Supported OS Scopes"
Cohesion: 0.13
Nodes (23): CoreImage, Android 001 - Native Android greeting (existing), API 36 emulator results (arm64 local, x86_64 hosted) in light and dark, Android app packages both supported CPU architectures, Android physical device coverage unverified, Android 002 - Lowest supported Android and large text (planned), 16 KiB memory page packaging, Declared Android minimum API 24 not yet exercised (+15 more)

### Community 15 - "Derivation Run and Origin Line Tests"
Cohesion: 0.11
Nodes (12): AC-3, AC-5, AC-6, AC-8: the happy path writes every file and the checkout then…, AC-3: each override reaches only its own identity file, and --version reaches…, AC-3: with one override the other platform keeps --app-id., AC-3, AC-7: a value that starts with a hyphen is refused, and its equals form…, AC-6: without the flags the origin line takes the remote, HEAD and today., AC-6: the foundation remote wins over origin, and the highest release tag wins., AC-3: the example of the criterion, with no other flag, writes 0.1.0 and build…, AC-5, AC-6: the remote's user and token are dropped before the URL is written… (+4 more)

### Community 16 - "Platform Rules and Native App Shells"
Cohesion: 0.11
Nodes (25): GreetingScreen, .body, String, Native components guidelines, Greeting as a single text element, Reusable native component (introduced on demand), Android rules, Checked-in Gradle wrapper (+17 more)

### Community 17 - "Spec 0003 and Starting a Product"
Cohesion: 0.14
Nodes (24): Spec 0003: A new project from the foundation: product identity in two files, one init command, updates by merge (Accepted), Follow-up: build the command that takes a foundation release (fetch, merge, apply the ownership table) when the first release is merged into a product, Follow-up: decide where dependency update bots run (a bot in every product changes foundation owned files and will conflict with merges), Follow-up: decide in the release path spec whether the iOS and Android versions must match, and add that test to --check if they must, Follow-up: allow a localized display name when a product needs one (it would move from the identity files to the catalogs), Follow-up: record where /graphify and /scope come from, with a way to do each step by hand, Follow-up: revisit keeping MobileFoundation as the Xcode project and scheme name if it confuses contributors to a product, Input validation rules (re.ASCII patterns for app ID, platform overrides, display name of 1 to 30 code points, version, build, foundation URL, ref and date) (+16 more)

### Community 18 - "Resource Generator"
Cohesion: 0.14
Nodes (19): check_schema(), generate(), load(), projections(), Validate authoritative sources, then materialize or check their projections., unique_members(), validator(), native_text() (+11 more)

### Community 19 - "Derivation Refusal Tests"
Cohesion: 0.09
Nodes (12): OutsideGitTests, AC-7: a local path remote, or no remote, is no usable foundation URL., AC-7: each input that breaks its rule is refused with exit 2, one line and no…, AC-7: a remote URL that is not UTF-8 is no usable foundation URL., AC-7: a derived checkout is refused., AC-7: each name outside the rule is refused on its own, with exit 2, one line…, AC-7: each application ID outside the rule of its flag is refused on its own., AC-7: each version, date, foundation URL and ref outside its rule is refused on… (+4 more)

### Community 20 - "Kotlin FFI Converters"
Cohesion: 0.17
Nodes (9): FfiConverter, FfiConverterRustBuffer, FfiConverterString, FfiType, uniffiTraitInterfaceCall(), uniffiTraitInterfaceCallWithError(), ByteBuffer, KotlinType (+1 more)

### Community 21 - "Spec 0001 Ownership Rules"
Cohesion: 0.19
Nodes (23): Spec 0001: One owner per responsibility, with rules kept beside the code, Automate only what a machine can judge, Decision: one owner per responsibility in an ownership matrix, topic-sized rule files, short AGENTS.md entry point, automated checks only where a machine is reliable, An exact dependency list, not a deny list, Follow-up: decide whether checks must pass before a change reaches main (branch rule or local hook), Follow-up: confirm or correct the inferred rationale, Follow-up: record reviewers per owner (CODEOWNERS) when a second contributor joins, Force: coding agents are regular contributors and act on what they load (+15 more)

### Community 22 - "Kotlin RustBuffer Handling"
Cohesion: 0.16
Nodes (7): ByReference, ByValue, ForeignBytes, `hello`(), RustBuffer, kotlin, Pointer

### Community 23 - "Derivation Test Checkout Fixture"
Cohesion: 0.16
Nodes (9): Checkout, AC-7: a modified or untracked file is refused, even when git status hides…, AC-7: a mixed checkout is refused., AC-4: a checkout that has no graph changes only the two identity files,…, AC-6: a README.md of one line without a newline still ends with the title,…, AC-6: only a foundation-v tag that points exactly at HEAD names the ref;…, AC-7: a change only in the index, and a deleted tracked file, both make the…, AC-7: git status leaves ignored files out, so an ignored local file is no… (+1 more)

### Community 24 - "Product Identity Files and Criteria"
Cohesion: 0.24
Nodes (19): apps/android/identity.properties (Android identity file: applicationId, displayName, versionName, versionCode), apps/ios/Config/Identity.xcconfig (iOS identity file: APP_BUNDLE_IDENTIFIER, APP_DISPLAY_NAME, MARKETING_VERSION, CURRENT_PROJECT_VERSION), Product identity (display name, application IDs, app version): owned by apps/ios/Config/Identity.xcconfig and apps/android/identity.properties; consumed by the Xcode and Gradle builds and scripts/init-project.sh, Project identity state check (init-project.sh --check and --test, CI identity comparison), Product identity result (2026-11-15: test.sh passed with --check printing foundation and --test passing 21 unit tests; both apps carried dev.foundation.mobile, Mobile Foundation, 0.1.0, build 1; a copy derived as Zoë's Proof built and matched its identity file), Checker note, not a blocker: the iOS icon caption reads MobileFoundation without a space although CFBundleDisplayName is Mobile Foundation; SpringBoard shortens long names (Acme Notes shows its space); a spaced caption needs a shorter name, which is a product decision, Manual step F009-1 (NOT_RUN): Xcode shows Identity.xcconfig in the file list and no target uses it as base config; proves spec 0003 AC-1; boxes ticked with it NOT_RUN: milestone 1, Build it, Verify it, The two apps disagree on their own identity (iOS dev.foundation.mobile / Mobile Foundation / 1.0, Android foundation.mobile / Foundation / 0.1.0) (+11 more)

### Community 25 - "Architecture Compliance and Spec Triggers"
Cohesion: 0.27
Nodes (18): Agent workflow: before editing (locate owner, contract, callers, tests), Dependency rules, New dependency edge needs an owning module, a use case and a test, Compatibility: version breaking contracts and coordinate regeneration, both apps and release, Revisit conditions: dependency direction change, async native boundary, independently versioned clients, new shared crate or service, Architecture compliance, Physical hardware verification for simulator-inaccessible capabilities, Spec under docs/specs and policy update for a new dependency or material architecture change (+10 more)

### Community 26 - "Identity Value Sourcing"
Cohesion: 0.18
Nodes (15): apps/android/app/src/main/AndroidManifest.xml, apps/android/app/src/main/res/values/app.xml (the app_name string leaves this file; the label comes from the appLabel manifest placeholder), apps/ios/Config/App.xcconfig (iOS app build settings), apps/ios/Config/Project.xcconfig (iOS project build settings), AC-6: README.md has the product name as title on line 1 and the origin line on line 3 followed by one blank line, Android build reads identity.properties: app/build.gradle.kts loads applicationId, versionName and versionCode, the label reaches the manifest as the appLabel placeholder, namespace stays foundation.mobile, Foundation ref resolution: --foundation-ref, else the highest foundation-v* tag exactly at HEAD, else the full HEAD commit ID, Foundation URL sourcing and normalization: --foundation-url, else the foundation remote, else origin; https, http, ssh and user@host:path forms written as https without user, token, .git or trailing slash (+7 more)

### Community 27 - "Workspace Scopes and Visual Definitions"
Cohesion: 0.18
Nodes (16): Android scope, Android app owns its screen, appearance changes and native localization lookup, Beta workflow (/check verify, then /test), Tracer Bullet build approach, Workspace completion at a glance: shared foundation 9 of 10 (open 010), iOS 1 of 2, Android 1 of 2, iOS scope, Apple app owns its screen, appearance changes and native localization lookup, 003 - Shared visual definitions (done) (+8 more)

### Community 28 - "Derivation Write Set Tests"
Cohesion: 0.12
Nodes (9): DerivationTests, AC-4: git sees changes in exactly the documented paths, and no rename., AC-6, AC-7: every accepted remote form becomes https without credentials; the…, AC-7: the in git test compares folders, not path spellings., AC-4: a graph removal that fails names every changed path and the way back., AC-4: each file is replaced in the documented order, and graphify-out/ goes…, AC-5: the template on disk, filled with the sample values, is the empty record…, AC-7: letters from any script, digits 0 to 9, single spaces, periods, hyphens… (+1 more)

### Community 29 - "Empty Verification Record and Refusals"
Cohesion: 0.16
Nodes (16): A new product would carry the foundation's verification record, scope rows, hosted run links and knowledge graph as its own, AC-5: the verification record becomes the empty record naming the product, foundation URL and revision, with every target unverified, AC-7: the command refuses, changes nothing and exits 2 with a one line reason (bad input, default ID, dirty tree, derived or mixed checkout, missing foundation URL or ref), Empty verification record: names the product, foundation URL and ref, lists every target as still unverified, holds no hosted run link, Positive: products install side by side under their own name and ID, a foundation fix reaches every product by one merge, a half derived checkout fails scripts/test.sh, records start empty, the identity mismatch is gone, every native run proves the built identity, Refusals: one line naming the input and the rule, exit 2, nothing written, User stories: one command names a clone, foundation releases arrive by merge, the verification record lists only what ran here, every push proves the command still works, Recommendation: --check does not look for hosted run links (+8 more)

### Community 30 - "Config Schema"
Cohesion: 0.14
Nodes (13): defaultLocale, schemaVersion, additionalProperties, const, properties, defaultLocale, schemaVersion, required (+5 more)

### Community 31 - "Generated Native Tokens"
Cohesion: 0.18
Nodes (9): FoundationTokens, Palette, FoundationTokens, Palette, CGFloat, Color, ColorScheme, Font (+1 more)

### Community 32 - "Kotlin Rust Call Status"
Cohesion: 0.23
Nodes (7): E, uniffiCheckCallStatus(), UniffiForeignFutureCompleteVoid, uniffiRustCall(), UniffiRustCallStatusErrorHandler, uniffiRustCallWithError(), U

### Community 33 - "Derivation State Check Tests"
Cohesion: 0.18
Nodes (5): AC-8: every departure from the exact form is a mismatch that names the file and…, AC-8: a derived checkout that lost one signal names that signal., AC-8: an identity file that is not UTF-8, and a missing README.md, are…, AC-8: changing only applicationId names that file and key against a foundation…, AC-8: default IDs under an origin line, and a second origin line, each make a…

### Community 34 - "Rule Set and Generated File Rules"
Cohesion: 0.29
Nodes (10): Rejected alternative: implementing application behavior independently in both apps, Follow-up: a small import scan in check-architecture.py for R3, R2: dependencies run one way, mobile-ffi -> foundation-core; core has no dependencies, R3: the two app trees do not import one another, R5: a generated file is never edited by hand; change the source and regenerate every output, R6: shared visual values live in tokens; shared copy, settings and brand sources live under shared/; generators never read back native output, Practices the standard replaces (duplicated Swift/Kotlin rules, hand-edited outputs, unpoliced dependencies, cross-app imports, speculative layers, copied literals), Rule set R1-R19 (rule, owner file, enforcement) (+2 more)

### Community 35 - "Anti-Duplication and Review-Only Rules"
Cohesion: 0.29
Nodes (10): Limits of CI checks, Reviewers trace changed behavior from owner into each client, Anti-duplication rules, Locate the owner before adding a constant, rule, DTO, translation or asset, Reviewers assess semantic duplication, R1: each responsibility has one authoritative owner (the matrix lists eleven), R9: search before adding a constant, rule, data shape, translation or asset, Review-only rules with no automated check (R1, R3, R8, R9, R11, R14, R15, R16, R18) (+2 more)

### Community 36 - "Android App Shell"
Cohesion: 0.33
Nodes (5): MainActivity, FoundationTheme(), GreetingScreen(), Bundle, ComponentActivity

### Community 37 - "Kotlin Handle Map and Lifting"
Cohesion: 0.42
Nodes (4): InternalException, T, UniffiHandleMap, UniffiNullRustCallStatusErrorHandler

### Community 38 - "Command Line Wrapper Tests"
Cohesion: 0.31
Nodes (5): CommandLineTests, Run the copied scripts/init-project.sh from another folder, as a person or CI…, AC-3, AC-8: the wrapper finds its own checkout, prints the five changed paths,…, AC-7: through the wrapper a refusal exits 2, prints one line on stderr only,…, AC-8: through the wrapper --check exits 1 and names the mismatch on stderr.

### Community 39 - "Mobile Contract Extension Conventions"
Cohesion: 0.43
Nodes (7): Mobile contract (FFI conventions), Explicit application records and enums; private core/transport shapes mapped at the adapter, Async and cancellation conventions for future exports, Conventions for extending the mobile contract, Native capability callback interfaces limited to operations the core requires, Typed UniFFI errors with stable variants; user-facing messages translated natively, Records, typed errors, async calls and native callbacks have no caller or test yet

### Community 40 - "Real Checkout Derivation Tests"
Cohesion: 0.33
Nodes (4): AC-9: the derivation proof is skipped, with its reason, in a checkout that is…, Run the checked in command on a temporary copy of this checkout. The checkout…, AC-9: the copy's own command derives the copy, which then reads derived and…, RealCheckoutTests

### Community 41 - "Shared Greeting Contract Tests"
Cohesion: 0.60
Nodes (5): 002 - Shared greeting contract (done), Generated bindings (code that carries values between languages), Neither app screen has shown a Unicode name, Unicode round trip through both generated bindings (Android emulator, iOS host executable), exported_contract_preserves_unicode()

### Community 42 - "iOS Greeting UI Test Helpers"
Cohesion: 0.50
Nodes (3): UInt8, CIContext, XCUIScreenshot

### Community 43 - "Kotlin FFI Integrity Checks"
Cohesion: 0.60
Nodes (3): IntegrityCheckingUniffiLib, uniffiCheckApiChecksums(), uniffiCheckContractApiVersion()

### Community 44 - "Android Rust Build Script"
Cohesion: 0.40
Nodes (4): CARGO_TARGET_AARCH64_LINUX_ANDROID_LINKER, CARGO_TARGET_X86_64_LINUX_ANDROID_LINKER, PATH, build-android-rust.sh script

### Community 46 - "Android Gradle Wrapper"
Cohesion: 0.83
Nodes (3): gradlew script, die(), warn()

### Community 47 - "iOS Rust Build Script"
Cohesion: 0.50
Nodes (3): CARGO_TARGET_DIR, PATH, build-ios-rust.sh script

### Community 48 - "Hosted Build Verification Scope"
Cohesion: 0.67
Nodes (3): 006 - Hosted build verification (done), Android hosted job installs the supported SDK packages, Three hosted jobs (foundation, iOS, Android) on the same revision

## Knowledge Gaps
- **67 isolated node(s):** `NoHandle`, `UniffiWithHandle`, `Explicit application records and enums; private core/transport shapes mapped at the adapter`, `apiChecksumMismatch`, `contractVersionMismatch` (+62 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `DerivationTests` connect `Derivation Write Set Tests` to `Derivation State Check Tests`, `test.sh, Init Checks and Verify Steps`, `Real Checkout Derivation Tests`, `Derivation Write Failure Tests`, `Derivation Run and Origin Line Tests`, `Derivation Refusal Tests`, `Derivation Test Checkout Fixture`?**
  _High betweenness centrality (0.118) - this node is a cross-community bridge._
- **Why does `Foundation verification 2026-11-15` connect `Verification Record and UI Tests` to `Planning Path, Scope Index and Policy Checks`, `Ownership Matrix, Architecture and Shared Resources`, `Design System, Schemas and Generator Checks`, `CI Workflow and Derived Run`, `test.sh, Init Checks and Verify Steps`, `Shared Greeting Contract Tests`, `Scope 009 Coordination Records`, `Spec 0003 Decision History and Init Command`, `Rust Core and Greeting Contract`, `Native Greeting and Supported OS Scopes`, `Spec 0003 and Starting a Product`, `Product Identity Files and Criteria`, `Architecture Compliance and Spec Triggers`, `Workspace Scopes and Visual Definitions`, `Empty Verification Record and Refusals`?**
  _High betweenness centrality (0.105) - this node is a cross-community bridge._
- **Why does `.body` connect `Swift UniFFI Bindings` to `Platform Rules and Native App Shells`?**
  _High betweenness centrality (0.099) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Foundation verification 2026-11-15` (e.g. with `Record separately what compiled and what ran` and `tooling/derive/verification-record.md (empty verification record template for a derived product)`) actually correct?**
  _`Foundation verification 2026-11-15` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `NoHandle`, `UniffiWithHandle`, `Explicit application records and enums; private core/transport shapes mapped at the adapter` to the rest of the system?**
  _67 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Swift UniFFI Bindings` be split into smaller, more focused modules?**
  _Cohesion score 0.050686641697877656 - nodes in this community are weakly interconnected._
- **Should `Planning Path, Scope Index and Policy Checks` be split into smaller, more focused modules?**
  _Cohesion score 0.07431168136861802 - nodes in this community are weakly interconnected._