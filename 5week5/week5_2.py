a = int(input())
b = int(input())
if a < b:
    for tep in range(a, b + 1):
        print(tep, end=' ')
if a > b:
    for tep in range(a, b - 1, -1):
        print(tep, end=' ')
if a == b:
    print(a)
