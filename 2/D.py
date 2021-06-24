count = 0
numbers = [int(i) for i in input().split()]
for i in range(1, len(numbers) - 1):
    if numbers[i] > numbers[i + 1] and numbers[i] > numbers[i - 1]:
        count += 1
print(count)