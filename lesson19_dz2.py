N = int(input())

if N > 10 or N == 10:
    desiatky = N // 10
    if N % 10 > 5 or N % 10 == 5:
        piateorky = N % 10 // 5
        if N % 10 % 5 > 2 or N % 10 % 5 == 2:
            dvoiky = N % 10 % 5 // 2
            if N % 10 % 5 % 2 == 1:
                edinitsa = 1
            else:
                edinitsa = 0
        else:
            if N % 10 % 5 % 2 == 1:
                edinitsa = 1
            else:
                edinitsa = 0
    else:
        if N % 10 % 5 > 2 or N % 10 % 5 == 2:
            dvoiky = N % 10 % 5 // 2
            if N % 10 % 5 % 2 == 1:
                edinitsa = 1
            else:
                edinitsa = 0
        else:
            if N % 10 % 5 % 2 == 1:
                edinitsa = 1
            else:
                edinitsa = 0
else:
    if N % 10 > 5 or N % 10 == 5:
        piateorky = N % 10 // 5
        if N % 10 % 5 > 2 or N % 10 % 5 == 2:
            dvoiky = N % 10 % 5 // 2
            if N % 10 % 5 % 2 == 1:
                edinitsa = 1
            else:
                edinitsa = 0
        else:
            if N % 10 % 5 % 2 == 1:
                edinitsa = 1
            else:
                edinitsa = 0
    else:
        if N % 10 % 5 > 2 or N % 10 % 5 == 2:
            dvoiky = N % 10 % 5 // 2
            if N % 10 % 5 % 2 == 1:
                edinitsa = 1
            else:
                edinitsa = 0
        else:
            if N % 10 % 5 % 2 == 1:
                edinitsa = 1
            else:
                edinitsa = 0
print(desiatky + piateorky + dvoiky + edinitsa)