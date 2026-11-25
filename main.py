#!/usr/bin/env python3
"""Monday Morning Punchlines — entry program.

Writes exactly one joke about Monday mornings to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). The joke is a fixed string: the
competition judges the text, so the program's job is only to deliver
that text byte-exact, deterministically, with no network and no
non-stdlib dependency.
"""

import os

JOKE = (
    "Monday auto-renewed my weekend's free trial. "
    "There's no cancel button \u2014 just a 9 a.m. meeting with HR."
)

MAX_CHARS = 200


def validate(text: str) -> None:
    """Gate mirror: 1-200 UTF-8 chars, not whitespace-only, no newline."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"joke is {len(text)} chars, must be 1-200")
    if not text.strip():
        raise ValueError("joke must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    text.encode("utf-8")  # raises if somehow not encodable


def resolve_output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    validate(JOKE)
    path = resolve_output_path()
    with open(path, "wb") as f:
        f.write(JOKE.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
