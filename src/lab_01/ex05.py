fuo = input('ФИО:')
inizuals = fuo.split()
print(inizuals)
a1, a2, a3 = inizuals[0][0], inizuals[1][0], inizuals[2][0]
inizuals1 = ''.join(inizuals)

print(f'Инициалы: {a1}{a2}{a3}.')
print(f'Длина: {len(inizuals1)+2}')



