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
        with json_file.open('r', encoding = 'utf-8') as f: #открытие файла для чтение
            data = json.load(f) #чтение и загрузка даных

    except json.JSONDecodeError as e:
        raise ValueError(f'Ошибка чтения JSON: {e}')
    
    if not data:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    
    if not isinstance(data, list): # проверяет, что данные должны быть списком
        raise ValueError("JSON должен содержать список объектов")
    
    if not all(isinstance(item, dict) for item in data): #проверяет что все элементы должны быть списком
        raise ValueError("Все элементы JSON должны быть словарями")
    
    all_keys = set()
    for item in data:
        all_keys.update(item.keys()) #добавляетт все элементы во множество

    if data:  #проврека данных
        first_item_keys = list(data[0].keys())
        remaining_keys = sorted(all_keys - set(first_item_keys)) #находит ключи которых нет в 1 элементе
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
            reader = csv.DictReader(f) # создание читателя который возвращает словари
            if reader.fieldnames is None: ## список заголовков CSV файла
                raise ValueError("CSV файл не содержит заголовка")
            
            data = list(reader) #преобразование всех строк в список словарей
            
    except Exception as e:
        raise ValueError(f"Ошибка чтения CSV: {e}")

    if not data:
        raise ValueError("Пустой CSV файл")

    try:
        with json_file.open('w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2) # запись данных в JSON файл, форматирование с отступами в 2 пробела, разрешение Unicode символов
    except Exception as e:
        raise ValueError(f"Ошибка записи JSON: {e}")

json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")
csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")

# from pathlib import Path

# ss = Path('src/test.py')
# print(type(ss).__name__)
