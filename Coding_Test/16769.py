# Mixing Milk

arr = [[] for _ in range(3)]
for i in range(3):
    A, B = map(int, input().split())
    arr[i].extend([A, B])


count = 0
for count in range(100):
    # 순환적인 인덱스는 i % N으로 처리
    cur_idx = count % 3
    next_idx = (count + 1) % 3

    # 넘치지 않는 경우 -> 모두 부을 수 있음
    if arr[cur_idx][1] <= arr[next_idx][0] - arr[next_idx][1]:
        arr[next_idx][1] += arr[cur_idx][1]
        arr[cur_idx][1] = 0

    # 넘치는 경우 -> 넘치는 양만큼 남게됨
    else:
        over = -(arr[next_idx][0] - arr[next_idx][1] - arr[cur_idx][1])
        arr[next_idx][1] = arr[next_idx][0]
        arr[cur_idx][1] = over

[print(i[1]) for i in arr]
