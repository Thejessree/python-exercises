def list_dict():
    rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
    sampleDict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}
    sample_list = []
    for item in rollNumber:
        if item in sampleDict.values():
            sample_list.append(item)
    print(sample_list)
list_dict()