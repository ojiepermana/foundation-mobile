# Development rules

Start at the [ownership matrix](../architecture/ownership-matrix.md). Trace the calling screen, its generated binding, the FFI export and the core function before changing shared behavior. Limit each change to the smallest slice that can be exercised through its real caller.

Regenerate derived files alongside their canonical inputs. Review the generated diff for API, naming, locale or appearance changes. Keep binaries, signing material, developer SDK paths and IDE user data outside the repository. The Gradle wrapper JAR is a versioned bootstrap dependency with an upstream checksum.

Run [foundation checks](../quality/architecture-compliance.md) before handing off. A change to platform integration needs a build and, when the runtime is available, an invocation on that platform. Record separately what compiled and what ran.

Use a [plan](../plans/README.md) for a new capability. An ADR records a material architectural trade-off and the dependency or ownership consequences.
