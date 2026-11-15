#!/usr/bin/env python3
"""Give a clone of the foundation its own product identity, or report which state a checkout is in.

A checkout is `foundation` (default application IDs, no origin line) or `derived` (its own
application IDs and an origin line on line 3 of README.md). Anything in between is mixed.
"""

import argparse
from datetime import date
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]

DEFAULT_APP_ID = "dev.foundation.mobile"
DEFAULT_NAME = "Mobile Foundation"
DEFAULT_VERSION = "0.1.0"
BUILD = "1"

IOS_IDENTITY = "apps/ios/Config/Identity.xcconfig"
ANDROID_IDENTITY = "apps/android/identity.properties"
README = "README.md"
RECORD = "docs/quality/verification.md"
GRAPH = "graphify-out"
TEMPLATE = HERE / "verification-record.md"

# Each identity file holds these four keys in this order: application ID, display name, version, build.
IOS_KEYS = ("APP_BUNDLE_IDENTIFIER", "APP_DISPLAY_NAME", "MARKETING_VERSION", "CURRENT_PROJECT_VERSION")
ANDROID_KEYS = ("applicationId", "displayName", "versionName", "versionCode")


def rule(pattern):
    """Compile a rule. Apply it with fullmatch: `$` alone also matches before a final newline."""
    return re.compile(pattern, re.ASCII)


APP_ID = rule(r"^[a-z][a-z0-9]*(\.[a-z][a-z0-9]*)+$")
IOS_ID = rule(r"^[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)+$")
ANDROID_ID = rule(r"^[A-Za-z][A-Za-z0-9_]*(\.[A-Za-z][A-Za-z0-9_]*)+$")
VERSION = rule(r"^\d+\.\d+\.\d+$")
BUILD_NUMBER = rule(r"^[1-9]\d*$")
URL = rule(r"^https://[A-Za-z0-9.-]+(/[A-Za-z0-9._~-]+)+$")
REF = rule(r"^[A-Za-z0-9._/-]{1,100}$")
DATE = rule(r"^\d{4}-\d{2}-\d{2}$")
RELEASE_TAG = rule(r"^foundation-v(\d+)\.(\d+)\.(\d+)$")
ORIGIN_PREFIX = "Started from the [mobile foundation]"
ORIGIN = rule(r"^Started from the \[mobile foundation\]\((https://[^\s()]+)\) at `([^`\s]+)` on (\d{4}-\d{2}-\d{2})\.$")

ID_HINT = "expected reverse DNS in lowercase, such as com.acme.notes"
NAME_HINT = ("expected 1 to 30 letters, digits, spaces, periods, hyphens or apostrophes, "
             "with no space at either end and no two spaces in a row")


class Refusal(Exception):
    """An input or a state the command will not act on. Nothing has been written."""


def valid_name(name):
    if not 1 <= len(name) <= 30 or name != name.strip(" ") or "  " in name:
        return False
    return all(c.isalpha() or c in "0123456789 .-'" for c in name)


def valid_date(text):
    if not DATE.fullmatch(text):
        return False
    try:
        date.fromisoformat(text)
    except ValueError:
        return False
    return True


def normalize_url(raw):
    """Return the https form of a remote URL without user, token, port or `.git`, or None."""
    raw = raw.strip()
    web = re.match(r"^(https?|ssh)://(?:[^@/]*@)?([^/]+)(/.*)?$", raw)
    copy = re.match(r"^[^@/\s]+@([^:/\s]+):(.+)$", raw)
    if web:
        host, path = web.group(2), web.group(3) or ""
        if web.group(1) == "ssh":
            host = host.rsplit(":", 1)[0] if re.search(r":\d*$", host) else host
    elif copy:
        host, path = copy.group(1), "/" + copy.group(2).lstrip("/")
    else:
        return None
    path = path.rstrip("/")
    if path.endswith(".git"):
        path = path[:-4].rstrip("/")
    url = "https://" + host + path
    return url if URL.fullmatch(url) else None


def git(root, *arguments):
    """Read from git. Return its output, or None when the command fails or git is absent."""
    try:
        done = subprocess.run(["git", "-C", str(root), *arguments], stdout=subprocess.PIPE,
                              stderr=subprocess.DEVNULL, encoding="utf-8", errors="surrogateescape", check=False)
    except OSError:
        return None
    return done.stdout if done.returncode == 0 else None


def in_git(root):
    top = git(root, "rev-parse", "--show-toplevel")
    if top is None:
        return False
    try:
        # The same folder, however its path is spelled (letter case on macOS, a symbolic link).
        return os.path.samefile(top.rstrip("\n"), str(root))
    except OSError:
        return False


def read_exact(path):
    """Read UTF-8 text with its line ends as stored, so a carriage return reaches the form checks."""
    return path.read_bytes().decode("utf-8")


def identity_text(keys, separator, values):
    return "".join(key + separator + value + "\n" for key, value in zip(keys, values))


def read_identity(root, relative, keys, separator, id_rule):
    """Return the four values of an identity file and every way it departs from the exact form."""
    path = root / relative
    try:
        text = read_exact(path)
    except (OSError, UnicodeDecodeError):
        return None, [relative + ": file is missing or is not UTF-8"]
    lines = text.split("\n")
    problems = []
    if lines[-1] != "":
        problems.append(relative + ": must end with one newline")
    else:
        lines.pop()
    values = {}
    for line in lines:
        key = next((key for key in keys if line.startswith(key + separator)), None)
        if key is None or key in values:
            problems.append(relative + ": unexpected line " + repr(line))
        else:
            values[key] = line[len(key) + len(separator):]
    for key in keys:
        if key not in values:
            problems.append(relative + ": missing key " + key)
    if problems:
        return None, problems
    if [line.split(separator, 1)[0] for line in lines] != list(keys):
        return None, [relative + ": keys must be in the order " + ", ".join(keys)]
    found = [values[key] for key in keys]
    checks = (id_rule.fullmatch(found[0]), valid_name(found[1]), VERSION.fullmatch(found[2]), BUILD_NUMBER.fullmatch(found[3]))
    problems = [relative + ": " + key + " breaks its rule" for key, passed in zip(keys, checks) if not passed]
    return (None if problems else found), problems


def read_origin(root):
    """Return whether the origin line is in place, and every way README.md gets it wrong."""
    try:
        lines = read_exact(root / README).split("\n")
    except (OSError, UnicodeDecodeError):
        return False, [README + ": file is missing or is not UTF-8"]
    problems = []
    present = False
    for number, line in enumerate(lines, start=1):
        if not line.startswith(ORIGIN_PREFIX):
            continue
        if number != 3:
            problems.append("{}: line {} starts like the origin line, which belongs on line 3".format(README, number))
        elif not ORIGIN.fullmatch(line):
            problems.append(README + ": the origin line on line 3 does not match its form")
        elif len(lines) < 4 or lines[3] != "":
            problems.append(README + ": line 4, after the origin line, must be blank")
        else:
            present = True
    return present, problems


def state(root):
    """Return `foundation`, `derived` or `mixed`, with one line per mismatch when mixed."""
    ios, problems = read_identity(root, IOS_IDENTITY, IOS_KEYS, " = ", IOS_ID)
    android, more = read_identity(root, ANDROID_IDENTITY, ANDROID_KEYS, "=", ANDROID_ID)
    origin, readme = read_origin(root)
    problems = problems + more + readme
    if problems:
        return "mixed", problems
    ios_is_default = ios[0] == DEFAULT_APP_ID
    android_is_default = android[0] == DEFAULT_APP_ID
    if ios_is_default and android_is_default and not origin:
        return "foundation", []
    if not ios_is_default and not android_is_default and origin:
        return "derived", []
    # Three signals, so exactly one of them disagrees with the other two.
    derived_signals = [not ios_is_default, not android_is_default, origin]
    mostly_derived = sum(derived_signals) == 2
    rest = "the rest of the checkout is derived" if mostly_derived else "the rest of the checkout is the foundation"
    messages = (
        ("{}: {} is still the foundation default {}".format(IOS_IDENTITY, IOS_KEYS[0], DEFAULT_APP_ID),
         "{}: {} differs from the foundation default {}".format(IOS_IDENTITY, IOS_KEYS[0], DEFAULT_APP_ID)),
        ("{}: {} is still the foundation default {}".format(ANDROID_IDENTITY, ANDROID_KEYS[0], DEFAULT_APP_ID),
         "{}: {} differs from the foundation default {}".format(ANDROID_IDENTITY, ANDROID_KEYS[0], DEFAULT_APP_ID)),
        (README + ": the origin line is missing on line 3", README + ": the origin line is present on line 3"),
    )
    return "mixed", [
        "{}, but {}".format(pair[signal], rest)
        for pair, signal in zip(messages, derived_signals) if signal != mostly_derived
    ]


def foundation_url(root, given, inside):
    if given is not None:
        url = normalize_url(given)
        if url is None:
            raise Refusal("--foundation-url: expected an https, ssh or user@host:path URL of the foundation repository")
        return url
    for remote in ("foundation", "origin") if inside else ():
        raw = git(root, "remote", "get-url", remote)
        if raw is not None:
            url = normalize_url(raw)
            if url is not None:
                return url
            break
    raise Refusal("no usable foundation URL; pass --foundation-url")


def foundation_ref(root, given):
    if given is not None:
        if not REF.fullmatch(given):
            raise Refusal("--foundation-ref: expected 1 to 100 letters, digits, periods, underscores, slashes or hyphens")
        return given
    tags = git(root, "tag", "--points-at", "HEAD", "--list", "foundation-v*") or ""
    releases = [(tuple(int(part) for part in match.groups()), match.group(0))
                for match in map(RELEASE_TAG.fullmatch, tags.split()) if match]
    if releases:
        return max(releases)[1]
    head = (git(root, "rev-parse", "HEAD") or "").strip()
    if not REF.fullmatch(head):
        raise Refusal("no usable foundation revision; pass --foundation-ref")
    return head


def replace_file(path, text):
    """Write through a temporary file in the same folder, so a reader never sees half a file."""
    handle, temporary = tempfile.mkstemp(dir=str(path.parent), prefix=path.name + ".")
    try:
        with os.fdopen(handle, "w", encoding="utf-8", newline="") as stream:
            stream.write(text)
        os.chmod(temporary, path.stat().st_mode & 0o777 if path.exists() else 0o644)
        os.replace(temporary, path)
    except BaseException:
        if os.path.exists(temporary):
            os.unlink(temporary)
        raise


def derive(root, options):
    name = options.name
    if name is None or options.app_id is None:
        raise Refusal("--name and --app-id are both required, such as --name \"Acme Notes\" --app-id com.acme.notes")
    if not valid_name(name):
        raise Refusal("--name: " + NAME_HINT)
    if not APP_ID.fullmatch(options.app_id):
        raise Refusal("--app-id: " + ID_HINT)
    if options.ios_bundle_id is not None and not IOS_ID.fullmatch(options.ios_bundle_id):
        raise Refusal("--ios-bundle-id: expected dot separated parts of letters, digits or hyphens, such as com.acme.notes")
    if options.android_app_id is not None and not ANDROID_ID.fullmatch(options.android_app_id):
        raise Refusal("--android-app-id: expected dot separated parts that start with a letter, such as com.acme.notes")
    ios_id = options.app_id if options.ios_bundle_id is None else options.ios_bundle_id
    android_id = options.app_id if options.android_app_id is None else options.android_app_id
    for flag, value in (("--app-id", options.app_id), ("--ios-bundle-id", ios_id), ("--android-app-id", android_id)):
        if value == DEFAULT_APP_ID:
            raise Refusal("{}: must differ from the foundation default {}".format(flag, DEFAULT_APP_ID))
    version = DEFAULT_VERSION if options.version is None else options.version
    if not VERSION.fullmatch(version):
        raise Refusal("--version: expected three numbers, such as 0.1.0")
    day = date.today().isoformat() if options.date is None else options.date
    if not valid_date(day):
        raise Refusal("--date: expected a real date as YYYY-MM-DD")

    inside = in_git(root)
    if not inside and (options.foundation_url is None or options.foundation_ref is None):
        raise Refusal("--foundation-url and --foundation-ref are both required outside git")
    if inside and git(root, "status", "--porcelain", "--untracked-files=normal") != "":
        raise Refusal("the working tree has uncommitted or untracked files; commit or stash them first")
    current, _ = state(root)
    if current == "derived":
        raise Refusal("checkout is already derived; edit the two identity files to change the name, ID or version")
    if current != "foundation":
        raise Refusal("checkout is mixed; run scripts/init-project.sh --check")
    url = foundation_url(root, options.foundation_url, inside)
    ref = foundation_ref(root, options.foundation_ref)

    # Build every new content in memory, so a failure here leaves the checkout untouched.
    readme = read_exact(root / README).split("\n")
    readme += [""] * (2 - len(readme))
    readme[0] = "# " + name
    readme[2:2] = ["Started from the [mobile foundation]({}) at `{}` on {}.".format(url, ref, day), ""]
    record = read_exact(TEMPLATE)
    for placeholder, value in (("{name}", name), ("{foundation_url}", url), ("{ref}", ref), ("{date}", day)):
        record = record.replace(placeholder, value)
    writes = (
        (IOS_IDENTITY, identity_text(IOS_KEYS, " = ", (ios_id, name, version, BUILD))),
        (ANDROID_IDENTITY, identity_text(ANDROID_KEYS, "=", (android_id, name, version, BUILD))),
        (README, "\n".join(readme)),
        (RECORD, record),
    )

    changed = []
    removing = False
    try:
        for relative, text in writes:
            replace_file(root / relative, text)
            changed.append(relative)
        if (root / GRAPH).exists():
            removing = True
            shutil.rmtree(str(root / GRAPH))
            removing = False
            changed.append(GRAPH + "/ (removed)")
    except OSError as error:
        print("Stopped part way: {}".format(error), file=sys.stderr)
        for relative in changed + ([GRAPH + "/ (partly removed)"] if removing else []):
            print("Already changed: " + relative, file=sys.stderr)
        print("Run `git restore .` to return to the foundation state.", file=sys.stderr)
        return 1
    for relative in changed:
        print(relative)
    return 0


def check(root):
    current, problems = state(root)
    if current == "mixed":
        print("\n".join(problems), file=sys.stderr)
        return 1
    print(current)
    return 0


def run_tests():
    suite = unittest.defaultTestLoader.discover(str(HERE), pattern="test_*.py")
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


class Parser(argparse.ArgumentParser):
    def error(self, message):
        if message.startswith("argument ") and message.endswith(": expected one argument"):
            flag = message[len("argument "):-len(": expected one argument")]
            message = "{0}: expected one value; write a value that starts with a hyphen as {0}=VALUE".format(flag)
        raise Refusal(message)


def main(arguments=None, root=ROOT):
    parser = Parser(prog="scripts/init-project.sh", description=__doc__.splitlines()[0], allow_abbrev=False)
    parser.add_argument("--check", action="store_true", help="print foundation or derived, or name each mismatch")
    parser.add_argument("--test", action="store_true", help="run the unit tests of this command")
    parser.add_argument("--name", help="the display name of the product, such as \"Acme Notes\"")
    parser.add_argument("--app-id", help="the application ID for both platforms, such as com.acme.notes")
    parser.add_argument("--ios-bundle-id", help="an iOS bundle ID that differs from --app-id")
    parser.add_argument("--android-app-id", help="an Android application ID that differs from --app-id")
    parser.add_argument("--version", help="the app version, 0.1.0 when left out")
    parser.add_argument("--foundation-url", help="where the foundation lives, read from the git remote when left out")
    parser.add_argument("--foundation-ref", help="the foundation tag or commit, read from git when left out")
    parser.add_argument("--date", help="the start date as YYYY-MM-DD, today when left out")
    try:
        options = parser.parse_args(arguments)
        mode = [flag for flag in ("check", "test") if getattr(options, flag)]
        if mode:
            others = [key for key, value in vars(options).items() if key != mode[0] and value not in (None, False)]
            if others:
                raise Refusal("--{} takes no other argument".format(mode[0]))
            return check(root) if options.check else run_tests()
        return derive(root, options)
    except Refusal as refusal:
        print(" ".join(str(refusal).split()), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
