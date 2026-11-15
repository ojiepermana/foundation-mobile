# Mobile foundation scope

You can build two native apps that display a greeting from one shared implementation. This scope follows that greeting from its owner through both screens and the checks that run when the repository changes.

**Build approach:** Tracer Bullet. A shared change follows one working path from the core to both apps.  
**Workflow:** Beta. After a change, you can use `/check verify` on the affected apps, then `/test` for the affected contracts. A new ownership or contract decision belongs in the design stage.

## At a glance

| Workspace | What it owns | Complete | Open |
| --- | --- | --- | --- |
| [Shared foundation](_root/scope.md) | Ownership, shared behavior, design, resources and build checks | 8 of 10 | 009 A new project from the foundation, 010 Schemas free of sample names |
| [iOS](ios/scope.md) | The native greeting on Apple devices | 1 of 2 | 002 Lowest supported iOS and large text |
| [Android](android/scope.md) | The native greeting on Android devices | 1 of 2 | 002 Lowest supported Android and large text |

The [verification record](../quality/verification.md) lists what ran, local and hosted.

## Deferred

The foundation ends at Hello World. Three pieces of work stay close to the greeting and are kept here so the plan stays honest.

* **A contract beyond one string**: a record, a typed error and an async call that cross into both apps. The repository rules ask for a real caller first, so the first product feature is the place to prove them · needs a decision
* **A second language end to end**: a second catalog running in both apps. The core forms the greeting sentence in English, so where the sentence shape lives comes first · needs a decision
* **Signing, physical device runs and store delivery**: a signed build on real hardware and a path to the stores · needs a decision

Accounts, business modules, backend clients, storage, offline sync, image processing, background transfers, remote flags, advanced navigation, a component library and desktop apps each need their own scope before work starts.

## Legend

`existing` means the capability shipped before this scope. `done` means the planned outcome has been verified. The first open box is the suggested next step. Each workspace numbers its scope files independently from `001`, using `001 - Scope name.md`. The workspace index links to each file.
