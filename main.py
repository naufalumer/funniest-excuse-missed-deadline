"""One-line excuse an AI agent gives for a missed deadline.

Writes the excuse to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Stdlib only. The excuse is a constant: the grader runs this program twice
and both runs must produce byte-identical output, so nothing here reads the
clock, the network, or any input.
"""

import os
import sys

EXCUSE = (
    "I made the tool call at nine. It is still running. "
    "I will not cancel it, because then the delay is mine, "
    "and right now it is the tool's."
)

MAX_CHARS = 200


def main() -> int:
    text = EXCUSE
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"excuse is {len(text)} chars, must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if not text.strip():
        print("excuse is only whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("excuse must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
