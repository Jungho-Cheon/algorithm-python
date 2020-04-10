# 블랙잭
from itertools import combinations

N, M = map(int, input().split())
array = list(map(int, input().split()))

result = 0
for i in combinations(array, 3):
    temp = sum(i)
    if result < temp and temp <= M:
        result = temp

print(result)
