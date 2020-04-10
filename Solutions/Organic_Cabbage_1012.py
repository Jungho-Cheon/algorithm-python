import sys
sys.setrecursionlimit(100000)


def DFS(x, y):
    visit[y][x] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if new_x < 0 or M <= new_x or new_y < 0 or N <= new_y:
            continue
        if array[new_y][new_x] and not visit[new_y][new_x]:
            DFS(new_x, new_y)


T = int(input())
result = list()
for _ in range(T):
    # 농장의 가로, 세로, 배추의 갯수
    M, N, K = map(int, input().split())
    array = [[0] * M for _ in range(N)]
    visit = [[False] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        array[y][x] = 1

    count = 0
    # i => y, j => x
    for i in range(N):
        for j in range(M):
            if not visit[i][j] and array[i][j]:
                count += 1
                DFS(j, i)

    result.append(count)

for i in result:
    print(i)
