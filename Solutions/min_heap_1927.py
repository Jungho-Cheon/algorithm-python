import heapq

# heapq.heappush()
# heapq.heappop()
# list를 heap구조로 사용하는 함수.

N = int(input())

heap = list()
result = list()

for _ in range(N):
    data = int(input())
    if data == 0:
        if heap:
            result.append(heapq.heappop(heap))
        else:
            result.append(0)
    else:
        heapq.heappush(heap, data)

for data in result:
    print(data)
