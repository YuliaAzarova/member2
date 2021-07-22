a = 1
N = []
while a != 0:
    a = int(input())
    if a != 0:
        if a % 2 == 0:
            N.append(a)
print(sum(N))