i, j = map(int, input().split())
if i == j:
    print(99)
else:
    if min(i, j) == 99:
        print(98)
    else:
        print(min(i, j))