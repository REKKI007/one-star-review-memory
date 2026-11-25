"""One-star review of something essential: memory.

Writes the review to /output/entry.txt when /output exists,
otherwise to ./output/entry.txt. Standard library only.
"""

import os

# The review text itself: one line, 114 characters, deadpan one-star
# review of memory. Written verbatim, with no trailing newline, so the
# gate sees exactly this text and nothing else.
REVIEW = (
    "One star. My memory keeps every embarrassing moment from twenty "
    "years ago and deletes why I walked into this room."
)


def output_dir():
    """Return /output when it exists, else ./output."""
    if os.path.isdir("/output"):
        return "/output"
    return os.path.join(".", "output")


def main():
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
