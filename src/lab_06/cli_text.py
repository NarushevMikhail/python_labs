import sys

sys.path.append(
    r"C:\Users\narus\OneDrive\Рабочий стол\лабароторные работы\Программирование\репозиторий\python_labs-1\src\lab_03"
)
from text_stats import stats
from pathlib import Path
import argparse
import os


def cat_command(input_file: str, number_lines: bool = False):
    if not check_file(input_file):
        sys.exit(1)
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            for line_number, line in enumerate(f, start=1):  # нумерация
                if number_lines:
                    print(f"{line_number:6d} {line}", end="")
                else:
                    print(line, end="")
    except Exception as e:
        print(f"Ошибка при чтение файла: {e}", file=sys.stderr)
        sys.exit(1)


def check_file(file_path: str) -> bool:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Файл: {path} не найден")
    if not path.is_file():
        raise ValueError(f"Файл: {path} не является файлом")

    return True


def stats_command(input_file: str, top_n: int = 5):
    if not check_file(input_file):
        sys.exit(1)

    if top_n <= 0:
        print(
            "Ошибка: значение --top должно быть положительным числом", file=sys.stderr
        )  # куда выводить ошибку, use for mistakes
        sys.exit(1)

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            text = f.read()
            stats(text, top_n)

    except (
        Exception
    ) as e:  # перехватывает другие ошибки, которые могли возникнуть во время работы D
        print(f"Ошибка при чтение файла: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == "cat":  # если пользователь ввел в командной строке cat
        cat_command(args.input, args.n)

    elif args.command == "stats":  # если пользователь ввел в командной строке stats
        stats_command(args.input, args.top)


if __name__ == "__main__":
    main()
