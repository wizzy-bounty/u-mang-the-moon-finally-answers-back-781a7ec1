import os

LINE = "I have heard every wish, howl, and midnight promise; your follow-through is still in its darkest phase."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as entry_file:
        entry_file.write(LINE)


if __name__ == "__main__":
    main()
