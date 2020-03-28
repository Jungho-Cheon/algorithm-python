import sys
import heapq


N = int(input())
array = []
for _ in range(N):
    heapq.heappush(array, int(sys.stdin.readline()))

while array:
    print(heapq.heappop(array))
