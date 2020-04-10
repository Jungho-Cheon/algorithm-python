import random


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


MS = random.sample(range(0, 1000), 100)
MS = Merge_Sort(MS)
print(MS)
