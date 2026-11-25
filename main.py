import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

TAGLINE = "Your keys stay yours; your Solana wallet agent does the work the moment you say the word."


def pick_entry_path():
    entry_out = os.environ.get("ENTRY_OUT")
    if entry_out:
        if entry_out.endswith(".txt"):
            return entry_out
        return os.path.join(entry_out, "entry.txt")
    entry_out_dir = os.environ.get("ENTRY_OUT_DIR")
    if entry_out_dir:
        return os.path.join(entry_out_dir, "entry.txt")
    return "/output/entry.txt"


def emit_tagline(path):
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(TAGLINE + "\n")
    print(TAGLINE)


def main():
    emit_tagline(pick_entry_path())


if __name__ == "__main__":
    main()
