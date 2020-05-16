def num_occur():
    a = [11, 45, 8, 11, 23, 45, 23, 45, 89]
    countdict = dict()

    for item in a:
        if item in countdict:
            countdict[item]+=1
        else:
            countdict[item] = 1
    print(countdict)
num_occur()