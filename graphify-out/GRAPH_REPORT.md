# Graph Report - mobile  (2026-11-14)

## Corpus Check
- Corpus is ~20,428 words - fits in a single context window. You may not need a graph.

## Summary
- 682 nodes · 1412 edges · 31 communities (30 shown, 1 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 265 edges (avg confidence: 0.87)
- Token cost: 232,981 input · 52,024 output

## Community Hubs (Navigation)
- Swift UniFFI Bindings
- Scope Records and Verification
- Kotlin UniFFI Library Calls
- Greeting Contract and Rust Rules
- Shared Config and Localization
- Design Token Pipeline
- Codegen Tooling and Accessibility
- Native Greeting Screens
- Kotlin Foreign Future Callbacks
- Kotlin FFI Structures
- Kotlin RustBuffer Handling
- Kotlin FFI Converters
- CI Workflow and Build Checks
- Ownership Matrix and Repo Layout
- Development and Android Rules
- Hello Contract Call Flow
- Dependency Rules and Crates
- Architecture Layer Boundaries
- Kotlin Handle Map
- Kotlin Rust Call Helpers
- Design System Guide
- ADR-0001 Foundation Decision
- Planning Path and Architecture Check
- Kotlin Binding Integrity Checks
- FFI Extension Conventions
- Android Rust Build Script
- iOS Rust Build Script
- Cargo Workspace Members

## God Nodes (most connected - your core abstractions)
1. `UniffiLib` - 54 edges
2. `UniffiRustCallStatus` - 29 edges
3. `RustBuffer` - 27 edges
4. `Foundation verification 2026-11-14` - 23 edges
5. `Ownership matrix` - 18 edges
6. `Architecture compliance` - 18 edges
7. `Mobile foundation scope (index)` - 16 edges
8. `iOS 001 - Native iOS greeting (existing)` - 16 edges
9. `UniffiRustFutureContinuationCallback` - 15 edges
10. `Repository structure` - 15 edges

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
- **Greeting vertical slice: localized recipient through UniFFI to the Rust formatter** — readme_hello_world_greeting, shared_localization_readme_greeting_recipient, docs_architecture_overview_greeting_call_flow, docs_contracts_ffi_conventions_hello_contract, docs_architecture_overview_foundation_core_hello, docs_architecture_ownership_matrix_crates_mobile_ffi, docs_architecture_ownership_matrix_bindings, readme_uniffi [EXTRACTED 1.00]
- **Neutral JSON sources validated and generated into native theme and string resources** — design_system_readme_token_files, design_system_readme_tokens_schema, shared_config_readme_foundation_json, shared_localization_readme_catalog_format, design_system_readme_generate_design_tokens_modes, tooling_codegen_requirements_fastjsonschema, design_system_readme_generated_semantic_api, shared_localization_readme_generated_native_strings [INFERRED 0.85]
- **Canonical source over generated output: edit sources, regenerate, compare snapshots** — agents_never_hand_edit_generated_files, docs_architecture_ownership_matrix_derived_file_rule, docs_architecture_dependency_rules_one_way_generation, docs_decisions_adr_0001_foundation_checked_in_source_snapshots [INFERRED 0.85]
- **Design token pipeline from canonical JSON to native projections** — docs_design_system_token_conventions_canonical_token_sources, design_system_schemas_tokens_schema, scripts_generate_design_tokens, docs_design_system_platform_mapping_swiftui_token_projection, docs_design_system_platform_mapping_compose_token_projection, docs_quality_architecture_compliance_tokens_config_localization_check [INFERRED 0.85]
- **Automated architecture compliance checks** — docs_quality_architecture_compliance_rust_format_and_lint, docs_quality_architecture_compliance_core_and_ffi_contract_tests, docs_quality_architecture_compliance_cargo_dependency_and_governance_check, docs_quality_architecture_compliance_uniffi_generated_files_check, docs_quality_architecture_compliance_tokens_config_localization_check, docs_quality_architecture_compliance_ios_linkage_and_ui_check, docs_quality_architecture_compliance_android_linkage_and_ui_check [EXTRACTED 1.00]
- **Regenerate derived outputs with their canonical source, never hand-edit** — docs_rules_development_rules_regenerate_derived_files, docs_rules_design_system_rules_regenerate_projections, docs_quality_architecture_compliance_generated_drift_remediation, docs_rules_rust_rules_regenerate_after_signature_change, docs_rules_shared_resources_rules_generated_native_strings, docs_rules_anti_duplication_ffi_shapes_in_rust_export [INFERRED 0.85]
- **Tracer bullet greeting path from shared core to both native screens** — docs_scope_index_tracer_bullet_build_approach, docs_scope_root_002_shared_greeting_contract, docs_scope_root_002_shared_greeting_contract_one_string_in_one_string_out_contract, docs_scope_ios_001_native_ios_greeting, docs_scope_android_001_native_android_greeting, docs_scope_root_006_hosted_build_verification [INFERRED 0.85]
- **Open (planned) scope items across the three workspaces** — docs_scope_root_007_one_planning_path, docs_scope_root_008_hosted_results_in_the_verification_record, docs_scope_ios_002_lowest_supported_ios_and_large_text, docs_scope_android_002_lowest_supported_android_and_large_text [EXTRACTED 1.00]
- **Verification evidence chain: local checks, hosted jobs and the verification record** — docs_scope_root_005_reproducible_local_builds_and_checks, docs_scope_root_006_hosted_build_verification, docs_scope_root_008_hosted_results_in_the_verification_record, docs_scope_index_hosted_run_43593365100, docs_scope_root_005_reproducible_local_builds_and_checks_stale_local_verification_record, docs_scope_root_008_hosted_results_in_the_verification_record_single_list_of_unverified_targets [INFERRED 0.85]

## Communities (31 total, 1 thin omitted)

### Community 0 - "Swift UniFFI Bindings"
Cohesion: 0.05
Nodes (64): Array, createReader(), createWriter(), Data, FfiConverter, FfiConverterPrimitive, FfiConverterRustBuffer, FfiConverterString (+56 more)

### Community 1 - "Scope Records and Verification"
Cohesion: 0.05
Nodes (70): GreetingTest, GreetingUITests, UInt8, CIContext, CoreImage, Architecture compliance, Android linkage and UI check (Linux CI job, emulator instrumentation), GitHub Actions CI jobs (macOS and Linux) (+62 more)

### Community 2 - "Kotlin UniFFI Library Calls"
Cohesion: 0.05
Nodes (4): uniffiCheckCallStatus(), UniffiLib, UniffiRustCallStatus, UniffiRustFutureContinuationCallback

### Community 3 - "Greeting Contract and Rust Rules"
Cohesion: 0.06
Nodes (44): hello(), preserves_empty_names_and_whitespace(), String, main(), hello(), String, Per-target reading order and screen-reader review, Design definitions compile independently of Cargo and UniFFI (+36 more)

### Community 4 - "Shared Config and Localization"
Cohesion: 0.07
Nodes (43): Build-time generation: token JSON and locale JSON -> native theme inputs and localization resources, shared/config, shared/localization, shared/assets: owner of public settings, locale content and brand masters, Shared resource ownership rules, Draft 7 schemas in shared/specifications, Shared resources owner (build configuration, localization, brand assets), 004 - Shared settings, text and brand assets (existing), Greeting sentence 'Hello, {name}!' formed in English by the core, Single English localization catalog and public fallback locale (+35 more)

### Community 5 - "Design Token Pipeline"
Cohesion: 0.10
Nodes (40): Canonical token schema (tokens.schema.json), System text scaling via generated text styles, Native controls styled with semantic tokens, Native token mapping, Compose sp mapping of logical text units, Jetpack Compose token projection (FoundationTokens), Dynamic Type mapping of headline and reading scales, Logical spacing units adapt to display density (+32 more)

### Community 6 - "Codegen Tooling and Accessibility"
Cohesion: 0.08
Nodes (26): Accessibility (design system), Status conveyed by text or semantics, not color alone, Honor platform reduced-motion setting, Text contrast check (4.5:1 minimum), W3C WCAG 2.2 contrast minimum guidance, Design system and resources result (seven generator tests), check_schema(), generate() (+18 more)

### Community 7 - "Native Greeting Screens"
Cohesion: 0.07
Nodes (27): App, MainActivity, FoundationTheme(), FoundationTokens, Palette, GreetingScreen(), MobileFoundationApp, .body (+19 more)

### Community 8 - "Kotlin Foreign Future Callbacks"
Cohesion: 0.08
Nodes (19): Disposable, NoHandle, UniffiCallbackInterfaceClone, UniffiCallbackInterfaceFree, UniffiForeignFutureCompleteF32, UniffiForeignFutureCompleteF64, UniffiForeignFutureCompleteI16, UniffiForeignFutureCompleteI32 (+11 more)

### Community 9 - "Kotlin FFI Structures"
Cohesion: 0.11
Nodes (15): UniffiByValue, UniffiForeignFutureDroppedCallbackStruct, UniffiForeignFutureResultF32, UniffiForeignFutureResultF64, UniffiForeignFutureResultI16, UniffiForeignFutureResultI32, UniffiForeignFutureResultI64, UniffiForeignFutureResultI8 (+7 more)

### Community 10 - "Kotlin RustBuffer Handling"
Cohesion: 0.16
Nodes (9): ByReference, ByValue, ForeignBytes, `hello`(), RustBuffer, uniffiTraitInterfaceCall(), uniffiTraitInterfaceCallWithError(), kotlin (+1 more)

### Community 11 - "Kotlin FFI Converters"
Cohesion: 0.21
Nodes (7): FfiConverter, FfiConverterRustBuffer, FfiConverterString, FfiType, ByteBuffer, KotlinType, ULong

### Community 12 - "CI Workflow and Build Checks"
Cohesion: 0.20
Nodes (14): Agent workflow: before handoff (run checks, report commands and unverified targets), Pass representative values through both generated languages, Mobile foundation CI workflow, CI job: android (JDK 17, API 36 emulator, Kotlin binding + Compose UI), Light and dark appearance verification in CI, CI job: foundation (locked Rust build + scripts/test.sh on ubuntu-24.04), CI job: ios (macos-26, Xcode 26.5, simulator + unsigned device link), SHA-pinned GitHub Actions with read-only contents permission (+6 more)

### Community 13 - "Ownership Matrix and Repo Layout"
Cohesion: 0.26
Nodes (14): AGENTS.md: Working in the mobile foundation, Agent workflow: before editing (locate owner, contract, callers, tests), App trees do not import one another; core never calls platform UI, Ownership matrix, apps/android: owner of Android UI, presentation state and OS APIs, apps/ios: owner of Apple UI, presentation state and OS APIs, design-system/tokens and schemas: owner of canonical visual values and semantic roles, docs/ and root AGENTS.md: architecture, ADRs and agent workflow (+6 more)

### Community 14 - "Development and Android Rules"
Cohesion: 0.19
Nodes (13): gradlew script, die(), warn(), ADR and policy update for new dependency or material architecture change, Android rules, Checked-in Gradle wrapper, New ABI requires Rust cross-build and runtime test, Development rules (+5 more)

### Community 15 - "Hello Contract Call Flow"
Cohesion: 0.22
Nodes (11): Architecture overview, foundation_core::hello (sole greeting formatter), Greeting call flow: SwiftUI/Compose -> generated binding -> C ABI/JNA -> mobile-ffi -> foundation-core, tests/contracts: Cargo integration tests for exported behavior, Mobile contract (FFI conventions), Public contract: hello(name: String) -> String in crates/mobile-ffi, UniFFI derives native functions, buffer handling and contract checks; no raw pointers or hand-maintained C ABI declarations, Single greeting as the minimal exercise of interop, linking, resources and display (+3 more)

### Community 16 - "Dependency Rules and Crates"
Cohesion: 0.32
Nodes (12): Never hand-edit generated files, Dependency rules, Workspace edge: mobile-ffi depends on foundation-core (std-only core), Generators consume neutral sources and never recover canonical values from native output, Proc-macro exports define the cross-language API; bindgen feature gates host CLI deps, bindings/swift and bindings/kotlin: generated FFI source snapshots, crates/core: owner of shared behavior, domain rules and application validation, crates/mobile-ffi: owner of cross-language API, records and typed errors (UniFFI) (+4 more)

### Community 17 - "Architecture Layer Boundaries"
Cohesion: 0.21
Nodes (12): Architecture boundaries, Documented capability boundary; adapters need an actual caller, Layer: design system (generated Swift/Kotlin values as shared visual vocabulary), Layer: native platform integration (Swift owns Apple services, Kotlin owns Android services), Layer: native presentation (views render, adapt to appearance, handle events), Layer: resources and tooling (build-host validation and generation), Layer: shared Rust (core owns behavior, FFI crate maps exports), Color selection, font scaling, layout and accessibility run natively (no shared renderer) (+4 more)

### Community 18 - "Kotlin Handle Map"
Cohesion: 0.42
Nodes (4): InternalException, T, UniffiHandleMap, UniffiNullRustCallStatusErrorHandler

### Community 19 - "Kotlin Rust Call Helpers"
Cohesion: 0.32
Nodes (6): E, UniffiForeignFutureCompleteVoid, uniffiRustCall(), UniffiRustCallStatusErrorHandler, uniffiRustCallWithError(), U

### Community 20 - "Design System Guide"
Cohesion: 0.43
Nodes (7): Design system guide, generate-design-tokens.sh modes: write, --check (drift), --test (failure cases), Generated semantic token API consumed by native apps, Five canonical token JSON files (primitives and semantic aliases), tokens.schema.json: single Draft 7 document keyed by filename stem, Shared build and generation commands, fastjsonschema==2.21.2 (sha256 hash-pinned schema validator)

### Community 21 - "ADR-0001 Foundation Decision"
Cohesion: 0.43
Nodes (7): Agent workflow: during implementation (place change in owning layer), New dependency edge needs an owning module, a use case and a test, ADR 0001: Native apps with a shared Rust core, Decision: neutral JSON tokens and validated shared sources generate native theme inputs and localization, Rejected alternative: implementing application behavior independently in both apps, Revisit conditions: dependency direction change, async native boundary, independently versioned clients, new shared crate or service, Extension procedure: PRD plus short implementation plan with owner, contract, dependency direction and verification matrix

### Community 22 - "Planning Path and Architecture Check"
Cohesion: 0.38
Nodes (5): Planning the next capability, Capabilities outside the baseline (auth, ERP, transport, storage, sync, flags, desktop ports), 007 - One planning path (planned, needs a decision), Required document check should cover the scope index, Split planning path: docs/plans versus docs/scope

### Community 23 - "Kotlin Binding Integrity Checks"
Cohesion: 0.60
Nodes (3): IntegrityCheckingUniffiLib, uniffiCheckApiChecksums(), uniffiCheckContractApiVersion()

### Community 24 - "FFI Extension Conventions"
Cohesion: 0.40
Nodes (5): Explicit application records and enums; private core/transport shapes mapped at the adapter, Async and cancellation conventions for future exports, Compatibility: version breaking contracts and coordinate regeneration, both apps and release, Conventions for extending the mobile contract, Typed UniFFI errors with stable variants; user-facing messages translated natively

### Community 25 - "Android Rust Build Script"
Cohesion: 0.40
Nodes (4): CARGO_TARGET_AARCH64_LINUX_ANDROID_LINKER, CARGO_TARGET_X86_64_LINUX_ANDROID_LINKER, PATH, build-android-rust.sh script

### Community 26 - "iOS Rust Build Script"
Cohesion: 0.50
Nodes (3): CARGO_TARGET_DIR, PATH, build-ios-rust.sh script

## Knowledge Gaps
- **56 isolated node(s):** `.body`, `CoreImage`, `XCTest`, `UniffiWithHandle`, `NoHandle` (+51 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `.body` connect `Native Greeting Screens` to `Swift UniFFI Bindings`?**
  _High betweenness centrality (0.148) - this node is a cross-community bridge._
- **Why does `hello()` connect `Swift UniFFI Bindings` to `Native Greeting Screens`?**
  _High betweenness centrality (0.146) - this node is a cross-community bridge._
- **Why does `GreetingScreen` connect `Native Greeting Screens` to `Greeting Contract and Rust Rules`, `Design Token Pipeline`?**
  _High betweenness centrality (0.139) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Foundation verification 2026-11-14` (e.g. with `Deliver one exercisable vertical slice at a time and record observed results` and `Record separately what compiled and what ran`) actually correct?**
  _`Foundation verification 2026-11-14` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `.body`, `CoreImage`, `XCTest` to the rest of the system?**
  _56 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Swift UniFFI Bindings` be split into smaller, more focused modules?**
  _Cohesion score 0.05444596443228454 - nodes in this community are weakly interconnected._
- **Should `Scope Records and Verification` be split into smaller, more focused modules?**
  _Cohesion score 0.05160662122687439 - nodes in this community are weakly interconnected._