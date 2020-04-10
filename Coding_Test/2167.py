# 2차원 배열의 합
# 시간복잡도가 매우 크다. -> 누적합으로 해결

# 2차원 배열에서의 누적합은 조금 특이하다.
# DP[i][j] = DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1] + A[i-1][j-1]
# A[i-1][j-1]은 DP[i][j]와 위치가 같다. (DP배열이 가로 세로 1 더 큼)

import sys

N, M = map(int, sys.stdin.readline().split())
A = [[*map(int, sys.stdin.readline().split())] for _ in range(N)]
DP = [[0] * (M + 1) for _ in range(N + 1)]
K = int(input())
for i in range(1, N + 1):
    for j in range(1, M + 1):
        DP[i][j] = DP[i - 1][j] + DP[i][j - 1] - DP[i - 1][j - 1] + A[i - 1][j - 1]

result = []
for _ in range(K):
    i, j, x, y = map(int, input().split())

    result.append(DP[x][y] - DP[i - 1][y] - DP[x][j - 1] + DP[i - 1][j - 1])

[print(i) for i in result]
