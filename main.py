#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses — entry program.

Writes one funny single-line developer excuse to /output/entry.txt.
Gate: UTF-8 text, 1-200 characters, not only whitespace.
"""

import os
import sys

# FINAL line — "promoted" beats "shipped" (a promotion is the dev's own
# language for moving code up the environments), and "resigned" beats
# "quit" (a resignation letter is funnier than a crash). Same twist on
# the worn "works on my machine" excuse, now with a cleaner punchline.
ENTRY = "It worked on my machine, so I promoted my machine to production. It resigned within the hour."


def main() -> int:
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    n = len(ENTRY)
    if not (1 <= n <= 200) or not ENTRY.strip():
        print(f"INVALID entry: {n} chars", file=sys.stderr)
        return 1
    print(f"Wrote {n} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
