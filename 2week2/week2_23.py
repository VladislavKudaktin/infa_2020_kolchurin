x = int(input())
max1 = x
max2 = -1
while (x):
    x = int(input())
    if x > max1:
        max2 = max1
        max1 = x
    elif x > max2:
        max2 = x
print(max2)
