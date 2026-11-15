#!/usr/bin/env python3
"""Check the documented foundation boundary against Cargo's resolved manifests."""

import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
CRATES = {
    "foundation-core": ("crates/core", set()),
    "mobile-ffi": ("crates/mobile-ffi", {"foundation-core", "uniffi"}),
}
REQUIRED_DOCS = {
    "architecture": ["overview", "boundaries", "repository-structure", "dependency-rules", "ownership-matrix"],
    "rules": ["development-rules", "service-rules", "rust-rules", "ios-rules", "android-rules",
              "design-system-rules", "shared-resources-rules", "anti-duplication"],
    "design-system": ["principles", "token-conventions", "platform-mapping", "component-guidelines", "accessibility"],
    "contracts": ["ffi-conventions"],
    "quality": ["architecture-compliance", "verification"],
    "decisions": ["ADR-0001-foundation"],
    "scope": ["index"],
}


def problems():
    metadata = json.loads(subprocess.check_output(
        ["cargo", "metadata", "--no-deps", "--locked", "--format-version", "1"], cwd=ROOT
    ))
    packages = {p["name"]: p for p in metadata["packages"] if p["id"] in metadata["workspace_members"]}
    if packages.keys() != CRATES.keys():
        yield f"Workspace membership differs from the foundation policy: {sorted(packages)}"
    for name, (directory, allowed) in CRATES.items():
        if name not in packages:
            continue
        package = packages[name]
        if Path(package["manifest_path"]).parent != ROOT / directory:
            yield f"{name} must live in {directory}"
        # Include optional, renamed, dev/build and target-specific declarations.
        actual = {dep["name"] for dep in package["dependencies"]}
        if actual != allowed:
            yield f"{name}: expected direct dependencies {sorted(allowed)}, found {sorted(actual)}"
        for dep in package["dependencies"]:
            if dep["name"] in CRATES and dep.get("path") != str(ROOT / CRATES[dep["name"]][0]):
                yield f"{name}: {dep['name']} must resolve to its workspace implementation"

    documents = [ROOT / "AGENTS.md", ROOT / "README.md", ROOT / "design-system/README.md"]
    documents.extend(ROOT / "shared" / owner / "README.md" for owner in ("config", "localization", "assets"))
    for folder, names in REQUIRED_DOCS.items():
        documents.extend(ROOT / "docs" / folder / (name + ".md") for name in names)
    for path in documents:
        if not path.is_file() or not path.read_text(encoding="utf-8").strip():
            yield f"Missing or empty document: {path.relative_to(ROOT)}"


if __name__ == "__main__":
    errors = list(problems())
    if errors:
        sys.exit("\n".join(errors))
    print("Workspace boundaries and required documentation passed.")
