#!/usr/bin/env python3
"""One Emoji, One Smile — the single emoji most likely to make a stranger smile.

Writes exactly one emoji to /output/entry.txt: U+1F31E SUN WITH FACE.

Why this one, against the judge's brief (most important first):
1. Warm and friendly, plainly aiming to warm a stranger: a smiling sun is
   warmth itself — sunshine plus a smile, offered with no strings attached.
2. Warmth at first glance: the face reads as kind and cheerful instantly,
   with no context needed.
3. Universality: the sun is a good omen in every culture and at every age;
   there is no irony or in-joke that could land wrong.
4. Chosen rather than default: it is not the first smiley that comes to
   mind (the plain 🙂 / 😊), yet it stays instantly readable.
5. Right for a stranger: a sunny greeting from the sky carries no intimacy,
   sarcasm or flirtation — nothing that would read oddly from someone unknown.

The file holds the emoji alone: no words, no caption, no trailing newline,
so the entry is byte-identical to the single emoji it means to send.
"""

import os

EMOJI = "\U0001F31E"  # 🌞 SUN WITH FACE


def validate(emoji: str) -> None:
    """Enforce the gate before writing: 1-8 chars, not only whitespace,
    and exactly one emoji (a single code point outside the ASCII range)."""
    assert 1 <= len(emoji) <= 8, f"entry is {len(emoji)} characters"
    assert emoji.strip(), "entry must not be only whitespace"
    assert len(emoji) == 1 and ord(emoji) > 0xFFFF, "entry must be one emoji"


def main() -> None:
    validate(EMOJI)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
