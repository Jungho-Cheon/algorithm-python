# 컵라면

import heapq

N = int(input())
deadlines = []
heap = []

for _ in range(N):
    A, B = map(int, input().split())
    deadlines.append((A, B))

deadlines.sort()

for i in range(N):
    heapq.heappush(heap, deadlines[i][1])
    # heap의 사이즈가 곧 현재 시간이다.
    if deadlines[i][0] < len(heap):
        # 정해진 데드라인보다 큰 값이 들어온 경우 컵라면의 수가 가장 작은 값을 pop한다.
        heapq.heappop(heap)

print(sum(heap))
