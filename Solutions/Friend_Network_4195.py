# Union-Find Algorithm 사용
# 부모의 값을 변경시켜주어 연결되어있는 집합을 구분할 수 있다.

# 부모가 초기값이 아니라면 재귀적으로 부모를 찾는 함수
def Find(x):
    if x == parent[x]:
        return x
    else:
        p = Find(parent[x])
        parent[x] = p
        return parent[x]

# 부모가 다르다면 한쪽으로 연결하여 합집합한다.
def Union(x, y):
    x = Find(x)
    y = Find(y)

    # 서로 연결 되어있다는 것만 확인하면 되기 때문에 다르다면 한방향으로 연결하면된다.
    if x != y:
        parent[y] = x
        number[x] += number[y]


test_case = int(input())

for _ in range(test_case):
    parent = dict()
    number = dict()

    num_relation = int(input())

    for _ in range(num_relation):
        x, y = input().split(' ')

        if x not in parent:
            parent[x] = x
            number[x] = 1

        if y not in parent:
            parent[y] = y
            number[y] = 1

        Union(x, y)
        print(number[Find(x)])
