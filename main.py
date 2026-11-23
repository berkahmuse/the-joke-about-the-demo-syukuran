#!/usr/bin/env python3
"""The joke about the demo: one-line joke about working beside AI coding agents.

Writes the joke to /output/entry.txt (UTF-8, one line, 1-280 chars).
"""

import os

JOKE = "My AI coding agent interrupted my demo to ask who wrote this garbage, then apologized when git blame pointed at it."

def main() -> None:
    if not 1 <= len(JOKE) <= 280:
        raise ValueError(f"joke must be 1-280 chars, got {len(JOKE)}")
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
