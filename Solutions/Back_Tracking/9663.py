# N-Queen


def check(x):
    for i in range(x):
        if row[x] == row[i]:
            return False
        if abs(row[x] - row[i]) == x - i:
            return False
    return True


def solution(row_num):
    # 모든 행에 대해 접근했을 경우 가능한 경우이므로 결과 + 1
    if row_num == N:
        global result
        result += 1
    else:
        for i in range(N):
            row[row_num] = i
            if check(row_num):
                solution(row_num + 1)

    for i in range(N):




N = int(input())
# 각 행에 몇번째 열에 퀸이 있는지에 대한 배열
row = [0] * N
result = 0
solution(0)
print(result)
