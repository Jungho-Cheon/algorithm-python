test_case = int(input())

for cases in range(test_case):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    # data에 있는 요소들을 인덱스와 값을 가지는 튜플형태로 변환
    data = [(i, idx) for idx, i in enumerate(data)]

    count = 0
    while True:
        # data의 첫번쨰 요소를 비교하기 위해 lambda함수 사용
        if data[0][0] == max(data, key=lambda x: x[0])[0]:
            count += 1
            if data[0][1] == M:
                print(count)
                break
            else:
                data.pop(0)
        else:
            data.append(data.pop(0))
