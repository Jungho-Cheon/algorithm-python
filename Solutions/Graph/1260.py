def DFS(node):
    visited = list()
    need_visit = list([node])
    while need_visit:
        cur_node = need_visit.pop()
        if cur_node not in visited:
            if cur_node in node_data:
                need_visit.extend(reversed(node_data[cur_node]))
            visited.append(cur_node)

    [print(v, end=' ') for v in visited if visited]
    print()


def BFS(node):
    visited = list()
    need_visit = list([node])
    while need_visit:
        cur_node = need_visit.pop(0)
        if cur_node not in visited:
            if cur_node in node_data:
                need_visit.extend(node_data[cur_node])
            visited.append(cur_node)
    [print(v, end=' ') for v in visited if visited]
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
