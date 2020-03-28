# 바이러스

# Union-Find


def find(A):
    if parent[A] == A:
        return A
    p = find(parent[A])
    parent[A] = p
    return parent[A]


def union(A, B):
    A = find(A)
    B = find(B)
    if A != B:
        parent[B] = A
        count[A] += count[B]


N = int(input())
edge = int(input())

parent = [0] * (N + 1)
count = [1] * (N + 1)

for i in range(N + 1):
    parent[i] = i

for _ in range(edge):
    A, B = map(int, input().split())
    union(A, B)

print(count[find(1)] - 1)
