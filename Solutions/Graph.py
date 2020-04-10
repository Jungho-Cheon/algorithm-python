# 1) 무방향 그래프
# 2) 방향 그래프
# 3) 가중치 그래프
# 4) 연결 그래프(무방향 그래프이면서 모두 연결되어있음)와 비연결 그래프
# 5) 사이클과 비순환 그래프(사이클이 없는 연결 그래프)
# 6) 완전 그래프(그래프의 모든 노드가 서로 연결되어 있는 그래프)

# 딕셔너리와 리스트로 그래프릂 표현한다.
graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']


# 너비 우선 탐색 (BFS - Breadth-First Search)
# 시간복잡도는 간선의 수 + 노드의 수이다. O(V+E)
def BFS(graph, start_node):
    # 방문정보를 가진 큐를 만든다. (리스트 사용)
    visited = list()
    need_visit = list()

    need_visit.append(start_node)
    while need_visit:
        # pop(0) : 맨앞의 값을 pop하여 queue처럼 사용
        node = need_visit.pop(0)
        # not in : 해당 값이 있는지 확인
        if node not in visited:
            visited.append(node)
            # list.extend([a ,b]) : 리스트의 마지막에 리스트를 이어 붙힌다.
            need_visit.extend(graph[node])

    return visited


# 깊이 우선 탐색 (DFS - Depth-First Search)
# 시간복잡도는 간선의 수 + 노드의 수이다. O(V+E)
# need_visit을 스택으로 사용.
def DFS(graph, first_node):
    visited = list()
    need_visit = list()

    need_visit.append(first_node)
    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            # list.reverse() : list의 순서를 바꾼다. 리스트를 반환하지는 않음
            # reversed(list) : 순서가 반대로된 list를 반환한다.
            need_visit.extend(reversed(graph[node]))

    return visited


BFS_list = BFS(graph, 'A')
print("BFS :", BFS_list)

DFS_list = DFS(graph, 'A')
print("DFS :", DFS_list)
