def exact_char():
    word = str(input('Enter the word: '))
    word = word.lower()
    substring = 'USA'
    wordcount = word.count(substring.lower())
    print('The USA count is: ',wordcount)
exact_char()