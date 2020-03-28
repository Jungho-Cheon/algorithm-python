# 1) Pivot 선텍 : 일반적으로 가장 앞에있는 값으로함.
# 2) Pivot보다 작은 갚은 앞으로 큰 값은 뒤로 보낸다.
# 3) Pivot을 기준으로 두개의 리스트로 쪼갠다.
# 4) 재귀적으로 나눠진 리스트의 크기가 1이될때 까지 반복
# 시간복잡도 : nlogn (logn 만큼의 depth, depth당 n번 비교), 만약 피봇이 계속해서 가장 작은값이거나 큰값인경우 depth가 n이기 떄문에 최악의 경우 n^2의 시간복잡도를 갖는다.

from random import randint


def Create_Rand_List(size):
    rand_list = set()
    while len(rand_list) != size:
        rand_list.add(randint(0, 1000))
    return list(rand_list)


def Quick_Sort(rand_list):
    if len(rand_list) <= 1:
        return rand_list

    pivot = rand_list[0]
    left = list()
    right = list()
    for item in rand_list[1:]:
        if pivot >= item:
            left.append(item)
        else:
            right.append(item)
    # left = [item for item in rand_list[1:] if pivot >= item]
    # right = [item for item in rand_list[1:] if pivot < item]

    return Quick_Sort(left) + [pivot] + Quick_Sort(right)


rand_list = Create_Rand_List(100)
print(rand_list)
rand_list = Quick_Sort(rand_list)
print(rand_list)
