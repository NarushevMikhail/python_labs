import csv, sys
from pathlib import Path
sys.path.append(r'C:\Users\narus\OneDrive\Рабочий стол\лабароторные работы\Программирование\репозиторий\python_labs-1\src\lab_08')
from models import Student

class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        if not self.path.exists():
            self.path.write_text("", encoding="utf-8") #записывается файл с пустой строчкой

    def _read_all(self):
        # TODO: реализовать чтение строк из csv 
        rows = []
        if self.path.stat().st_size > 0: #проверка, что файл не пустой
            with open(self.path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file) #преобразование каждой строчки в словарь
                for row in reader:
                    if 'gpa' in row: #есть ли gpa в словаре
                        try: 
                            row['gpa'] = float(row["gpa"]) #преобразование строчик с точкой в число
                        except (ValueError, TypeError): #строка не прилбразована в число или значение не строкового типа
                            row['gpa'] = 0.0 # значение по умолчанию при ошибке
                    rows.append(row)
        return rows


    def _write_all(self, rows): #запись всего в CSV файл
        with open(self.path, 'w', encoding='utf-8', newline = '') as file:
            if rows: #если списко не пустой
                writer = csv.DictWriter(file, fieldnames=rows[0].keys()) #создание объекта для записей, названия столбцов берутся из ключей первой строки
                writer.writeheader() #записываем сроку с заголовками
                writer.writerows(rows) #запись всех строк в файл
    
    def list(self):
        # TODO: реализовать метод list()
        rows = self._read_all()
        return [Student(**row) for row in rows] #создание объекта Student, распаковывая словарь
        

    def add(self, student: Student):
         # TODO: реализовать метод add()
         rows = self._read_all()

         student_dict = { #создаем словарь из данных атрибутов объекта Student
             'fio': student.fio,
             'birthdate': student.birthdate,
             'group': student.group,
             'gpa': student.gpa
         }

         rows.append(student_dict) 
         self._write_all(rows) #записываем обновленный список обратно в файл

    def find(self, substr: str):
        # TODO: реализовать метод find()
        rows = self._read_all()
        found_rows = [r for r in rows if substr.lower() in r["fio"].lower()] #поиск подстроки без учета регистра
        return [Student(**row) for row in found_rows]

    def remove(self, fio: str):
        # TODO: реализовать метод remove()
        rows = self._read_all()
        new_rows = [r for r in rows if r["fio"] != fio] #фильтруем список, оставляем тех, чьё фио не равно искомому

        if len(new_rows) != len(rows):
            self._write_all(new_rows)
            return True
        return False # студент не найден

    def update(self, search_fio: str, **fields): # **fields - словарь
        # TODO: реализовать метод update()
        rows = self._read_all()
        update = False

        for row in rows:
            if row["fio"] == search_fio:
                # Обновляем только допустимые поля
                for key, value in fields.items(): #перебор пар из переданных аргументов
                    if key in row:
                        row[key] = value
                updated = True
                break
        
        if updated:
            self._write_all(rows)
        return updated
    

if __name__ == "__main__":
    group = Group("data/lab_09/student.csv")
    
    student = Student("Нарушев Михаил", "2007/06/22", "БИВТ25-5", 4.0)
    
    print("1. Добавление студента...")
    group.add(student)
    
    print("\n2. Все студенты:")
    for s in group.list():
        print(f"{s.fio}, {s.group}, GPA: {s.gpa}")
    
    print("\n3. Поиск 'Peter':")
    results = group.find("Peter")
    for r in results:
        print(f"  Найден: {r.fio}")
    
    print("\n4. Обновление данных")
    group.update("Нарушев Михаил", fio="Иванов Иван", gpa=5.0)
    
    print("\n5. Удаление студента...")
    group.remove("Иванов Иван")
