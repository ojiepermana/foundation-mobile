# 005 - Reproducible local builds and checks

**Phase** Verification · **Status** `existing`

You can build both apps from a checkout and see when checked in bindings or resources differ from their sources.

**Done when:** the documented commands build both native packages, exercise the shared contract and reject invalid dependencies or generated files. The verification record names the targets exercised and the limits of those results. [Build commands](../../../README.md) · [Shared checks](../../../scripts/test.sh) · [Local results](../../quality/verification.md)

The local record predates the hosted run and still says the hosted jobs have not been executed. That update is planned in [008](008%20-%20Hosted%20results%20in%20the%20verification%20record.md).
