package foundation.designsystem

import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Typography
import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.runtime.Composable

@Composable
internal fun FoundationTheme(content: @Composable () -> Unit) {
    val dark = isSystemInDarkTheme()
    val palette = FoundationTokens.palette(dark)
    val base = if (dark) darkColorScheme() else lightColorScheme()
    MaterialTheme(
        colorScheme = base.copy(
            primary = palette.primary,
            secondary = palette.secondary,
            error = palette.error,
            background = palette.background,
            onBackground = palette.textPrimary,
            surface = palette.surface,
            onSurface = palette.textPrimary,
            outline = palette.border,
        ),
        typography = Typography(headlineLarge = FoundationTokens.typographyHeading),
        content = content,
    )
}
