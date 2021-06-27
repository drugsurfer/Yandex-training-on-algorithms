n, m = map(int, input().split())
events = []
for i in range(m):
    b, e = map(int, input().split())
    events.append((b, -1))
    events.append((e, 1))
events.sort()
result = n
count_teach = 0
left, count = 0, 0
for event in events:
    if event[1] == -1:
        if count_teach == 0:
            left = event[0]
        count_teach += 1
    elif event[1] == 1:
        count_teach -= 1
        if count_teach == 0:
            result -= event[0] - left + 1
print(result)