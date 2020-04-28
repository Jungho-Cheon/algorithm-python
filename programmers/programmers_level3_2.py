# https://programmers.co.kr/learn/courses/30/lessons/42627
# 디스크 컨트롤러

import heapq


def solution(jobs):
    jobs.sort()
    answer = 0
    time = 0
    heap = []
    j = 0
    while (j < len(jobs) or heap):
        if (j < len(jobs) and time >= jobs[j][0]):
            heapq.heappush(heap, (jobs[j][1], jobs[j][0]))
            j += 1
            continue
        if heap:
            tmp = heapq.heappop(heap)
            time += tmp[0]
            answer += time - tmp[1]
        else:
            time = jobs[j][0]
    return answer // len(jobs)


print(solution([[0, 3], [1, 9], [500, 6]]))
