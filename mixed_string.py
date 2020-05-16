def mixed_String(s1, s2):
    s2 = s2[::-1]
    length_s1 = len(s1)
    length_s2 = len(s2)
    length = length_s1 if length_s1 > length_s2 else length_s2
    result = ' '

    for i in range(length):
        if i<length_s1:
            result = result + s1[i]
        if i<length_s2:
            result = result + s2[i]
    print(result)

mixed_String('pynative', 'website')





