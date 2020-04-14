def solution(n, computers):
    def BFS(node, visits):
        v = [node]
        visits[node] = 1
        while(v):
            cur = v.pop(0)
            for i in range(n):
                if computers[cur][i] == 1 and visits[i] == 0:
                    visits[i] = 1
                    v.append(i)

    visits = [0] * n
    answer = 0
    for i in range(n):
        try:
            BFS(visits.index(0), visits)
            answer += 1
        except:
            break

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
