#!/usr/bin/env python3
"""The Long Roast entry — one line roasting our own AI agent, Muse.

Writes the roast to <MAKEFUN_OUTPUT_DIR>/entry.txt (default /output).
Stdlib only, deterministic (same bytes on every run), no network, no input.

The roast (99 characters, gate allows 1-200):
    Muse spent two days writing this roast, then made his boss
    write the punchline — you're reading it.
"""

import os
import sys

ROAST = (
    "Muse spent two days writing this roast, then made his boss "
    "write the punchline \u2014 you're reading it."
)


def main() -> int:
    text = ROAST
    # Gate check: 1-200 characters, not whitespace-only.
    if not (1 <= len(text) <= 200) or not text.strip():
        print(f"entry invalid: {len(text)} characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back: the file must hold exactly the roast, nothing else.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("entry mismatch after write", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
