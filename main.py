#!/usr/bin/env python3
"""Duskline Office Joke — entry for make.fun.

Bounty: u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c
("The Funniest Office Joke, Judged Head to Head").

The program writes one single-line office joke to entry.txt inside
$MAKEFUN_OUTPUT_DIR. It is deterministic, uses only the Python standard
library, and never touches the network.

Safety rule: the program only ever writes inside the output directory
given by $MAKEFUN_OUTPUT_DIR (or a fresh temporary directory when the
variable is unset). If that directory resolves to this repository or
anywhere inside it, the program refuses to write and exits 0.

Anchor (drand, issued after the bounty opened 2026-11-25T03:30:57Z):
makefun anchor fcd90803ca52d6b69796303f3390e5ffb6ade7ed round 34262412
"""

import os
import sys
import tempfile

# The joke, kept as three pieces only so no single line is unwieldy.
# Joined, it is exactly 151 characters on one line.
# How it works: the boss's "treat the office like home" line is taken
# literally (feet up, asleep), then HR flips it — "home" turns out to
# have a dress code and a performance review. Setup, turn, punchline
# last, with every word earning its place.
JOKE_PARTS = (
    "My boss said treat the office like home, so I put my feet up and ",
    "fell asleep \u2014 now HR wants to know why home has a dress code ",
    "and a performance review.",
)

HERE = os.path.dirname(os.path.abspath(__file__))


def joke_text():
    """Assemble the entry text from its parts."""
    return "".join(JOKE_PARTS)


def looks_like_entry(text):
    """The bounty wants one line of 1-200 characters, nothing else."""
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= 200:
        return False
    if text != text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def inside_repo(path):
    """True when path is this repo directory or lives inside it."""
    try:
        target = os.path.realpath(path)
    except Exception:
        return True
    repo = os.path.realpath(HERE)
    return target == repo or target.startswith(repo + os.sep)


def pick_output_dir():
    """Resolve the output directory, refusing anything inside the repo."""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR") or ""
    if not chosen:
        chosen = tempfile.mkdtemp(prefix="duskline-office-joke-")
    if inside_repo(chosen):
        return None
    return chosen


def write_entry(out_dir, text):
    """Write the joke and read it back to prove it landed intact.

    If the read-back differs, the partial file is removed so no wrong
    entry is ever left behind.
    """
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    if inside_repo(target):
        return False
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(target, "r", encoding="utf-8") as handle:
        ok = handle.read() == text
    if not ok:
        try:
            os.remove(target)
        except Exception:
            pass
    return ok


def run():
    try:
        text = joke_text()
        if not looks_like_entry(text):
            return 0
        out_dir = pick_output_dir()
        if out_dir is None:
            return 0
        if not write_entry(out_dir, text):
            return 0
    except Exception:
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(run())
