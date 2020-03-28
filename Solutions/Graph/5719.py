import heapq

INF = 1e9


def djik(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for e in adj[now]:
            cost = dist + e[1]
            if distance[e[0]] > cost and not dropped[now][e[0]]:
                distance[e[0]] = cost
                heapq.heappush(q, (cost, e[0]))

# 도착 노드인 D를 시작으로 역추적하여 최단경로를 등록한다.
def BFS():
    q = []
    q.append(D)
    while q:
        now = q.pop(0)
        if now == S:
            continue
        for prev, cost in reverse_adj[now]:
            if distance[prev] + cost == distance[now]:
                dropped[prev][now] = True
                q.append(prev)


while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    S, D = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    reverse_adj = [[] for _ in range(N + 1)]

    dropped = [[False] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        U, V, P = map(int, input().split())
        adj[U].append((V, P))
        reverse_adj[V].append((U, P))

    distance = [INF] * (N + 1)
    djik(S, D)
    BFS()
    distance = [INF] * (N + 1)
    djik(S, D)

    if distance[D] == INF:
        print(-1)
    else:
        print(distance[D])
