def sort_num(number):
    s = ''
    for i in number:
        if i >= '0':
            s += i
    if len(s) == 11:
        s = s[1:]
    elif len(s) == 7:
        s = '495' + s
    return s

num_ = sort_num(input())
num = [sort_num(input()), sort_num(input()), sort_num(input())]
for s in num:
    if num_[0:3] == s[0:3] and num_[3:] == s[3:]:
        print('YES')
    else:
        print('NO')