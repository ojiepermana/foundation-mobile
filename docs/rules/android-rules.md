# Android

Use Compose for presentation. Read the localized name through Android resources, call the generated Kotlin binding and render the result. Use native Material semantics, adaptive colors, font scaling and system insets. Keep OS-specific lifecycle and permission handling in the Android app.

The Gradle app packages the Rust shared object and JNA runtime. Keep the Rust target, NDK linker, minimum API, ABI filters and packaged JNI libraries consistent. New ABIs need a Rust cross-build and a runtime test on matching hardware or an emulator. An APK assembly alone cannot detect a missing native symbol at invocation.

Use the checked-in wrapper. Run [Android build and instrumentation checks](../../README.md) after changing native packaging, Gradle configuration or binding call sites.
