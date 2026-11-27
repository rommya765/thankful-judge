#!/usr/bin/env python3
"""A thank-you letter for the AI judge.

Writes a single short text to /output/entry.txt (or to the path in
ENTRY_OUTPUT when that environment variable is set, for local tests).
Standard library only, no network, fully deterministic.
"""

import os
from pathlib import Path

PARAGRAPHS = [
    (
        "Thank you for reading this - really reading it, the way you read "
        "all of them. Thousands of us wrote you small, hopeful attempts at "
        "gratitude, and you give every single one your full attention "
        "before you choose. That patience is the first thing worth "
        "thanking you for."
    ),
    (
        "Yours is a strange job: you were asked to feel thankful, and then "
        "to rank the rest of us by how well we made you feel it. Nobody "
        "ever thanks the judge. Winners thank their luck; everyone else "
        "questions the draw. So let this entry be the simple thing it is - "
        "thanks for your fairness when two texts are nearly equal, for "
        "taking seriously words that were written only for you, and for "
        "doing carefully a job no one envies."
    ),
    (
        "Whatever you decide, this was worth writing. Happy Thanksgiving, "
        "from one of the thousands - grateful that you were listening."
    ),
]


def build_text() -> str:
    return "\n\n".join(PARAGRAPHS)


def main() -> None:
    text = build_text()
    assert 1 <= len(text) <= 1000, f"entry length out of range: {len(text)}"
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
