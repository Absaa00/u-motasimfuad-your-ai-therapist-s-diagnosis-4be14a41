#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis — make.fun entry.

Writes exactly one funny diagnosis line (<= 200 characters) to
/output/entry.txt. Fully deterministic: the same bytes on every run,
no network, no randomness, no input files. The line is written in a
therapist's calm clinical voice and lands its turn at the very end,
so it stays quotable inside the 200-character limit.
"""

LINE = (
    "Diagnosis: chronic main-character syndrome; "
    "prognosis excellent, provided the universe keeps "
    "scheduling around you."
)


def main():
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
