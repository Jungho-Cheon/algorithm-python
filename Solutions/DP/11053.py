# 가장 긴 증가하는 부분수열

N = int(input())
array = [[1] * N for _ in range(2)]
array[0] = list(map(int, input().split()))

result = 0
for i in range(N):
    lower = 0
    for j in range(i):
        if lower < array[1][j] and array[0][i] > array[0][j]:
            lower = array[1][j]
    lower += 1
    array[1][i] = lower
    result = max(result, lower)

print(result)
