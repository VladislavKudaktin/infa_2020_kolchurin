x = 0
a = 0
x = int(input())
max = x
while(x):
    if x > max:
        max = x
        a = 1
    else:
        if x == max:
            a = a + 1
    x = int(input())
print(a)
