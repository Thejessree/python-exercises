import random

string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()'
options = list(range(10)) + list(string.letters)
passlen = 8
p = ''.join(map(random.sample(options, passlen)))
print(p)
