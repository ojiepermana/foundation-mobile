# Design principles

Use semantic names for decisions that both apps share. The greeting demonstrates the complete path from the background, foreground, type and page-spacing roles to system-rendered text. Changing an existing role starts in the canonical JSON and propagates through code generation.

Keep layout, native text measurement, gestures and focus behavior in presentation. Design definitions compile to native code independently of Cargo and UniFFI. See [platform mapping](platform-mapping.md).
