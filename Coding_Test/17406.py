# 배열 돌리기 4
# 회전은 방향 벡터를 사용한다.
from copy import deepcopy

N, M, K = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(N)]
Q = [[*map(int, input().split())] for _ in range(K)]
directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

ans = 10000


def value(arr):
    return min([sum(i) for i in arr])


def convert(arr, query):
    r, c, s = query
    r, c = r - 1, c - 1

    # deepcopy를 사용허여 기존의 값이 덮어씌워지는 것을 방지한다.
    new_arr = deepcopy(arr)
    for i in range(1, s + 1):
        # 오른쪽 대각선 위 첫번째 인덱스로 시작한다.
        cur_r, cur_c = r - i, c + i
        for dr, dc in directions:
            for d in range(i * 2):
                next_r, next_c = cur_r + dr, cur_c + dc
                new_arr[next_r][next_c] = arr[cur_r][cur_c]
                cur_r, cur_c = next_r, next_c

    return new_arr


def dfs(arr, query):
    if sum(query) == K:
        global ans
        ans = min(ans, value(arr))
        return

    for i in range(K):
        if query[i]:
            continue

        new_arr = convert(arr, Q[i])

        # 백트래킹
        query[i] = 1
        dfs(new_arr, query)
        query[i] = 0


# 비트 마스크
dfs(A, [0 for i in range(K)])


print(ans)
