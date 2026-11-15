// Generated from design-system/tokens by scripts/generate-design-tokens.sh.
package foundation.designsystem

import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

object FoundationTokens {
    data class Palette(
        val background: Color,
        val border: Color,
        val brand: Color,
        val error: Color,
        val primary: Color,
        val secondary: Color,
        val success: Color,
        val surface: Color,
        val textPrimary: Color,
        val textSecondary: Color,
        val warning: Color,
    )

    private val darkPalette = Palette(
        background = Color(0xFF111824),
        border = Color(0xFF738098),
        brand = Color(0xFF9ABCFF),
        error = Color(0xFFFFA5A6),
        primary = Color(0xFF9ABCFF),
        secondary = Color(0xFF71D5CC),
        success = Color(0xFF8CD9A2),
        surface = Color(0xFF202B3D),
        textPrimary = Color(0xFFFFFFFF),
        textSecondary = Color(0xFFCBD6E5),
        warning = Color(0xFFFFBC6A),
    )

    private val lightPalette = Palette(
        background = Color(0xFFF4F6FA),
        border = Color(0xFFBBC6D6),
        brand = Color(0xFF235CBA),
        error = Color(0xFFA9262D),
        primary = Color(0xFF235CBA),
        secondary = Color(0xFF006A69),
        success = Color(0xFF216B41),
        surface = Color(0xFFFFFFFF),
        textPrimary = Color(0xFF172133),
        textSecondary = Color(0xFF46546B),
        warning = Color(0xFF895000),
    )

    fun palette(dark: Boolean): Palette = if (dark) darkPalette else lightPalette

    val spacingContent = 12.dp
    val spacingPage = 24.dp

    val radiusSurface = 16.dp

    const val motionFeedbackMillis = 160

    val typographyBody = TextStyle(
        fontSize = 16.sp,
        lineHeight = 24.sp,
        fontWeight = FontWeight(400),
    )
    val typographyHeading = TextStyle(
        fontSize = 32.sp,
        lineHeight = 40.sp,
        fontWeight = FontWeight(600),
    )
}
