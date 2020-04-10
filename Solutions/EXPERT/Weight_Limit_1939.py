# 그래프의 탐색을 위해 BFS사용
# BFS는 두개의 큐를 사용해 구현한다. (visited, need_visit)


def BFS(c):
    need_visit = list()
    need_visit.append(start_node)
    visited = [False] * (N + 1)
    visited[start_node] = True
    while need_visit:
        node = need_visit.pop(0)
        for y, weight in adj[node]:
            # BFS 탐색에 조건문을 추가해 다음 경로로 가는 중량이 현재보다 작다면 탐색하지 않도록한다.
            if not visited[y] and c <= weight:
                visited[y] = True
                need_visit.append(y)
    # 조건을 만족하면서 end_node까지 도달했다면 True를 반환한다.
    return visited[end_node]


N, M = map(int, input().split())

# 경로에 대한 data
adj = list([[] for _ in range(N + 1)])


MIN = 1000000000
MAX = 1

for _ in range(M):
    A, B, weight = map(int, input().split())
    adj[A].append((B, weight))
    adj[B].append((A, weight))
    MIN = min(MIN, weight)
    MAX = max(MAX, weight)

start_node, end_node = map(int, input().split())

result = MIN

while(MIN <= MAX):
    mid = (MAX + MIN) // 2
    # BFS()를 만족할 경우 현재 중량이 통과 가능하므로 더 큰 중량으로 검증한다.
    if BFS(mid):
        result = mid
        MIN = mid + 1
    else:
        MAX = mid - 1

print(result)
