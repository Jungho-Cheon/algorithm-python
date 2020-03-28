tc = int(input())

res = 0


def getMaxPrice(x, y, cnt, sum_, price):
    if sum_ > C:
        return
    global res
    res = max(res, price)
    if cnt == M:
        return

    getMaxPrice(x, y+1, cnt+1, sum_ +
                board[x][y], price + (board[x][y] * board[x][y]))
    getMaxPrice(x, y+1, cnt+1, sum_, price)


def solve(x, y):
    global res
    res = 0
    getMaxPrice(x, y, 0, 0, 0)
    priceA = res

    priceB = 0
    second = y + M
    is_first = True
    for i in range(x, N):
        if is_first:
            is_first = False
            for j in range(second, N-M+1):
                res = 0
                getMaxPrice(i, j, 0, 0, 0)
                priceB = max(priceB, res)
        else:
            for j in range(N-M+1):
                res = 0
                getMaxPrice(i, j, 0, 0, 0)
                priceB = max(priceB, res)

    return priceA + priceB


for t in range(tc):
    N, M, C = map(int, input().split())
    board = [[*map(int, input().split())] for _ in range(N)]

    # print('**')
    # [print(i) for i in board]
    # print("--")

    maxAnswer = 0

    for i in range(N):
        for j in range(N - M + 1):
            maxAnswer = max(maxAnswer, solve(i, j))

    print("#{} {}".format(t+1, maxAnswer))
