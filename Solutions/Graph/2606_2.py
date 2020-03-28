# 바이러스
# BFS


def BFS(node):
    q = list([node])
    visit = [False] * (N + 1)
    count = 0
    while q:
        now = q.pop(0)
        if not visit[now]:
            visit[now] = True
            count += 1
            if edge[now]:
                q.extend(edge[now])
    return count - 1


N = int(input())
M = int(input())
edge = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    edge[A].append(B)
    edge[B].append(A)

print(BFS(1))
