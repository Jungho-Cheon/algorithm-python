import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        cur = heapq.heappop(scoville)
        if cur >= K:
            break
        else:
            if scoville:
                next_ = heapq.heappop(scoville)
                heapq.heappush(scoville, cur + (next_ * 2))
            else:
                return -1
        answer += 1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
