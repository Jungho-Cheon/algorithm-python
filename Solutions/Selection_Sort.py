import random


def Random_List(size):
    random_list = set()
    while len(random_list) != size:
        random_list.add(random.randint(0, 100))
    random_list = list(random_list)
    return random_list

# 선택 정렬은 버블소트와 비슷하지만 최솟값을 찾아 정렬하는 알고리즘 O(n^2)


def Selection_Sort(data):
    for i in range(len(data) - 1):
        min = i
        for j in range(i + 1, len(data)):
            if data[min] > data[j]:
                min = j
        data[i], data[min] = data[min], data[i]


random_list = Random_List(5)
Selection_Sort(random_list)
print(random_list)
