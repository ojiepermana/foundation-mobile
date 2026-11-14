# 001 - Native iOS greeting

**Phase** First working slice · **Status** `existing`

You can launch the app and read the string returned by the shared core. The screen follows the system appearance and uses a native text style that supports Dynamic Type.

**Done when:** the app links the shared library, displays `Hello, World!` from the localized recipient, and exposes the greeting to accessibility in light and dark appearance. [App entry](../../../apps/ios/App/MobileFoundationApp.swift) · [Greeting screen](../../../apps/ios/Presentation/GreetingScreen.swift) · [UI test](../../../apps/ios/UITests/GreetingUITests.swift)

The iPhone 17 simulator on iOS 27.0 passed both appearances locally. The hosted run passed both appearances on iOS 26.5, with a fresh boot for each one. An earlier local attempt on iOS 26.5 stayed light when dark appearance was requested. The unsigned device build linked successfully. The minimum version and large text runs are planned in [002](002%20-%20Lowest%20supported%20iOS%20and%20large%20text.md). Physical device coverage remains unverified. [Local results](../../quality/verification.md) · [Hosted run 43593365100](https://github.com/ojiepermana/foundation-mobile/actions/runs/43593365100)
