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

FIXTURE = Path(__file__).resolve().parent / "fixtures/sources"
TOKEN_SCHEMA = "design-system/schemas/tokens.schema.json"
LOCALIZATION_SCHEMA = "shared/specifications/localization.schema.json"


def token_groups():
    return {path.stem: generate.load(path) for path in (FIXTURE / "design-system/tokens").glob("*.json")}


class GenerationTests(unittest.TestCase):
    def test_alias_and_text_contrast(self):
        colors = generate.load(FIXTURE / "design-system/tokens/colors.json")
        broken = deepcopy(colors)
        broken["semantic"]["textPrimary"]["dark"] = "missing"
        with self.assertRaisesRegex(ValueError, "unknown primitive"):
            tokens.palettes(broken)
        broken["semantic"]["textPrimary"]["dark"] = colors["semantic"]["background"]["dark"]
        with self.assertRaisesRegex(ValueError, "contrast"):
            tokens.palettes(broken)

    def test_schema_rejects_invalid_token_shapes(self):
        groups = token_groups()
        generate.check_schema(groups, TOKEN_SCHEMA, "tokens")
        invalid = deepcopy(groups)
        invalid["colors"]["primitives"]["red"] = "red"
        with self.assertRaisesRegex(ValueError, "tokens:"):
            generate.check_schema(invalid, TOKEN_SCHEMA, "tokens")
        for group, role in (("spacing", "page"), ("typography", "heading"), ("typography", "body")):
            invalid = deepcopy(groups)
            del invalid[group]["semantic"][role]
            with self.assertRaisesRegex(ValueError, "tokens:"):
                generate.check_schema(invalid, TOKEN_SCHEMA, "tokens")

    def test_typography_uses_native_mapping_from_neutral_scales(self):
        groups = token_groups()
        projections = tokens.render(groups)
        self.assertIn("static let typographyHeading: Font = .system(.title, weight: .bold)",
                      projections[tokens.SWIFT_PATH])
        self.assertIn("val typographyHeading = TextStyle(", projections[tokens.KOTLIN_PATH])
        self.assertIn("fontSize = 30.sp", projections[tokens.KOTLIN_PATH])
        self.assertIn("lineHeight = 36.sp", projections[tokens.KOTLIN_PATH])

        groups["typography"]["primitives"]["scale"]["headline"]["appleStyle"] = "headline"
        with self.assertRaisesRegex(ValueError, "tokens:"):
            generate.check_schema(groups, TOKEN_SCHEMA, "tokens")

    def test_schema_requires_closed_configuration_and_valid_resource_keys(self):
        schema = "shared/specifications/config.schema.json"
        for config in ({"schemaVersion": True, "defaultLocale": "en"},
                       {"schemaVersion": 2, "defaultLocale": "en"},
                       {"schemaVersion": 1, "defaultLocale": "en", "unexpected": True}):
            with self.assertRaisesRegex(ValueError, "config:"):
                generate.check_schema(config, schema, "config")
        with self.assertRaisesRegex(ValueError, "localization:"):
            generate.check_schema({"welcome_title": "Welcome", "Upper": "invalid"},
                                  LOCALIZATION_SCHEMA, "localization")

    def test_localization_schema_asks_for_one_key_and_names_none(self):
        schema = generate.load(generate.ROOT / LOCALIZATION_SCHEMA)
        self.assertEqual(schema.get("minProperties"), 1)
        self.assertNotIn("required", schema)
        self.assertNotIn("properties", schema)
        with self.assertRaisesRegex(ValueError, "localization: data must contain at least 1 properties"):
            generate.check_schema({}, LOCALIZATION_SCHEMA, "localization")
        for catalog in ({"a": "Text"}, {"welcome_title": "Welcome", "second_key": "More"}):
            generate.check_schema(catalog, LOCALIZATION_SCHEMA, "localization")

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
            shutil.copytree(FIXTURE, root, dirs_exist_ok=True)
            locale = root / "shared/localization/fr.json"
            locale.write_text('{"welcome_title": "Bienvenue"}')
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

    def test_sources_without_a_sample_name_generate_and_check(self):
        with TemporaryDirectory() as temp, redirect_stdout(StringIO()):
            root = Path(temp)
            shutil.copytree(FIXTURE, root, dirs_exist_ok=True)
            generate.generate(root, check=False)
            generate.generate(root, check=True)
            strings = (root / resources.ANDROID_RESOURCES / "values/foundation_strings.xml").read_text()
            self.assertIn('<string name="welcome_title" formatted="false">"Welcome"</string>', strings)
            self.assertIn("typographyHeading", (root / tokens.SWIFT_PATH).read_text())
            self.assertIn("typographyHeading", (root / tokens.KOTLIN_PATH).read_text())


if __name__ == "__main__":
    unittest.main()
