#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../apps/android"

# Support stock Android Studio installations on macOS and CI JDK/SDK overrides.
if [[ -z "${JAVA_HOME:-}" && -d "/Applications/Android Studio.app/Contents/jbr/Contents/Home" ]]; then
    export JAVA_HOME="/Applications/Android Studio.app/Contents/jbr/Contents/Home"
fi
if [[ -z "${ANDROID_HOME:-}" && -d "$HOME/Library/Android/sdk" ]]; then
    export ANDROID_HOME="$HOME/Library/Android/sdk"
fi
if [[ $# -eq 0 ]]; then
    set -- :app:assembleDebug
fi
exec ./gradlew "$@"
