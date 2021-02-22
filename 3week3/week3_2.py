n = int(input())
i = 1
b = 0
while i <= n:
    a = float(1 / (i ** 2))
    i = i + 1
    b = b + a
print(float(b))
