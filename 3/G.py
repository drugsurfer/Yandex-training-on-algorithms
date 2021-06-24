N = int(input())
turtle = set()
for i in range(N):
    a, b = map(int, input().split())
    if (a + b == N - 1) and ((a, b) not in turtle) and a >= 0 and b >= 0:
        turtle.add((a, b))
print(turtle)
print(len(turtle))