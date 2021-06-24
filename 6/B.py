def binsearch(x, array):
    start = 0
    end = len(array) - 1
    while start < end:
        mid = (start + end) // 2
        if array[mid] >= x:
            end = mid
        else:
            start = mid + 1
    return start

n, k = map(int, input().split())
num1 = [int(i) for i in input().split()]
num2 = [int(i) for i in input().split()]
for i in range(len(num2)):
    found = binsearch(num2[i], num1)
    if found == n:
        print(num1[found - 1])
    elif found == 0:
        print(num1[0])
    else:
        if num2[i] - num1[found - 1] <= num1[found] - num2[i]:
            print(num1[found - 1])
        else:
            print(num1[found])
