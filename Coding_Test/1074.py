def solution(N, R, C, value):
    if N == 0:
        return value
    mid = 2**(N - 1)
    adj = 4**(N - 1)
    result = 0
    if R < mid and C < mid:
        result = solution(N - 1, R, C, value)
    elif R < mid and mid <= C:
        result = solution(N - 1, R, C - mid, value + adj)
    elif mid <= R and C < mid:
        result = solution(N - 1, R - mid, C, value + adj * 2)
    else:
        result = solution(N - 1, R - mid, C - mid, value + adj * 3)

    return result


N, R, C = map(int, input().split())

print(solution(N, R, C, 0))
