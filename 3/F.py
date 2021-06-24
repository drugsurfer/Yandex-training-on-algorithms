genom1 = input()
genom2 = input()

g = set()
for i in range(len(genom2) - 1):
    g.add(genom2[i:i+2])
count = 0
for i in range(len(genom1) - 1):
    if genom1[i:i+2] in g:
        count += 1
print(count)