n = int(input())
x = int(input())
y = int(input())
a = x * 100 + y
b = a + (a * n / 100)
r = int(b // 100)
k = int(b % 100)
print(r, k)
