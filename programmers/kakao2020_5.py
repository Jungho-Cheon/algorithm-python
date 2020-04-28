def solution(n, build_frame):
    board = [[-1] * (n + 1) for _ in range(n + 1)]

    for frame in build_frame:
        x, y, a, b = frame
        print(x, y, a, b)
        # 기둥인 경우
        if a == 0:
            # 삭제
            if b == 0:
                if board[x][y+1] == 0:
                    continue
                for i in range(1, x):
                    if board[i][y+1] == 1:
                        if board[i-1][y+1]
                board[x][y] = -1
            # 설치
            else:
                if y == 0:
                    board[x][y] = 0
                else:
                    if board[x][y-1] == 0 or board[x-1][y] == 1:
                        board[x][y] = 0

        # 보인 경우
        else:
            # 삭제
            if b == 0:

                # 설치
            else:

    return


print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [
      2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))


# 000000
# 000000
# 002222
# 021001
# 010001

# 000000 000000
# 000000 000000
# 001001 002222
# 011001 022000
# 010001 000000
