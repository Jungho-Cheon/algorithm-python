# 1. 시작노드에서 도착노드까지 최단 거리를 구한다.
# 2. 마지막노드에서 시작노드까지 BFS를 수행하면서 (현재 노드까지의 최단 거리 = 이전 노드까지의 최단 거리 + 둘 사이의 거리)를 만족하는지 검사하여 최단 거리를 추적한다.
# 3. 최단 거리에 해당하는 간선을 기록한다. (dropped)
# 4. 최단 거리에 해당하는 간선을 피해 다시한번 최단 거리를 구한다.

from collections import deque
import heapq


INF = 1e9


def dijkstra(start):
    heap_data = []
    heapq.heappush(heap_data, (0, start))
    distance[start] = 0
    while heap_data:
        dist, now = heapq.heappop(heap_data)
        if distance[now] < dist:
            continue
        for i in adj[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost and not dropped[now][i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap_data, (cost, i[0]))


def BFS():
    q = deque()
    q.append(D)
    while q:
        now = q.popleft()
        if now == S:
            continue
        for prev, cost in reverse_adj[now]:
            if distance[prev] + cost == distance[now]:
                dropped[prev][now] = True
                q.append(prev)


while True:
    # N : 장소의 수 (0 ~ N-1)
    # M : 도로의 수
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    # S : 시작점
    # D : 도착점
    S, D = map(int, input().split())

    adj = [[] for _ in range(N)]
    reverse_adj = [[] for _ in range(N)]
    dropped = [[False] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        # U에서 V까지 가는 도로의 길이 P
        U, V, P = map(int, input().split())
        adj[U].append((V, P))
        reverse_adj[V].append((U, P))

    distance = [INF] * N
    dijkstra(S)
    BFS()
    distance = [INF] * N
    dijkstra(S)
    if distance[D] == 1e9:
        print(-1)
    else:
        print(distance[D])
