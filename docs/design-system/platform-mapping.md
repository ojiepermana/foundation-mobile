# Native token mapping

| Role | SwiftUI | Jetpack Compose |
| --- | --- | --- |
| Color | `FoundationTokens.palette(for: colorScheme)` yields sRGB `Color` properties | `FoundationTokens.palette(dark)` yields opaque `Color` properties for the current appearance |
| Typography | System text style plus weight, through `Font.system` | `TextStyle` with sp size, sp line height and `FontWeight` |
| Spacing and radius | `CGFloat` in points | `Dp` |
| Motion | `TimeInterval` in seconds | Integer milliseconds |

Swift maps the canonical `headline` and `reading` scales to the Dynamic Type styles `.title` and `.body`. Apple's text styles determine the actual metrics across text sizes. Compose maps each logical size and line-height unit to one sp, so Android applies the user's font scale. Register the corresponding SwiftUI style in the token generator when introducing a new scale.

`typographyHeading` and `spacingPage` have the same role in both projections. The native presentation owns layout, typography measurement and environment updates. Use logical spacing in these APIs so the system can adapt to display density. [SwiftUI system text styles](https://developer.apple.com/documentation/swiftui/font/system(_:design:weight:)) · [Compose theming](https://developer.android.com/develop/ui/compose/designsystems/material3)
