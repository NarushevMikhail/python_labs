m = int(input('минуты:'))
hours = (m//60)
min = m % 60
print(f'{hours}:{min:02d}')