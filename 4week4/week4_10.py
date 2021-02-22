def sum():
    n = int(input())
    if n == 0:
        return n
    return n + sum()


print(sum())
