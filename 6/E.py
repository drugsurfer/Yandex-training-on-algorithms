def binsearch(a, b, c):
    start = 0
    end = a + b + c
    while start < end:
        mid = (start + end) // 2
        if (2 * a + 3 * b + 4 * c + 5 * mid) * 2 >= (a + b + c + mid) * 7:
            end = mid
        else:
            start = mid + 1
    return start

a, b, c = int(input()), int(input()), int(input())
print(binsearch(a, b, c))