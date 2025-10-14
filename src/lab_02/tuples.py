def format_record(s):
    if len(s) != 3:
        raise ValueError('Кортеж короче 3 элементов')
    else:
        fuo = s[0].split()
        group = s[1]
        gpa = s[2]
        if type(s[2]) != float:
            return 'TypeError'
        else:
            if len(fuo) == 2:
                return f'"{fuo[0]} {fuo[1][0]}., гр. {group}, GPA {gpa:.2f}"'
            elif fuo[0] != fuo[0].title() and len(fuo) == 3:
                return f'"{fuo[0].title()} {fuo[1][0].title()}.{fuo[2][0].title()}., гр. {group}, GPA {gpa:.2f}"'
            elif fuo[0] != fuo[0].title() and len(fuo) == 2:
                return f'"{fuo[0].title()} {fuo[1][0].title()}., гр. {group}, GPA {gpa:.2f}"'
            else:
                return f'"{fuo[0]} {fuo[1][0]}.{fuo[2][0]}., гр. {group}, GPA {gpa:.2f}"'
    

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("ABB-01", 3.999)))

# if isinstance(1, int)
# #1 объект который мы проверяем