# Лабораторная работа №8
## Задание A `models.py`
<img width="2106" height="1433" alt="image" src="https://github.com/user-attachments/assets/17a9618f-14ca-41c8-8338-82208307ef8b" />
<img width="1546" height="685" alt="image" src="https://github.com/user-attachments/assets/40246fd7-a962-4004-afe6-1bada4328c3e" />

```
from dataclasses import dataclass
from datetime import date, datetime

@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self): #метод, который вызывается после создании объекта
        try:
            datetime.strptime(self.birthdate, "%Y/%m/%d") #преобразование строки в объект даты - время по заданному формату
        except ValueError:
            # (по-хорошему, тут должен быть raise ValueError(...))
            raise ValueError(f'birthdate format might be invalid: {self.birthdate}. Expected format: YYYY/MM/DD')
        if not (0 <= self.gpa <= 5):
            raise ValueError(f"gpa must be between 0 and 5, got {self.gpa}")

    def age(self) -> int:
        birth_day = datetime.strptime(self.birthdate, "%Y/%m/%d").date() #отбрасываем время. ((для времени: (%H:%M:%S)))
        today = date.today() #получение текущей даты
        if today.month > birth_day.month:
            return today.year - birth_day.year
        if today.month < birth_day.month:
            return today.year - birth_day.year - 1
        if today.day >= birth_day.day:
            return today.year - birth_day.year
        return today.year - birth_day.year - 1

    def to_dict(self) -> dict: #преобразование объекта в словарь
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod #используем, когда создаем новый объект
    def from_dict(cls, d: dict): #создание объекта из словаря
        # TODO: реализовать десереализацию из словаря
        return cls(
            fio = d["fio"],
            birthdate = d["birthdate"],
            group = d["group"],
            gpa = d["gpa"]
        )

    def __str__(self): #строковое представление
        # TODO: f"{}, {}, {}"
        return f"{self.fio}, {self.birthdate}, {self.group}, {self.gpa}"
    

#strftime = "string format time" (дата → строка)
#strptime = "string parse time" (строка → дата)
```

## Задание B `serialize.py`
<img width="1142" height="981" alt="image" src="https://github.com/user-attachments/assets/6b8ea08d-6732-40f5-bdd3-bef5ad7e9f63" />

```
import json, csv
import sys
from models import Student

def students_to_json(students, path):
    try:
        data = [s.to_dict() for s in students]
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        sys.exit(1) 


def students_from_json(path):
    with open(path, 'r', encoding = 'utf-8') as f:
        data = json.load(f)
        students = []
        for item in data: 
            try:
                student = Student.from_dict(item)
                students.append(student)
            except Exception as e:
                print(f"Допущена ошибка: {e}")
        return students
```

## Файл `main`
<img width="1267" height="648" alt="image" src="https://github.com/user-attachments/assets/dbf1ac96-4f68-4221-88cc-e0ee9e082f0f" />

```
from models import Student
from serialize import students_to_json, students_from_json

def main():
    s1 = Student("Иван Иванович Петрович", "2020/10/02", "HGHG", 3.5)
    s2 = Student("Иван Иванович", "2020/10/02", "HGHG", 4.5)
    s3 = Student("Иван Петрович", "2020/10/02", "HGHG", 2.0)
    print('Преобразую список объектов в Json...')
    students_to_json([s1, s2, s3], r"data\lab_08\students_output.json")
    print('Считываю студентов с файла Json...')
    cnt = 0
    for s in students_from_json(r"data\lab_08\students_input.json"):
        cnt += 1
        print(cnt,"Student:", s)

if __name__ == "__main__":
    main()
```

## Файл `Json для задания A`
<img width="843" height="774" alt="image" src="https://github.com/user-attachments/assets/924a3f9a-f8a7-48d8-b8f3-6be53085be51" />

## Вывод в термнале для задания B
<img width="737" height="781" alt="image" src="https://github.com/user-attachments/assets/1f51b1f6-6364-4ef6-b4f0-d4d96d6b464b" />

<img width="1019" height="134" alt="image" src="https://github.com/user-attachments/assets/afa16bd3-5936-453e-acda-5099ae3b3d6d" />
