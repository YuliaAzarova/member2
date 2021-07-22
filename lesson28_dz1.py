N = int(input())
if N % 9 != 0:
    n = N // 9 + 1
    if n % 2 == 0:
        print(2)
    else:
        print(1)
else:
    n = N // 9
    if n % 2 == 0:
        print(2)
    else:
        print(1)