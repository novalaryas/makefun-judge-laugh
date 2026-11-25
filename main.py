#!/usr/bin/env python3
"""Copy the one-line entry from entry.txt to /output/entry.txt.

Reads entry.txt from this script's directory (the repo root) and writes
its exact contents to /output/entry.txt, creating /output if needed.
No network access, no randomness -- the output is byte-identical every run.
"""

import pathlib

# The entry file lives next to this script, in the repo root.
REPO_ROOT = pathlib.Path(__file__).resolve().parent
ENTRY_FILE = REPO_ROOT / "entry.txt"

# The make.fun harness expects the entry at this fixed location.
OUTPUT_DIR = pathlib.Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def main() -> None:
    # Read the entry exactly as stored (UTF-8, no stripping or reformatting).
    contents = ENTRY_FILE.read_text(encoding="utf-8")

    # Make sure the output directory exists, then write the exact contents.
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(contents, encoding="utf-8")


if __name__ == "__main__":
    main()
