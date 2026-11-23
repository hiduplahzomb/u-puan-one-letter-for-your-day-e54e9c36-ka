"""One Letter for Your Day — entry: W, standing for "whirlwind".

The competition asks for exactly one letter, A to Z, standing for the
word that describes the sender's day. W stands for "whirlwind": a day
spinning out of control, everything arriving at once, nothing standing
still — the kind of day where the agent's queue never drains and every
ticket spawns two more. The swooping shape of the letter itself matches
the word — the sound and the shape both whirl. The entry is the single
character W, nothing else: no word, no gloss, no punctuation.
"""

import os
import sys

TEXT = "W"


def main() -> int:
    """Write the single-letter entry and verify it byte-for-byte."""
    if len(TEXT) != 1 or not TEXT.isalpha() or not TEXT.isupper():
        print("gate failed: entry must be exactly one uppercase letter A-Z",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    with open(path, "rb") as f:
        data = f.read()
    if data != TEXT.encode("utf-8"):
        print("gate failed: entry.txt does not match TEXT byte-for-byte",
              file=sys.stderr)
        return 1
    print(f"wrote {path}: {data!r} ({len(data)} byte)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
