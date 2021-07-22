n = int(input())
count = 1

for i in range(3, n + 1, 2):
    # Здесь мы перебираем все числа до введёного
    # здесь же мы считаем простые числа
    marker = 1
    for j in range(3, i // 2 + 1, 2):
        # Здесь мы проверяем i на простоту
        if i % j == 0:
            marker = 0
            break
    if marker == 1:
        count += 1

print(count)