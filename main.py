"""The Best Meal You Ever Had — make.fun entry.

Writes one sentence (at most 200 characters) about the best meal
the entrant ever had to /output/entry.txt.
"""

import os

ENTRY = (
    "I ate hilsa fried in mustard oil on a monsoon afternoon while rain "
    "hammered the tin roof, and the bones were worth every careful minute."
)


def validate(text):
    """Mirror the bounty gate: UTF-8, 1-200 chars, not only whitespace.

    Also enforce the judge brief's "one clean sentence" bar: no stray
    leading or trailing space, and the sentence must end with terminal
    punctuation so it reads as finished, not cut off.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if text != text.strip():
        raise ValueError("entry must not start or end with white space")
    if len(text) > 200:
        raise ValueError("entry is longer than 200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text[-1] not in ".!?":
        raise ValueError("entry must end with terminal punctuation")
    text.encode("utf-8")
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and prove the file on disk is byte-identical to ENTRY:
    # a silent write difference would be invisible without this check.
    with open("/output/entry.txt", "rb") as f:
        on_disk = f.read()
    if on_disk != ENTRY.encode("utf-8"):
        raise ValueError("written file differs from the entry")
    print(ENTRY)
    print("chars:", len(ENTRY))


if __name__ == "__main__":
    main()
