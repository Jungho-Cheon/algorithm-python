# 2048 (easy)
# 4방향에 대해 처리하는 방식 대신 맵을 회전시키는 식으로 진행한다.
# Ex) 왼쪽으로만 움직이고 맵을 회전하여 위, 아래, 오른쪽을 구현한다.
from copy import deepcopy

N = int(input())
Board = [[*map(int, input().split())] for _ in range(N)]


def rotate_90(B, N):
    NB = deepcopy(B)
    for i in range(N):
        for j in range(N):
            NB[j][N - i - 1] = B[i][j]
    return NB


def convert(lst, N):
    # 인자로 넘어온 리스트에서 양수만 뽑는다.
    new_list = [i for i in lst if i]
    # 2 2 2 2
    #  -> 4 0 4 0
    for i in range(1, len(new_list)):
        if new_list[i - 1] == new_list[i]:
            new_list[i - 1] *= 2
            new_list[i] = 0
    # 또 한번 양수만 추출한다.
    new_list = [i for i in new_list if i]
    return new_list + ([0] * (N - len(new_list)))


def dfs(N, B, count):
    # 2차원 배열에서 최댓값을 추출하는 방법
    ret = max([max(i) for i in B])
    if count == 0:
        return ret

    for _ in range(4):
        X = [convert(i, N) for i in B]
        if X != B:
            ret = max(ret, dfs(N, X, count - 1))

        B = rotate_90(B, N)
    return ret


print(dfs(N, Board, 5))

