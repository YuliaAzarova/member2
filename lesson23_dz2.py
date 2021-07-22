num = input()
num = list(num)
chetnie = []
for i in range(len(num)):
    if int(num[i]) % 2 == 0:
        chetnie.append(int(num[i]))
if len(chetnie) == 0:
    print('NO')
else:
    print(min(chetnie))