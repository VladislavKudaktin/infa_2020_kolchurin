def IsPointInSquare(x, y, xc, yc, r):
    return (x - xc) ** 2 + (y - yc) ** 2 <= r ** 2
x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())
if IsPointInSquare(x, y, xc, yc, r):
    print("YES")
else:
    print("No")
