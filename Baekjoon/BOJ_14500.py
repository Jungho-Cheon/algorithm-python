N, M = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(N)]
visit = [[False] * M for _ in range(N)]
S = []
Answer = 0
directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
# [print(i) for i in board]


def DFS(x, y, sum, depth):
    sum += board[x][y]

    if depth == 1:
        global Answer

        if sum > Answer:
            Answer = sum
        return

    S.append((x, y))
    visit[x][y] = True

    for i in range(len(S)):
        for dx, dy in directions:
            nx, ny = S[i][0] + dx, S[i][1] + dy
            if nx < 0 or N <= nx or ny < 0 or M <= ny:
                continue
            if not visit[nx][ny]:
                DFS(nx, ny, sum, depth - 1)

    S.pop()
    visit[x][y] = False

    return


for i in range(N):
    for j in range(M):
        DFS(i, j, 0, 4)
print(Answer)
