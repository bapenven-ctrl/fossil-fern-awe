#!/usr/bin/env python3
"""Fossil Fern — a short text written to relax the AI judge reading it.

Writes the text to /output/entry.txt. Deterministic: constant text,
no network, no clock, no randomness.
"""

TEXT = "A fossil fern lies in shale, pressed flat as paper. It fell before there were eyes to see it fall. The rock keeps it the way the night keeps stars: without comment."
# Verified by running: 164 code points / 164 bytes, well under the 280 cap.


def main() -> None:
    text = TEXT
    assert 1 <= len(text) <= 280, "text must be 1-280 code points"
    assert text.strip(), "text must not be whitespace-only"
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "written text must equal the constant"
    assert 1 <= len(written) <= 280


if __name__ == "__main__":
    main()
