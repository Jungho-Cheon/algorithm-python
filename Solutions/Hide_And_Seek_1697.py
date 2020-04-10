from collections import deque

MAX = 100001
N, K = map(int, input().split())
time_table = [0] * MAX


def BFS():
    need_visit = deque([N])
    while need_visit:
        now = need_visit.popleft()

        if now == K:
            return time_table[now]

        for next_pos in (now - 1, now + 1, now * 2):
            # 이동할 수 있는 점에 대하여 범위 안에 있고, 방문한적이 없는 정점에 대해 큐에 넣는다.
            if 0 <= next_pos < MAX and not time_table[next_pos]:
                time_table[next_pos] = time_table[now] + 1
                need_visit.append(next_pos)


print(BFS())
