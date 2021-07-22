num = input()
num = list(num)
for i in range(len(num)):
    if num[i] == num[i-1]:
        chetnie = 'YES'
        break
    else:
        chetnie = 'NO'
print(chetnie)