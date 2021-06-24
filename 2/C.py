N = int(input())
numbers = [int(i) for i in input().split()]
x = int(input())
a = [abs(numbers[i] - x) for i in range(len(numbers))]
print(numbers[a.index(min(a))])