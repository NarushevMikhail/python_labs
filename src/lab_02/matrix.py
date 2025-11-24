def transpose(s):
    if len(s) == 0:
        return []
    else:
        if any(len(x) != len(s[0]) for x in s):
            return "ValueError"
        else:
            return [list(x) for x in zip(*s)]


def row_sums(s):
    if any(len(x) != len(s[0]) for x in s):
        return "ValueError"
    else:
        return [sum(x) for x in s]


def col_sums(s):
    if any(len(x) != len(s[0]) for x in s):
        return "ValueError"
    else:
        return [sum(x) for x in zip(*s)]


print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))
print("")
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))
print("")
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
