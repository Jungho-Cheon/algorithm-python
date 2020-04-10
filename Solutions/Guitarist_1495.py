N, S, M = map(int, input().split())
volume_adj = list(map(int, input().split()))

# 마지막 곡에서 가능한 볼륨을 모두 찾은 후 가장 큰 볼륨을 출력해야한다...

DP = [[False] * (M + 1) for _ in range(N + 1)]
DP[0][S] = True
for i in range(0, N):
    for j in range(M + 1):
        if DP[i][j]:
            if j + volume_adj[i] <= M:
                DP[i + 1][j + volume_adj[i]] = True
            if j - volume_adj[i] >= 0:
                DP[i + 1][j - volume_adj[i]] = True

result = -1
for v in range(M, -1, -1):
    if DP[N][v] and result < v:
        result = v
        break

print(result)
