n = int(input())

for i in range(n):
    for j in range(n):
        if n // 2 + 1 == i + 1:
            print('*', end=' ')
        elif n // 2 + 1 == j + 1:
            print('*', end=' ')
        elif i == j:
            print('*', end=' ')
        elif j + 1 == n - i:
            print('*', end=' ')
        else:
            print('.', end=' ')
    print()