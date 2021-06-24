n = int(input())
points = []
for i in range(n):
    x, y  = map(int, input().split())
    points.append(y)
m = int(input())
road = []
for i in range(m):
    s, f = map(int, input().split())
    road.append((s, f))
height = [0] * n
inv_height = [0] * n
for i in range(1, n):
    height[i] = height[i - 1] + max(0, points[i] - points[i - 1])
    inv_height[n - 1 - i] = inv_height[n - i] + max(0, points[n - 1 - i] - points[n - i])

for i, j in road:
    if j >= i:
        print(height[j - 1] - height[i - 1])
    else:
        print(inv_height[j - 1] - inv_height[i - 1])