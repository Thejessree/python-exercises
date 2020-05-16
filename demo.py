def middle_three_char():
    word = input('Enter the string: ')
    middleIndex = int(len(word) /2)
    middleThree = word[middleIndex-1:middleIndex+2]
    print(middleThree)
middle_three_char()