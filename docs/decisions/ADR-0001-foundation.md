# ADR 0001 · Native apps with a shared Rust core

**Status** Accepted for the initial foundation, 2026-11-14.

## Context

The product needs independently native Apple and Android presentations with one implementation of shared behavior and one shared visual vocabulary. A single greeting is enough to exercise language interoperability, linking, resources and display before committing to additional services.

## Decision

Use two Cargo workspace members. The dependency-free core owns the formatter. The FFI crate exports it with UniFFI proc macros and includes a feature-gated host generator entry point. Compile an Apple static library and Android shared libraries. Each native app consumes a checked-in generated language binding.

Maintain visual primitives and semantic tokens as neutral JSON. Generate native theme inputs and native localization resources from validated shared sources. Apply appearance and type scaling on each platform. Keep public configuration definitions and brand conventions under shared resources.

Keep source snapshots in version control so Xcode and Gradle can compile a reviewed contract directly. Regenerate in a fresh directory during verification and compare results. Ignore target binaries and SDK installations.

## Consequences

A mobile API change affects the export, both binding snapshots and both app verification paths. The two build systems retain platform-specific SDK and linker setup. Keeping contract types separate from the implementation allows the core to evolve without leaking internal types into native applications. Visual and copy changes can ship through resource generation without touching Rust.

A shared UI runtime would move control of navigation and rendering away from the native frameworks. Independently implementing application behavior in both apps would create two places to change a rule. The chosen boundaries preserve the native presentation and one behavioral owner.

## Revisit when

Record a new decision if a capability changes the dependency direction, crosses the native boundary asynchronously, requires independently versioned clients, or adds a new shared crate or service. A feature plan must first identify a real caller and verification strategy.
