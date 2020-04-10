import random
import datetime


def Create_List(size):
    rand_list = set()
    while(len(rand_list) != size):
        rand_list.add(randint(0, 100))
    return list(rand_list)

# 이진 탐색은 데이터가 정렬되어있는 상태에서 진행한다.


def Binary_Search(data, search):
    print(data)
    if len(data) == 1 and data[0] == search:
        return True
    if len(data) == 1 and data[0] != search:
        return False
    if len(data) == 0:
        return False

    mid = len(data) // 2
    if data[mid] == search:
        return True
    else:
        if data[mid] > search:
            return Binary_Search(data[:mid], search)
        else:
            return Binary_Search(data[mid + 1:], search)


def Merge(left, right):
    merge_list = list()
    left_idx, right_idx = 0, 0

    # case 1 : left, right 둘 다 존재할 경우
    while len(left) > left_idx and len(right) > right_idx:
        if left[left_idx] < right[right_idx]:
            merge_list.append(left[left_idx])
            left_idx += 1
        else:
            merge_list.append(right[right_idx])
            right_idx += 1

    # case 2 : left혹은 right만 존재할 경우
    while len(left) > left_idx:
        merge_list.append(left[left_idx])
        left_idx += 1

    while len(right) > right_idx:
        merge_list.append(right[right_idx])
        right_idx += 1

    return merge_list


def Merge_Sort(data):
    if len(data) <= 1:
        return data
    med = len(data) // 2
    left = Merge_Sort(data[:med])
    right = Merge_Sort(data[med:])
    return Merge(left, right)


def Quick_Sort(rand_list):
    if len(rand_list) <= 1:
        return rand_list

    pivot = rand_list[0]
    left = [item for item in rand_list[1:] if pivot >= item]
    right = [item for item in rand_list[1:] if pivot < item]

    return Quick_Sort(left) + [pivot] + Quick_Sort(right)


random_list = random.sample(range(1000), 500)
test_sort = random_list
test_merge_sort = random_list
test_quick_sort = random_list

before = datetime.datetime.now()
test_sort.sort()
after = datetime.datetime.now()
print("sort() : ", after - before)

before = datetime.datetime.now()
Merge_Sort(test_merge_sort)
after = datetime.datetime.now()
print("Merge Sort : ", after - before)

before = datetime.datetime.now()
Quick_Sort(test_quick_sort)
after = datetime.datetime.now()
print("Quick Sort : ", after - before)
