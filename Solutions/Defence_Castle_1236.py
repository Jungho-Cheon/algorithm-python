N, M = map(int, input().split())
data = []
for i in range(N):
    data.append(input())

row = [0] * N
column = [0] * M

for i in range(N):
    for j in range(M):
        if data[i][j] == 'X':
            row[i] = 1
            column[j] = 1

row_count = 0
column_count = 0
for i in range(N):
    if row[i] == 0:
        row_count += 1
for j in range(M):
    if column[j] == 0:
        column_count += 1

print(max(row_count, column_count))
