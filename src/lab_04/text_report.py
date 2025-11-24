import sys
import os

sys.path.append(
    r"C:\Users\narus\OneDrive\Рабочий стол\лабароторные работы\Программирование\репозиторий\python_labs\python_labs-1\src"
)  # импортирует модуль sys, который предоставляет доступ к объектам и функциям

from text import top_n, tokenize, normalize, count_freq
from analize_text import main
from io_txt_csv import read_text, write_csv


input_text = read_text(
    r"C:\Users\narus\OneDrive\Рабочий стол\лабароторные работы\Программирование\репозиторий\python_labs\python_labs-1\src\data\input_2.txt"
)
# читаем текст из указанного файла


normalized_text = normalize(input_text)
tokenized_words = tokenize(normalized_text)
freqs = count_freq(tokenized_words)
top_words = top_n(freqs, 5)

print(main(input_text))

write_csv(
    top_n(tokenize(normalize(input_text)), 20),
    path=r"C:\Users\narus\OneDrive\Рабочий стол\лабароторные работы\Программирование\репозиторий\python_labs\python_labs-1\src\data\check_sv2",
    header=["WORD", "COUNT"],
)
# нормализуем текст, разбиваем на слова, получаем топ-... слов
# write_csv(...) - записываем в CSV файл с заголовком ['WORD', 'COUNT'] и сохраняет файл
