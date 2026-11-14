# Mobile foundation scope

You can build two native apps that display a greeting from one shared implementation. This scope follows that greeting from its owner through both screens and the checks that run when the repository changes.

**Build approach:** Tracer Bullet. A shared change follows one working path from the core to both apps.  
**Workflow:** Beta. After a change, you can use `/check verify` on the affected apps, then `/test` for the affected contracts. A new ownership or contract decision belongs in the design stage.

## At a glance

| Workspace | What it owns | Complete | Open |
| --- | --- | --- | --- |
| [Shared foundation](_root/scope.md) | Ownership, shared behavior, design, resources and build checks | 6 of 6 | |
| [iOS](ios/scope.md) | The native greeting on Apple devices | 1 of 1 | |
| [Android](android/scope.md) | The native greeting on Android devices | 1 of 1 | |

All three hosted jobs passed on `6587579`, including the iOS and Android greeting tests in both appearances. [Hosted results](https://github.com/ojiepermana/foundation-mobile/actions/runs/43593365100)

## Deferred

The foundation ends at Hello World. Accounts, business modules, backend clients, storage, offline sync, image processing, background transfers, remote flags, advanced navigation, a component library and desktop apps need their own product brief and scope. Signing and store delivery are outside this slice.

## Legend

`existing` means the capability shipped before this scope. `done` means the planned outcome has been verified. The first open box is the suggested next step. Each workspace numbers its scope files independently from `001`, using `001 - Scope name.md`. The workspace index links to each file.
