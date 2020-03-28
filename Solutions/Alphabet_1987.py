def DFS(x, y):
    global result
    visited.add(array[y][x])
    result = max(result, len(visited))
    for dx, dy in direction:
        new_x = x + dx
        new_y = y + dy
        if 0 <= new_x < C and 0 <= new_y < R and array[new_y][new_x] not in visited:
            DFS(new_x, new_y)
    visited.remove(array[y][x])


def BFS(x, y):
    global result
    q = set()
    q.add((x, y, array[y][x]))
    while q:
        cx, cy, step = q.pop()
        result = max(result, len(step))
        for dx, dy in direction:
            new_x = cx + dx
            new_y = cy + dy
            if 0 <= new_x < C and 0 <= new_y < R and array[new_y][new_x] not in step:
                q.add((new_x, new_y, step + array[new_y][new_x]))


R, C = map(int, input().split())
array = [input() for _ in range(R)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = set()
result = 0
#DFS(0, 0)
BFS(0, 0)
print(result)
