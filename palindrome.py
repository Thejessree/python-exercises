def palindrome():
    string = str(input('Enter a string: '))
    reverse = string[::-1]

    if string == reverse:
        print('This is a palindrome')
    else:
        print('This is not a palindrome')

palindrome()