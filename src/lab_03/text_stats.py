import sys
sys.path.append(r'c:/Users/narus/OneDrive/Рабочий стол/лабароторные работы/Программирование/репозиторий/python_labs/python_labs-1/src/lib/')

from lab_03.text import normalize, tokenize, count_freq

def table(arr: list[tuple[str, int]], isTable: bool = True) -> str: #список кортежей, где каждый кортеж содержит в себе str, int
    if not arr: #если arr пустой
        return "(нет данных)"
    s = str()
    
def main(text: str):
    text = text.strip() #лишние пробелы в начале и конце
    tokens = normalize(text)
    tokens = tokenize(tokens)
    freqs = count_freq(tokens)
    total_words = len(tokens)
    unique_words = len(freqs)
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    top5 = sorted(freqs.items(), key=lambda x: x[0])
    top_result = sorted(top5, key=lambda x: x[1], reverse=True)
    print("Топ-5:")
    for i in top_result:
        print(f'{i[0]}: {i[1]}')

main(sys.stdin.buffer.read().decode('utf-8'))