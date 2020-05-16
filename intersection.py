def intersection():
    First_Set = {65, 42, 78, 83, 23, 57, 29}
    Second_Set = {67, 73, 43, 48, 83, 57, 29}
    Third_Set = set()
    for item in First_Set:
        if item in Second_Set:
            Third_Set.add(item)
    print(Third_Set)
    for ele in Third_Set:
        if ele in First_Set:
            First_Set.remove(ele)
    print(First_Set)
intersection()