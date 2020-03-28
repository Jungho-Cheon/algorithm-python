# 전깃줄
# LIS
N = int(input())
arr = []
LIS = [1] * N

for _ in range(N):
    A, B = map(int, input().split())
    arr.append((A, B))

arr.sort()

max_length = 0
for i in range(1, N):
    for j in range(i):
        if arr[j][1] < arr[i][1] and LIS[j] >= LIS[i]:
            LIS[i] = LIS[j] + 1
    max_length = max(max_length, LIS[i])


print(N - max_length)
