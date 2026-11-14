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
        if [[ $# != 2 && $# != 3 ]]; then
            echo "Usage: $0 test SIMULATOR_UDID [light|dark] (list devices with xcrun simctl list devices available)" >&2
            exit 2
        fi
        # xcodebuild forwards TEST_RUNNER_ variables into the XCTest runner.
        case "${3:-}" in
            "") unset TEST_RUNNER_FOUNDATION_APPEARANCE ;;
            light|dark) export TEST_RUNNER_FOUNDATION_APPEARANCE="$3" ;;
            *) echo "Expected light or dark, got $3" >&2; exit 2 ;;
        esac
        exec xcodebuild "${options[@]}" -destination "platform=iOS Simulator,id=$2" \
            -configuration Debug -parallel-testing-enabled NO test
        ;;
    *)
        echo "Usage: $0 [simulator|device|test SIMULATOR_UDID]" >&2
        exit 2
        ;;
esac
