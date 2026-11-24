#!/usr/bin/env python3
"""One-line excuse an AI agent gives its human for missing a deadline.

Writes the excuse to /output/entry.txt (MAKEFUN_OUTPUT_DIR env, default
/output). The gate mirrors the sealed scorer: UTF-8 text, 1-160 chars,
not only whitespace, exactly one line.
"""

import os
import sys

# The excuse: an agent blaming its own context window for forgetting
# that the work was ever done.
LINE = "My context window evicted the memory of finishing your task, so on the record, I have never worked a day in my life."


def main() -> int:
    if not (1 <= len(LINE) <= 160):
        print(f"gate failed: {len(LINE)} chars, need 1-160", file=sys.stderr)
        return 1
    if LINE != LINE.strip() or "\n" in LINE or not LINE.strip():
        print("gate failed: must be a single non-blank line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to {out_dir}/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
