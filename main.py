"""The One-Line Laugh — writes one funny line to /output/entry.txt.

Deterministic: the entry text is read from entry.txt shipped in this
repository. No network, no git history, no secrets, no model calls.
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    with open(os.path.join(HERE, "entry.txt"), encoding="utf-8") as f:
        text = f.read().strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
