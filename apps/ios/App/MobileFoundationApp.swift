import SwiftUI

@main
struct MobileFoundationApp: App {
    var body: some Scene {
        WindowGroup {
            GreetingScreen(greeting: hello(name: String(localized: "greeting_recipient")))
        }
    }
}
