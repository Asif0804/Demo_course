def level2_9(list, index):
    try:
        result = list[index]
        print(result)
    except IndexError:
        print("Index is out of range.")


list = [1, 2, 3, 4, 5]

level2_9(list, 11)