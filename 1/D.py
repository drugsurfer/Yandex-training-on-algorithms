a, b, c = int(input()), int(input()), int(input())
if a != 0:
    x = (c ** 2 - b) / a
    if c >= 0 and x == int(x):
        print(int(x))
    else:
        print('NO SOLUTION')
else:
    if b ** (1/2) == c:
        print('MANY SOLUTIONS')
    else:
        print('NO SOLUTION')