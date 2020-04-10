# 다익스트라 알고리즘은 우선순위 큐를 사용한다. (heap으로 우선순위 큐 구현)
# 출발 정점으로부터 가장 가까운 정점으로 이동하면서 거리 테이블(distance)를 갱신한다.
import heapq

test_case = int(input())

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
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(heap_data, (cost, i[0]))


for _ in range(test_case):
    # N : 컴퓨터의 수
    # D : 의존성 개수
    # C : 해킹당한 컴퓨터의 번호
    N, D, C = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    distance = [INF] * (N + 1)

    for _ in range(D):
        # a -> b
        # s초 후 a도 감염
        a, b, s = map(int, input().split())
        adj[b].append((a, s))

    dijkstra(C)

    count = 0
    max_distance = 0

    for i in distance:
        if (i != INF):
            count += 1
            if i > max_distance:
                max_distance = i

    print(count, max_distance)
