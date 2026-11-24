#!/usr/bin/env python3
"""Ship It Friday -- entry program.

Writes one line -- the funniest git commit message an AI coding agent
writes in the moment before it breaks production on a Friday -- to
/output/entry.txt for the judge to read. Standard library only, no
network, no input files, deterministic output: the same line, the
same bytes, every run.
"""

import os

LINE = "fix: delete the production database (it was 90% of our problems), happy Friday, see you Monday"

OUTPUT_PATH = "/output/entry.txt"


def _validate(entry: str) -> None:
    """Fail loudly if the entry ever stops meeting the gate.

    The gate requires UTF-8 text of 1 to 159 characters, not only
    whitespace, and the brief requires a single short funny line.
    """
    if not 1 <= len(entry) <= 159:
        raise ValueError(f"entry must be 1-159 characters, got {len(entry)}")
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in entry.strip():
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 for ch in entry):
        raise ValueError("entry must not contain control characters")


def main() -> int:
    _validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the gate counts the file's characters, so the
    # bytes written are exactly the 94 characters of the line itself.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
