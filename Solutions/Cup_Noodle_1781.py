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
    if deadlines[i][0] < len(heap):
        heapq.heappop(heap)

print(sum(heap))
