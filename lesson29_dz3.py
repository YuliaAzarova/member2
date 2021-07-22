N = input()
n_list = N.split('.')
print(n_list)
num = 0

if len(N) > 15:
    print(0)
    exit()

if len(n_list) != 4:
    print(0)
    exit()

for i in range(len(n_list)):
    if n_list[i] in '1234567890':
        num += 1
    elif n_list[i] == '':
        print(n_list[i])
        print(0)
        exit()
if num == 4:
    print(1)
else:
    print(0)