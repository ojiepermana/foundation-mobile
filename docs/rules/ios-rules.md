# iOS

Use SwiftUI for presentation, including adaptive layout, Dynamic Type, native colors resolved for the active appearance and standard accessibility semantics. Use generated semantic tokens and the native localization resource. Render the returned Rust string verbatim so the framework treats it as data.

Call the generated Swift function for shared behavior. Keep native permissions, UIKit delegates and device lifecycle in the Apple adapter that needs them. Introduce presentation state or a ViewModel when the view actually needs state management.

The Xcode target compiles the generated Swift binding and imports the generated Clang module. Match the Rust archive to the selected SDK and CPU. A simulator arm64 archive and a device arm64 archive are different targets. Use the [build and UI verification commands](../../README.md) after changes to Xcode settings, Rust linking or the greeting.
