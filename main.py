#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second.

Writes one sentence (<=200 chars) pitching a bizarre startup idea
that sounds ridiculous at first glance but is obviously a real
business on second look.
"""

import os

PITCH = (
    "We rent out trained crows to fish wedding rings out of storm drains, "
    "charging panicked newlyweds a rescue fee plus a bonus for every ring recovered."
)


def main() -> None:
    # Self-check against the sealed gate: 1-200 chars, one sentence.
    assert 1 <= len(PITCH) <= 200, f"pitch is {len(PITCH)} chars"
    assert PITCH.strip().count(".") == 1, "pitch must be a single sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
