N = int(input())
shirt = [int(i) for i in input().split()]
M = int(input())
pants = [int(i) for i in input().split()]

min_p, min_s = 0, 0
min = abs(shirt[min_s] - pants[min_p])
i, j = 0, 0
while i < len(shirt) and j < len(pants):
    s = abs(shirt[i] - pants[j])
    if s == 0:
        min_s, min_p = i, j
        break
    if s < min:
        min = s
        min_s, min_p = i, j
    if shirt[i] <= pants[j]:
        i += 1
    else:
        j += 1
print(shirt[min_s], pants[min_p])