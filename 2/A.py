numbers = [int(i) for i in input().split()]
flag = True
for i in range(len(numbers) - 1):
    if numbers[i] >= numbers[i + 1]:
        flag = False
if flag == True:
    print('YES')
else:
    print('NO')