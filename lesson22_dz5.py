children = input() # все росты детей,  (1)

Child = list(filter(lambda x : x.isdigit(),children.split())) # (2)

Child = list(map(int,Child)) # (3)

X = int(input()) # (5)

Child.append(X)
Child.sort(reverse = True) # (4)

max = len(Child)-1

for i in range(len(Child)): # (6)
    if Child[max-i] == X:
        print(max-i+1) # (7)
        break


#       К  О  Н  Е  Ц


# 1. Ввести строку                                              +
# 2. Разбить строку на числа                                    +
# 3. Ввести X - рост Пети                                             +
# 4. Отсортировать массив по убыванию                           +
#                                        +
# 6. Начинать искать X в массиве.                               +
# 7. При нахождении вычесть из длины массива найденную позиции
