# 트리의 높이와 너비
# 루트 노드가 항상 1이 아닐 수 있는 점을 주의해야한다.


class Node():
    def __init__(self, value, left, right):
        self. parent = -1
        self.value = value
        self.left = left
        self.right = right


def inorder(node, level):
    if node == -1:
        return
    global max_depth, x
    max_depth = max(max_depth, level)

    inorder(tree[node].left, level + 1)

    level_min[level] = min(level_min[level], x)
    level_max[level] = max(level_max[level], x)
    x += 1

    inorder(tree[node].right, level + 1)


N = int(input())
tree = {}
root = -1
x = 1
max_depth = 0
level_min = [N]
level_max = [0]

# 노드를 미리 생성해 부모노드가 없게끔함. 각 level의 최댓값, 최솟값을 구하기 위한 초기화
for i in range(1, N + 1):
    tree[i] = Node(i, -1, -1)
    level_min.append(N)
    level_max.append(0)


# 노드를 입력받고 자식노드가 있는경우 부모노드를 초기화해준다. 이후 부모노드가 없는 노드를 root 노드로 사용하게된다.
for _ in range(N):
    parent, left, right = map(int, input().split())
    tree[parent].left = left
    tree[parent].right = right
    if left != -1:
        tree[left].parent = parent
    if right != -1:
        tree[right].parent = parent

# root node 찾기
for i in range(1, N + 1):
    if tree[i].parent == -1:
        root = i

# root node를 시작점으로 중위 순회한다.
inorder(root, 1)


max_level = 0
max_breadth = 0
for i in range(1, max_depth + 1):
    cur_breadth = level_max[i] - level_min[i] + 1
    if max_breadth < cur_breadth:
        max_level, max_breadth = i, cur_breadth

print(max_level, max_breadth)
