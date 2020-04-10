import random


def Random_List(size):
    random_list = set()
    while len(random_list) != size:
        random_list.add(random.randint(0, 100))
    random_list = list(random_list)
    return random_list


def Insertion_Sort(data):
    for i in range(1, len(data)):
        index = i
        while index != 0:
            j = index - 1
            if data[j] > data[index]:
                data[j], data[index] = data[index], data[j]
                index = index - 1
                j = j - 1
            else:
                break


def Check_Sort(data):
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            return False
    return True


random_list = Random_List(10)
Insertion_Sort(random_list)
print(Check_Sort(random_list))
