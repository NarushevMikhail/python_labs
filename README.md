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
<img width="2079" height="1354" alt="image" src="https://github.com/user-attachments/assets/e7c012b6-c62d-4bec-b07f-eb650ce7c551" />

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





