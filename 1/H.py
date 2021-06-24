a, b, n, m = int(input()), int(input()), int(input()), int(input())
min1 = n + (n - 1) * a
max1 = n + (n + 1) * a
min2 = m + (m - 1) * b
max2 = m + (m + 1) * b

t1 = set(range(min1, max1 + 1))
t2 = set(range(min2, max2 + 1))

t = t1.intersection(t2)
if len(t) == 0:
    print(-1)
else:
    print(min(t), max(t))
