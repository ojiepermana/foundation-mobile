"""Validate authoritative sources, then materialize or check their projections."""
import argparse
from functools import lru_cache
import json
from pathlib import Path
import sys

import fastjsonschema

import resources
import tokens


ROOT = Path(__file__).resolve().parents[2]


def unique_members(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_members)
    except ValueError as error:
        raise ValueError(f"{path}: {error}") from error


@lru_cache(maxsize=None)
def validator(path):
    return fastjsonschema.compile(load(ROOT / path), use_default=False)


def check_schema(value, schema, label):
    try:
        validator(schema)(value)
    except fastjsonschema.JsonSchemaException as error:
        raise ValueError(f"{label}: {error}") from error


def projections(root):
    groups = {path.stem: load(path) for path in (root / "design-system/tokens").glob("*.json")}
    check_schema(groups, "design-system/schemas/tokens.schema.json", "tokens")
    config = load(root / "shared/config/foundation.json")
    check_schema(config, "shared/specifications/config.schema.json", "foundation.json")
    catalogs = {}
    for path in (root / "shared/localization").glob("*.json"):
        catalogs[path.stem] = load(path)
        check_schema(catalogs[path.stem], "shared/specifications/localization.schema.json", path.name)
    return {**tokens.render(groups), **resources.render(catalogs, config["defaultLocale"])}


def generate(root, check):
    expected = projections(root)
    stale = resources.obsolete(root, expected)
    drift = []
    for relative, value in expected.items():
        output = root / relative
        data = value.encode("utf-8")
        if output.is_file() and output.read_bytes() == data:
            continue
        drift.append(relative)
        if not check:
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_bytes(data)
    if check and (drift or stale):
        paths = sorted(str(p) for p in drift + [p.relative_to(root) for p in stale])
        raise ValueError("generated files differ; run scripts/generate-design-tokens.sh:\n" + "\n".join(paths))
    for file in stale:
        file.unlink()
    print(f"Validated tokens, configuration and localizations ({len(expected)} generated files).")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail on drift without writing")
    args = parser.parse_args()
    try:
        generate(ROOT, args.check)
    except (OSError, ValueError) as error:
        sys.exit(str(error))
