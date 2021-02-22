def rec():
    n = int(input())
    if n != 0:
        rec()
        print(n)
    else:
        print(0)


rec()
