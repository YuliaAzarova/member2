prostoe_chislo = current_chislo = 7
count = 4
while True: # (2)
    print(count)
    marker = 1
    current_chislo += 1
    for i in range(2, current_chislo // 2 + 1, 2): # (3)
        if (current_chislo % (i+1)) == 0: # (4)
            marker = 0
            break
    if marker == 1:
        prostoe_chislo = current_chislo
        count +=1
    if count == 1000000: # (6)
        print(current_chislo)
        break


# 1. Объявляем переменные+
# 2. Делаем глобальный цикл по количеству простых чисел (1млн)+
# 3. Берем число - current_chislo
# 4. Проверяем его на простоту
# 5. Если оно простое, сохраняем его в prostoe_chislo и
# увеличиваем счетчик (count) простых числен а один
# 6. Если счетчик простых чисел (count) равен 1млн,
# то выводим текущее число (current_chislo)
# 7. Если счетчик меньше 1млн,
# то увеличиваем текущее число на 1