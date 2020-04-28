# https://programmers.co.kr/learn/courses/30/lessons/42861
# 섬 연결하기

parents = []


def find(a):
    if parents[a] == a:
        return a
    parents[a] = find(parents[a])
    return parents[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parents[b] = a


def ck():
    tmp = find(parents[0])
    for i in range(1, len(parents)):
        if tmp != find(parents[i]):
            return False
    return True

# 사이클을 이루는지 확인


def ck2(a, b):
    if find(parents[a]) != find(parents[b]):
        return False
    return True


def solution(n, costs):
    global parents
    parents = [i for i in range(n)]
    costs.sort(key=lambda x: x[2])
    answer = 0
    for a, b, dist in costs:
        if ck2(a, b):
            continue
        union(a, b)
        answer += dist
        if ck():
            break
    return answer


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
