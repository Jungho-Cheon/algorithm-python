# APC

import sys

N, L, K = map(int, input().split())
arr = []
for i in range(N):
    sub1, sub2 = map(int, input().split())
    arr.append((sub1, sub2))

count = 0
result = 0
for i in range(N):
    if arr[i][1] <= L:
        result += 140
        count += 1
    if count == K:
        print(result)
        sys.exit()

for i in range(N):
    if arr[i][0] <= L < arr[i][1]:
        result += 100
        count += 1

    if count == K or L < arr[i][0]:
        print(result)
        break
