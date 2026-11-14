"""Render validated design tokens as native value types."""

from pathlib import Path


SWIFT_PATH = Path("apps/ios/DesignSystem/Generated/FoundationTokens.swift")
KOTLIN_PATH = Path("apps/android/designsystem/src/main/kotlin/foundation/designsystem/FoundationTokens.kt")
HEADER = "// Generated from design-system/tokens by scripts/generate-design-tokens.sh."
SWIFT_TEXT_STYLES = {"headline": "title", "reading": "body"}
SWIFT_WEIGHTS = {
    100: "ultraLight", 200: "thin", 300: "light", 400: "regular", 500: "medium",
    600: "semibold", 700: "bold", 800: "heavy", 900: "black",
}


def resolve(primitives, name, role):
    if name not in primitives:
        raise ValueError(f"{role} references unknown primitive {name!r}")
    return primitives[name]


def property_name(prefix, role):
    return prefix + role[:1].upper() + role[1:]


def luminance(rgb):
    channels = (int(rgb[i:i + 2], 16) / 255 for i in (0, 2, 4))
    linear = [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in channels]
    return sum(v * w for v, w in zip(linear, (0.2126, 0.7152, 0.0722)))


def palettes(colors):
    result = {}
    for mode in ("dark", "light"):
        palette = {
            role: resolve(colors["primitives"], aliases[mode], f"{role}.{mode}")[1:]
            for role, aliases in sorted(colors["semantic"].items())
        }
        for text in ("textPrimary", "textSecondary"):
            for background in ("background", "surface"):
                low, high = sorted(luminance(palette[role]) for role in (text, background))
                if (high + 0.05) / (low + 0.05) < 4.5:
                    raise ValueError(f"{mode} {text}/{background} contrast is below 4.5:1")
        result[mode] = palette
    return result


def render(tokens):
    sw = [HEADER, "import SwiftUI", "", "enum FoundationTokens {", "    struct Palette {"]
    kt = [
        HEADER, "package foundation.designsystem", "",
        "import androidx.compose.ui.graphics.Color",
        "import androidx.compose.ui.text.TextStyle",
        "import androidx.compose.ui.text.font.FontWeight",
        "import androidx.compose.ui.unit.dp", "import androidx.compose.ui.unit.sp", "",
        "object FoundationTokens {", "    data class Palette(",
    ]
    modes = palettes(tokens["colors"])
    for role in modes["light"]:
        sw.append(f"        let {role}: Color")
        kt.append(f"        val {role}: Color,")
    sw.append("    }")
    kt.append("    )")
    for mode, palette in modes.items():
        sw.extend(["", f"    private static let {mode} = Palette("])
        kt.extend(["", f"    private val {mode}Palette = Palette("])
        for role, rgb in palette.items():
            r, g, b = (int(rgb[i:i + 2], 16) for i in (0, 2, 4))
            sw.append(f"        {role}: Color(.sRGB, red: {r}/255, green: {g}/255, blue: {b}/255),")
            kt.append(f"        {role} = Color(0xFF{rgb}),")
        sw[-1] = sw[-1].rstrip(",")
        sw.append("    )")
        kt.append("    )")
    sw.extend(["", "    static func palette(for scheme: ColorScheme) -> Palette {",
               "        scheme == .dark ? dark : light", "    }"])
    kt.extend(["", "    fun palette(dark: Boolean): Palette = if (dark) darkPalette else lightPalette"])
    for group in ("spacing", "radius", "motion"):
        sw.append("")
        kt.append("")
        for role, alias in sorted(tokens[group]["semantic"].items()):
            value = int(resolve(tokens[group]["primitives"], alias, f"{group}.{role}"))
            name = property_name(group, role)
            if group == "motion":
                sw.append(f"    static let {name}: TimeInterval = {value} / 1000")
                kt.append(f"    const val {name}Millis = {value}")
            else:
                sw.append(f"    static let {name}: CGFloat = {value}")
                kt.append(f"    val {name} = {value}.dp")
    typography = tokens["typography"]
    sw.append("")
    kt.append("")
    for role, aliases in sorted(typography["semantic"].items()):
        scale = resolve(typography["primitives"]["scale"], aliases["scale"], f"typography.{role}.scale")
        weight = int(resolve(typography["primitives"]["weight"], aliases["weight"], f"typography.{role}.weight"))
        scale_name = aliases["scale"]
        if scale_name not in SWIFT_TEXT_STYLES:
            raise ValueError(f"typography.{role}: add a SwiftUI text-style mapping for scale {scale_name!r}")
        name = property_name("typography", role)
        sw.append(f"    static let {name}: Font = .system(.{SWIFT_TEXT_STYLES[scale_name]}, weight: .{SWIFT_WEIGHTS[weight]})")
        kt.extend([f"    val {name} = TextStyle(",
                   f"        fontSize = {scale['size']}.sp,",
                   f"        lineHeight = {scale['lineHeight']}.sp,",
                   f"        fontWeight = FontWeight({weight}),", "    )"])
    return {SWIFT_PATH: "\n".join(sw + ["}", ""]), KOTLIN_PATH: "\n".join(kt + ["}", ""])}
