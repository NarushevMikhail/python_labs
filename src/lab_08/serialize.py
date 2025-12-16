import json, csv
import sys
from models import Student

def students_to_json(students, path):
    try:
        data = [s.to_dict() for s in students]
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2) #записывает файл Python в формате Json, запись кирилицы без escape, отсупы 2 пробела
    except Exception as e:
        sys.exit(1) 


def students_from_json(path):
    with open(path, 'r', encoding = 'utf-8') as f:
        data = json.load(f) #читает Json из файла и преобразует в Python объект
        students = []
        for item in data: 
            try:
                student = Student.from_dict(item)
                students.append(student)
            except Exception as e:
                print(f"Допущена ошибка: {e}")
        return students