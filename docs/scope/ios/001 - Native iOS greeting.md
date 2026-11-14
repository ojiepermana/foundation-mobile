# 001 - Native iOS greeting

**Phase** First working slice · **Status** `existing`

You can launch the app and read the string returned by the shared core. The screen follows the system appearance and uses a native text style that supports Dynamic Type.

**Done when:** the app links the shared library, displays `Hello, World!` from the localized recipient, and exposes the greeting to accessibility in light and dark appearance. [App entry](../../../apps/ios/App/MobileFoundationApp.swift) · [Greeting screen](../../../apps/ios/Presentation/GreetingScreen.swift) · [UI test](../../../apps/ios/UITests/GreetingUITests.swift)

The iPhone 17 simulator on iOS 27.0 passed both appearances. On iOS 26.5 the greeting appeared, but the simulator stayed light when dark appearance was requested. The unsigned device build linked successfully. Physical device and minimum version runtime coverage remain unverified. [Local results](../../quality/verification.md)
