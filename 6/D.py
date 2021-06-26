def binsearch(a, b, w, h, n):
    start = 0
    end = w
    while start < end:
        mid = (start + end + 1) // 2
        if (w // (a + 2 * mid)) * (h // (b + 2 * mid)) >= n:
            start = mid
        else:
            end = mid - 1
    return start

n, a, b, w, h = map(int, input().split())
d1 = binsearch(a, b, w, h, n)
d2 = binsearch(b, a, w, h, n)
print(max(d1, d2))