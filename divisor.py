def divisor():
    num = int(input('Enter a number:'))
    listrange = range(1, num+1)
    divisorlist = []

    for number in listrange:
        if num%number == 0:
            divisorlist.append(number)

    print(divisorlist)

divisor()