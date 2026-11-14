# 006 - Hosted build verification

**Phase** Verification · **Status** `done`

You can use the hosted jobs to check the shared contract and both native apps on the same revision. Android installs the supported SDK packages. The iOS simulator boots in each system appearance before XCTest reads the greeting and samples the rendered background.

**Done when:** the shared checks pass and both hosted native jobs build and exercise the greeting on the same revision. The result identifies the revision and each job outcome. [Workflow](../../../.github/workflows/foundation.yml)

* [x] Repair the hosted checks with `/develop hosted build verification`.
* [x] Verify all three jobs on commit `65875793e37c708f31088fb65dca939d57cc2a50`. The foundation, iOS and Android jobs all passed. Both apps exercised light and dark appearance. [Hosted run 43593365100](https://github.com/ojiepermana/foundation-mobile/actions/runs/43593365100)
