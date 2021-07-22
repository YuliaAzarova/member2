n = int(input())
otvet = 0
for i in range(n):
    k = 0
    for j in range(2, i // 2+1):
        if (n % j == 0):
            k = k+1
    if (k <= 0):
        otvet += 1
print(otvet)