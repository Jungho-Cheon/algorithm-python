import heapq

N = int(input())
input_data = []
result = 0

for _ in range(N):
    heapq.heappush(input_data, int(input()))


while len(input_data) != 1:
    A = heapq.heappop(input_data)
    B = heapq.heappop(input_data)
    heapq.heappush(input_data, A + B)
    result += (A + B)

print(result)
