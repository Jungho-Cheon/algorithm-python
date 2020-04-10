# 쿠르스칼 알고리즘을 사용해서 최소 신장 트리(MST)를 구한다.
# 노드가 N개일때 존재할 수 있는 모든 간선의 수는 약 N^2이고
# 간선의 수가 N^2일때 쿠르스칼 알고리즘의 시간복잡도는 N^2 * log(N^2)이다
import math


def get_distance(p1, p2):
    a = p1[0] - p2[0]
    b = p1[1] - p2[1]
    return math.sqrt((a * a) + (b * b))

# 사이클이 존재하면 안되기 때문에 Union Find 알고리즘으로 부모를 확인한다.


def get_parent(parent, n):
    if parent[n] == n:
        return n
    return get_parent(parent, parent[n])


def union_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a == b:
        return True
    else:
        return False


edges = []
parent = {}
locations = []
N, M = map(int, input().split())


# 좌표
for _ in range(N):
    x, y = map(int, input().split())
    locations.append((x, y))

length = len(locations)


# 가능한 모든 간선을 구한다.
for i in range(length - 1):
    for j in range(i + 1, length):
        edges.append((i + 1, j + 1, get_distance(locations[i], locations[j])))

for i in range(1, N + 1):
    parent[i] = i

for i in range(M):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 간선들을 길이가 짧은순서로 정렬
edges.sort(key=lambda x: x[2])


# 쿠르스칼 알고리즘.. (가장 거리가 짧은 간선 순으로 선택한다. 다만 선택할 간선이 사이클을 만드는 경우 건너뛴다.)
result = 0
for a, b, cost in edges:
    if not find_parent(parent, a, b):
        union_parent(parent, a, b)
        result += cost

print("%0.2f" % result)
