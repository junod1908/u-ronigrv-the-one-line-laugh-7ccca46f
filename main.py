"""The One-Line Laugh — writes one funny line to /output/entry.txt.

Deterministic: the entry text is read from entry.txt shipped in this
repository. No network, no git history, no secrets, no model calls.
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    with open(os.path.join(HERE, "entry.txt"), encoding="utf-8") as f:
        text = f.read().strip()
    # Gate rule: the entry must be 1-200 characters, one sentence, not
    # only whitespace. Fail loudly instead of shipping an invalid entry.
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry.txt must be 1-200 characters, got {len(text)}")
    if not text or text.isspace():
        raise SystemExit("entry.txt must not be only whitespace")
    if "\n" in text:
        raise SystemExit("entry.txt must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
