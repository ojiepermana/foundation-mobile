package foundation.mobile

import android.content.res.Configuration
import androidx.compose.ui.semantics.SemanticsActions
import androidx.compose.ui.text.TextLayoutResult
import androidx.compose.ui.test.assertIsDisplayed
import androidx.compose.ui.test.junit4.createAndroidComposeRule
import androidx.compose.ui.test.onNodeWithText
import androidx.compose.ui.test.performSemanticsAction
import foundation.designsystem.FoundationTokens
import org.junit.Assert.assertEquals
import org.junit.Rule
import org.junit.Test
import uniffi.mobile_ffi.hello

class GreetingTest {
    @get:Rule val compose = createAndroidComposeRule<MainActivity>()

    @Test fun roundTripsUnicodeThroughRust() {
        assertEquals("Hello, Zoë 🌍!", hello("Zoë 🌍"))
    }

    @Test fun displaysTheSharedGreeting() {
        val recipient = compose.activity.getString(R.string.greeting_recipient)
        val label = compose.onNodeWithText(hello(recipient)).assertIsDisplayed()

        val uiMode = compose.activity.resources.configuration.uiMode
        val dark = uiMode and Configuration.UI_MODE_NIGHT_MASK == Configuration.UI_MODE_NIGHT_YES
        val layouts = mutableListOf<TextLayoutResult>()
        label.performSemanticsAction(SemanticsActions.GetTextLayoutResult) { it(layouts) }
        val style = layouts.single().layoutInput.style
        assertEquals(FoundationTokens.typographyHeading.fontSize, style.fontSize)
        assertEquals(FoundationTokens.palette(dark).textPrimary, style.color)
    }
}
