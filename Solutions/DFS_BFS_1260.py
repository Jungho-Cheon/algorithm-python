from collections import deque


def DFS(node):
    visit = list()
    need_visit = deque()
    need_visit.append(node)
    while need_visit:
        visit_node = need_visit.pop()
        if visit_node in visit:
            continue
        need_visit.extend(reversed(node_data[visit_node]))
        visit.append(visit_node)
        print(visit_node, end=' ')
    print()


def BFS(node):
    visit = list()
    need_visit = deque()
    need_visit.append(node)
    while need_visit:
        visit_node = need_visit.popleft()
        if visit_node in visit:
            continue
        need_visit.extend(node_data[visit_node])
        visit.append(visit_node)

    for i in visit:
        print(i, end=' ')
    print()


N, M, V = map(int, input().split())
node_data = dict()
for _ in range(M):
    A, B = map(int, input().split())
    if A in node_data:
        node_data[A].append(B)
        node_data[A].sort()
    else:
        node_data[A] = [B]
    if B in node_data:
        node_data[B].append(A)
        node_data[B].sort()
    else:
        node_data[B] = [A]


DFS(V)
BFS(V)
