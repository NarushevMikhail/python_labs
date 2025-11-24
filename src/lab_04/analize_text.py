from text import *
import sys


def main(text: str):
    text = text.strip()  # лишние пробелы в начале и конце
    tokens = normalize(text)
    tokens = tokenize(tokens)
    freqs = count_freq(tokens)
    total_words = len(tokens)
    unique_words = len(freqs)
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    top5 = sorted(freqs.items(), key=lambda x: x[0])
    n = 5
    top_result = sorted(top5, key=lambda x: x[1], reverse=True)[:n]
    print("Топ-5:")
    for i in top_result:
        print(f"{i[0]}: {i[1]}")
    sys.exit(1)
