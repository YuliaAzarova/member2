a, b = map(int, input().split())

if a > b:
    x = b
    while x != 0:
        if a % x == 0 and b % x == 0:
            print(x)
            exit()
        else:
            x -= 1
else:
    x = b
    while x != 0:
        if a % x == 0 and b % x == 0:
            print(x)
            exit()
        else:
            x -= 1