N = int(input())
meters = [int(i) for i in input().split()]
maxm = meters.index(max(meters))
maxv = 0
for i in range(1, N - 1):
    if meters[i] % 10 == 5 and meters[i + 1] < meters[i] and maxm < i:
        if meters[i] > maxv:
            maxv = meters[i]
if maxv == 0:
    print(0)
else:
    k = 0
    for i in range(N):
        if meters[i] > maxv:
            k += 1
    print(k + 1)