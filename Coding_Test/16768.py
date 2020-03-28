# Mooyo Mooyo
# BFS version
# * ISSUE : BFS 함수에서 ck를 바로 True로 바꾸지 않으면 탐색을 여러번할 수 있다.
#           방향 벡터에 대해서 큐에 삽입하기 전에 True로 바꿔서 중복되는 좌표들이 큐에 들어가지
#           않도록 한다.

from collections import deque

N, K = map(int, input().split())
arr = [list(input()) for _ in range(N)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def down():  # 내리기
    for i in range(10):
        tmp = []
        for j in range(N):
            if arr[j][i] != '0':
                tmp.append(arr[j][i])
        for j in range(N - len(tmp)):
            arr[j][i] = '0'
        for j in range(N - len(tmp), N):
            arr[j][i] = tmp[j - (N - len(tmp))]


def BFS1(x, y, val):  # 갯수 구하기
    q = deque([(x, y)])
    check = 0
    ck[y][x] = True
    while q:
        cur_x, cur_y = q.popleft()
        check += 1
        for dx, dy in directions:
            new_x, new_y = cur_x + dx, cur_y + dy
            if 0 <= new_x < 10 and 0 <= new_y < N:
                if not ck[new_y][new_x] and arr[new_y][new_x] == val:
                    ck[new_y][new_x] = True
                    q.append((new_x, new_y))
    return check


def BFS2(x, y, val):  # 지우기
    q = deque([(x, y)])
    ck2[y][x] = True
    while q:
        cur_x, cur_y = q.popleft()
        arr[cur_y][cur_x] = '0'
        for dx, dy in directions:
            new_x, new_y = cur_x + dx, cur_y + dy
            if 0 <= new_x < 10 and 0 <= new_y < N:
                if not ck2[new_y][new_x] and arr[new_y][new_x] == val:
                    ck2[new_y][new_x] = True
                    q.append((new_x, new_y))


while True:
    exist = False
    ck = [[False] * 10 for _ in range(N)]
    ck2 = [[False] * 10 for _ in range(N)]

    for i in range(N):
        for j in range(10):
            if arr[i][j] == '0' or ck[i][j]:
                continue
            ret = BFS1(j, i, arr[i][j])
            #print(arr[i][j], ret)
            if ret >= K:
                BFS2(j, i, arr[i][j])
                exist = True

    if not exist:
        break
    down()

for i in arr:
    print(''.join(i))
