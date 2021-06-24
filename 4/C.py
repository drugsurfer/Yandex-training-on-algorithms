inFile = open("input.txt", "r")
outFile = open("output.txt", "w")
a = []
dct = {}
for i in inFile.read().split('\n'):
    a += i.split()
for i in a:
    if i not in dct.keys():
        dct[i] = 0
    dct[i] += 1
max_count, max_word = 0, ''
for i in dct.keys():
    if dct[i] > max_count:
        max_count = dct[i]
        max_word = i
    elif dct[i] == max_count:
        if i < max_word:
            max_word = i
outFile.write(max_word)