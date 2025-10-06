<h1>Лаборатоная работа №1</h1>
<h2>Задание 1.</h2>
<img width="1985" height="445" alt="image" src="https://github.com/user-attachments/assets/6eae8287-75c5-4285-a683-45588fe2c06f" />

<h2>Задание 2.</h2>
<img width="1783" height="618" alt="image" src="https://github.com/user-attachments/assets/3ae5b6ae-9a1b-44fd-baff-6826b76c82de" />

<h2>Задане 3.</h2>
<img width="1807" height="729" alt="image" src="https://github.com/user-attachments/assets/b7f95065-7a10-4549-8f53-9d04b61fd2c6" />

<h2>Задание 4.</h2>
<img width="1756" height="559" alt="image" src="https://github.com/user-attachments/assets/26913c08-807d-44eb-ad3c-f176958eda4c" />

<h2>Задание 5.</h2>
<img width="1805" height="583" alt="image" src="https://github.com/user-attachments/assets/f5cf663f-a79e-4647-8e57-d348c08d026f" />


<h1>Лабораторная работа №2</h1>
<h2>Задане 1.</h2>
<img width="1929" height="1494" alt="image" src="https://github.com/user-attachments/assets/e1bb232a-7191-45ca-9979-5dcf559e6428" />
<div>Функция min_max возвращает минимальный и максимальный элемент из списка, если список пустой, то ValueError. Следущая функция unique_sorted, которая возвращает отсортированный список, в котором все элементы уникальны. В последней функции проверям сначала, что матрица не рванная, иначе вернется ValueError, затем тип эллементов в списки, если хотя бы один из них не int, то возвращаем TypeError. В рузультате работы данной программы переменные возвращаются одним списком.</div>

def min_max(s):
    if len(s) == 0:
        return 'ValueError'
    else:
        return min(s), max(s)

def unique_sorted(s):
    return sorted(set(s))

def flatten(s):
    task3 = []
    if len(s) == 0:
        return 'ValueError'
    else:
        for x in s:
            for i in x:
                if type(i) != int:
                    return 'TypeError'
                else:
                    task3.append(i)
        return task3


print('')
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42, 42]))
print(min_max([-5, -2, -9]))
print(min_max([]))
print(min_max([1.5, 2, 2.0, -3.1]))
print('')
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))
print('')
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))

<h2>Задание B.</h2>
<img width="1828" height="1462" alt="image" src="https://github.com/user-attachments/assets/08d54569-a18d-4485-9d8a-4f39db51a737" />


<h2>Задание C.</h2>
<img width="1917" height="1015" alt="image" src="https://github.com/user-attachments/assets/b77397e6-ed71-45d0-8069-54598270c5cc" />



