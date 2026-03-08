import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)


def print_directory_structure(path, prefix=""):
    entries = sorted(path.iterdir(), key=lambda e: (e.is_file(), e.name))

    for index, entry in enumerate(entries):
        is_last = index == len(entries) - 1
        connector = "┗ " if is_last else "┣ "
        extension = "  " if is_last else "┃ "

        if entry.is_dir():
            print(f"{prefix}{connector}{Fore.BLUE}📂 {entry.name}")
            print_directory_structure(entry, prefix + extension)
        else:
            print(f"{prefix}{connector}{Fore.GREEN}📜 {entry.name}")


def main():
    if len(sys.argv) < 2:
        print("Використання: python task3.py /шлях/до/директорії")
        sys.exit(1)

    path = Path(sys.argv[1])

    if not path.exists():
        print(f"Шлях '{path}' не існує.")
        sys.exit(1)

    if not path.is_dir():
        print(f"'{path}' не є директорією.")
        sys.exit(1)

    print(f"{Fore.BLUE}📦 {path.name}")
    print_directory_structure(path)


if __name__ == "__main__":
    main()