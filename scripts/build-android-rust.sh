#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
ndk_dir=${1:?expected the path to the Android NDK}
minimum_api=${2:?expected the Android minimum API level}
output_dir=${3:?expected the JNI libraries output directory}
export PATH="${CARGO_HOME:-$HOME/.cargo}/bin:$PATH"

case "$(uname -s)" in
    Darwin) host=darwin-x86_64 ;;
    Linux) host=linux-x86_64 ;;
    *) echo "Android Rust builds require macOS or Linux." >&2; exit 1 ;;
esac
compiler_dir="$ndk_dir/toolchains/llvm/prebuilt/$host/bin"
if [[ ! -x "$compiler_dir/clang" ]]; then
    echo "Missing Android NDK toolchain at $compiler_dir (install ndk;$(basename "$ndk_dir"))." >&2
    exit 1
fi
export CARGO_TARGET_AARCH64_LINUX_ANDROID_LINKER="$compiler_dir/aarch64-linux-android${minimum_api}-clang"
export CARGO_TARGET_X86_64_LINUX_ANDROID_LINKER="$compiler_dir/x86_64-linux-android${minimum_api}-clang"
for abi in arm64-v8a x86_64; do
    case "$abi" in
        arm64-v8a) triple=aarch64-linux-android ;;
        x86_64) triple=x86_64-linux-android ;;
    esac
    cargo build --locked --release -p mobile-ffi --lib --target "$triple" --target-dir target/android
    mkdir -p "$output_dir/$abi"
    cp "target/android/$triple/release/libmobile_ffi.so" "$output_dir/$abi/"
done
