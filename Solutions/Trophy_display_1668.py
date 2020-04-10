N = int(input())
data = []
for _ in range(N):
    data.append(int(input()))

left_start = data[0]
right_start = data[-1]

left_count = 1
right_count = 1
for i in range(N):
    if left_start < data[i]:
        left_count += 1
        left_start = data[i]
    if right_start < data[-i - 1]:
        right_count += 1
        right_start = data[-i - 1]

print(left_count)
print(right_count)
