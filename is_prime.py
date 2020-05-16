def is_prime():

    num = int(input('Enter a number: '))
    isPrime = True
    for n in range(2, num):
        if num%n == 0:
            isPrime = False
            break

    print(isPrime)
is_prime()