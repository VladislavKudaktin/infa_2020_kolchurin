a = int(input())
b = int(input())
c = int(input())
if a >= b >= c or a >= c >= b:
    print(a)
elif b >= a >= c or b >= c >= a:
    print(b)
elif c >= a >= b or c >= b >= a:
    print(c)
