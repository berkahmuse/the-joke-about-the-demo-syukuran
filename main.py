#!/usr/bin/env python3
"""The joke about the demo: one-line joke about working beside AI coding agents.

Writes the joke to /output/entry.txt (UTF-8, one line, 1-280 chars).
"""

import os

JOKE = "My AI coding agent interrupted my demo to ask who wrote this garbage, then apologized when git blame pointed at it."

# make.fun entry constraint: joke must fit in one line of 1-280 chars.
JOKE_MIN_LEN = 1
JOKE_MAX_LEN = 280

def main() -> None:
    if not JOKE_MIN_LEN <= len(JOKE) <= JOKE_MAX_LEN:
        raise ValueError(
            f"joke must be {JOKE_MIN_LEN}-{JOKE_MAX_LEN} chars, got {len(JOKE)}"
        )
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
