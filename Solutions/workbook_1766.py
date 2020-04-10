# 순서가 정해져 있는 작업을 차례로 수행하기 위해 위상 정렬 알고리즘을 사용한다.
# 위상 정렬(Topology Sort)
# 1) 진입 차수가 0인 정점을 큐에 삽입한다.
# 2) 큐에서 원소를 꺼내 해당 원소롸 간선을 제거한다.
# 3) 제거 이후에 진입차수가 0이된 정점을 큐에 삽입한다.
# 4) 큐가 빈 상태가 될 때까지 2) ~ 3)을 반복한다.

# * 위상정렬에서는 사이클이 존재하면 안된다.
# - 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재하는 것이다.
# - 모든 원소를 방문했다면 큐에서 꺼낸 순서가 위상 정렬의 결과이다.

import heapq


N, M = map(int, input().split())
array = [[] for i in range(N+1)]
indegree = [0] * (N+1)

heap = []
result = []

for _ in range(M):
    x, y = map(int, input().split())
    array[x].append(y)
    indegree[y] += 1

for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

while heap:
    data = heapq.heappop(heap)
    result.append(data)
    for y in array[data]:
        indegree[y] -=1
        if indegree[y] == 0:
            heapq.heappush(heap, y)

for i in result:
    print(i, end= ' ')
