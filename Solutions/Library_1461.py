import heapq


N, M = map(int, input().split())
books = list(map(int, input().split()))

books_left = []
books_right = []
max_length = max(max(books), -min(books))


# python에서 지원하는 heapq는 최소 힙이기 때문에 음수처리한 수 결과값에 음수처리를 다시한다.
for book in books:
    if book <= 0:
        heapq.heappush(books_left, book)
    else:
        heapq.heappush(books_right, -book)

result = 0

while books_left:
    result += heapq.heappop(books_left)
    for _ in range(M - 1):
        if books_left:
            heapq.heappop(books_left)

while books_right:
    result += heapq.heappop(books_right)
    for _ in range(M - 1):
        if books_right:
            heapq.heappop(books_right)

print(-result * 2 - max_length)
