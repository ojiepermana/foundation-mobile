# Planning the next capability

The baseline ends at the displayed Rust greeting and the native resources it needs. Authentication, user and ERP features, transport clients, storage, sync, image processing, background transfers, flag engines, advanced navigation, large component libraries and desktop ports each require separate analysis.

For a new capability, write a PRD and a short implementation plan here. Include the user outcome, scope, acceptance criteria, existing owner, public contract, dependency direction, platform-specific work and a verification matrix. Identify existing behavior or assets to reuse. Justify each proposed crate, service or framework. Record material architecture decisions under `docs/decisions/` and link the plan to them.

Deliver one exercisable vertical slice at a time. Update the plan with observed results, including runtime checks still outstanding.
