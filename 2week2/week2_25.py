n = int(input())
n1 = n
max = 1
while n != 0:
    n = int(input())
    count = 1
    while n == n1:
        count += 1
        n = int(input())
    if max < count:
        max = count
    n1 = n
print(max)
