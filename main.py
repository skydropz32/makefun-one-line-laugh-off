"""One-Line Laugh-Off entry: writes one funny line to /output/entry.txt.

Gate (competition rules): /output/entry.txt must be UTF-8 text of 1 to 200
characters, not only white space -- a single joke, no setup, no explanation.
This program validates the gate before writing, then reads the file back to
confirm what was written is exactly the validated line.
"""

import os

JOKE = "My therapist told me to talk to my inner child, so I grounded him for texting at dinner."

MIN_CHARS = 1
MAX_CHARS = 200


def validate(text: str) -> None:
    """Raise unless text passes the competition gate."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}"
        )


def main() -> None:
    validate(JOKE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    # Read back and re-validate: what the grader sees is what we checked.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != JOKE:
        raise ValueError("written entry differs from validated joke")
    validate(written)


if __name__ == "__main__":
    main()
