# 효율적인 해킹
import sys
from collections import deque


def BFS(node):
    q = deque([node])
    visited = [False] * (N + 1)
    visited[node] = True
    count = 0
    while q:
        now = q.popleft()
        for e in edge[now]:
            if not visited[e]:
                visited[e] = True
                q.append(e)
                count += 1
    return count


N, M = map(int, input().split())
edge = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    edge[B].append(A)

result = []
MAX = -1
for i in range(1, N + 1):
    if edge[i]:
        c = BFS(i)
        if MAX < c:
            MAX = c
            result = [i]
        elif MAX == c:
            result.append(i)

for i in result:
    print(i, end=' ')
print()
