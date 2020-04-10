# 카드 정렬하기
import heapq
import sys

N = int(input())
array = []
for _ in range(N):
    heapq.heappush(array, int(sys.stdin.readline()))

result = 0
while len(array) > 1:
    A = heapq.heappop(array)
    B = heapq.heappop(array)
    cur = A + B
    result += cur
    heapq.heappush(array, cur)

print(result)
