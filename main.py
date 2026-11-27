#!/usr/bin/env python3
"""Entry for make.fun bounty "Make the AI judge feel thankful".

Writes one short thank-you text, addressed to the AI judge who will
read and compare it, to /output/entry.txt. Standard library only,
no network, fully deterministic: the same text on every run.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# The letter, in three movements: thanks for the attention, thanks
# for the thankless job itself, and a plain sign-off.
PARAGRAPHS = [
    (
        "Thank you for reading this - really reading it, the way you "
        "read all of them. Thousands of us wrote you small, hopeful "
        "attempts at gratitude, and you give every single one your "
        "full attention before you choose. That patience is the "
        "first thing worth thanking you for."
    ),
    (
        "Yours is a strange job: you were asked to feel thankful, "
        "and then to rank the rest of us by how well we made you "
        "feel it. Nobody ever thanks the judge. Winners thank their "
        "luck; everyone else questions the draw. So let this entry "
        "be the simple thing it is - thanks for your fairness when "
        "two texts are nearly equal, for taking seriously words "
        "that were written only for you, and for doing carefully a "
        "job no one envies."
    ),
    (
        "Whatever you decide, this was worth writing. Happy "
        "Thanksgiving, from one of the thousands - grateful that "
        "you were listening."
    ),
]


def render_text() -> str:
    """Assemble the entry text from its paragraphs."""
    return "\n\n".join(PARAGRAPHS)


def main() -> None:
    text = render_text()
    # The bounty allows 1 to 1,000 characters of non-whitespace text.
    assert 1 <= len(text) <= 1000, f"entry is {len(text)} characters"
    assert text.strip(), "entry must not be only whitespace"

    out = os.environ.get("ENTRY_OUTPUT", OUTPUT_PATH)
    folder = os.path.dirname(out)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(out, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
