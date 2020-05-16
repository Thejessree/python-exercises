import random

number = random.randint(1, 11)
guess = 0
count = 0
while guess != number and guess != 'exit':
    guess = input('What is your guess? ')

    if guess == 'exit':
        break
    guess = int(guess)
    count += 1

    if guess < number:
        print('Your guess is low')
    elif guess > number:
        print('Your guess is high')
    else:
        print('Your guess is correct')
        print("And it only took you",count,"tries!")

