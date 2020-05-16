def person_info():
    name = input('What is your name? ')
    age = int(input('What is your age? '))
    year = str((2020 - age)+100)

    print(name + ' will be turning 100 years old this year ' +year)

person_info()