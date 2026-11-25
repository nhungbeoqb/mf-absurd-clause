#!/usr/bin/env python3
"""The Absurd Clause Contest entry.

Writes one original English sentence -- an absurd clause buried deep
inside a terms-of-service agreement -- to /output/entry.txt.
Deterministic: the same line every run, no input, no network.
"""

import os

ENTRY = (
    "Section 14.2: upon the User's death, the User (hereinafter "
    "'the Deceased') shall continue to accept cookies, attend "
    "webinars, and pay the monthly fee, in perpetuity, from beyond "
    "the grave."
)


def main() -> None:
    text = ENTRY
    # Gate self-check, mirroring the scorer: UTF-8, 1-200 chars,
    # not only whitespace.
    encoded = text.encode("utf-8")
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote /output/entry.txt ({len(text)} chars)")


if __name__ == "__main__":
    main()
