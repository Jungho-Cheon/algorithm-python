# 중량 제한
# 가능한 중량을 찾고자 한다.
# 하지만 중량은 10억으로 log단위의 시간복잡도를 가지는 알고리즘을 짜야한다.

from collections import deque


def BFS(c):
    q = deque([start])
    visited = [False] * (N + 1)
    visited[start] = True
    while q:
        node = q.popleft()
        for y, weight in adj[node]:
            #print(y, weight)
            if weight >= c and not visited[y]:
                visited[y] = True
                q.append(y)
    return visited[end]


N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
MIN = 1e9
MAX = 0

for _ in range(M):
    A, B, weight = map(int, input().split())
    adj[A].append((B, weight))
    adj[B].append((A, weight))
    MIN = min(MIN, weight)
    MAX = max(MAX, weight)

start, end = map(int, input().split())

result = MIN
while MIN <= MAX:
    mid = (MIN + MAX) // 2
    if BFS(mid):
        MIN = mid + 1
        result = mid
    else:
        MAX = mid - 1

print(result)
