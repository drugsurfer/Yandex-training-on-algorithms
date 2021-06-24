N = int(input())
numbers = input().split()
for i in range(N):
    if numbers[i:] == numbers[i:][::-1]:
        print(i)
        print(*numbers[:i][::-1])
        break