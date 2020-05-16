def append_word():
    word1 = str(input('Enter first word: '))
    word2 = str(input('Enter second word: '))
    middle_index = int(len(word1)/2)
    appending = word1[:middle_index-1] + word2 + word1[middle_index-1:]
    print(appending)
append_word()