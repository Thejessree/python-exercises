def letter_count():
    word = str(input('Enter the word: '))
    upper_count = 0
    lower_count = 0
    digit_count = 0
    symbol_count = 0

    for char in word:
        if char.islower():
            lower_count+=1
        elif char.isupper():
            upper_count+=1
        elif char.isnumeric():
            digit_count+=1
        else:
            symbol_count+=1
    print('lower character = ',lower_count, 'upper character = ',upper_count, 'digit count = ', digit_count, 'symbol count = ', symbol_count)

letter_count()

