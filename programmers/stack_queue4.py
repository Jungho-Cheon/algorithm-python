def solution(prices):
    answer = [i for i in range(len(prices)-1, -1, -1)]

    s = []
    for idx, p in enumerate(prices):
        cur = (idx, p)
        if not s:
            s.append(cur)
        else:
            while s:
                # 현재 값과 stack의 top의 값을 비교해서 가격이 하락했다면
                # 인덱스를 비교해서 걸린 시간을 구한다.
                if cur[1] < s[-1][1]:
                    answer[s[-1][0]] = cur[0] - s[-1][0]
                    s.pop()
                else:
                    break
            s.append(cur)

    return answer


print(solution([1, 2, 3, 2, 3]))
