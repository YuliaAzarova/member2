a = int(input())
b = int(input())

if a == b:
    if a % 2 == 1:
        print(a // 2 + 1, a)
    else:
        print(a // 2, a)
else:
    min_a = min(a, b)
    max_a = max(a, b)
    if max_a % 2 == 1:
        print(max_a // 2 + 1, min_a)
    else:
        print(max_a // 2, min_a)