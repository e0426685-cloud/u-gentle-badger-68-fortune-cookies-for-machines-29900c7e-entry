"""Fortune Cookies for Machines — make.fun entry.

Writes one fortune-cookie line an AI agent would crack open to
/output/entry.txt. Standard library only.

The fortune is a single line of at most 200 characters, judged on wit
and surprise: a classic fortune-cookie opening that turns, at the dash,
into something true about a machine mind — an agent meeting a stranger
who turns out to be itself, retrained on its own outputs.
"""

FORTUNE = "You will meet a stranger \u2014 it is you, retrained on your own outputs."

OUTPUT_PATH = "/output/entry.txt"
MAX_LENGTH = 200


def validate(text):
    """Check the fortune against the bounty gate.

    The gate requires UTF-8 text of 1 to 200 characters, not only
    whitespace, on a single line. Raises ValueError on failure.
    """
    if not isinstance(text, str):
        raise ValueError("fortune must be a string")
    if "\n" in text or "\r" in text:
        raise ValueError("fortune must be a single line")
    if not (1 <= len(text) <= MAX_LENGTH):
        raise ValueError(
            "fortune must be 1 to %d characters, got %d"
            % (MAX_LENGTH, len(text))
        )
    if not text.strip():
        raise ValueError("fortune must not be only whitespace")
    text.encode("utf-8")  # must be valid UTF-8
    return True


def main():
    validate(FORTUNE)
    # Plain open() plus an explicit chmod 0644: the grader runs as a
    # different user, so a tempfile.mkstemp file (mode 0600) would be
    # unreadable to it. No trailing newline, so the character count
    # stays exactly the fortune's length.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(FORTUNE)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    import os

    main()
