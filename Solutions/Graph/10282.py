# 해킹
import heapq

INF = 1e9


def dijk(start):
    q = []
    # heapq 에 튜플이 들어간 경우 첫 번째 요소로 최소힙이 구현된다.
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in array[now]:
            # 누적 합을 구하여 distance 테이블의 값과 비교하여 더 작다면 값을 바꾼다.
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


test_case = int(input())

for _ in range(test_case):
    N, D, C = map(int, input().split())

    array = [[] for _ in range(N + 1)]
    distance = [INF] * (N + 1)

    for _ in range(D):
        A, B, S = map(int, input().split())
        array[B].append((A, S))

    dijk(C)

    count = 0
    max_distance = 0

    for i in distance:
        if i != INF:
            count += 1
            max_distance = max(max_distance, i)

    print(count, max_distance)
