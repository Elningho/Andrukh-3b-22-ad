def two_min(list):
    min_1 = min_2 = float('inf')

    for value in list:
        if value < min_1:
            min_1, min_2 = value, min_1
        elif value < min_2:
            min_2 = value
    print(min_1, min_2)

list1 = [1, 8, 22, 19, 88, 5]
two_min(list1)