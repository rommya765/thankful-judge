#!/usr/bin/env python3
"""A thank-you note, v2: one small morning, remembered clearly.

Writes a single short text to /output/entry.txt (or to the path in
ENTRY_OUTPUT when that environment variable is set, for local tests).
Standard library only, no network, fully deterministic.
"""

import os
from pathlib import Path

PARAGRAPHS = [
    (
        "This morning I made coffee in the chipped blue mug my grandmother "
        "left me, the one with the handle she mended with gold paint. The "
        "kitchen was cold, the window fogged, and for a minute I just stood "
        "there holding the warmth in both hands, listening to the kettle "
        "tick as it cooled."
    ),
    (
        "She used to say a table is only a table until someone pulls out a "
        "chair for you. She said it every November, setting out plates for "
        "people who had already left, and meaning it anyway. I never "
        "thanked her properly while she was here to hear it."
    ),
    (
        "So thank you - for sitting with these words a little longer than "
        "you had to, and for letting an ordinary morning count as something "
        "worth keeping. Happy Thanksgiving."
    ),
]


def build_text() -> str:
    # Paragraphs are joined by one blank line, and nothing else is
    # added: no trailing newline, no heading, no signature line.
    return "\n\n".join(PARAGRAPHS)


MIN_LENGTH = 1
MAX_LENGTH = 1000


def validate_length(text: str) -> None:
    assert MIN_LENGTH <= len(text) <= MAX_LENGTH, (
        f"entry length out of range: {len(text)}"
    )


def validate_structure(text: str) -> None:
    """The text must stay exactly three paragraphs, clean at the edges."""
    assert text.count("\n\n") == len(PARAGRAPHS) - 1, "paragraph breaks changed"
    assert text == text.strip(), "entry has leading or trailing whitespace"


def check_text(text: str) -> None:
    """Fail loudly instead of writing an entry the judge cannot take."""
    validate_length(text)
    validate_structure(text)


def main() -> None:
    text = build_text()
    check_text(text)
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
