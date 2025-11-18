import sys

print("Это нормальное сообщение")  # stdout
print("Это ошибка", file=sys.stderr)  # stderr