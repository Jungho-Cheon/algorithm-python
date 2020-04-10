# 소수의 곱
import heapq
from copy import deepcopy

K, N = map(int, input().split())
arr = [*map(int, input().split())]


lst = deepcopy(arr)
heapq.heapify(lst)
ck = set()

ist = 0
while ist < N:
    MIN = heapq.heappop(lst)
    if MIN in ck:
        continue
    ist += 1
    ck.add(MIN)
    for i in arr:
        value = i * MIN
        if value < 2 ** 32 and value not in ck:
            heapq.heappush(lst, value)
        if MIN % i == 0:
            break

print(MIN)
