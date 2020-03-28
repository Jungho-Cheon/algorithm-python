# 유기농 배추
import sys


def BFS(x, y):
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

    q = [(x, y)]
    while q:
        now = q.pop(0)
        if not visited[now[1]][now[0]]:
            visited[now[1]][now[0]] = True
            for dx, dy in directions:
                next_x = now[0] + dx
                next_y = now[1] + dy
                if 0 <= next_x < M and 0 <= next_y < N:
                    if array[next_y][next_x] == 1:
                        q.append((next_x, next_y))


test_case = int(sys.stdin.readline())
result = []
for _ in range(test_case):
    M, N, K = map(int, sys.stdin.readline().split())
    array = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        array[y][x] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and array[i][j] == 1:
                BFS(j, i)
                count += 1

    result.append(count)

[print(i) for i in result]
