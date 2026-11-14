#!/usr/bin/env bash
set -euo pipefail

if (( $# > 1 )) || [[ $# == 1 && $1 != --check ]]; then
  echo "Usage: $0 [--check]" >&2
  exit 2
fi
cd "$(dirname "$0")/.."
case "$(uname -s)" in
  Darwin) library=libmobile_ffi.dylib ;;
  Linux) library=libmobile_ffi.so ;;
  *) echo "Generate bindings on macOS or Linux" >&2; exit 1 ;;
esac

# Both the tool and the metadata-bearing host library use the workspace lockfile.
cargo build --locked --target-dir target -p mobile-ffi --features bindgen --bin uniffi-bindgen
cargo build --locked --target-dir target -p mobile-ffi --lib
output=$(mktemp -d)
trap 'rm -rf "$output"' EXIT
for language in swift kotlin; do
  target/debug/uniffi-bindgen generate "target/debug/$library" \
    --language "$language" --no-format --metadata-no-deps --out-dir "$output/$language"
done

if [[ ${1:-} == --check ]]; then
  diff -ru "$output" bindings
else
  mkdir -p bindings
  rsync -rc --delete "$output/" bindings/
fi
