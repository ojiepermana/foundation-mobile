#!/usr/bin/env bash
set -euo pipefail
repo=$(cd "$(dirname "$0")/.." && pwd)
mode=${1:-simulator}
options=(-project "$repo/apps/ios/MobileFoundation.xcodeproj" -scheme MobileFoundation -derivedDataPath "$repo/build/ios")
case "$mode" in
    simulator)
        exec xcodebuild "${options[@]}" -destination 'generic/platform=iOS Simulator' \
            -configuration Debug "ARCHS=$(uname -m)" build
        ;;
    device)
        exec xcodebuild "${options[@]}" -destination 'generic/platform=iOS' \
            -configuration Release CODE_SIGNING_ALLOWED=NO build
        ;;
    test)
        if [[ $# != 2 ]]; then
            echo "Usage: $0 test SIMULATOR_UDID (list devices with xcrun simctl list devices available)" >&2
            exit 2
        fi
        exec xcodebuild "${options[@]}" -destination "platform=iOS Simulator,id=$2" \
            -configuration Debug -parallel-testing-enabled NO test
        ;;
    *)
        echo "Usage: $0 [simulator|device|test SIMULATOR_UDID]" >&2
        exit 2
        ;;
esac
