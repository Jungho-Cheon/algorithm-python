def solution(citations):
    citations.sort(reverse=True)
    return max(map(min, enumerate(citations, start=1)))


print(solution([0, 1, 3, 5, 6]))
