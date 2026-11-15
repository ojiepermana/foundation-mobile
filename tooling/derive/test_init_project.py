"""Checks for the derivation command: every write, every refusal and both clean states."""
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
import os
from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest import mock

import init_project

SAMPLE_NAME = "Zoë's Proof"
SAMPLE_ID = "dev.example.derived"
SAMPLE_ORIGIN = ["--foundation-url", "https://example.invalid/foundation",
                 "--foundation-ref", "foundation-v0.0.0", "--date", "2026-01-01"]
SAMPLE = ["--name", SAMPLE_NAME, "--app-id", SAMPLE_ID]
ORIGIN_LINE = "Started from the [mobile foundation](https://example.invalid/foundation) at `foundation-v0.0.0` on 2026-01-01."

# Keep the developer's own git settings, signing and identity out of every test repository.
GIT_ENVIRONMENT = {
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_NOSYSTEM": "1",
    "GIT_AUTHOR_NAME": "Derivation Test",
    "GIT_AUTHOR_EMAIL": "derivation@example.invalid",
    "GIT_COMMITTER_NAME": "Derivation Test",
    "GIT_COMMITTER_EMAIL": "derivation@example.invalid",
}
# A caller such as a git hook exports these. They would point the fixture's git at the caller's repository.
GIT_LOCATORS = ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_OBJECT_DIRECTORY",
                "GIT_ALTERNATE_OBJECT_DIRECTORIES", "GIT_COMMON_DIR", "GIT_NAMESPACE", "GIT_PREFIX")
EXPECTED_RECORD = """# Zoë's Proof verification · 2026-01-01

This record lists what ran, where it ran and what has not run yet. Nothing has run in this repository yet. This project started from the [mobile foundation](https://example.invalid/foundation) at `foundation-v0.0.0`. The foundation's own results live in that repository. They are not results for this project.

## Local checks

None yet. Add a row for each check after it runs here.

## Hosted run

None yet. Record the first hosted run here with its link, its revision and each job outcome.

## Still unverified

This is the one list of targets that have not run. A target leaves this list when a local or hosted result above covers it.

- The shared checks in `scripts/test.sh`.
- The iOS simulator build, the unsigned device link and the greeting test in light and dark appearance.
- The Android debug build and the instrumentation tests in light and dark appearance.
- All three hosted jobs.
- Physical devices on either platform.
- Signed distribution.
- The minimum supported OS versions.
- An Android runtime with 16 KiB pages.
- An x86_64 iOS simulator runtime.
"""
FOUNDATION_FILES = {
    init_project.IOS_IDENTITY: init_project.identity_text(
        init_project.IOS_KEYS, " = ",
        (init_project.DEFAULT_APP_ID, init_project.DEFAULT_NAME, init_project.DEFAULT_VERSION, init_project.BUILD)),
    init_project.ANDROID_IDENTITY: init_project.identity_text(
        init_project.ANDROID_KEYS, "=",
        (init_project.DEFAULT_APP_ID, init_project.DEFAULT_NAME, init_project.DEFAULT_VERSION, init_project.BUILD)),
    init_project.README: "# Native mobile foundation\n\nThe opening paragraph.\n\n## Build\n\nSteps.\n",
    init_project.RECORD: "# Foundation verification\n\n[Hosted run](https://example.invalid/runs/1) passed.\n",
    "graphify-out/graph.json": "{}\n",
    "graphify-out/cache/semantic/entry.json": "{}\n",
    "crates/core/src/lib.rs": "pub fn greeting() {}\n",
}


class Checkout(unittest.TestCase):
    """A small foundation checkout in a temporary folder, in git unless a test says otherwise."""

    in_git = True

    def setUp(self):
        folder = TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        environment = mock.patch.dict(os.environ, GIT_ENVIRONMENT)
        environment.start()
        self.addCleanup(environment.stop)
        for name in GIT_LOCATORS:
            os.environ.pop(name, None)
        self.root = Path(folder.name).resolve() / "checkout"
        for relative, text in FOUNDATION_FILES.items():
            self.write(relative, text)
        if self.in_git:
            self.git("init", "-q")
            self.git("remote", "add", "origin", "https://example.invalid/owner/foundation.git")
            self.commit("Foundation")

    def git(self, *arguments):
        return subprocess.run(["git", "-C", str(self.root), "-c", "commit.gpgsign=false", *arguments],
                              check=True, stdout=subprocess.PIPE, universal_newlines=True).stdout

    def commit(self, message):
        self.git("add", "-A")
        self.git("commit", "-q", "-m", message)

    def write(self, relative, text):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(text.encode("utf-8"))

    def read(self, relative):
        return (self.root / relative).read_bytes().decode("utf-8")

    def snapshot(self):
        return {str(path.relative_to(self.root)): path.read_bytes()
                for path in sorted(self.root.rglob("*")) if path.is_file() and ".git" not in path.parts}

    def run_command(self, *arguments):
        output, errors = StringIO(), StringIO()
        with redirect_stdout(output), redirect_stderr(errors):
            code = init_project.main(list(arguments), root=self.root)
        return code, output.getvalue(), errors.getvalue()

    def assert_refused(self, arguments, reason):
        before = self.snapshot()
        code, output, errors = self.run_command(*arguments)
        self.assertEqual((code, output), (2, ""), errors)
        self.assertEqual(errors.count("\n"), 1, "a refusal is one line: " + errors)
        self.assertIn(reason, errors)
        self.assertEqual(self.snapshot(), before, "a refusal must leave every file unchanged")

    def assert_mixed(self, mismatch):
        code, output, errors = self.run_command("--check")
        self.assertEqual((code, output), (1, ""), errors)
        self.assertIn(mismatch, errors)


class DerivationTests(Checkout):
    def test_writes_identity_readme_and_empty_record(self):
        self.assertEqual(self.run_command("--check"), (0, "foundation\n", ""))
        code, output, errors = self.run_command(*SAMPLE, *SAMPLE_ORIGIN)
        self.assertEqual((code, errors), (0, ""))
        self.assertEqual(self.read(init_project.IOS_IDENTITY),
                         "APP_BUNDLE_IDENTIFIER = dev.example.derived\nAPP_DISPLAY_NAME = Zoë's Proof\n"
                         "MARKETING_VERSION = 0.1.0\nCURRENT_PROJECT_VERSION = 1\n")
        self.assertEqual(self.read(init_project.ANDROID_IDENTITY),
                         "applicationId=dev.example.derived\ndisplayName=Zoë's Proof\nversionName=0.1.0\nversionCode=1\n")
        self.assertEqual(self.read(init_project.README),
                         "# Zoë's Proof\n\n" + ORIGIN_LINE + "\n\nThe opening paragraph.\n\n## Build\n\nSteps.\n")
        self.assertEqual(self.read(init_project.RECORD), EXPECTED_RECORD)
        self.assertFalse((self.root / "graphify-out").exists())
        self.assertEqual(output.splitlines(), [init_project.IOS_IDENTITY, init_project.ANDROID_IDENTITY,
                                               init_project.README, init_project.RECORD, "graphify-out/ (removed)"])
        self.assertEqual(self.run_command("--check"), (0, "derived\n", ""))

    def test_changes_exactly_the_documented_paths(self):
        self.assertEqual(self.run_command(*SAMPLE, *SAMPLE_ORIGIN)[0], 0)
        self.assertEqual(self.git("status", "--porcelain").splitlines(), [
            " M README.md",
            " M apps/android/identity.properties",
            " M apps/ios/Config/Identity.xcconfig",
            " M docs/quality/verification.md",
            " D graphify-out/cache/semantic/entry.json",
            " D graphify-out/graph.json",
        ])

    def test_overrides_reach_only_their_own_platform(self):
        code, _, errors = self.run_command(
            *SAMPLE, *SAMPLE_ORIGIN, "--ios-bundle-id", "com.Acme.notes-ios",
            "--android-app-id", "com.acme.notes_android", "--version", "2.10.3")
        self.assertEqual((code, errors), (0, ""))
        ios, android = self.read(init_project.IOS_IDENTITY), self.read(init_project.ANDROID_IDENTITY)
        self.assertIn("APP_BUNDLE_IDENTIFIER = com.Acme.notes-ios\n", ios)
        self.assertIn("MARKETING_VERSION = 2.10.3\nCURRENT_PROJECT_VERSION = 1\n", ios)
        self.assertIn("applicationId=com.acme.notes_android\n", android)
        self.assertIn("versionName=2.10.3\nversionCode=1\n", android)
        self.assertNotIn(SAMPLE_ID, ios + android)
        self.assertEqual(self.run_command("--check"), (0, "derived\n", ""))

    def test_one_override_leaves_the_other_platform_on_the_shared_id(self):
        cases = (("--ios-bundle-id", "com.Acme.notes-ios", "com.Acme.notes-ios", SAMPLE_ID),
                 ("--android-app-id", "com.acme.notes_android", SAMPLE_ID, "com.acme.notes_android"))
        for flag, value, ios_id, android_id in cases:
            with self.subTest(flag=flag):
                self.assertEqual(self.run_command(*SAMPLE, *SAMPLE_ORIGIN, flag, value)[0], 0)
                self.assertIn("APP_BUNDLE_IDENTIFIER = " + ios_id + "\n", self.read(init_project.IOS_IDENTITY))
                self.assertIn("applicationId=" + android_id + "\n", self.read(init_project.ANDROID_IDENTITY))
                self.assertEqual(self.run_command("--check"), (0, "derived\n", ""))
                self.git("restore", ".")

    def test_a_name_that_starts_with_a_hyphen_uses_the_equals_form(self):
        self.assert_refused(["--name", "-Acme", "--app-id", SAMPLE_ID],
                            "--name: expected one value; write a value that starts with a hyphen as --name=VALUE")
        self.assertEqual(self.run_command("--name=-Acme", "--app-id", SAMPLE_ID)[0], 0)
        self.assertIn("displayName=-Acme\n", self.read(init_project.ANDROID_IDENTITY))

    def test_reads_url_revision_and_date_from_the_checkout(self):
        head = self.git("rev-parse", "HEAD").strip()
        self.assertEqual(self.run_command(*SAMPLE)[0], 0)
        line = self.read(init_project.README).split("\n")[2]
        url, ref, day = init_project.ORIGIN.match(line).groups()
        self.assertEqual((url, ref), ("https://example.invalid/owner/foundation", head))
        self.assertEqual(day, init_project.date.today().isoformat())

    def test_prefers_the_foundation_remote_and_the_highest_release_tag(self):
        self.git("remote", "add", "foundation", "git@example.invalid:base/mobile.git")
        for tag in ("foundation-v0.9.0", "foundation-v0.10.0", "foundation-v0.10.0-rc", "v9.9.9"):
            self.git("tag", tag)
        self.assertEqual(self.run_command(*SAMPLE)[0], 0)
        self.assertIn("(https://example.invalid/base/mobile) at `foundation-v0.10.0` on ",
                      self.read(init_project.README).split("\n")[2])

    def test_remote_forms_are_written_as_https_without_credentials(self):
        for raw in ("https://user:token@example.invalid/owner/repo.git",
                    "http://example.invalid/owner/repo/",
                    "ssh://git@example.invalid:22/owner/repo.git",
                    "git@example.invalid:owner/repo.git"):
            self.assertEqual(init_project.normalize_url(raw), "https://example.invalid/owner/repo", raw)
        for raw in ("/srv/git/foundation", "../foundation", "file:///srv/foundation", "git://example.invalid/a/b",
                    "https://example.invalid", "https://example.invalid/a b", "https://example.invalid/a)b"):
            self.assertIsNone(init_project.normalize_url(raw), raw)

    def test_refuses_a_remote_that_is_a_local_path(self):
        self.git("remote", "set-url", "origin", "/srv/git/foundation")
        self.assert_refused(SAMPLE, "no usable foundation URL; pass --foundation-url")
        self.git("remote", "remove", "origin")
        self.assert_refused(SAMPLE, "no usable foundation URL; pass --foundation-url")

    def test_refuses_inputs_that_break_a_rule(self):
        cases = (
            (["--name", "Acme", "--app-id", "com.Acme.notes"], "--app-id: expected reverse DNS in lowercase"),
            (["--name", "Acme", "--app-id", "notes"], "--app-id: expected reverse DNS in lowercase"),
            (["--name", "Acme", "--app-id", init_project.DEFAULT_APP_ID],
             "--app-id: must differ from the foundation default dev.foundation.mobile"),
            ([*SAMPLE, "--android-app-id", init_project.DEFAULT_APP_ID],
             "--android-app-id: must differ from the foundation default dev.foundation.mobile"),
            ([*SAMPLE, "--ios-bundle-id", "com.acme.notes_ios"], "--ios-bundle-id: expected"),
            ([*SAMPLE, "--android-app-id", "com.acme.1notes"], "--android-app-id: expected"),
            (["--name", "Acme $(HOME)", "--app-id", SAMPLE_ID], "--name: expected"),
            (["--name", " Acme", "--app-id", SAMPLE_ID], "--name: expected"),
            (["--name", "Acme  Notes", "--app-id", SAMPLE_ID], "--name: expected"),
            (["--name", "Acme // Notes", "--app-id", SAMPLE_ID], "--name: expected"),
            (["--name", "Acme\nNotes", "--app-id", SAMPLE_ID], "--name: expected"),
            (["--name", "A" * 31, "--app-id", SAMPLE_ID], "--name: expected"),
            (["--name", "", "--app-id", SAMPLE_ID], "--name: expected"),
            ([*SAMPLE, "--ios-bundle-id", init_project.DEFAULT_APP_ID],
             "--ios-bundle-id: must differ from the foundation default dev.foundation.mobile"),
            (["--name", "Acme", "--app-id", "com.acme.notes\n"], "--app-id: expected reverse DNS in lowercase"),
            (["--name", "Acme", "--app-id", init_project.DEFAULT_APP_ID + "\n"], "--app-id: expected reverse DNS"),
            (["--name", "Acme", "--app-id", "com.acme.n\u0663"], "--app-id: expected reverse DNS in lowercase"),
            ([*SAMPLE, "--ios-bundle-id", "com.acme.notes\n"], "--ios-bundle-id: expected"),
            ([*SAMPLE, "--android-app-id", "com.acme.notes\n"], "--android-app-id: expected"),
            ([*SAMPLE, "--ios-bundle-id", ""], "--ios-bundle-id: expected"),
            ([*SAMPLE, "--android-app-id", ""], "--android-app-id: expected"),
            (["--name", "Acme\n", "--app-id", SAMPLE_ID], "--name: expected"),
            ([*SAMPLE, "--version", "1.0"], "--version: expected three numbers"),
            ([*SAMPLE, "--version", "1.2.3\n"], "--version: expected three numbers"),
            ([*SAMPLE, "--version", "\u0661.2.3"], "--version: expected three numbers"),
            ([*SAMPLE, "--version", ""], "--version: expected three numbers"),
            ([*SAMPLE, "--date", "2026-13-40"], "--date: expected a real date"),
            ([*SAMPLE, "--date", "2026-01-01\n"], "--date: expected a real date"),
            ([*SAMPLE, "--date", ""], "--date: expected a real date"),
            ([*SAMPLE, "--foundation-url", ""], "--foundation-url: expected"),
            ([*SAMPLE, "--foundation-ref", "foundation-v0.0.0\n"], "--foundation-ref: expected"),
            ([*SAMPLE, "--foundation-ref", ""], "--foundation-ref: expected"),
            ([*SAMPLE, "--foundation-url", "/srv/git/foundation"], "--foundation-url: expected"),
            ([*SAMPLE, "--foundation-ref", "main`; rm"], "--foundation-ref: expected"),
            (["--name", "Acme"], "--name and --app-id are both required"),
            ([*SAMPLE, "--check"], "--check takes no other argument"),
            ([*SAMPLE, "--rename-everything"], "unrecognized arguments"),
        )
        for arguments, reason in cases:
            with self.subTest(arguments=arguments):
                self.assert_refused(arguments, reason)

    def test_refuses_a_tree_with_uncommitted_or_untracked_files(self):
        self.write("crates/core/src/lib.rs", "pub fn changed() {}\n")
        self.assert_refused(SAMPLE, "uncommitted or untracked files")
        self.git("restore", ".")
        self.write("notes.txt", "untracked\n")
        self.assert_refused(SAMPLE, "uncommitted or untracked files")
        self.git("config", "status.showUntrackedFiles", "no")
        self.assertEqual(self.git("status", "--porcelain"), "")
        self.assert_refused(SAMPLE, "uncommitted or untracked files")

    def test_refuses_a_remote_url_that_is_not_text(self):
        self.git("remote", "set-url", "origin", b"https://example.invalid/\xff/foundation")
        self.assert_refused(SAMPLE, "no usable foundation URL; pass --foundation-url")

    def test_a_checkout_reached_through_a_link_is_still_in_git(self):
        link = self.root.parent / "link"
        link.symlink_to(self.root, target_is_directory=True)
        self.assertTrue(init_project.in_git(link))
        self.assertFalse(init_project.in_git(self.root / "crates"))

    def test_names_a_graph_removal_that_stopped_part_way(self):
        def stop_part_way(path):
            (Path(path) / "graph.json").unlink()
            raise PermissionError("cannot remove " + path)

        errors = StringIO()
        with mock.patch.object(init_project.shutil, "rmtree", stop_part_way), redirect_stdout(StringIO()), \
                redirect_stderr(errors):
            code = init_project.main([*SAMPLE, *SAMPLE_ORIGIN], root=self.root)
        self.assertEqual(code, 1)
        self.assertEqual(errors.getvalue().splitlines()[1:], [
            "Already changed: apps/ios/Config/Identity.xcconfig",
            "Already changed: apps/android/identity.properties",
            "Already changed: README.md",
            "Already changed: docs/quality/verification.md",
            "Already changed: graphify-out/ (partly removed)",
            "Run `git restore .` to return to the foundation state.",
        ])
        self.git("restore", ".")
        self.assertEqual(self.run_command("--check"), (0, "foundation\n", ""))
        self.assertEqual(self.git("status", "--porcelain"), "")

    def test_refuses_a_checkout_that_is_already_derived(self):
        self.assertEqual(self.run_command(*SAMPLE, *SAMPLE_ORIGIN)[0], 0)
        self.commit("Derived")
        self.assert_refused(["--name", "Second Name", "--app-id", "com.second.name"], "checkout is already derived")

    def test_refuses_a_mixed_checkout(self):
        self.write(init_project.ANDROID_IDENTITY,
                   FOUNDATION_FILES[init_project.ANDROID_IDENTITY].replace(init_project.DEFAULT_APP_ID, "com.acme.notes"))
        self.commit("Half derived")
        self.assert_refused(SAMPLE, "checkout is mixed; run scripts/init-project.sh --check")

    def test_check_names_each_mismatch(self):
        ios = FOUNDATION_FILES[init_project.IOS_IDENTITY]
        readme = FOUNDATION_FILES[init_project.README]
        cases = (
            (init_project.IOS_IDENTITY, ios.replace(init_project.DEFAULT_APP_ID, "com.acme.notes"),
             "apps/ios/Config/Identity.xcconfig: APP_BUNDLE_IDENTIFIER differs from the foundation default"),
            (init_project.IOS_IDENTITY, ios + "DEVELOPMENT_TEAM = ABCDE12345\n",
             "apps/ios/Config/Identity.xcconfig: unexpected line 'DEVELOPMENT_TEAM = ABCDE12345'"),
            (init_project.IOS_IDENTITY, "// Product identity\n" + ios,
             "apps/ios/Config/Identity.xcconfig: unexpected line '// Product identity'"),
            (init_project.IOS_IDENTITY, ios.replace("MARKETING_VERSION = 0.1.0\n", ""),
             "apps/ios/Config/Identity.xcconfig: missing key MARKETING_VERSION"),
            (init_project.IOS_IDENTITY, "".join(reversed(ios.splitlines(True))),
             "apps/ios/Config/Identity.xcconfig: keys must be in the order"),
            (init_project.IOS_IDENTITY, ios + "\n", "apps/ios/Config/Identity.xcconfig: unexpected line ''"),
            (init_project.IOS_IDENTITY, ios.rstrip("\n"), "apps/ios/Config/Identity.xcconfig: must end with one newline"),
            (init_project.IOS_IDENTITY, ios.replace("\n", "\r\n"),
             "apps/ios/Config/Identity.xcconfig: APP_BUNDLE_IDENTIFIER breaks its rule"),
            (init_project.IOS_IDENTITY, ios.replace("\n", "\r"), "apps/ios/Config/Identity.xcconfig: must end with one newline"),
            (init_project.ANDROID_IDENTITY, FOUNDATION_FILES[init_project.ANDROID_IDENTITY].replace("\n", "\r\n"),
             "apps/android/identity.properties: versionCode breaks its rule"),
            (init_project.ANDROID_IDENTITY,
             FOUNDATION_FILES[init_project.ANDROID_IDENTITY].replace("versionCode=1", "versionCode=0"),
             "apps/android/identity.properties: versionCode breaks its rule"),
            (init_project.ANDROID_IDENTITY,
             FOUNDATION_FILES[init_project.ANDROID_IDENTITY].replace("Mobile Foundation", "Mobile $(X)"),
             "apps/android/identity.properties: displayName breaks its rule"),
            (init_project.README, readme.replace("## Build", ORIGIN_LINE),
             "README.md: line 5 starts like the origin line, which belongs on line 3"),
            (init_project.README, "# Title\n\n" + ORIGIN_LINE + "\n\nText.\n",
             "README.md: the origin line is present on line 3, but the rest of the checkout is the foundation"),
            (init_project.README, "# Title\n\n" + ORIGIN_LINE.replace("https://", "http://") + "\n\nText.\n",
             "README.md: the origin line on line 3 does not match its form"),
            (init_project.README, "# Title\n\n" + ORIGIN_LINE + "\nText.\n",
             "README.md: line 4, after the origin line, must be blank"),
            (init_project.README, "# Title\r\n\r\n" + ORIGIN_LINE + "\r\n\r\nText.\r\n",
             "README.md: the origin line on line 3 does not match its form"),
        )
        for relative, text, mismatch in cases:
            with self.subTest(mismatch=mismatch):
                self.write(relative, text)
                self.assert_mixed(mismatch)
                self.write(relative, FOUNDATION_FILES[relative])
        (self.root / init_project.ANDROID_IDENTITY).unlink()
        self.assert_mixed("apps/android/identity.properties: file is missing")

    def test_check_names_a_derived_checkout_that_lost_a_part(self):
        self.assertEqual(self.run_command(*SAMPLE, *SAMPLE_ORIGIN)[0], 0)
        derived = self.read(init_project.README)
        self.write(init_project.README, FOUNDATION_FILES[init_project.README])
        self.assert_mixed("README.md: the origin line is missing on line 3, but the rest of the checkout is derived")
        self.write(init_project.README, derived)
        self.write(init_project.IOS_IDENTITY, FOUNDATION_FILES[init_project.IOS_IDENTITY])
        self.assert_mixed("APP_BUNDLE_IDENTIFIER is still the foundation default dev.foundation.mobile, "
                          "but the rest of the checkout is derived")


class OutsideGitTests(Checkout):
    in_git = False

    def test_needs_both_foundation_values(self):
        self.assert_refused(SAMPLE, "--foundation-url and --foundation-ref are both required outside git")
        self.assert_refused([*SAMPLE, "--foundation-url", "https://example.invalid/foundation"],
                            "--foundation-url and --foundation-ref are both required outside git")
        code, _, errors = self.run_command(*SAMPLE, *SAMPLE_ORIGIN)
        self.assertEqual((code, errors), (0, ""))
        self.assertEqual(self.run_command("--check"), (0, "derived\n", ""))

    def test_a_folder_inside_another_repository_is_not_in_git(self):
        outer = self.root.parent
        subprocess.run(["git", "-C", str(outer), "init", "-q"], check=True)
        self.assertFalse(init_project.in_git(self.root))
        self.assert_refused(SAMPLE, "both required outside git")


class RealCheckoutTests(unittest.TestCase):
    """Run the checked in command on a temporary copy of this checkout. The checkout itself is only read."""

    WATCHED = (init_project.IOS_IDENTITY, init_project.ANDROID_IDENTITY, init_project.README, init_project.RECORD)

    def watched(self):
        root = init_project.ROOT
        files = {relative: (root / relative).read_bytes() for relative in self.WATCHED}
        return files, (root / init_project.GRAPH).exists()

    def test_derivation_on_a_copy(self):
        root = init_project.ROOT
        if not init_project.in_git(root):
            self.skipTest("this checkout is not in git, so there is no file list to copy")
        if init_project.state(root)[0] == "derived":
            self.skipTest("this checkout is already derived; the derivation proof belongs to the foundation")
        listing = subprocess.run(["git", "-C", str(root), "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
                                 check=True, stdout=subprocess.PIPE).stdout
        before = self.watched()
        folder = TemporaryDirectory()
        try:
            copy = Path(folder.name).resolve() / "copy"
            for name in filter(None, listing.split(b"\0")):
                relative = os.fsdecode(name)
                if (root / relative).is_file():
                    (copy / relative).parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(str(root / relative), str(copy / relative))

            environment = {key: value for key, value in os.environ.items() if key not in GIT_LOCATORS}

            def in_copy(*command):
                return subprocess.run(command, cwd=str(copy), env=environment, stdout=subprocess.PIPE,
                                      stderr=subprocess.STDOUT, universal_newlines=True)

            command = str(copy / "scripts/init-project.sh")
            derived = in_copy(command, *SAMPLE, *SAMPLE_ORIGIN)
            self.assertEqual(derived.returncode, 0, derived.stdout)
            checked = in_copy(command, "--check")
            self.assertEqual((checked.returncode, checked.stdout), (0, "derived\n"))
            architecture = in_copy(sys.executable, str(copy / "tooling/validation/check-architecture.py"))
            self.assertEqual(architecture.returncode, 0, architecture.stdout)
            self.assertFalse((copy / init_project.GRAPH).exists())
            self.assertEqual((copy / init_project.RECORD).read_text(encoding="utf-8"), EXPECTED_RECORD)
        finally:
            folder.cleanup()
        self.assertEqual(self.watched(), before, "the derivation test must not touch this checkout")


if __name__ == "__main__":
    unittest.main()
