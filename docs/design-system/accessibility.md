# Accessibility

The generator checks `textPrimary` and `textSecondary` against both `background` and `surface` in each appearance. It compares sRGB relative luminance using an unrounded minimum ratio of 4.5 to 1. Additional color combinations require their own review before use. [W3C contrast guidance](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)

Use the generated SwiftUI text styles and Compose sp sizes so system text scaling applies. Give text room to wrap at large sizes. Review reading order, native screen-reader announcements and layout on each target. Convey status through text or semantics as well as color. When adding animated interactions, honor the platform’s reduced-motion setting.
