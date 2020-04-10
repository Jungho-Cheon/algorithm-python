# 유기농 배추
# Flood Fill
import sys
from collections import deque


def BFS(x, y, label):
    q = deque([(x, y)])
    visited[i][j] = True
    arr[y][x] = label
    while q:
        cur_x, cur_y = q.popleft()
        #print("**", cur_x, cur_y)
        for dx, dy in directions:
            new_x, new_y = cur_x + dx, cur_y + dy
            if 0 <= new_x < M and 0 <= new_y < N and not visited[new_y][new_x] and arr[new_y][new_x] == 1:
                arr[new_y][new_x] = label
                visited[new_y][new_x] = True
                q.append((new_x, new_y))


test_case = int(input())
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
result = []

for _ in range(test_case):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        arr[y][x] = 1

    #[print(i) for i in arr]

    count = 1
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and not visited[i][j]:
                BFS(j, i, count)
                #[print(i) for i in visited]
                count += 1

    result.append(count)
    [print(i) for i in arr]
[print(i - 1) for i in result]
