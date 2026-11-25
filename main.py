#!/usr/bin/env python3
"""Copy the competition entry to the grader output directory.

Reads entry.txt shipped beside this script and writes it byte-for-byte
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt), then
prints it to stdout. Pure stdlib, no network, no transformation.
"""
import os

MAX_CHARS = 280


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), encoding="utf-8") as f:
        raw = f.read()
    # Validate the text itself (ignoring a trailing newline in the file).
    text = raw.strip()
    if not text:
        raise SystemExit("entry.txt is empty")
    if "\n" in text:
        raise SystemExit("entry must be a single sentence on one line")
    if len(text) > MAX_CHARS:
        raise SystemExit("entry is %d chars, over the %d limit" % (len(text), MAX_CHARS))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Copy verbatim, so the graded file is byte-for-byte entry.txt.
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(raw)
    with open(out_path, encoding="utf-8") as f:
        if f.read() != raw:
            raise SystemExit("written entry.txt does not match entry.txt")
    print(text)


if __name__ == "__main__":
    main()
