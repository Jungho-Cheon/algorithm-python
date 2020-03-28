# Longest Increase Subsequence - 가장 긴 증가하는 부분 수열

# 점화식
# D[i] = array[i]를 마지막으로 가지는 수열의 최대 길이.

N = int(input())
array = [[1] * N for _ in range(2)]
array[0] = list(map(int, input().split()))
result = 0


for i in range(N):
    lower = 0
    for j in range(i):
        if array[0][i] > array[0][j]:
            if lower < array[1][j]:
                lower = array[1][j]
    array[1][i] = lower + 1
    if result < array[1][i]:
        result = array[1][i]

print(result)
