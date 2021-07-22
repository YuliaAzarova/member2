N = int(input())
if N % 1000 == 0:
    n = N // 1000
    if n % 2 == 0:
        print(1)
    else:
        print(2)