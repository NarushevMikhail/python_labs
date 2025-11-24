import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
        ("  ", ""),
    ],
)
def test_normalize(source, expected):
    assert normalize(source) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello world test", ["hello", "world", "test"]),
        ("по-настоящему не круто", ["по-настоящему", "не", "круто"]),
        ("", []),
        ("  ", []),
        ("знаки, препинания! тест.", ["знаки", "препинания", "тест"]),
    ],
)
def test_tokenize(text, expected):
    assert tokenize(text) == expected


def test_count_freq_basic():
    tokens = ["apple", "banana", "apple", "carrot", "banana"]
    result = count_freq(tokens)
    expected = {"apple": 2, "banana": 2, "carrot": 1}
    assert result == expected


def test_count_freq_empty():
    assert count_freq([]) == {}


def test_top_n_basic():
    freq = {"apple": 5, "orange": 10, "carrot": 4, "ginger": 1}
    result = top_n(freq, 2)
    excepted = [("orange", 10), ("apple", 5)]
    assert result == excepted


def test_top_n_alfavit():
    freq = {"apple": 2, "pineapple": 2, "orange": 2}
    result = top_n(freq, 3)
    excepted = [("apple", 2), ("orange", 2), ("pineapple", 2)]
    assert result == excepted


def test_top_n_empty():
    assert top_n({}, 5) == []


def test_full_all():
    text = "Всем привет! Привет мир! Привет всем и каждому"
    normalized = normalize(text)
    tokens = tokenize(normalized)
    freq = count_freq(tokens)
    top_world = top_n(freq, 2)
    ####
    assert normalized == "всем привет! привет мир! привет всем и каждому"
    assert tokens == [
        "всем",
        "привет",
        "привет",
        "мир",
        "привет",
        "всем",
        "и",
        "каждому",
    ]
    assert freq == {"всем": 2, "привет": 3, "мир": 1, "и": 1, "каждому": 1}
    assert top_world == [("привет", 3), ("всем", 2)]
