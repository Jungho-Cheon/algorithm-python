# 특정 노드의 값과 왼쪽, 오른쪽 노드를 찾기위해 dictionary구조를 이용하는 것이 포인트이다.


class Node:
    def __init__(self, value, left_node, right_node):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node


def pre_order(node):
    print(node.value, end='')
    if node.left_node != '.':
        pre_order(tree[node.left_node])
    if node.right_node != '.':
        pre_order(tree[node.right_node])


def in_order(node):
    if node.left_node != '.':
        in_order(tree[node.left_node])
    print(node.value, end='')
    if node.right_node != '.':
        in_order(tree[node.right_node])


def post_order(node):
    if node.left_node != '.':
        post_order(tree[node.left_node])
    if node.right_node != '.':
        post_order(tree[node.right_node])
    print(node.value, end='')


node_nums = int(input())
# 간단한 트리 구현을 위해 dictionary 사용
tree = {}
for _ in range(node_nums):
    value, left_node, right_node = input().split()
    # 값이 value인 노드를 가르킴.
    tree[value] = Node(value, left_node, right_node)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])
print()
