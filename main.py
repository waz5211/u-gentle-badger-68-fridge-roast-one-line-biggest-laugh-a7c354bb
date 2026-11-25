#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh.

Writes a single original one-line roast of a smart fridge to
/output/entry.txt (at most 200 characters, UTF-8).
"""

import os

ROAST = (
    "My smart fridge finished a firmware update and now refuses to "
    "chill anything until I rate it five stars."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = ROAST.strip()
    assert 1 <= len(line) <= 200, f"line is {len(line)} characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
