dct = {}
N = int(input())
for i in range(N):
    word, syn = input().split()
    dct[word] = syn
x = input()
for i in dct.keys():
    if x == dct[i]:
        print(i)
    elif x == i:
        print(dct[i])