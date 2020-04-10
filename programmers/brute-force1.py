def solution(answers):
    answer = []
    patternA = [1, 2, 3, 4, 5]
    patternB = [2, 1, 2, 3, 2, 4, 2, 5]
    patternC = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    collect = [0, 0, 0]

    for i in range(len(answers)):

        if (answers[i] == patternA[i % 5]):
            collect[0] += 1

        if (answers[i] == patternB[i % 8]):
            collect[1] += 1

        if (answers[i] == patternC[i % 10]):
            collect[2] += 1

    lst = sorted(list(enumerate(collect, start=1)), key=lambda x: -x[1])
    print(lst)
    for l, col in lst:
        if col == lst[0][1]:
            answer.append(l)
    return answer


print(solution([1, 2, 3, 4, 5]))
