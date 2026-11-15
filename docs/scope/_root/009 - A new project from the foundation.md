# 009 - A new project from the foundation

**Phase** Foundation · **Status** `in-progress`

You can turn this repository into a new product without hunting for names by hand. Today nothing describes that path. The two apps already disagree on their own identity. The iOS app is `dev.foundation.mobile`, shown as Mobile Foundation, at version 1.0. The Android app is `foundation.mobile`, shown as Foundation, at version 0.1.0. A new product would also carry this repository's verification record, scope rows, hosted run links and knowledge graph as if they were its own.

**Done when:** one recorded decision separates the names the foundation keeps from the identity a product changes, one command gives a copy of this repository its own name, identifiers and version on both platforms, a hosted check proves that command on a temporary copy, the inherited records start clean in the new product, and the new product records which foundation revision it came from. [iOS settings](../../../apps/ios/Config/App.xcconfig) · [Android settings](../../../apps/android/app/build.gradle.kts) · [Verification record](../../quality/verification.md) · [Ownership matrix](../../architecture/ownership-matrix.md) · [Spec 0003](../../specs/_root/0003-new-project-from-foundation.md)

* [x] Design it (spec): `/architect a new project from the foundation`
* [ ] Build it: `/develop a new project from the foundation`
   * [ ] Identity in one file per platform, with the same defaults on both apps (AC-1, AC-2)
   * [ ] The init command, its state check and its unit tests (AC-3 to AC-9)
   * [ ] The workflow input for a derived run and the identity comparison in both native jobs (AC-10)
   * [ ] The README path and the document updates (AC-11, AC-12)
* [ ] Verify it: `/check verify a new project from the foundation`
* [ ] Test it: `/test a new project from the foundation`
