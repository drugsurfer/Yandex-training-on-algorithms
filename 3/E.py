a = set([int(i) for i in input().split()])
num = set(map(int, input()))
c = len(num.difference(a))
if c == 0:
    print(0)
else:
    print(c)