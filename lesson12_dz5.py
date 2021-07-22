H = int(input())

schetchik1 = 1
for i in range(H):
    for k in range(H-i-1):
        print(' ', end='')
    for j in range(schetchik1):
            print('*', end='')
    schetchik1 += 2
    if i == H-1:
        exit()
    print('\n')