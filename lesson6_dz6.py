A = int(input())
B = int(input())
AB = []


schetchik_A = (A + 1)// 2 * 2
schetchik_B = (B // 2) * 2 + 1

for i in range(schetchik_A, schetchik_B, 2):
    AB.append(i)
#print(str(AB).strip('[]'), end = ' ')
#print(str(AB))
for j in range(len(AB)):
    print(AB[j], end = ' ')