# 가장 큰 정사각형

# ex)
# 1, 2, 3은 모두 1이며 블록을 위해 표현하면
# 1     1,2     1,2     2
# 1,3   1,2,3   1,2,3   2
# 1,3   1,2,3   1,2,3   2
# 3     3       3       ?
#
# DP[i][j] = min(DP[i-1][j], DP[i][j-1], DP[i-1][j-1]) + 1 (if A[i][j] == 1 else 0)


N, M = map(int, input().split())
A = [[0] * (M + 1) for _ in range(N + 1)]
DP = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(N):
    for idx, j in enumerate([*map(int, list(input()))]):
        A[i + 1][idx + 1] = j

MAX = 0
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if A[i][j]:
            DP[i][j] = min(DP[i - 1][j], DP[i][j - 1], DP[i - 1][j - 1]) + 1
            MAX = max(MAX, DP[i][j])

print(MAX ** 2)
