# Dynamic Programming
# 유명한 문제이니 기억할것!

# ex) N=4, K=7 인경우
# 0 ~ 7 까지 모든 무게의 경우의 수에 대하여 최대 가치를 구한다.
# 점화식
# D[i][j] = D[i-1][j] (if j < W[i]),
#           max(D[i-1][j], D[i-1][j-W[i]] + V[i]) (if j >= W[i])

N, K = map(int, input().split())
D = [[0] * (K + 1) for _ in range(N + 1)]


for i in range(1, N + 1):
    W, V = map(int, input().split())
    for j in range(1, K + 1):
        if j < W:
            D[i][j] = D[i - 1][j]
        else:
            D[i][j] = max(D[i - 1][j], D[i - 1][j - W] + V)


print(D[N][K])
