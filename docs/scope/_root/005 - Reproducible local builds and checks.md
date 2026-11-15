# 005 - Reproducible local builds and checks

**Phase** Verification · **Status** `done`

You can build both apps from a checkout and see when checked in bindings or resources differ from their sources.

**Done when:** the documented commands build both native packages, exercise the shared contract and reject invalid dependencies or generated files. The verification record names the targets exercised and the limits of those results. [Build commands](../../../README.md) · [Shared checks](../../../scripts/test.sh) · [Local results](../../quality/verification.md)

* [x] Verify on commit `58e3d2c570a0f5074357cd22eb228f5bf393e8a6`. `scripts/test.sh` passed on macOS 27.0.1, including the dependency policy and the test for stale, edited and missing generated files. [Hosted run 43593365100](https://github.com/ojiepermana/foundation-mobile/actions/runs/43593365100) built both native apps and exercised the contract on `65875793e37c708f31088fb65dca939d57cc2a50`, and no build script or app source has changed since. The record lists the runtimes exercised and one list of targets still unverified. [Verification record](../../quality/verification.md)
