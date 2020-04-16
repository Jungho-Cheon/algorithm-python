def solution(budgets, M):
    budgets.sort()
    if sum(budgets) < M:
        return budgets[-1]

    answer = 0
    prev_val = 0

    MIN = 0
    MAX = 1000000

    while True:
        threshold = (MIN + MAX) // 2

        cur_total = sum([min(b, threshold) for b in budgets])

        if threshold == prev_val:
            answer = threshold
            break

        if M < cur_total:
            MAX = threshold
        else:
            MIN = threshold

        prev_val = threshold

    return answer


print(solution([120, 110, 140, 150], 485))
