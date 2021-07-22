n = input()
n = list(n)
parol = 0

if len(n) < 8:
    print('NO')
    exit()
else:
    parol += 1

for i in range(len(n)):
    if n[i] in '1234567890':
            parol += 1
            break

for i in range(len(n)):
    if n[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        parol += 1
        break

for i in range(len(n)):
        if n[i] in 'abcdefghijklmnopqrstuvwxyz':
            parol += 1
            break

if parol == 4:
    print('YES')
else:
    print('NO')