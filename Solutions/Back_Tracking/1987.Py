# 알파벳


def BFS(x, y):
    global result
    q = set()
    q.add((x, y, array[y][x]))
    while q:
        cx, cy, step = q.pop()
        # 최대로 갈 수 있는 거리
        result = max(result, len(step))
        for dx, dy in directions:
            new_x = cx + dx
            new_y = cy + dy
            if 0 <= new_x < C and 0 <= new_y < R and array[new_y][new_x] not in step:
                # new technique!
                # 최대 거리 측정을 위해 q에 들어가는 튜플의 3번째 인자를 string으로 사용한다.
                q.add((new_x, new_y, step + array[new_y][new_x]))


R, C = map(int, input().split())
array = [input() for _ in range(R)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
result = 0
BFS(0, 0)
print(result)
