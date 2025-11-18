import sys, argparse
sys.path.append(r'C:\Users\narus\OneDrive\Рабочий стол\лабароторные работы\Программирование\репозиторий\python_labs-1\src\lab_06')
sys.path.append(r'C:\Users\narus\OneDrive\Рабочий стол\лабароторные работы\Программирование\репозиторий\python_labs-1\src\lib')
from csv_xlsx import csv_to_xlsx
from json_csv import json_to_csv, csv_to_json
from cli_text import check_file

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd", required=True) #пользователь должен указать одну команду, без неё скрипт выдаст ошибку

    p1 = sub.add_parser("json2csv")
    p1.add_argument("--in", dest="input", required=True, help='Входной JSON файл')
    p1.add_argument("--out", dest="output", required=True, help='Выходной CSV файл')

    p2 = sub.add_parser("csv2json")
    p2.add_argument("--in", dest="input", required=True, help='Входной CSV файл')
    p2.add_argument("--out", dest="output", required=True, help='Выходной JSON файл')

    p3 = sub.add_parser("csv2xlsx")
    p3.add_argument("--in", dest="input", required=True, help='Входной CSV файл')
    p3.add_argument("--out", dest="output", required=True, help='Выходной XLSX файл')

    args = parser.parse_args()

    try:
        if args.cmd == 'json2csv':
            if not check_file(args.input):
                print(f'Ошибка: файл {args.input} не существует или недосутпен')
                return 1

            json_to_csv(args.input, args.output)
            print(f'Усешно: JSON --> CSV')

        elif args.cmd == 'csv2json':
            if not check_file(args.input):
                print(f'Ошибка: файл {args.input} не существует или недоступен')
                return 1

            csv_to_json(args.input, args.output)
            print(f'Успешно: CSV --> JSON')

        elif args.cmd == 'csv2xlsx':
            if not check_file(args.input):
                print(f'Ошибка: файл {args.input} не найжен или недоступен')
                return 1

            csv_to_xlsx(args.input, args.output)
            print(f'Успешгно: CSV --> XLSX')

        else:
            print(f'Ошибка: неизвестная команда')
            return 1
        
        return 0


    except Exception as e:
        print(f'Ошибка при конфертации: {str(e)}')
        sys.exit(1)


if __name__ == '__main__':
    sys.exit(main())
