n = int(input())
b = tuple(range(n))
for i in range(1, n + 1):
    for j in range(1, len(b) + 1):
        if 0 < j <= i:
            print(j, end='')
    print()
