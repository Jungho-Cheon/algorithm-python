from collections import deque


def BFS():
    visit = list()
    q = deque([1])
    while q:
        node = q.popleft()
        if node not in visit:
            visit.append(node)
            q.extend(network[node])
    print(len(visit) - 1)


def DFS():
    visit = list()
    stack = list([1])
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(reversed(network[node]))
    print(len(visit) - 1)


N = int(input())
M = int(input())
network = dict()
for _ in range(M):
    A, B = map(int, input().split())
    if A in network:
        network[A].append(B)
    else:
        network[A] = [B]
    if B in network:
        network[B].append(A)
    else:
        network[B] = [A]

#BFS()
DFS()
