# 수빈이와 수열

N = int(input())
B = [*map(int, input().split())]
A = [0]
for i in range(N):
    cur = B[i] * (i + 1)
    A.append(cur - sum(A))

[print(i, end=' ') for i in A[1:]]
print()
