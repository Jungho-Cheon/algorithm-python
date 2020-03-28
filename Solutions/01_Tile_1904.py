# Dynamic Programming (DP)

# 점화식
# 1) N = 1, Output = 1 (1)
# 2) N = 2, Output = 2 (11, 00)
# 3) N = 3, Output = 3 (111, 100, 001)
# 4) N = 4, Output = 5 (1111 // 1100, 1001, 0011 // 0000)
# 5) N = 5, Output = 8 (11111, 00111, 10011, 11001, 11100, 00001, 00100, 10000)
# 6) N = 6, Output = 13


import sys

N = int(sys.stdin.readline())
A, B = 0, 1
result = 0
for _ in range(N):
    result = A + B
    A, B = B, result

print(result % 15746)
