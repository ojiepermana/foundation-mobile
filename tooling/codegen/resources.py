"""Compile shared localized strings to native resource bundles."""
from collections import Counter
from pathlib import Path
import re
from string import Formatter
from xml.sax.saxutils import escape


IOS_RESOURCES = Path("apps/ios/App/Resources")
ANDROID_RESOURCES = Path("apps/android/app/src/main/res")
MARKER = "Generated from shared/localization by scripts/generate-design-tokens.sh."


def parse_template(text):
    if not text.strip() or any(ord(c) < 32 and c not in "\t\n" for c in text):
        raise ValueError("expected non-blank localizable text without control characters")
    # Only named string placeholders are supported. Doubled braces denote literals.
    parts = list(Formatter().parse(text))
    names = []
    for _, name, spec, conversion in parts:
        if name is None:
            continue
        if not re.fullmatch(r"[a-z][a-z0-9_]*", name) or spec or conversion:
            raise ValueError(f"unsupported localization placeholder in {text!r}")
        names.append(name)
    return parts, names


def native_text(parts, names, suffix):
    text = ""
    for literal, name, _, _ in parts:
        text += literal.replace("%", "%%") if names else literal
        if name is not None:
            text += f"%{names.index(name) + 1}${suffix}"
    return text


def quoted(text):
    return '"' + (text.replace("\\", "\\\\").replace('"', '\\"')
                  .replace("\n", "\\n").replace("\t", "\\t")) + '"'


def render(catalogs, default_locale):
    if default_locale not in catalogs:
        raise ValueError(f"missing fallback catalog {default_locale}.json")
    baseline = catalogs[default_locale]
    canonical_names = {key: parse_template(value)[1] for key, value in baseline.items()}
    outputs = {}
    for locale, catalog in sorted(catalogs.items()):
        if not re.fullmatch(r"[a-z]{2}(?:-[A-Z]{2})?", locale):
            raise ValueError(f"unsupported locale filename {locale}.json (use ll or ll-RR)")
        if set(catalog) != set(baseline):
            missing = sorted(set(baseline) - set(catalog))
            extra = sorted(set(catalog) - set(baseline))
            raise ValueError(f"{locale}: missing keys {missing}, extra keys {extra}")
        apple = [f"/* {MARKER} */"]
        android = ['<?xml version="1.0" encoding="utf-8"?>', f"<!-- {MARKER} -->", "<resources>"]
        for key, value in sorted(catalog.items()):
            parts, names = parse_template(value)
            canonical = canonical_names[key]
            if Counter(names) != Counter(canonical):
                raise ValueError(f"{locale}.{key}: placeholder mismatch, expected {canonical}, got {names}")
            parameters = list(dict.fromkeys(canonical))
            ios_text = native_text(parts, parameters, "@")
            android_text = native_text(parts, parameters, "s")
            apple.append(f'{quoted(key)} = {quoted(ios_text)};')
            # Android's outer resource quotes retain leading, trailing and repeated spaces.
            format_attr = '' if parameters else ' formatted="false"'
            android.append(f'    <string name="{key}"{format_attr}>{escape(quoted(android_text))}</string>')
        directory = "values" if locale == default_locale else "values-b+" + locale.replace("-", "+")
        outputs[IOS_RESOURCES / f"{locale}.lproj/Localizable.strings"] = "\n".join(apple + [""])
        outputs[ANDROID_RESOURCES / directory / "foundation_strings.xml"] = "\n".join(android + ["</resources>", ""])
    return outputs


def obsolete(root, expected):
    candidates = list((root / IOS_RESOURCES).glob("*.lproj/Localizable.strings"))
    candidates += list((root / ANDROID_RESOURCES).glob("values*/foundation_strings.xml"))
    return [file for file in candidates if file.relative_to(root) not in expected and
            MARKER in file.read_text(encoding="utf-8")]
