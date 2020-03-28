N, S, M = map(int, input().split())
adj, DP = [*map(int, input().split())], [S]
for i in adj:
    DP = [*set([j + i for j in DP if i + j <= M] + [j - i for j in DP if j - i >= 0])]
print(max(DP) if DP else -1)
