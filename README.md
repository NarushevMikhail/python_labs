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

<h2>Задание B.</h2>
<img width="1828" height="1462" alt="image" src="https://github.com/user-attachments/assets/08d54569-a18d-4485-9d8a-4f39db51a737" />

<h2>Задание C.</h2>
<img width="1917" height="1015" alt="image" src="https://github.com/user-attachments/assets/b77397e6-ed71-45d0-8069-54598270c5cc" />
def format_record(s):
    if len(s) != 3:
        return 'ValueError'
    else:
        fuo = s[0].split()
        group = s[1]
        gpa = s[2]
        if type(s[2]) != float:
            return 'TypeError'
        else:
            if len(fuo) == 2:
                return f'{fuo[0]} {fuo[1][0]}., гр. {group}, GPA {gpa:.2f}'
            elif fuo[0] != fuo[0].title() and len(fuo) == 3:
                return f'{fuo[0].title()} {fuo[1][0].title()}.{fuo[2][0].title()}., гр. {group}, GPA {gpa:.2f}'
            elif fuo[0] != fuo[0].title() and len(fuo) == 2:
                return f'{fuo[0].title()} {fuo[1][0].title()}., гр. {group}, GPA {gpa:.2f}'
            else:
                return f'{fuo[0]} {fuo[1][0]}.{fuo[2][0]}., гр. {group}, GPA {gpa:.2f}'
    

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))




