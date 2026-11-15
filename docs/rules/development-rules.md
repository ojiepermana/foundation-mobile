# Development rules

Start at the [ownership matrix](../architecture/ownership-matrix.md). Trace the calling screen, its generated binding, the FFI export and the core function before changing shared behavior. Limit each change to the smallest slice that can be exercised through its real caller.

Regenerate derived files alongside their canonical inputs. Review the generated diff for API, naming, locale or appearance changes. Keep binaries, signing material, developer SDK paths and IDE user data outside the repository. The Gradle wrapper JAR is a versioned bootstrap dependency with an upstream checksum.

Run [foundation checks](../quality/architecture-compliance.md) before handing off. A change to platform integration needs a build and, when the runtime is available, an invocation on that platform. Record separately what compiled and what ran.

Plan a new capability in the [scope](../scope/index.md). Add a row to the owning workspace and treat it as the brief: it states the user outcome and a done when line. Then write a spec under `docs/specs/` before code. A smaller change needs a spec only when it changes ownership, a contract or a dependency. The [service rules](service-rules.md), the [dependency rules](../architecture/dependency-rules.md), the [FFI conventions](../contracts/ffi-conventions.md), the [quality checks](../quality/architecture-compliance.md) and the Revisit when list in the [foundation decision](../decisions/ADR-0001-foundation.md) name those triggers. `/scope` and `/architect` are the usual way to write both files.

A spec for a new capability covers the user outcome, scope, acceptance criteria, existing owner, public contract, dependency direction, platform specific work and a verification matrix. It names existing behavior or assets to reuse and justifies each proposed crate, service or framework. Specs are numbered `NNNN-kebab-title.md` in the folder that mirrors the scope workspace. A spec that replaces an earlier record marks that record as superseded. The foundation decision is the founding record and stays in `docs/decisions/`.

Record progress in the scope row and what ran in the [verification record](../quality/verification.md).
