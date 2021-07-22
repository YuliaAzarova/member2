n = int(input())
spisok = []
for i in range(n):
    element = input().split(' ')
    spisok.append(element)

print(spisok)
for i in range(len(spisok)):
    for j in range(len(spisok[i])):
        print(spisok[i][j], end = ' ')
    print()