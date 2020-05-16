def even_odd():
    num = int(input('Give me a number:'))
    check = int(input('Give me a number to divide: '))
    if num % 4 == 0:
        print(num, 'is a divisible of 4')
    elif num % 2 == 0:
        print('Given number is even')
    else:
        print('Given number is odd')

    if num % check == 0:
        print(num, 'is evenly divided by check')
    else:
        print(num, 'is not evenly divided by check')
even_odd()