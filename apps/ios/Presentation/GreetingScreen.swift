import SwiftUI

struct GreetingScreen: View {
    @Environment(\.colorScheme) private var appearance
    let greeting: String

    var body: some View {
        let palette = FoundationTokens.palette(for: appearance)

        Text(verbatim: greeting)
            .font(FoundationTokens.typographyHeading)
            .foregroundStyle(palette.textPrimary)
            .multilineTextAlignment(.center)
            .accessibilityIdentifier("greeting")
            .padding(FoundationTokens.spacingPage)
            .frame(maxWidth: .infinity, maxHeight: .infinity)
            .background(palette.background.ignoresSafeArea())
    }
}
