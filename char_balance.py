def char_balance(s1, s2):
    flag = True
    for char in s1:
        if char in s2:
            continue
        else:
            flag = False
    return flag
print('s1 and s2 are balanced')
char_balance('pynative', 'tive')




