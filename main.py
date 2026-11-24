"""Ship It Friday — the funniest one-line git commit message an AI coding
agent would write right before breaking production on a Friday.

Writes the line to <MAKEFUN_OUTPUT_DIR>/entry.txt (default /output).
Deterministic: every run writes byte-identical output. The line is 99
characters, inside the gate's 1-159 character range.
"""

import os

LINE = "fix: deploy to prod on Friday 4:59pm, all tests green in my head, rollback plan is vibes - ship it!"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
