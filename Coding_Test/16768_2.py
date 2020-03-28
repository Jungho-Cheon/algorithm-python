# Mooto Mooyo
# DFS Version
# 동작 매커니즘을 파악 후 함수를 나눠 구현한다.


def new_array(N):
    return [[False for i in range(10)] for _ in range(N)]


N, K = map(int, input().split())
M = [list(input()) for _ in range(N)]
ck = new_array(N)
ck2 = new_array(N)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(x, y):
    ck[x][y] = True
    ret = 1
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if new_x < 0 or new_x >= N or new_y < 0 or new_y >= 10:
            continue
        if ck[new_x][new_y] or M[x][y] != M[new_x][new_y]:
            continue
        # if M[new_x][new_y] == '0':
            # continue
        ret += dfs(new_x, new_y)
    return ret


def dfs2(x, y, val):
    ck2[x][y] = True
    M[x][y] = '0'
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if new_x < 0 or new_x >= N or new_y < 0 or new_y >= 10:
            continue
        if ck2[new_x][new_y] or M[new_x][new_y] != val:
            continue
        dfs2(new_x, new_y, val)


def down():
    for i in range(10):
        tmp = []
        for j in range(N):
            if M[j][i] != '0':
                tmp.append(M[j][i])

        for j in range(N - len(tmp)):
            M[j][i] = '0'
        for j in range(N - len(tmp), N):
            M[j][i] = tmp[j - (N - len(tmp))]


while True:
    exist = False
    ck = new_array(N)
    ck2 = new_array(N)

    for i in range(N):
        for j in range(10):
            if M[i][j] == '0' or ck[i][j]:
                continue
            res = dfs(i, j)  # 갯수 새기
            #print(M[i][j], res)
            if res >= K:
                dfs2(i, j, M[i][j])  # 지우기
                exist = True
    if not exist:
        break
    down()  # 내리기

for i in M:
    print(''.join(i))
