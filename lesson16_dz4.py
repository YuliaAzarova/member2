a = int(input())
b = int(input())
def sum(a,b):
    if a > 0:
        return sum(a - 1, b + 1)
    else:
        return b

print(sum(a,b))