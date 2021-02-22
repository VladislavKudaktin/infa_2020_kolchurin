n = int(input())
i = 2
if n >= 2:
    if n % i == 0:
        print(i)
    else:
        while n % i != 0:
            i = i + 1
            if n % i == 0:
                print(i)
else:
    print("NO")
