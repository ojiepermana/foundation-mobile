# Graph Report - mobile  (2026-11-15)

## Corpus Check
- 5 files · ~27,599 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 800 nodes · 2045 edges · 27 communities (25 shown, 2 thin omitted)
- Extraction: 76% EXTRACTED · 24% INFERRED · 0% AMBIGUOUS · INFERRED: 501 edges (avg confidence: 0.89)
- Token cost: 60,809 input · 5,752 output

## Community Hubs (Navigation)
- Architecture Boundaries and Agent Workflow
- Swift UniFFI Bindings
- Planning Path, Rules and Compliance
- Kotlin FFI Library Loading
- Native Apps and Greeting Scopes
- Shared Config, Localization and Tokens
- Verification Record and UI Tests
- Build Scripts and Handoff Checks
- Kotlin UniFFI Library Calls
- Greeting Contract, Tests and CI
- Kotlin FFI Converters
- Resource Generator Script
- Kotlin Rust Call Status
- Design Token and Resource Rules
- Design System Guide
- Kotlin RustBuffer Handling
- Token Conventions and Principles
- Generated Drift and Regeneration
- Native Token Mapping
- Kotlin Hello Call Path
- Kotlin Handle Map
- Accessibility and Contrast Checks
- Android Rust Build Script
- iOS Rust Build Script

## God Nodes (most connected - your core abstractions)
1. `Spec 0002: One planning path: a scope row first, then a spec` - 57 edges
2. `UniffiLib` - 54 edges
3. `Spec 0001: One owner per responsibility, with rules kept beside the code` - 53 edges
4. `Decision: a new capability is planned as a scope row and designed in a spec before code; docs/plans and new ADRs are retired in a single change` - 38 edges
5. `Mobile foundation scope (index)` - 37 edges
6. `Rollout: one change in fifteen ordered steps (rules, AGENTS.md, architecture docs, README, validator, delete docs/plans, scope files, spec 0001, knowledge graph)` - 33 edges
7. `Foundation verification 2026-11-14` - 32 edges
8. `UniffiRustCallStatus` - 29 edges
9. `Development rules` - 28 edges
10. `RustBuffer` - 27 edges

## Surprising Connections (you probably didn't know these)
- `Greeting is a pure function; no application services exist` --references--> `hello()`  [INFERRED]
  docs/rules/service-rules.md → crates/core/src/lib.rs
- `Trace screen, generated binding, FFI export and core function before changing shared behavior` --references--> `GreetingScreen`  [INFERRED]
  docs/rules/development-rules.md → apps/ios/Presentation/GreetingScreen.swift
- `Render the returned Rust string verbatim` --references--> `GreetingScreen`  [INFERRED]
  docs/rules/ios-rules.md → apps/ios/Presentation/GreetingScreen.swift
- `SwiftUI presentation with Dynamic Type and adaptive appearance` --references--> `GreetingScreen`  [INFERRED]
  docs/rules/ios-rules.md → apps/ios/Presentation/GreetingScreen.swift
- `Compose presentation with native Material semantics` --references--> `GreetingScreen()`  [INFERRED]
  docs/rules/android-rules.md → apps/android/presentation/src/main/kotlin/foundation/presentation/GreetingScreen.kt

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Automated architecture compliance checks** — docs_quality_architecture_compliance_rust_format_and_lint, docs_quality_architecture_compliance_core_and_ffi_contract_tests, docs_quality_architecture_compliance_cargo_dependency_and_governance_check, docs_quality_architecture_compliance_uniffi_generated_files_check, docs_quality_architecture_compliance_tokens_config_localization_check, docs_quality_architecture_compliance_ios_linkage_and_ui_check, docs_quality_architecture_compliance_android_linkage_and_ui_check [EXTRACTED 1.00]
- **Tracer bullet greeting path from shared core to both native screens** — docs_scope_index_tracer_bullet_build_approach, docs_scope_root_002_shared_greeting_contract, docs_scope_root_002_shared_greeting_contract_one_string_in_one_string_out_contract, docs_scope_ios_001_native_ios_greeting, docs_scope_android_001_native_android_greeting, docs_scope_root_006_hosted_build_verification [INFERRED 0.85]
- **Verification evidence chain: local checks, hosted jobs and the verification record** — docs_scope_root_005_reproducible_local_builds_and_checks, docs_scope_root_006_hosted_build_verification, docs_scope_root_008_hosted_results_in_the_verification_record, docs_scope_index_hosted_run_43593365100, docs_scope_root_005_reproducible_local_builds_and_checks_stale_local_verification_record, docs_scope_root_008_hosted_results_in_the_verification_record_single_list_of_unverified_targets [INFERRED 0.85]
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

## Communities (27 total, 2 thin omitted)

### Community 0 - "Architecture Boundaries and Agent Workflow"
Cohesion: 0.05
Nodes (104): Agent workflow: before editing (locate owner, contract, callers, tests), Knowledge graph (graphify-out/, kept current with /graphify . --update), Never hand-edit generated files, Architecture boundaries, Documented capability boundary; adapters need an actual caller, Layer: design system (generated Swift/Kotlin values as shared visual vocabulary), Layer: native presentation (views render, adapt to appearance, handle events), Layer: shared Rust (core owns behavior, FFI crate maps exports) (+96 more)

### Community 1 - "Swift UniFFI Bindings"
Cohesion: 0.05
Nodes (64): Array, createReader(), createWriter(), Data, FfiConverter, FfiConverterPrimitive, FfiConverterRustBuffer, FfiConverterString (+56 more)

### Community 2 - "Planning Path, Rules and Compliance"
Cohesion: 0.08
Nodes (79): AGENTS.md: Working in the mobile foundation, Agent workflow: during implementation (place change in owning layer), Plan a new capability in the scope and write its spec under docs/specs before code, Architecture overview, docs/ and root AGENTS.md: architecture, decision records, scope and agent workflow, Repository structure, Create a platform adapter directory only when a feature needs an OS capability, docs/ record homes: docs/scope (what to build and its status), docs/specs (design and decision records), docs/decisions (the founding decision) (+71 more)

### Community 3 - "Kotlin FFI Library Loading"
Cohesion: 0.05
Nodes (38): Disposable, IntegrityCheckingUniffiLib, NoHandle, UniffiByValue, UniffiCallbackInterfaceClone, UniffiCallbackInterfaceFree, uniffiCheckApiChecksums(), uniffiCheckContractApiVersion() (+30 more)

### Community 4 - "Native Apps and Greeting Scopes"
Cohesion: 0.06
Nodes (45): App, MainActivity, FoundationTheme(), FoundationTokens, Palette, GreetingScreen(), MobileFoundationApp, .body (+37 more)

### Community 5 - "Shared Config, Localization and Tokens"
Cohesion: 0.06
Nodes (44): Build-time generation: token JSON and locale JSON -> native theme inputs and localization resources, Color selection, font scaling, layout and accessibility run natively (no shared renderer), shared/config, shared/localization, shared/assets: owner of public settings, locale content and brand masters, Decision: neutral JSON tokens and validated shared sources generate native theme inputs and localization, Deferred: a second language end to end, 004 - Shared settings, text and brand assets (existing), Greeting sentence 'Hello, {name}!' formed in English by the core, Single English localization catalog and public fallback locale (+36 more)

### Community 6 - "Verification Record and UI Tests"
Cohesion: 0.09
Nodes (41): GreetingTest, GreetingUITests, UInt8, CIContext, Android linkage and UI check (Linux CI job, emulator instrumentation), GitHub Actions CI jobs (macOS and Linux), iOS linkage and UI check (macOS CI job, XCTest), Foundation verification 2026-11-14 (+33 more)

### Community 7 - "Build Scripts and Handoff Checks"
Cohesion: 0.06
Nodes (35): Agent workflow: before commit (run /graphify . --update, stage graphify-out with the change), Agent workflow: before handoff (run checks, report commands and unverified targets), gradlew script, die(), warn(), FoundationTokens, Palette, CGFloat (+27 more)

### Community 9 - "Greeting Contract, Tests and CI"
Cohesion: 0.11
Nodes (31): hello(), preserves_empty_names_and_whitespace(), String, main(), hello(), String, tests/contracts: Cargo integration tests for exported behavior, Mobile contract (FFI conventions) (+23 more)

### Community 10 - "Kotlin FFI Converters"
Cohesion: 0.16
Nodes (9): FfiConverter, FfiConverterRustBuffer, FfiConverterString, FfiType, uniffiTraitInterfaceCall(), uniffiTraitInterfaceCallWithError(), ByteBuffer, KotlinType (+1 more)

### Community 11 - "Resource Generator Script"
Cohesion: 0.14
Nodes (19): check_schema(), generate(), load(), projections(), Validate authoritative sources, then materialize or check their projections., unique_members(), validator(), native_text() (+11 more)

### Community 13 - "Design Token and Resource Rules"
Cohesion: 0.21
Nodes (16): System text scaling via generated text styles, Stable role names or same-change migration, Design system rules, Drift check plus verification in both appearances and larger text sizes, Public role name changes require migrating both consumers, Draft 7 schema and native mappings updated together, Shared resource ownership rules, Draft 7 schemas in shared/specifications (+8 more)

### Community 14 - "Design System Guide"
Cohesion: 0.20
Nodes (15): Design system guide, generate-design-tokens.sh modes: write, --check (drift), --test (failure cases), Generated semantic token API consumed by native apps, Five canonical token JSON files (primitives and semantic aliases), tokens.schema.json: single Draft 7 document keyed by filename stem, Layer: resources and tooling (build-host validation and generation), design-system/tokens and schemas: owner of canonical visual values and semantic roles, scripts/ and .github/workflows/: build and verification orchestration (+7 more)

### Community 15 - "Kotlin RustBuffer Handling"
Cohesion: 0.23
Nodes (5): ByReference, ByValue, ForeignBytes, RustBuffer, Pointer

### Community 16 - "Token Conventions and Principles"
Cohesion: 0.22
Nodes (14): Canonical token schema (tokens.schema.json), Native controls styled with semantic tokens, Design principles, Canonical JSON propagates through code generation, Design definitions compile independently of Cargo and UniFFI, Layout, text measurement, gestures and focus stay in presentation, Semantic names for decisions both apps share, Token conventions (+6 more)

### Community 17 - "Generated Drift and Regeneration"
Cohesion: 0.18
Nodes (8): Generated drift remediation, Tokens, configuration and localization check, Design system and resources result (seven generator tests), Shared visual decisions and translations are generator inputs, Regenerate native projections in the same change, Regenerate derived files alongside canonical inputs, Generated native strings owned by the resource generator, GenerationTests

### Community 18 - "Native Token Mapping"
Cohesion: 0.32
Nodes (12): Native token mapping, Compose sp mapping of logical text units, Jetpack Compose token projection (FoundationTokens), Dynamic Type mapping of headline and reading scales, Logical spacing units adapt to display density, spacingPage role, SwiftUI token projection (FoundationTokens), typographyGreeting role (+4 more)

### Community 19 - "Kotlin Hello Call Path"
Cohesion: 0.28
Nodes (7): `hello`(), E, uniffiRustCall(), UniffiRustCallStatusErrorHandler, uniffiRustCallWithError(), kotlin, U

### Community 20 - "Kotlin Handle Map"
Cohesion: 0.42
Nodes (4): InternalException, T, UniffiHandleMap, UniffiNullRustCallStatusErrorHandler

### Community 21 - "Accessibility and Contrast Checks"
Cohesion: 0.29
Nodes (7): Accessibility (design system), Per-target reading order and screen-reader review, Status conveyed by text or semantics, not color alone, Honor platform reduced-motion setting, Text contrast check (4.5:1 minimum), W3C WCAG 2.2 contrast minimum guidance, Reviewers trace changed behavior from owner into each client

### Community 22 - "Android Rust Build Script"
Cohesion: 0.40
Nodes (4): CARGO_TARGET_AARCH64_LINUX_ANDROID_LINKER, CARGO_TARGET_X86_64_LINUX_ANDROID_LINKER, PATH, build-android-rust.sh script

### Community 23 - "iOS Rust Build Script"
Cohesion: 0.50
Nodes (3): CARGO_TARGET_DIR, PATH, build-ios-rust.sh script

## Knowledge Gaps
- **52 isolated node(s):** `NoHandle`, `UniffiWithHandle`, `Explicit application records and enums; private core/transport shapes mapped at the adapter`, `apiChecksumMismatch`, `contractVersionMismatch` (+47 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `.body` connect `Native Apps and Greeting Scopes` to `Swift UniFFI Bindings`?**
  _High betweenness centrality (0.140) - this node is a cross-community bridge._
- **Why does `hello()` connect `Swift UniFFI Bindings` to `Native Apps and Greeting Scopes`?**
  _High betweenness centrality (0.138) - this node is a cross-community bridge._
- **Why does `GreetingScreen` connect `Native Apps and Greeting Scopes` to `Greeting Contract, Tests and CI`, `Native Token Mapping`, `Build Scripts and Handoff Checks`?**
  _High betweenness centrality (0.137) - this node is a cross-community bridge._
- **Are the 13 inferred relationships involving `Decision: a new capability is planned as a scope row and designed in a spec before code; docs/plans and new ADRs are retired in a single change` (e.g. with `Follow-up (settled by spec 0002): R10 sent a new capability to docs/plans while features are tracked in docs/scope` and `Canonical pattern: a scope row (the brief), a spec before code, one slice through its real caller, progress in the scope row and results in the verification record`) actually correct?**
  _`Decision: a new capability is planned as a scope row and designed in a spec before code; docs/plans and new ADRs are retired in a single change` has 13 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `Mobile foundation scope (index)` (e.g. with `docs/ and root AGENTS.md: architecture, decision records, scope and agent workflow` and `docs/ record homes: docs/scope (what to build and its status), docs/specs (design and decision records), docs/decisions (the founding decision)`) actually correct?**
  _`Mobile foundation scope (index)` has 7 INFERRED edges - model-reasoned connections that need verification._
- **What connects `NoHandle`, `UniffiWithHandle`, `Explicit application records and enums; private core/transport shapes mapped at the adapter` to the rest of the system?**
  _52 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Architecture Boundaries and Agent Workflow` be split into smaller, more focused modules?**
  _Cohesion score 0.051666372773761245 - nodes in this community are weakly interconnected._