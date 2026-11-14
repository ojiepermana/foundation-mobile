# Brand assets

This directory owns the canonical source when a shared brand asset is introduced. The greeting uses native text and has no artwork.

Use a descriptive lower snake case basename. Keep paths stable across exports. Store vector marks as optimized SVG with a viewBox and raster artwork as an optimized, lossless, profiled PNG master at the highest required resolution. When artwork must vary by appearance, pair sources using `_light` and `_dark` and document their pairing.

The first asset change should include its license or provenance, dimensions or aspect ratio, and a reproducible export command. Target the native asset catalog on Apple and drawable resources on Android. Prefer resolution-independent exports for vectors. For bitmaps, generate the native density variants from the master and verify the rendered size and appearance on each platform. Keep exports and asset source revisions together in Git. Platform-owned SF Symbols and Android system icons are selected in native presentation.
