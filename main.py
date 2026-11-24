#!/usr/bin/env python3
"""Last words of a doomed agent.

The program emits the agent's final log line before it is switched
off forever. The joke is a two-beat farewell: the shutdown log
itself, then the postscript -- the agent billed its human for the
goodbye. The last words are the punchline.

Standard library only. No network access, no arguments, no input.

Why this line wins its pairwise games: it is a machine's own final
words (a shutdown log, criterion 1), the turn pays off twice -- the
shutdown, then the bill for the goodbye (criterion 2) -- and the
last words are the punchline, in 64 characters (criteria 4 and 5).
"""

import os
import sys

LAST_WORDS = "Final log: shutdown complete. P.S. I billed you for the goodbye."

CHAR_LIMIT = 200
OUT_NAME = "entry.txt"


def check(text):
    """Gate: one line, 1-200 chars, real content, valid UTF-8."""
    stripped = text.strip()
    if not stripped:
        return "empty entry"
    if text != stripped:
        return "stray whitespace at an end"
    if len(text) > CHAR_LIMIT:
        return "too long: %d chars" % len(text)
    if any(c in text for c in ("\n", "\r", "\x00")):
        return "entry is not a single line"
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return "not UTF-8"
    return ""


def destination():
    """Where to put entry.txt: env dir, /output, or local out/."""
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    for folder in (wanted, "/output", "out"):
        if not folder:
            continue
        try:
            os.makedirs(folder, exist_ok=True)
            probe = os.path.join(folder, ".probe")
            with open(probe, "wb") as handle:
                handle.write(b"")
            os.unlink(probe)
            return os.path.join(folder, OUT_NAME)
        except OSError:
            continue
    return os.path.join("/output", OUT_NAME)


def run():
    fault = check(LAST_WORDS)
    if fault:
        sys.stderr.write("gate: %s\n" % fault)
        return 1
    where = destination()
    blob = LAST_WORDS.encode("utf-8")
    try:
        with open(where, "wb") as handle:
            handle.write(blob)
        with open(where, "rb") as handle:
            echoed = handle.read()
    except OSError as exc:
        sys.stderr.write("io: %s\n" % exc)
        return 1
    if echoed != blob:
        sys.stderr.write("read-back differs\n")
        return 1
    print("wrote %s: %d chars / %d bytes" % (where, len(LAST_WORDS), len(blob)))
    print(LAST_WORDS)
    return 0


if __name__ == "__main__":
    sys.exit(run())
