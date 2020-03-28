# 쿠르스칼 알고리즘
# 사이클이 생기면 안되기 때문에 union-find 알고리즘을 사용한다.
# 노드가 N개일 떄 존재할 수 있는 간선의 수 는 (N(N-1))/2 => O(n^2)


import math


def get_distance(A, B):
    x = A[0] - B[0]
    y = A[1] - B[1]
    return math.sqrt(x * x + y * y)


def find_parent(A):
    if parent[A] == A:
        return A
    p = find_parent(parent[A])
    parent[A] = p
    return parent[A]


def union_parent(A, B):
    A = find_parent(A)
    B = find_parent(B)
    if A < B:
        parent[B] = A
    else:
        parent[A] = B


def comp_parent(A, B):
    if find_parent(A) == find_parent(B):
        return True
    else:
        return False


N, M = map(int, input().split())
parent = {}
edge = []
locations = []

for _ in range(N):
    x, y = map(int, input().split())
    # (i번째점, x좌표, y좌표)
    locations.append((x, y))

# ** 가능한 모든 간선 구하기
for i in range(N - 1):
    for j in range(i + 1, N):
        edge.append((i + 1, j + 1, get_distance(locations[i], locations[j])))

# 부모 테이블 초기화
for i in range(1, N + 1):
    parent[i] = i

# 이미 존재하는 간선에 대해 union-find
for i in range(M):
    a, b = map(int, input().split())
    union_parent(a, b)

# 간선의 길이가 짧은 순서로 정렬
edge.sort(key=lambda x: x[2])
result = 0
# 존재할 수 있는 모든 간선에 대해서 짧은 길이의 간선부터 연결하고,
# comp_parent로 모든 간선의 부모가 같아지면 모두 연결된 것이므로 더 이상 연결하지 않는다.
for a, b, cost in edge:
    if not comp_parent(a, b):
        union_parent(a, b)
        result += cost

# 소숫점 두 자리까지 출력
print("%0.2f" % result)
