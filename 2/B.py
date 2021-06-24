last_num = int(input())
num = int(input())
pol = 0
otr = 0
nul = 0
while num != -2 * 10**9:
    if num - last_num > 0:
        pol += 1
    elif num - last_num < 0:
        otr += 1
    else:
        nul += 1
    last_num = num
    num = int(input())
if pol * otr * nul > 0:
    print('RANDOM')
elif pol > 0 and otr + nul == 0:
    print('ASCENDING')
elif otr > 0 and pol + nul == 0:
    print('DESCENDING')
elif pol * nul > 0 and otr == 0:
    print('WEAKLY ASCENDING')
elif otr * nul > 0 and pol == 0:
    print('WEAKLY DESCENDING')
elif nul > 0 and pol + otr == 0:
    print('CONSTANT')