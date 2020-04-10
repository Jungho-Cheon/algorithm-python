# 소수의 곱

# heap을 사용해서 현재 heap의 최소값을 리스트의 모든 값과 각각 곱해 다시 heap에 넣는다
# 중복의 경우 (2 * 3, 3 * 2)
# heap에서 나온 현재 값 % 리스트의 현재 값 == 0 일경우 반복문을 종료하여 중복 값을 힙에 넣지 않는다.

import heapq
from copy import deepcopy

K, N = map(int, input().split())
p_list = [*map(int, input().split())]
lst, ck = deepcopy(p_list), set()

heapq.heapify(p_list)
ith = 0

while ith < N:
    MIN = heapq.heappop(lst)

    # 중복 처리
    if MIN in ck:
        continue
    ith += 1
    ck.add(MIN)

    # 최소값에서 다시 리스트의 모든 값들을 한번 씩 곱한 값들을 heap에 추가한다.
    for i in p_list:
        value = MIN * i
        if value * i < 2 ** 31:
            heapq.heappush(lst, MIN * i)

        if value % i == 0:
            break

print(MIN)
