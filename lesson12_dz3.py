n = int(input())

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            if j % 2 == 1:
                print('*', end='')
            else:
                print('.', end='')
        else:
            if j % 2 == 1:
                print('.', end='')
            else:
                print('*', end='')
    print('')