n, m = map(int, input().split())
events = []
for i in range(n):
    a, b = map(int, input().split())
    events.append((min(a, b), -1))
    events.append((max(a, b), 1))
points = [int(i) for i in input().split()]
for i in range(m):
    events.append((points[i], 0, i))
events.sort()
ans = [0] * m
count = 0
for event in events:
    if event[1] == -1:
        count += 1
    elif event[1] == 1:
        count -= 1
    elif event[1] == 0:
        ans[event[2]] = count
print(*ans)