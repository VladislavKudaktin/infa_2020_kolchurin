n = int(input())
a = 1
b = 0
while n != 0:
    if n >= a:
        a = n
        n = int(input())
    elif n <= a:
        a = a
        n = int(input())
print(a)
