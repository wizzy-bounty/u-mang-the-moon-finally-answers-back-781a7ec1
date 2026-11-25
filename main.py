import os

LINE = "I have heard every wish, howl, and midnight promise; your follow-through is still in its darkest phase."


def entry_path(out_dir: str) -> str:
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = entry_path(output_dir)
    with open(output_path, "w", encoding="utf-8", newline="") as entry_file:
        entry_file.write(LINE)


if __name__ == "__main__":
    main()
