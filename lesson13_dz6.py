n = int(input())
spisok = []
schetchik = 1

for i in range(n):
    element = input().split(' ')
    spisok.append(element)

diagonal_general = diagonal_additional = 0

for i in range(n):
    for j in range(n):
        if i == j:
            diagonal_general += int(spisok[i][j])
        if j + 1 == n - i:
            diagonal_additional += int(spisok[i][j])
# print(diagonal_general)
# print(diagonal_additional)
if diagonal_general > diagonal_additional:
    print(1)
elif diagonal_general < diagonal_additional:
    print(2)
else:
    print(0)