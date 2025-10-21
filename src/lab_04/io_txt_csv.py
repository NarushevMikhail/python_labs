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
            w.writerow(header) #записывет заголовок
        else:
            header = ['Слово', 'Частота'] #header - заголовок таблицы
            w.writerow(header)
        for r in rows: #rows - список, кортеж, строки с какой - то последовательностью
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