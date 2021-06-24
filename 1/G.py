N, K, M = map(int, input().split())
a = K % M
t = K - a
if t == 0:
    print(0)
else:
    print(((N - a) //  t) * (t // M))