test_case = int(input())


def find_parent(x):
    if parent[x] == x:
        return x
    else:
        p = find_parent(parent[x])
        parent[x] = p
        return parent[x]


def union_find(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x != y:
        parent[y] = x
        number[x] += number[y]


for _ in range(test_case):
    F = int(input())
    parent = dict()
    number = dict()
    for _ in range(F):
        A, B = input().split()
        if A not in parent:
            parent[A] = A
            number[A] = 1
        if B not in parent:
            parent[B] = B
            number[B] = 1
        union_find(A, B)
        print(number[find_parent(A)])
