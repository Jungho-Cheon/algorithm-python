import heapq
import sys

N = int(input())
array = []
for _ in range(N):
    input_data = int(sys.stdin.readline())
    if input_data == 0:
        if not array:
            print(0)
        else:
            print(heapq.heappop(array))
    else:
        heapq.heappush(array, input_data)
