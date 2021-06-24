N = int(input())
a = [int(i) for i in input().split()]
dct = dict((i + 1, a[i]) for i in range(N))
k = int(input())
push = [int(i) for i in input().split()]
for i in push:
    dct[i] -= 1
for i in dct.keys():
    if dct[i] < 0:
        print('YES')
    else:
        print('NO')