def remove_duplicate():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    result_overlap = [num for num in a if num in b]
    result = []

    for element in result_overlap:
        if element not in result:
            result.append(element)
remove_duplicate()

