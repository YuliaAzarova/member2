n, m, x, y = map(int, input().split())
if n > m:
    long = n
    short = m
else:
    long = m
    short = n

range_long = long - x
range_short = short - y

if range_long > range_short:
    print(range_short - 1)
else:
    print(range_long - 1)