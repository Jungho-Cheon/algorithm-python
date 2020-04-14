import heapq


def solution(stock, dates, supplies, k):
    answer = 0
    ds = []
    idx = 0
    while(stock < k):
        for i in range(idx, len(dates)):
            if dates[i] <= stock:
                heapq.heappush(ds, -supplies[i])
                idx += 1
            else:
                break
        stock -= heapq.heappop(ds)
        answer += 1

    return answer


print(solution(4, [4, 10, 15], [20, 5, 10], 30))
# 4, [4, 10, 15], [20, 5, 10], 30
