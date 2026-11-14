# 002 - Lowest supported iOS and large text

**Phase** Verification · **Status** `planned`

You can trust the declared minimum version and the Dynamic Type claim, because both have run. The project deploys to iOS 17, and the greeting has only run on iOS 26.5 and 27.0. No test changes the text size.

**Done when:** the greeting test passes on an iOS 17 simulator in light and dark appearance, the greeting stays whole at the largest accessibility text size, and the result names the runtime. [Deployment target](../../../apps/ios/Config/Project.xcconfig) · [UI test](../../../apps/ios/UITests/GreetingUITests.swift)

* [ ] Add the runs with `/develop lowest supported iOS and large text`.
