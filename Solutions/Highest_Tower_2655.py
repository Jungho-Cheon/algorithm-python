# 한가지 factor(무게)로 정렬한 후 다른 factor(넓이)로 LIS 수행한다.
# 기준 값 i에 대해 비교값 j를 갱신하며 최대 높이를 구한다.
# 최대 높이를 구한 뒤 DP상에서 최대 높이가 기록된 index를 구하여 역으로 블록의 번호를 구한다.

N = int(input())
array = []

# 블록 번호, 넓이, 높이, 무게
array.append((0, 0, 0, 0))
for i in range(1, N + 1):
    area, height, weight = map(int, input().split())
    array.append((i, area, height, weight))

# 무게로 정렬
array = sorted(array, key=lambda x: x[3])

DP = [0] * (N + 1)

# 정렬된 무게로 넓이 비교
for i in range(1, N + 1):
    for j in range(0, i):
        if array[i][1] > array[j][1]:
            DP[i] = max(DP[i], DP[j] + array[i][2])

max_value = max(DP)
index = N
result = []

while index != 0:
    if max_value == DP[index]:
        result.append(array[index][0])
        max_value -= array[index][2]
    index -= 1

print(len(result))
result.reverse()
[print(i) for i in result]
