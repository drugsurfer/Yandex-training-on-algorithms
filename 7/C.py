from heapq import heappop, heappush
n, d = map(int, input().split())
students = [int(i) for i in input().split()]
events = [0] * (n * 2)
for i in range(len(students)):
    events[2 * i] = (students[i], -1, i)
    events[2 * i + 1] = (students[i] + d, 1, i)
events.sort()
max_num = 0
heap = list(range(1, n + 1))
results = [0] * n
for x, event, num in events:
    if event == -1:
       next_num = heappop(heap)
       max_num = max(next_num, max_num)
       results[num] = next_num
    elif event == 1:
        now_num = results[num]
        heappush(heap, now_num)
print(max_num)
print(*results)