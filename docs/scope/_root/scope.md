# Shared foundation scope

You can change shared behavior, visual definitions or text in one place and consume the result in both apps. The [project scope](../index.md) sets the Tracer Bullet approach and Beta workflow.

## At a glance

| # | Feature | Phase | Status |
| --- | --- | --- | --- |
| 1 | Ownership and development rules | Foundation | existing |
| 2 | Shared greeting contract | Foundation | existing |
| 3 | Shared visual definitions | Foundation | existing |
| 4 | Shared settings, text and brand assets | Foundation | existing |
| 5 | Reproducible local builds and checks | Verification | existing |
| 6 | Hosted build verification | Verification | done |

## Foundation

### 1. Ownership and development rules · existing

You can find the owner of a change, its permitted dependencies and when a new capability needs a design decision.

**Done when:** the repository names one owner for each shared responsibility and tells contributors which rules and checks apply. [Agent instructions](../../../AGENTS.md) · [Ownership matrix](../../architecture/ownership-matrix.md) · [Foundation decision](../../decisions/ADR-0001-foundation.md)

### 2. Shared greeting contract · existing

Both native apps call the same greeting function through generated bindings, the code that carries values between languages.

**Done when:** each app can pass a name and display the returned string, including Unicode text, with one implementation of the greeting. [Core](../../../crates/core/src/lib.rs) · [Mobile export](../../../crates/mobile-ffi/src/lib.rs) · [Contract conventions](../../contracts/ffi-conventions.md)

### 3. Shared visual definitions · existing

The apps share named values for color, type, spacing, corners and motion. Each platform renders them using its own native controls.

**Done when:** one set of source values generates both themes, both screens use the shared colors, type and spacing, and light and dark text meet the documented contrast threshold. [Design sources](../../../design-system/README.md) · [Accessibility](../../design-system/accessibility.md)

### 4. Shared settings, text and brand assets · existing

You can change the public fallback locale and shared copy at their source. The brand rules identify where future artwork and its exports belong.

**Done when:** both apps receive the English greeting recipient from one catalog, invalid settings and translation placeholders are detected, and brand asset ownership is documented. [Configuration](../../../shared/config/README.md) · [Localization](../../../shared/localization/README.md) · [Assets](../../../shared/assets/README.md)

## Verification

### 5. Reproducible local builds and checks · existing

You can build both apps from a checkout and see when checked in bindings or resources differ from their sources.

**Done when:** the documented commands build both native packages, exercise the shared contract and reject invalid dependencies or generated files. The verification record names the targets exercised and the limits of those results. [Build commands](../../../README.md) · [Shared checks](../../../scripts/test.sh) · [Local results](../../quality/verification.md)

### 6. Hosted build verification · done

You can use the hosted jobs to check the shared contract and both native apps on the same revision. Android installs the supported SDK packages. The iOS simulator boots in each system appearance before XCTest reads the greeting and samples the rendered background.

**Done when:** the shared checks pass and both hosted native jobs build and exercise the greeting on the same revision. The result identifies the revision and each job outcome. [Workflow](../../../.github/workflows/foundation.yml)

* [x] Repair the hosted checks with `/develop hosted build verification`.
* [x] Verify all three jobs on commit `65875793e37c708f31088fb65dca939d57cc2a50`. The foundation, iOS and Android jobs all passed. Both apps exercised light and dark appearance. [Hosted run 43593365100](https://github.com/ojiepermana/foundation-mobile/actions/runs/43593365100)
