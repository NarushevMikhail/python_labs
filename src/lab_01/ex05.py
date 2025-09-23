fuo = input('ФИО:')
inizuals = fuo.split()
a1, a2, a3 = inizuals[0][0], inizuals[1][0], inizuals[2][0]
dlina = fuo.strip()

print(f'Инициалы: {a1}{a2}{a3}.')
print(f'Длина: {len(dlina)}')