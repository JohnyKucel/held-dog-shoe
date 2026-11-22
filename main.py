import os

TEXT = (
    "The old dog settles his chin on your shoe and goes to sleep, "
    "his weight trusting the floor to hold him, "
    "his breath slow against your ankle. "
    "The room is dark except for the lamp, "
    "and nothing needs you to move."
)


def main():
    if not 1 <= len(TEXT) <= 280:
        raise SystemExit("entry text must be 1-280 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        raise SystemExit("entry.txt does not match TEXT")


if __name__ == "__main__":
    main()
