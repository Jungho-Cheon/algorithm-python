import heapq

N, M = map(int, input().split())
books = [*map(int, input().split())]
books.sort()

left_q = []
right_q = []
MAX = 0
for i in books:
    # 음수인 경우
    if i < 0:
        heapq.heappush(left_q, i)
        MAX = max(MAX, -i)
    # 양수인 경우
    else:
        heapq.heappush(right_q, -i)
        MAX = max(MAX, i)

result = 0
while left_q:
    result += heapq.heappop(left_q)
    for _ in range(M - 1):
        if left_q:
            heapq.heappop(left_q)

while right_q:
    result += heapq.heappop(right_q)
    for _ in range(M - 1):
        if right_q:
            heapq.heappop(right_q)

# heapq는 min heap이기 때문에 max heap을 만들기 위해 음수로 push하고 pop결과에 -한다.
print((result * -2) - MAX)
