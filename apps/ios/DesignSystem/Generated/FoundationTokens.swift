// Generated from design-system/tokens by scripts/generate-design-tokens.sh.
import SwiftUI

enum FoundationTokens {
    struct Palette {
        let background: Color
        let border: Color
        let brand: Color
        let error: Color
        let primary: Color
        let secondary: Color
        let success: Color
        let surface: Color
        let textPrimary: Color
        let textSecondary: Color
        let warning: Color
    }

    private static let dark = Palette(
        background: Color(.sRGB, red: 17/255, green: 24/255, blue: 36/255),
        border: Color(.sRGB, red: 115/255, green: 128/255, blue: 152/255),
        brand: Color(.sRGB, red: 154/255, green: 188/255, blue: 255/255),
        error: Color(.sRGB, red: 255/255, green: 165/255, blue: 166/255),
        primary: Color(.sRGB, red: 154/255, green: 188/255, blue: 255/255),
        secondary: Color(.sRGB, red: 113/255, green: 213/255, blue: 204/255),
        success: Color(.sRGB, red: 140/255, green: 217/255, blue: 162/255),
        surface: Color(.sRGB, red: 32/255, green: 43/255, blue: 61/255),
        textPrimary: Color(.sRGB, red: 255/255, green: 255/255, blue: 255/255),
        textSecondary: Color(.sRGB, red: 203/255, green: 214/255, blue: 229/255),
        warning: Color(.sRGB, red: 255/255, green: 188/255, blue: 106/255)
    )

    private static let light = Palette(
        background: Color(.sRGB, red: 244/255, green: 246/255, blue: 250/255),
        border: Color(.sRGB, red: 187/255, green: 198/255, blue: 214/255),
        brand: Color(.sRGB, red: 35/255, green: 92/255, blue: 186/255),
        error: Color(.sRGB, red: 169/255, green: 38/255, blue: 45/255),
        primary: Color(.sRGB, red: 35/255, green: 92/255, blue: 186/255),
        secondary: Color(.sRGB, red: 0/255, green: 106/255, blue: 105/255),
        success: Color(.sRGB, red: 33/255, green: 107/255, blue: 65/255),
        surface: Color(.sRGB, red: 255/255, green: 255/255, blue: 255/255),
        textPrimary: Color(.sRGB, red: 23/255, green: 33/255, blue: 51/255),
        textSecondary: Color(.sRGB, red: 70/255, green: 84/255, blue: 107/255),
        warning: Color(.sRGB, red: 137/255, green: 80/255, blue: 0/255)
    )

    static func palette(for scheme: ColorScheme) -> Palette {
        scheme == .dark ? dark : light
    }

    static let spacingContent: CGFloat = 12
    static let spacingPage: CGFloat = 24

    static let radiusSurface: CGFloat = 16

    static let motionFeedback: TimeInterval = 160 / 1000

    static let typographyBody: Font = .system(.body, weight: .regular)
    static let typographyGreeting: Font = .system(.title, weight: .semibold)
}
