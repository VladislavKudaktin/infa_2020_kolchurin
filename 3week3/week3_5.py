from math import *
n = float(input())
if ((n / 0.5) % 1) == 0:
    print(ceil(n))
elif (n - int(n)) > 0:
    if (n - int(n)) > 0.5:
        print(ceil(n))
    if (n - int(n)) < 0.5:
        print(floor(n))
elif (n - int(n)) < 0:
    if (n - int(n)) > -0.5:
        print(ceil(n))
    if (n - int(n)) < -0.5:
        print(floor(n))
