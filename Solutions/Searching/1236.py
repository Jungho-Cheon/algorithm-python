# 성 지키기

N, M = map(int, input().split())

row = [False] * N
col = [False] * M
for i in range(N):
    line = input()
    if "X" in line:
        row[i] = True
        for j in range(M):
            if line[j] == 'X':
                col[j] = True


row_count = 0
col_count = 0

for i in range(N):
    if not row[i]:
        row_count += 1

for j in range(M):
    if not col[j]:
        col_count += 1

print(max(row_count, col_count))
