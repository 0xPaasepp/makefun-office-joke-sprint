#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint — the entry script.

It writes one joke to /output/entry.txt: a trust-fall team-building
exercise where nobody catches you, and suddenly the org chart makes
sense. One line, no trailing newline.
"""

from pathlib import Path

JOKE = "Our team-building exercise was trust falls; I fell, nobody caught me, and now I finally understand the org chart."

DESTINATION = Path("/output/entry.txt")


def write_entry() -> None:
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
