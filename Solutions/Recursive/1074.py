# Z


def solution(N, r, c, result):
    if N == 0:
        print(result)
        return
    mid = (2 ** N) / 2
    value = 4**(N - 1)
    # 1사분면
    if r < mid and c < mid:
        solution(N - 1, r, c, result)
    # 2사분면
    elif r < mid and c >= mid:
        solution(N - 1, r, c - mid, result + value)
    elif r >= mid and c < mid:
        solution(N - 1, r - mid, c, result + 2 * value)
    else:
        solution(N - 1, r - mid, c - mid, result + 3 * value)


N, R, C = map(int, input().split())
solution(N, R, C, 0)
