inFile = open("input.txt", "r")
outFile = open("output.txt", "w")
dct = {}
for i in inFile.read().split('\n'):
    buyer, good, cnt = i.split()
    buyer += ':'
    if buyer not in dct.keys():
        dct[buyer] = {}
    if good not in dct[buyer].keys():
        dct[buyer][good] = 0
    dct[buyer][good] += int(cnt)
for i in sorted(dct.keys()):
    outFile.write(i + '\n')
    for j in sorted(dct[i].keys()):
        outFile.write(j + ' ' + str(dct[i][j]) + '\n')