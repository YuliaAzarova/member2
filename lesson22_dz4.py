N = int(input())
n = 0
i = 0
while i != N:
    a = int(input())
    if a == 1:
        n += 1
        i += 1
    else:
        i += 1
print(n)