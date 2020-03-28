# 평범한 배낭
# DP
# K가 주어졌을 때 0~K 까지 모든 무게에 대해서 가치를 잰다.
# DP[i][j] = 배낭에 넣은 물품의 무게 합이 j일 때 얻을 수 있는 최대 가치.


N, K = map(int, input().split())
DP = [[0] * (K + 1) for _ in range(N + 1)]


for i in range(1, N + 1):
    weight, value = map(int, input().split())
    for j in range(1, K + 1):
        if j < weight:
            DP[i][j] = DP[i - 1][j]
        else:
            DP[i][j] = max(DP[i - 1][j], DP[i - 1][j - weight] + value)

print(DP[N][K])
