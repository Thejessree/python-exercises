def lower_upper():
    word = str(input('Enter first word: '))
    word = list(word)
    lower = []
    upper = []
    for char in word:
        if char.islower():
            lower.append(char)
        else:
            upper.append(char)
    out = lower + upper
    print(''.join(out))
lower_upper()