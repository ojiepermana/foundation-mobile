"""Regression checks for cross-file validation and native projection drift."""
from copy import deepcopy
from io import StringIO
from contextlib import redirect_stdout
import shutil
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

import generate
import resources
import tokens


class GenerationTests(unittest.TestCase):
    def test_alias_and_text_contrast(self):
        colors = generate.load(generate.ROOT / "design-system/tokens/colors.json")
        broken = deepcopy(colors)
        broken["semantic"]["textPrimary"]["dark"] = "missing"
        with self.assertRaisesRegex(ValueError, "unknown primitive"):
            tokens.palettes(broken)
        broken["semantic"]["textPrimary"]["dark"] = colors["semantic"]["background"]["dark"]
        with self.assertRaisesRegex(ValueError, "contrast"):
            tokens.palettes(broken)

    def test_schema_rejects_invalid_token_shapes(self):
        groups = {path.stem: generate.load(path) for path in (generate.ROOT / "design-system/tokens").glob("*.json")}
        invalid = deepcopy(groups)
        invalid["colors"]["primitives"]["red"] = "red"
        with self.assertRaisesRegex(ValueError, "tokens:"):
            generate.check_schema(invalid, "design-system/schemas/tokens.schema.json", "tokens")
        invalid = deepcopy(groups)
        del invalid["spacing"]["semantic"]["page"]
        with self.assertRaisesRegex(ValueError, "tokens:"):
            generate.check_schema(invalid, "design-system/schemas/tokens.schema.json", "tokens")

    def test_typography_uses_native_mapping_from_neutral_scales(self):
        groups = {p.stem: generate.load(p) for p in (generate.ROOT / "design-system/tokens").glob("*.json")}
        headline = groups["typography"]["primitives"]["scale"]["headline"]
        headline.update({"size": 31, "lineHeight": 39})
        projections = tokens.render(groups)
        self.assertIn(".system(.title, weight: .semibold)", projections[tokens.SWIFT_PATH])
        self.assertIn("fontSize = 31.sp", projections[tokens.KOTLIN_PATH])
        self.assertIn("lineHeight = 39.sp", projections[tokens.KOTLIN_PATH])

        headline["appleStyle"] = "headline"
        with self.assertRaisesRegex(ValueError, "tokens:"):
            generate.check_schema(groups, "design-system/schemas/tokens.schema.json", "tokens")

    def test_schema_requires_closed_configuration_and_valid_resource_keys(self):
        schema = "shared/specifications/config.schema.json"
        for config in ({"schemaVersion": True, "defaultLocale": "en"},
                       {"schemaVersion": 2, "defaultLocale": "en"},
                       {"schemaVersion": 1, "defaultLocale": "en", "unexpected": True}):
            with self.assertRaisesRegex(ValueError, "config:"):
                generate.check_schema(config, schema, "config")
        with self.assertRaisesRegex(ValueError, "localization:"):
            generate.check_schema({"greeting_recipient": "World", "Upper": "invalid"},
                                  "shared/specifications/localization.schema.json", "localization")

    def test_placeholders_reorder_and_literals_escape(self):
        catalogs = {"en": {"message": '{first} & {last}, "100%"'},
                    "fr-CA": {"message": '{last} + {first}, {{100%}}'}}
        files = resources.render(catalogs, "en")
        self.assertIn(r'%1$@ & %2$@, \"100%%\"', files[resources.IOS_RESOURCES / "en.lproj/Localizable.strings"])
        self.assertIn("%2$s + %1$s, {100%%}", files[resources.ANDROID_RESOURCES / "values-b+fr+CA/foundation_strings.xml"])
        self.assertIn("%1$s &amp; %2$s", files[resources.ANDROID_RESOURCES / "values/foundation_strings.xml"])

    def test_placeholder_key_and_locale_mismatch(self):
        baseline = {"a": "{name} {name}", "b": "Ok"}
        for translation in ({"a": "{name} {name}"}, {"a": "{name}", "b": "Ok"},
                            {"a": "{other} {other}", "b": "Ok"}):
            with self.assertRaises(ValueError):
                resources.render({"en": baseline, "fr": translation}, "en")
        for locale in ("fr_CA", "EN", "../"):
            with self.assertRaisesRegex(ValueError, "unsupported locale"):
                resources.render({"en": baseline, locale: baseline}, "en")

    def test_stale_edited_and_missing_files(self):
        with TemporaryDirectory() as temp, redirect_stdout(StringIO()):
            root = Path(temp)
            for part in ("design-system", "shared"):
                shutil.copytree(generate.ROOT / part, root / part)
            locale = root / "shared/localization/fr.json"
            locale.write_text('{"greeting_recipient": "Monde"}')
            generate.generate(root, check=False)
            generate.generate(root, check=True)
            locale.unlink()
            edited = root / tokens.KOTLIN_PATH
            edited.write_text("edited")
            (root / tokens.SWIFT_PATH).unlink()
            with self.assertRaisesRegex(ValueError, "generated files differ"):
                generate.generate(root, check=True)
            self.assertEqual(edited.read_text(), "edited")
            generate.generate(root, check=False)
            generate.generate(root, check=True)
            self.assertFalse((root / resources.IOS_RESOURCES / "fr.lproj/Localizable.strings").exists())
            self.assertFalse((root / resources.ANDROID_RESOURCES / "values-b+fr/foundation_strings.xml").exists())


if __name__ == "__main__":
    unittest.main()
