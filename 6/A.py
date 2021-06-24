def binsearch(x, array):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if x == array[mid]:
            return 'YES'
        if x < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return 'NO'

n, k = map(int, input().split())
num1 = [int(i) for i in input().split()]
num2 = [int(i) for i in input().split()]
for i in range(len(num2)):
    print(binsearch(num2[i], num1))
