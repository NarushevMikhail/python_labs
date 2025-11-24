import re
from collections import Counter


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        translation_table = str.maketrans({"ё": "е", "Ё": "Е"})
        text = text.translate(translation_table)
    translation_table_controls = str.maketrans(
        {
            "\t": " ",
            "\r": " ",
            "\n": " ",
            "\v": " ",
            "\f": " ",
        }
    )
    text = text.translate(translation_table_controls)
    text = " ".join(text.split())

    return text


def tokenize(text: str) -> list[str]:
    pattern = r"\w+(?:-\w+)*"
    tokens = re.findall(pattern, text)
    return tokens


def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = Counter(tokens)  # специальный объект Counter
    return dict(freq)  # преобразование в обычный словарь


def top_n(tokens, n=10):
    if isinstance(tokens, dict):
        freq = tokens
    else:
        freq = {}
        for token in tokens:
            freq[token] = freq.get(token, 0) + 1
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:n]
