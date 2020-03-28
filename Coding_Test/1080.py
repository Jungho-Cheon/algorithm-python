# 행렬

# 3x3이 아닌 다른 유형의 문제가 많다.
# 첫번째 점을 시작으로 비교한다.

N, M = map(int, input().split())
A = [[*map(int, input())] for _ in range(N)]
B = [[*map(int, input())] for _ in range(N)]


def flip(x, y, A):
    for i in range(3):
        for j in range(3):
            A[x + i][y + j] ^= 1  # XOR


ans = 0

for i in range(0, N - 2):
    for j in range(0, M - 2):
        if A[i][j] != B[i][j]:
            # 뒤집어야 한다.
            flip(i, j, A)
            ans += 1

print(ans if A == B else -1)
