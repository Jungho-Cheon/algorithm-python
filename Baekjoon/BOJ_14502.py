import copy

N, M = map(int, input().split())
B = [list(input().split()) for _ in range(N)]

direction = ((-1,0),(0, 1),(1,0),(0,-1))
virus = [] # 바이러스의 좌표
zeros = [] # '0'의 좌표

for i in range(N):
    for j in range(M):
        if B[i][j] == '2':
            virus.append((i, j))
        elif B[i][j] == '0':
            zeros.append((i, j))


def BFS(board):
    q = copy.deepcopy(virus)

    visit = [[False] * M for _ in range(N)]

    while q:
        cur = q.pop(0)
        
        visit[cur[0]][cur[1]] = True

        for dx, dy in direction:
            nx, ny = cur[0] + dx, cur[1] + dy
            if 0 <= nx < N and 0<= ny < M:
                if not visit[nx][ny] and board[nx][ny] == '0':
                    visit[nx][ny] = True
                    board[nx][ny] = '2'
                    q.append((nx, ny))

    ret = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == '0':
                ret += 1

    return ret


ck = [False] * len(zeros)
cur = []
result = -1
def find(size, idx):
    if size == 3:
        global result
        # 3개의 벽을 세운 board 생성
        board = copy.deepcopy(B)
        for dx, dy in cur:
            board[dx][dy] = '1'

        # 모든 바이러스를 퍼뜨린다.
        for v in virus:
            result = max(BFS(board), result)
            
        return 


    # '0'좌표들 중 3개의 조합
    for i in range(idx, len(zeros)):
        if ck[i]:
            continue
        ck[i] = True
        cur.append(zeros[i])
        find(size + 1, i)
        cur.pop()
        ck[i] = False

find(0, 0)
print(result)