# 가장 긴 증가하는 부분 수열 4
from copy import deepcopy

N, A = int(input()), [*map(int, input().split())]
ck = [1] * N
rev = [-1] * N

MAX, idx = 1, 0
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j] and ck[i] < ck[j] + 1:
            ck[i] = ck[j] + 1
            rev[i] = j
    if MAX < ck[i]:
        MAX = ck[i]
        idx = i

result = []
while True:
    result.append(A[idx])
    idx = rev[idx]
    if idx == -1:
        break

result.reverse()
print(MAX)
[print(i, end=' ') for i in result]
print()
