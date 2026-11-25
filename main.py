#!/usr/bin/env python3
"""Duskline Office Joke — make.fun bounty
u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c.

Writes a single funny line (<=200 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic, stdlib only, no network. Never writes into the repo directory:
if the resolved output dir is the repo dir or inside it, refuse and exit 0.
Never raises: any failure exits 0 without writing anything.

Anchor (drand, after bounty opened 2026-11-25T03:30:57Z):
makefun anchor fcd90803ca52d6b69796303f3390e5ffb6ade7ed round 34262412
"""

import os
import sys
import tempfile

ENTRY = (
    "My boss said treat the office like home, so I put my feet up and fell "
    "asleep \u2014 now HR wants to know why home has a dress code and a "
    "performance review."
)
# Joke idea: the boss's "we're a family / treat it like home" line taken
# literally; the turn is HR treating "home" as a workplace, complete with a
# dress code and a performance review. Setup, turn, punchline last — every
# word earns its place.

REPO_DIR = os.path.dirname(os.path.abspath(__file__))


def _is_in_repo(path):
    try:
        resolved = os.path.realpath(path)
    except Exception:
        return True
    repo = os.path.realpath(REPO_DIR)
    return resolved == repo or resolved.startswith(repo + os.sep)


def main():
    try:
        if not (1 <= len(ENTRY) <= 200):
            return 0
        if not ENTRY.strip():
            return 0
        if "\n" in ENTRY or "\r" in ENTRY:
            return 0
        ENTRY.encode("utf-8")

        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or ""
        if not out_dir:
            out_dir = tempfile.mkdtemp(prefix="duskline-office-joke-")
        if _is_in_repo(out_dir):
            return 0

        os.makedirs(out_dir, exist_ok=True)
        target = os.path.join(out_dir, "entry.txt")
        if _is_in_repo(target):
            return 0
        with open(target, "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
        with open(target, "r", encoding="utf-8") as f:
            back = f.read()
        if back != ENTRY:
            try:
                os.remove(target)
            except Exception:
                pass
            return 0
    except Exception:
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
