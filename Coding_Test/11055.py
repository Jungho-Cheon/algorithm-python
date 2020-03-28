# 가장 큰 증가 부분 수열
from copy import deepcopy

N = int(input())
arr = [*map(int, input().split())]
inc = [1] * N
DP = deepcopy(arr)

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            DP[i] = max(DP[i], arr[i] + DP[j])

print(max(DP))
