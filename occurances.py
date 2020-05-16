def occurances():
    word = str(input('Enter the word: '))
    countdict = dict()
    for char in word:
        count = word.count(char)
        countdict[char] = count
    print(countdict)
occurances()