# Solution Key : 문제의 breadth를 구하기 위해 중위 순회를 이용한다..
# 추가적으로 depth를 구하기위해 depth를 구해 저장한다.


class Node():
    def __init__(self, value, left_node, right_node):
        self.parent = -1
        self.value = value
        self.left_node = left_node
        self.right_node = right_node


# 중위 순회를 이용하여 가장 왼쪽 끝 노드로 향한다.
# x 좌표 값을 1씩 증가하며 현재 depth의 최대 최소값을 갱신한다.
def in_order(node, level):
    global level_depth, x
    level_depth = max(level_depth, level)
    if node.left_node != -1:
        in_order(tree[node.left_node], level + 1)
    level_min[level] = min(level_min[level], x)
    level_max[level] = max(level_max[level], x)
    x += 1
    if node.right_node != -1:
        in_order(tree[node.right_node], level + 1)


n = int(input())
tree = {}
level_depth = 1
x = 1
level_min = [n]
level_max = [0]
root = 1

# tree 초기화
for i in range(1, n + 1):
    tree[i] = Node(i, -1, -1)
    level_min.append(n)
    level_max.append(0)

# node입력 받기
# 입력 node의 parent, left, right node assign
for _ in range(n):
    value, left_node, right_node = map(int, input().split())
    tree[value].left_node = left_node
    tree[value].right_node = right_node
    if left_node != -1:
        tree[left_node].parent = value
    if right_node != -1:
        tree[right_node].parent = value

# parent가 -1인 node를 찾아 root로 정한다.
for i in range(1, n + 1):
    if tree[i].parent == -1:
        root = i

in_order(tree[root], 1)

result_level = 1
result_width = level_max[1] - level_min[1] + 1
for i in range(2, level_depth + 1):
    width = level_max[i] - level_min[i] + 1
    if result_width < width:
        result_width = width
        result_level = i

print(result_level, result_width)
