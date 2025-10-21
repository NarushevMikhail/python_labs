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
<h1>Лабораторная работа №3</h1>
<h2>Задание text.py</h2>
<h3>Normalize</h3><div> Данная функция, для начала она приводит текст к нижнему регистру, затем заменяет все буквы 'ё' на 'е', только потом заменяет все управляющие символы (табуляции, переносы строк) на проблеы. После этого удаляем все лишние пробелы через split, оставляя только одинарные между словами.</div>
<h3>tokensize</h3><div>Используеn регулярные выражения, благодаря которым будет находится слова с дефисом. Возвращает список токенов.</div>
<h3>count_freq</h3><div>Использует Counter из collection, и чтобы вернул обычный словарь нужно использовать dict()</div>
<h3>top_n</h3><div>Сортирует слова по убываию частот, а при равенстве пол алфавиту</div>
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

<h2>Здание text_stats.py</h2>

<div>
    Импортируем sys, через который указываем путь до файла, затем из файла text Ипортируем функции, Объявляем основную функцию программы (main), которая принимает строку text для анализа. Потом в top5 сортируем слова по алфавиту, а затем в top_result по убыванию.
</div>

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
<img width="1590" height="664" alt="image" src="https://github.com/user-attachments/assets/d999179f-1c59-4c63-bf5e-f3cfe4b0b97a" />

### Пункт 2 + задание под звездочкой.
<img width="2047" height="1220" alt="image" src="https://github.com/user-attachments/assets/f7448d2f-00ac-4b0d-8acc-341f3f97020f" />

### Вывод
<img width="2138" height="773" alt="image" src="https://github.com/user-attachments/assets/c646df54-9d7e-4623-aa8c-8a5c13775764" />

### Папка с check.csv
<img width="852" height="306" alt="image" src="https://github.com/user-attachments/assets/5ed6f796-17c1-4480-8e87-8b4daef2f020" />









