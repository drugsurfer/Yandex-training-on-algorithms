def binsearch(w, h, n):
    start = 0
    end = w * n
    while start < end:
        mid = (start + end) // 2
        if (mid // w) * (mid // h) >= n:
            end = mid
        else:
            start = mid + 1
    return start
w, h, n = map(int, input().split())
print(binsearch(w, h, n))