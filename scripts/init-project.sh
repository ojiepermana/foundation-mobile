#!/usr/bin/env bash
# Give a clone of the foundation its own name, application ID and version.
# Forms: --name N --app-id ID [overrides] | --check | --test. See the README section on starting a project.
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$root/tooling/derive/init_project.py" "$@"
