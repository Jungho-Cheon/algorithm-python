# 숨바꼭질

MAX = 100001
N, K = map(int, input().split())
time_table = [0] * MAX


def BFS():
    need_visit = list([N])
    while need_visit:
        now = need_visit.pop(0)
        if now == K:
            return time_table[now]
        for next_pos in [now - 1, now + 1, now * 2]:

            # count 변수 사용시 매번 pop할 때마다 증가한다.
            # -1, +1, *2가 되서 움직일 수 있는 경우 파생된 시간 + 1로 해결한다.
            if 0 <= next_pos < MAX and not time_table[next_pos]:
                time_table[next_pos] = time_table[now] + 1
                need_visit.append(next_pos)


print(BFS())
