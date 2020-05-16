def fourth_char():
    List = [54, 44, 27, 79, 91, 41]
    element = List.pop(4)
    List.insert(2, element)
    List.append(element)
    print(List)
fourth_char()