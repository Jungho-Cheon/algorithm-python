# 기본적인 백트래킹은 DFS나 BFS를 사용하여 알고리즘을 구현한다.
# 일반적으로 걸리는 시간 : DFS > BFS -> 스택구조를 사용하기 때문
# 퀸은 대각선, 상하좌우로 움직일 수 있다.

# 1) 각 행에대해 재귀적으로 접근한다.
# 2) 재귀의 한단계에서 for문을 통해 현재 행의 모든 열에 대해서 퀸을 둘 수 있는지 따진다
# 3) 가능하다면 다음 행으로 넘어간다.


def check(x):
    for i in range(x):
        # 같은 열에 퀸이 존재할 경우
        if row[x] == row[i]:
            return False
        # 대각선상에 존재할 경우
        if abs(row[x] - row[i]) == x - i:
            return False
    return True


def DFS(x):
    global result
    if x == N:
        result += 1
    else:
        for i in range(N):
            row[x] = i
            if check(x):
                DFS(x + 1)


N = int(input())
row = [0] * N
result = 0
DFS(0)
print(result)
