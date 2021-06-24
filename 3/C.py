N, M = map(int, [i for i in input().split()])
a, b = [], []
for i in range(N):
    a.append(int(input()))
for i in range(M):
    b.append(int(input()))
a, b = set(a), set(b)
c = a.intersection(b)
print(len(c))
print(*sorted(c))
c = a.difference(b)
print(len(c))
print(*sorted(c))
c = b.difference(a)
print(len(c))
print(*sorted(c))