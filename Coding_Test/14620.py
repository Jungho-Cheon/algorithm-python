# 꽃길

# 구하고자 하는 좌표의 갯수가 3개로 고정되어있는 점에서 O(N^3)을 고려
# N <= 100 -> N^3 = 1,000,000


N = int(input())
arr = [[*map(int, input().split())] for _ in range(N)]


directions = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)]
cost_data = []

INF = 1e9
result = INF


def ck(lst):  # a, b, c
    ret = 0
    flow = []
    for flower in lst:
        x = flower // N
        y = flower % N
        if 0 < x < N - 1 and 0 < y < N - 1:
            for dx, dy in directions:
                # 범위 내의 좌표들을 모두 추가한 뒤 중복을 없애서 겹치는 경우를 따진다.
                flow.append((x + dx, y + dy))
                ret += arr[x + dx][y + dy]
        else:
            return INF

    # 한 좌표를 기준으로 5개의 방향백터를 더한 좌표들이 세 개의 씨앗 모두 들어간 경우 5 * 3
    if len(set(flow)) != 15:
        return INF
    return ret


# i, j, k는 각각 점을 의미
for i in range(N * N):
    for j in range(i + 1, N * N):
        for k in range(j + 1, N * N):
            result = min(result, ck([i, j, k]))

print(result)
