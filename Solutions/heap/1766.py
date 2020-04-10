# 문제집
# 위상정렬 : 진입차수가 0인 노드를 먼저 방문한다.
import heapq


class Node:
    def __init__(self, value):
        self.value = value
        self.prenode = list()
        self.postnode = list()


def BFS(start_nodes):
    q = start_nodes
    while q:
        now = heapq.heappop(q)
        print(now, end=' ')
        for i in graph[now].postnode:
            graph[i].prenode.remove(now)
            if not graph[i].prenode:
                heapq.heappush(q, i)


N, M = map(int, input().split())
graph = [Node(i) for i in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[B].prenode.append(A)
    graph[A].postnode.append(B)

root = []
for i in range(1, N + 1):
    if not graph[i].prenode:
        root.append(i)

root.sort()
BFS(root)
print()
