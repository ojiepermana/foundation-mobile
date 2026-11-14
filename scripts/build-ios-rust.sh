#!/usr/bin/env bash
# Called by the app target for both Xcode Run and command-line builds.
set -euo pipefail
cd "$SRCROOT/../.."
export PATH="${CARGO_HOME:-$HOME/.cargo}/bin:$PATH"
export CARGO_TARGET_DIR="$PWD/target"
# Cargo also compiles host proc macros. Let rustc select each target's own SDK.
unset SDKROOT
profile=dev
output=debug
if [[ $CONFIGURATION == Release ]]; then
    profile=release
    output=release
fi
libraries=()
for arch in $ARCHS; do
    case "$PLATFORM_NAME/$arch" in
        iphoneos/arm64) triple=aarch64-apple-ios ;;
        iphonesimulator/arm64) triple=aarch64-apple-ios-sim ;;
        iphonesimulator/x86_64) triple=x86_64-apple-ios ;;
        *) echo "Unsupported Apple build destination: $PLATFORM_NAME/$arch" >&2; exit 1 ;;
    esac
    if ! rustup target list --installed | grep -Fxq "$triple"; then
        rustup target add "$triple"
    fi
    cargo build --locked --package mobile-ffi --lib --target "$triple" --profile "$profile"
    libraries+=("$CARGO_TARGET_DIR/$triple/$output/libmobile_ffi.a")
done
library="$BUILT_PRODUCTS_DIR/libmobile_ffi.a"
if (( ${#libraries[@]} == 1 )); then
    cp -f "${libraries[0]}" "$library"
else
    xcrun lipo -create "${libraries[@]}" -output "$library"
fi
