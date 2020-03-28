N, M = map(int, input().split())
cx, cy, cdir = map(int, input().split())
board = [list(input().split()) for _ in range(N)]
visit = [[False] * M for _ in range(N)]
Answer = 0
directions = ((-1, 0), (0, 1), (1, 0), (0, -1))


def DFS(nDx, nDy, cdir):
    if not visit[nDx][nDy]:
        global Answer
        visit[nDx][nDy] = True
        Answer += 1

    is_find = False
    for d in range(1, 5):
        ndir = cdir - d if cdir - d >= 0 else cdir - d + 4

        nx, ny = nDx + directions[ndir][0], nDy + directions[ndir][1]
        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == '0' and not visit[nx][ny]:

                is_find = True
                DFS(nx, ny, ndir)
                break

    if not is_find:
        bx = nDx - directions[cdir][0]
        by = nDy - directions[cdir][1]
        if 0 <= bx < N and 0 <= by < M:
            if board[bx][by] == '1':
                return
            DFS(bx, by, cdir)


DFS(cx, cy, cdir)
print(Answer)
