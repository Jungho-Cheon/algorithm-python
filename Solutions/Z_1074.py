def solution(N, A, B, value):
    if N <= 0:
        return value
    breadth = (2 ** (N - 1))
    add = (4 ** (N - 1))

    # 1사분면
    if x < breadth + A and y < breadth + B:
        return solution(N - 1, A, B, value)
    # 2사분면
    elif x < breadth + A and y >= breadth + B:
        return solution(N - 1, A, B + breadth, value + add)
    # 3사분면
    elif x >= breadth + A and y < breadth + B:
        return solution(N - 1, A + breadth, B, value + add * 2)
    # 4사분면
    else:
        return solution(N - 1, A + breadth, B + breadth, value + add * 3)


N, x, y = map(int, input().split())
print(solution(N, 0, 0, 0))
