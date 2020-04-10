# 트리 순회


def preorder(node):
    if node == '.':
        return
    print(node, end='')
    preorder(data[node][0])
    preorder(data[node][1])


def inorder(node):
    if node == '.':
        return
    inorder(data[node][0])
    print(node, end='')
    inorder(data[node][1])


def postorder(node):
    if node == '.':
        return
    postorder(data[node][0])
    postorder(data[node][1])
    print(node, end='')


N = int(input())
data = dict()
for _ in range(N):
    parent, left, right = input().split()
    data[parent] = (left, right)

preorder("A")
print()
inorder("A")
print()
postorder("A")
print()
