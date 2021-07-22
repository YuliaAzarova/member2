stepen = int(input())
schetchic = 1

if schetchic == stepen:
    print('YES')
    exit()
else:
    while schetchic != stepen:
        schetchic = schetchic * 2
        if schetchic == stepen:
            print('YES')
            exit()
        elif schetchic > stepen:
            print('NO')
            exit()