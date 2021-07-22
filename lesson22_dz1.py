schetchik = 1
vse_chisla = []
otvet = 0

while schetchik != 0:
    chisla = input()
    if int(chisla) == 0:
        schetchik = 0
    else:
        schetchik = 1
        vse_chisla.append(int(chisla))
for i in range(len(vse_chisla)):
    if vse_chisla[i] == 0:
        break
    if vse_chisla[-i] > vse_chisla[-i+1]:
        otvet += 1

print(otvet)