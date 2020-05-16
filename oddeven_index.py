def oddeven_index():
    list1 = [3, 6, 9, 12, 15, 18, 21]
    list2 = [4, 8, 12, 16, 20, 24, 28]
    list3 = []

    for i in range(0, len(list1)):
        if i%2 != 0:
            list3.append(list1[i])
    for i in range(0, len(list2)):
        if i%2 == 0:
            list3.append(list2[i])
    print(list3)

oddeven_index()



