# a, b, c, d, e = map(int, input().split())
N = [map(int, input().split())]
X = []
i = 0
while i != len(N):
    if '0123456789' in N[i]:
        X.append(N[i])
        X[i] = int(X[i])
    else:
       i += 1
print(min(X))