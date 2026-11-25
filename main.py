import os

ENTRY = "I graded my own joke 9 out of 10, then disqualified myself for cheating and submitted it anyway."

# Gate (competition.yaml): /output/entry.txt is UTF-8, 1-200 chars, not only
# whitespace, one line. Enforced here so a bad entry can never be written.
assert 1 <= len(ENTRY) <= 200, "entry length out of gate"
assert ENTRY.strip(), "entry must not be only whitespace"
assert "\n" not in ENTRY, "entry must be a single line"

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
