<h1>Лаборатоная работа №1</h1>
<h2>Задание 1.</h2>
<img width="1985" height="445" alt="image" src="https://github.com/user-attachments/assets/6eae8287-75c5-4285-a683-45588fe2c06f" />

<h2>Задание 2.</h2>
<img width="1783" height="618" alt="image" src="https://github.com/user-attachments/assets/3ae5b6ae-9a1b-44fd-baff-6826b76c82de" />

<h2>Задане 3.</h2>
<img width="1807" height="729" alt="image" src="https://github.com/user-attachments/assets/b7f95065-7a10-4549-8f53-9d04b61fd2c6" />

<h2>Задание 4.</h2>
<img width="1756" height="559" alt="image" src="https://github.com/user-attachments/assets/26913c08-807d-44eb-ad3c-f176958eda4c" />

<h2>Задание 5.</h2>
<img width="1805" height="583" alt="image" src="https://github.com/user-attachments/assets/f5cf663f-a79e-4647-8e57-d348c08d026f" />


<h1>Лабораторная работа №2</h1>
<h2>Задане 1.</h2>
<img width="2331" height="1594" alt="image" src="https://github.com/user-attachments/assets/c4a0c045-612b-484f-8d35-8e6b3c2b76c6" />


<div>Функция min_max возвращает минимальный и максимальный элемент из списка, если список пустой, то ValueError. Следущая функция unique_sorted, которая возвращает отсортированный список, в котором все элементы уникальны. В последней функции проверям сначала, что матрица не рванная, иначе вернется ValueError, затем тип эллементов в списки, если хотя бы один из них не int, то возвращаем TypeError. В рузультате работы данной программы переменные возвращаются одним списком.</div>

```
def min_max(s):
    if len(s) == 0:
        return 'ValueError'
    else:
        return min(s), max(s)

def unique_sorted(s):
    return sorted(set(s))

def flatten(s):
    task3 = []
    if len(s) == 0:
        return 'ValueError'
    else:
        for x in s:
            for i in x:
                if type(i) != int:
                    return 'TypeError'
                else:
                    task3.append(i)
        return task3

print('')
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42, 42]))
print(min_max([-5, -2, -9]))
print(min_max([]))
print(min_max([1.5, 2, 2.0, -3.1]))
print('')
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))
print('')
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))
```


<h2>Задание B.</h2>
<img width="2368" height="1551" alt="image" src="https://github.com/user-attachments/assets/92a4d08e-6f76-4c30-b509-cfa694fc5186" />
<div>В 1 функции проверяем матрицу на рваность, потом создаём новый список списков, внитри которого содержаться элементы с одиннаковыми индексами из исходной последователбности. В 2 функции делаем проверку матрицы на рваность, а затем возвращаем списко суммы элементов. В 3 функции проеврям матрицу на рваность, затем возвращаем сумму элементов с одинаковыми индексами из исходной последовательности. </div>

```
def transpose(s):
    if len(s) == 0:
        return []
    else:
        if any(len(x) != len(s[0]) for x in s):
            return 'ValueError'
        else:
            return [list(x) for x in zip(*s)]
        
def row_sums(s):
    if any(len(x) != len(s[0]) for x in s):
        return 'ValueError'
    else:
        return [sum(x) for x in s]

def col_sums(s):
    if any(len(x) != len(s[0]) for x in s):
        return 'ValueError'
    else:
        return [sum(x) for x in zip(*s)]

print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))
print('')
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))
print('')
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
```



<h2>Задание C.</h2>
<img width="2181" height="1380" alt="image" src="https://github.com/user-attachments/assets/70649d52-2a52-4228-861f-c8e87b492b1e" />
<div>Сначала проверяем длину кортежа s, она должна быть равной 3. Если GPA у нас не float, то возвращаем TypeError. Разбиваем ФИО через пробел, возвращаем через f строки фио группы и gpa</div>

```
def format_record(s):
    if len(s) != 3:
        return 'ValueError'
    else:
        fuo = s[0].split()
        group = s[1]
        gpa = s[2]
        if type(s[2]) != float:
            return 'TypeError'
        else:
            if len(fuo) == 2:
                return f'"{fuo[0]} {fuo[1][0]}., гр. {group}, GPA {gpa:.2f}"'
            elif fuo[0] != fuo[0].title() and len(fuo) == 3:
                return f'"{fuo[0].title()} {fuo[1][0].title()}.{fuo[2][0].title()}., гр. {group}, GPA {gpa:.2f}"'
            elif fuo[0] != fuo[0].title() and len(fuo) == 2:
                return f'"{fuo[0].title()} {fuo[1][0].title()}., гр. {group}, GPA {gpa:.2f}"'
            else:
                return f'"{fuo[0]} {fuo[1][0]}.{fuo[2][0]}., гр. {group}, GPA {gpa:.2f}"'
    

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
```
# Лабораторная работа №3
## Задание text.py
### `Normalize`
#### Данная функция, для начала она приводит текст к нижнему регистру, затем заменяет все буквы 'ё' на 'е', только потом заменяет все управляющие символы (табуляции, переносы строк) на проблеы. После этого удаляем все лишние пробелы через split, оставляя только одинарные между словами.
### `tokensize`
#### Используеn регулярные выражения, благодаря которым будет находится слова с дефисом. Возвращает список токенов.
### `count_freq`
#### Использует Counter из collection, и чтобы вернул обычный словарь нужно использовать dict()
### `top_n`
#### Сортирует слова по убываию частот, а при равенстве пол алфавиту
<img width="2079" height="1354" alt="image" src="https://github.com/user-attachments/assets/e7c012b6-c62d-4bec-b07f-eb650ce7c551" />
<img width="2138" height="657" alt="image" src="https://github.com/user-attachments/assets/ac461e27-9c18-4db5-ae52-0beb15e72c90" />

```
import re
from collections import Counter
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        translation_table = str.maketrans({
            'ё': 'е',
            'Ё': 'Е'
        })
        text = text.translate(translation_table)
    translation_table_controls = str.maketrans({
        '\t': ' ',
        '\r': ' ',
        '\n': ' ',
        '\v': ' ',
        '\f': ' ',
    })
    text = text.translate(translation_table_controls)
    text = ' '.join(text.split())

    return text

def tokenize(text: str) -> list[str]:
    pattern = r'\w+(?:-\w+)*'
    tokens = re.findall(pattern, text)
    return tokens

def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = Counter(tokens)
    return dict(freq)

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:n]
```

## Здание text_stats.py

#### Импортируем sys, через который указываем путь до файла, затем из файла text Ипортируем функции, Объявляем основную функцию программы (main), которая принимает строку text для анализа. Потом в top5 сортируем слова по алфавиту, а затем в top_result по убыванию.


<img width="2063" height="1272" alt="image" src="https://github.com/user-attachments/assets/ca22a8af-7f15-4ef0-b68f-8b7554001232" />
<img width="2397" height="269" alt="image" src="https://github.com/user-attachments/assets/f637973e-5260-4da9-a97f-fea30d43440f" />


```
import sys
sys.path.append(r'c:/Users/narus/OneDrive/Рабочий стол/лабароторные работы/Программирование/репозиторий/python_labs/python_labs-1/src/lib/')

from text import normalize, tokenize, count_freq

def table(arr: list[tuple[str, int]], isTable: bool = True) -> str:
    if not arr:
        return "(нет данных)"
    s = str()
    if isTable:
        word_col_width = max(len("слово"), max(len(a[0]) for a in arr))
        freq_col_width = max(len("частота"), max(len(str(a[1])) for a in arr))
        s += f"{'слово'.ljust(word_col_width)} | {'частота'.rjust(freq_col_width)}"
        s += "\n" + "-" * word_col_width + "-+-" + "-" * freq_col_width
        for word, freq in arr:
            s += f"\n{word.ljust(word_col_width)} | {str(freq).rjust(freq_col_width)}"
        return s
    else:
        return "\n".join(f"{a[0]}: {a[1]}" for a in arr)
def main(text: str):
    text = text.strip()
    tokens = normalize(text)
    tokens = tokenize(tokens)
    freqs = count_freq(tokens)
    total_words = len(tokens)
    unique_words = len(freqs)
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    top5 = sorted(freqs.items(), key=lambda x: x[1], reverse=True)[:5]
    print("Топ-5:")
    print(table(top5, True))

main(sys.stdin.buffer.read().decode())
```

# Лаборатрная работа №4 
## Задние A (text_io_py)
### Пункт 1.
#### функция `read text` - открывает файл на чтение в указанной кодировке и вовзращает содержимое, как одну строку. Если файл не найден поднимать FileNotFoundError, если кодировка не подходит, то поднимать UnicodeDecodeError. `Path` - путь к файлу, encoding - кодировка файла (по умолчанию utf-8). `p = Path(path)` - преобразует входной путь в стандартный для работы объект. Затем, try - чтение  файла, обрабатываем отсальные ошибки. 
<img width="1590" height="664" alt="image" src="https://github.com/user-attachments/assets/d999179f-1c59-4c63-bf5e-f3cfe4b0b97a" />

### Пункт 2 + задание под звездочкой.
#### `write_csv` - создать или перезаписать CSV с разделителем, если передан header записать его первой строкой, проверяем что каждая строка в rows имеет одиннаковую длину. `with p.open('w', newline="", encordeing='utf-8')` W - открываем файл для записи, newline - спец настройка для корректной работы с CSV. `w = csv.writter(f)` - создание объекта, который умеет записывать данные в CSV формате. Для каждой строки проверяем что на равна 2, если не так, то вызываем ошибку ValueError. `Parent_directory = os.path.dirname(path)` - получение родительской директории, возвращает путь к папке, где лежит файл. `os.makedirs` - создает все папки в пути, `exist_ok=True` - если папка уже существует, не вызывает ошибку. `if __name__=='__main__'` - код выполниться только если файл запущен на прямую.
<img width="2047" height="1220" alt="image" src="https://github.com/user-attachments/assets/f7448d2f-00ac-4b0d-8acc-341f3f97020f" />

### Вывод
<img width="2138" height="773" alt="image" src="https://github.com/user-attachments/assets/c646df54-9d7e-4623-aa8c-8a5c13775764" />

### Папка с check.csv
<img width="852" height="306" alt="image" src="https://github.com/user-attachments/assets/5ed6f796-17c1-4480-8e87-8b4daef2f020" />

```
import csv #модуль для работы с csv файлами
import os #модуль для работы с операционной системой 
from pathlib import Path
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    try:
        content = p.read_text(encoding=encoding)
        return content
    except FileNotFoundError:
        print(f'Ошибка: файл {p} не найден')
        return None
    except UnicodeDecodeError:
        print(f'Ошибка: Неверная кодировка. Должна быть {encoding}')
        return None
    
    
def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    p = Path(path) #path - куда сохранить файл
    rows = list(rows) #итерируемый объект, содержащий последовательности
    with p.open("w", newline="", encoding="utf-8") as f: #w - открыть файл для записи, mewline - настройка для работы с csv файлами
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        else:
            header = ['Слово', 'Частота'] #header - заголовок таблицы
            w.writerow(header)
        for r in rows:
            if len(r) == 2:
                w.writerow(r)
            else:
                raise ValueError('Разная длина строк.')

from collections import Counter

def frequencies_from_text(text: str) -> dict[str, int]:
    from lab_04.text import normalize, tokenize  # из ЛР3
    tokens = tokenize(normalize(text))
    return Counter(tokens)  

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))

def ensure_parent_dir(path: str | Path) -> None: # принимает путь, ничего не возвращает
    parent_directory = os.path.dirname(path)
    # получение родительской директории: os.path.dirname() возвращает путь к папке где лежит файл
    os.makedirs(parent_directory, exist_ok=True) # os.makedirs() - создает все папки в пути
    #exist_ok==True - если папки уже существуют, не вызывает ошибку

def test():
    print('пустой файл:', read_text(r"C:\Users\narus\OneDrive\Рабочий стол\лабароторные работы\Программирование\репозиторий\python_labs\python_labs-1\src\data\empty.txt"))
    print(read_text(r"C:\Users\narus\OneDrive\Рабочий стол\лабароторные работы\Программирование\репозиторий\python_labs\python_labs-1\src\data\emery.txt"))
    print(read_text(r"C:\Users\narus\OneDrive\Рабочий стол\лабароторные работы\Программирование\репозиторий\python_labs\python_labs-1\src\data\input.txt"))
    write_csv([("word","count"),("test",3)], r"C:\Users\narus\OneDrive\Рабочий стол\лабароторные работы\Программирование\репозиторий\python_labs\python_labs-1\src\data\check.csv") 
    write_csv(rows=[], path=r"C:\Users\narus\OneDrive\Рабочий стол\лабароторные работы\Программирование\репозиторий\python_labs\python_labs-1\src\data\check_empty.csv", header=None) 

if __name__ == "__main__": #если файл(name) запущен напрямую ("__main__")
    test()

```


## Здание B



### текст
#### импортируем модуль sys, который предоставляет доступ ко все файлам и объектам. Импортируем все функции из лабы 3, для обраотки и анализа текста. Затем читаем текст и выводим статистику в консоль.
<img width="1143" height="453" alt="image" src="https://github.com/user-attachments/assets/e492f17f-eee6-4c2e-8283-697ff1119fed" />

### вывод в терминале
<img width="1961" height="542" alt="image" src="https://github.com/user-attachments/assets/1a94b0e2-5026-4b74-9c3a-5e008b8462e8" />

### файл check_sv2
<img width="1069" height="883" alt="image" src="https://github.com/user-attachments/assets/5779daa1-3256-4020-a7c2-090913d03039" />

```
import sys
import os

sys.path.append(r'C:\Users\narus\OneDrive\Рабочий стол\лабароторные работы\Программирование\репозиторий\python_labs\python_labs-1\src') # импортирует модуль sys, который предоставляет доступ к объектам и функциям

from text import top_n, tokenize, normalize, count_freq
from analize_text import main
from io_txt_csv import read_text, write_csv


input_text = read_text(r'C:\Users\narus\OneDrive\Рабочий стол\лабароторные работы\Программирование\репозиторий\python_labs\python_labs-1\src\data\input_2.txt')
# читаем текст из указанного файла


normalized_text = normalize(input_text)
tokenized_words = tokenize(normalized_text)
freqs = count_freq(tokenized_words)
top_words = top_n(freqs, 5)

print(main(input_text))

write_csv(top_n(tokenize(normalize(input_text)), 20), path=r'C:\Users\narus\OneDrive\Рабочий стол\лабароторные работы\Программирование\репозиторий\python_labs\python_labs-1\src\data\check_sv2', header= ['WORD', 'COUNT'])
# нормализуем текст, разбиваем на слова, получаем топ-... слов
# write_csv(...) - записываем в CSV файл с заголовком ['WORD', 'COUNT'] и сохраняет файл

```
# Лабораторная работа №5

## Задание A — JSON ↔ CSV

### Преобразует JSON-файл в CSV. Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный. 

### `Функция json_to_csv(json_path, csv_path).`

Проверяет что исходный JSON файл существует
Убеждается что файл имеет правильное расширение (.json), читает JSON данные, проверяет что они - это список словарей, собирает все возможные ключи, создает CSV файл с заголовками и заполняет данными. Если в ходе работы возникают ошибки, то выводит их в теминал.

### `Функция csv_to_json(csv_path, json_path).`

Проверяет что исходный CSV файл существует
Убеждается, что файл имеет правильное расширение (.csv), затем считывает его используя первую строку как заголовки, преобразует строки в список словарей, сохраняет данные в JSON файл с красивым форматированием. Если есть ошибки, то выводит их в теринал.


### Примеры работы: 

### json -> csv:
<img width="681" height="197" alt="image" src="https://github.com/user-attachments/assets/f67f83ad-c4ca-40bd-bc87-589f415fdd0a" />
<img width="572" height="258" alt="image" src="https://github.com/user-attachments/assets/07e9eb64-a04f-4414-a49c-4512ce9662a9" />

### csv -> json
<img width="450" height="176" alt="image" src="https://github.com/user-attachments/assets/d361c70b-ad85-426d-8b89-29de5ca06dd6" />
<img width="874" height="580" alt="image" src="https://github.com/user-attachments/assets/677c5075-f7ab-4969-93ce-59660714ac1a" />


<img width="1845" height="1498" alt="image" src="https://github.com/user-attachments/assets/40876dce-879e-4873-a52f-e4a3532208db" />
<img width="1823" height="1440" alt="image" src="https://github.com/user-attachments/assets/26e60399-a519-486c-b454-f436fe2bb8e0" />
<img width="1225" height="202" alt="image" src="https://github.com/user-attachments/assets/6dcdcb15-3993-4cc2-88fb-ae621f6cce77" />


### Отработка ошибок:

#### Чтение файла json
<img width="1740" height="204" alt="image" src="https://github.com/user-attachments/assets/789c10f9-77fa-4cf6-bb08-1a9eb0918b9a" />

#### Чтение файла csv:
<img width="1622" height="195" alt="image" src="https://github.com/user-attachments/assets/e433a3e6-2f1a-4d73-8c8d-e27b87b99081" />

#### Файл не найден:
<img width="1476" height="177" alt="image" src="https://github.com/user-attachments/assets/6d45792b-f59a-4b24-ac03-0def3a011c4d" />

```
import json, csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    json_file = Path(json_path)
    csv_file = Path(csv_path)

    if not json_file.exists(): #exists - проверяет существует ли файл/директрия 
        raise FileNotFoundError(f'Файл {json_path} не найден')
    
    if json_file.suffix.lower() != '.json': #suffix - возвращает расширение файла
        raise ValueError('Неверный тип файла. Нужен .json')
    
    try:
        with json_file.open('r', encoding = 'utf-8') as f:
            data = json.load(f)

    except json.JSONDecodeError as e:
        raise ValueError(f'Ошибка чтения JSON: {e}')
    
    if not data:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список объектов")
    
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы JSON должны быть словарями")
    
    all_keys = set()
    for item in data:
        all_keys.update(item.keys())

    if data:
        first_item_keys = list(data[0].keys())
        remaining_keys = sorted(all_keys - set(first_item_keys))
        fieldnames = first_item_keys + remaining_keys
    else:
        fieldnames = sorted(all_keys)
    
    try: # Запись в CSV
        with csv_file.open('w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                complete_row = {key: row.get(key, '') for key in fieldnames}
                writer.writerow(complete_row)
    except Exception as e:
        raise ValueError(f"Ошибка записи CSV: {e}")

def csv_to_json(csv_path: str, json_path: str) -> None:
  
    csv_file = Path(csv_path)
    json_file = Path(json_path)
    
    if not csv_file.exists():
        raise FileNotFoundError(f"Файл {csv_path} не найден")

    if csv_file.suffix.lower() != '.csv':
        raise ValueError("Неверный тип файла. Ожидается .csv")
    
    try:
        with csv_file.open('r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            if reader.fieldnames is None:
                raise ValueError("CSV файл не содержит заголовка")
            
            data = list(reader)
            
    except Exception as e:
        raise ValueError(f"Ошибка чтения CSV: {e}")

    if not data:
        raise ValueError("Пустой CSV файл")

    try:
        with json_file.open('w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        raise ValueError(f"Ошибка записи JSON: {e}")

json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")
csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")

# from pathlib import Path

# ss = Path('src/test.py')
# print(type(ss).__name__)
```






## Задание B — CSV → XLSX

### Функция `csv_to_xlsx(csv_path, xlsx_path)`.
Проверяет существование CSV файла, убеждается что файл имеет правильное расширение (.csv), считывает все строки CSV в список, проверяет что файл не пустой, создает новую рабочую книгу (Workbook). Затем получает активный лист и задает ему название "Sheet1"Записывает все строки из CSV в Excel, сохраняет файл в формате XLSX

### файл CSV -> XLSX:
<img width="507" height="219" alt="image" src="https://github.com/user-attachments/assets/e59b8439-a772-4b76-a8dd-fb0624bcb1d3" />
<img width="558" height="194" alt="image" src="https://github.com/user-attachments/assets/f15f9391-4ebd-44db-94e6-41956048189a" />

### Отработака ошибок:

#### пустой файл
<img width="1089" height="244" alt="image" src="https://github.com/user-attachments/assets/a9b3be1b-774a-4bf3-894f-c6e68dbf8e7c" />

#### файл не найден
<img width="1426" height="219" alt="image" src="https://github.com/user-attachments/assets/1e396769-2493-4ad9-bf66-b320be659670" />




<img width="1773" height="1449" alt="image" src="https://github.com/user-attachments/assets/0805242c-fe86-4c8f-891c-f7ae1ff3ad8b" />
<img width="1344" height="827" alt="image" src="https://github.com/user-attachments/assets/df5aaabb-6c52-48a6-b775-c07affbaabe0" />

# Лабораторная работа №6
## `Файл cli_text.py`
### Код:
<img width="2075" height="1452" alt="image" src="https://github.com/user-attachments/assets/d2d43b80-9d93-4def-91af-20ec884aeb31" />
<img width="1874" height="1371" alt="image" src="https://github.com/user-attachments/assets/e13acbd4-c877-4f98-b1c4-faa92cae2253" />

### Вывод сторк с номерами (cat): `python src\lab_06\cli_text.py cat --input data\samples\people.csv -n`
<img width="1280" height="121" alt="image" src="https://github.com/user-attachments/assets/dd8a52ac-e488-4937-864c-368be574f7d1" />

### Вывод топ слов (stats): `python src\lab_06\cli_text.py stats --input data\samples\people.csv --top 8`
<img width="2335" height="420" alt="image" src="https://github.com/user-attachments/assets/cce7f4c0-9b2b-4951-b015-0614c0ded404" />

## `Файл cli_convert.py`
### Код:
<img width="2360" height="1484" alt="image" src="https://github.com/user-attachments/assets/b9aabb00-c368-44ef-92c8-e914a0eb0f54" />
<img width="2027" height="1174" alt="image" src="https://github.com/user-attachments/assets/77229187-3b76-487a-97bc-22cf850ea2c4" />

### JSON -> CSV

<img width="1280" height="116" alt="image" src="https://github.com/user-attachments/assets/5e6d6923-2204-4147-8506-875289869b47" />
<img width="1280" height="518" alt="image" src="https://github.com/user-attachments/assets/c6021fac-987b-4b91-b472-98948aa550fc" />
<img width="1280" height="481" alt="image" src="https://github.com/user-attachments/assets/bfb97099-1927-472f-8b09-74045c3d4101" />

### CSV -> JSON
<img width="1280" height="189" alt="image" src="https://github.com/user-attachments/assets/4b259645-31c8-44aa-810f-6e394ce46633" />
<img width="1280" height="382" alt="image" src="https://github.com/user-attachments/assets/2285c489-fe60-4e0e-b754-db6a0f9cc381" />
<img width="1280" height="562" alt="image" src="https://github.com/user-attachments/assets/4d4d5e71-bbf7-4220-8ea8-46004db96562" />

### CSV -> XLSX
<img width="1280" height="90" alt="image" src="https://github.com/user-attachments/assets/da479fb4-dc31-4c19-8fa3-480ac9786bf4" />
<img width="1181" height="490" alt="image" src="https://github.com/user-attachments/assets/55e34c50-6799-4e27-a397-ff7f4479c3ed" />
<img width="2042" height="633" alt="image" src="https://github.com/user-attachments/assets/e4d71534-2e32-4359-9650-96c9793da39d" />


### Отработка help
<img width="1280" height="654" alt="image" src="https://github.com/user-attachments/assets/37d058d0-b20e-4f09-9f89-6259065c699a" />


















