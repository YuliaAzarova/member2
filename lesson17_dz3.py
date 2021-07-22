n = 92
schetchik = count = 0

for i in range(10001, 100000, 2):
    x = 3
    while x != 93:
        if n % x == 0 and i % x == 0:
            break
        else:
            x += 1
    if x == 93:
        count += 1
print(count)