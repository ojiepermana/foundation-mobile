#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
generator="$root/tooling/codegen"
# Load one pure-Python wheel from a private cache. Install nothing globally.
requirements="$generator/requirements.txt"
lock_hash="$(python3 -c 'import hashlib,sys; print(hashlib.sha256(open(sys.argv[1], "rb").read()).hexdigest())' "$requirements")"
cache="$root/build/tooling/$lock_hash"
wheel="$cache/schema-validator.whl"
if [[ ! -f "$wheel" ]]; then
  mkdir -p "$cache"
  download="$(mktemp -d "$cache/download.XXXXXX")"
  trap 'rm -rf "$download"' EXIT
  python3 -m pip download --disable-pip-version-check --require-hashes --only-binary=:all: \
    --no-deps --dest "$download" -r "$requirements"
  mv "$download"/*.whl "$wheel"
  rmdir "$download"
  trap - EXIT
fi
export PYTHONPATH="$wheel"
if [[ "${1:-}" == "--test" ]]; then
  exec python3 -m unittest discover -s "$generator" -p 'test_*.py' -v
fi
exec python3 "$generator/generate.py" "$@"
