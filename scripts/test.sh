#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
cargo fmt --all -- --check
cargo clippy --locked --workspace --all-targets --all-features -- -D warnings
cargo test --locked --workspace
python3 tooling/validation/check-architecture.py
scripts/generate-bindings.sh --check
scripts/generate-design-tokens.sh --check
scripts/generate-design-tokens.sh --test
