package foundation.mobile

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.runtime.remember
import androidx.compose.ui.res.stringResource
import foundation.designsystem.FoundationTheme
import foundation.presentation.GreetingScreen
import uniffi.mobile_ffi.hello

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            val recipient = stringResource(R.string.greeting_recipient)
            val greeting = remember(recipient) { hello(recipient) }
            FoundationTheme {
                GreetingScreen(greeting)
            }
        }
    }
}
