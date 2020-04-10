# 가장 높은 탑 쌓기

N = int(input())
array = [(0, 0, 0, 0)]
adj = [0] * (N + 1)
for i in range(N):
    area, height, weight = map(int, input().split())
    array.append((area, height, weight, i + 1))

# 밑면의 넓이로 정렬
array.sort(key=lambda x: x[0])

for i in range(1, N + 1):
    for j in range(i):
        # 무게가 더 클 경우 최대 높이를 갱신해준다.
        if array[i][2] > array[j][2]:
            adj[i] = max(adj[i], adj[j] + array[i][1])

# 가장 높은 높이를 찾는다
max_height = max(adj)
index = N
result = []

# 가장 높은 높이부터 그 높이를 가능하게 만든 블럭을 찾는다. (역추적)
while index > 0:
    if adj[index] == max_height:
        result.append(array[index][3])
        max_height -= array[index][1]
    index -= 1

print(len(result))
result.reverse()
[print(i) for i in result]
