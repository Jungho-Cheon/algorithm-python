# The Candy War

test_case = int(input())


def one_phase():
    # 1 순환
    temp = [arr[i] // 2 for i in range(N)]
    for i in range(N):
        arr[i] = temp[i]
        if i == 0:
            arr[i] += temp[-1]
        else:
            arr[i] += temp[i - 1]

    # 사탕이 홀수인 경우 1개를 더 해준다.
    for i in range(N):
        if arr[i] % 2 != 0:
            arr[i] += 1


result = []
for _ in range(test_case):
    N = int(input())
    arr = [*map(int, input().split())]

    # 사탕이 홀수인 경우 1개를 더 해준다. (초기화.)
    for i in range(N):
        if arr[i] % 2 != 0:
            arr[i] += 1

    count = 0
    while len(set(arr)) > 1:
        one_phase()
        count += 1

    result.append(count)

[print(i) for i in result]
