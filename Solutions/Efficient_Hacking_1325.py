# 정점의 수가 많을경우 BFS로 구현하는 것이 효과적이다
from collections import deque


def BFS(node):
    q = deque([node])
    visited = [False] * (N + 1)
    visited[node] = True
    count = 1
    while q:
        v = q.popleft()
        for e in array[v]:
            if not visited[e]:
                q.append(e)
                visited[e] = True
                count += 1
    return count


N, M = map(int, input().split())
array = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    array[B].append(A)


MAX = -1
result = []

for i in range(1, N + 1):
    c = BFS(i)
    if MAX < c:
        result = [i]
        MAX = c
    elif MAX == c:
        result.append(i)

for i in result:
    print(i, end=" ")
print()
