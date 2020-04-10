# 집 사이의 간격에 대해 이진 탐색 알고리즘을 사용한다.
# N <= 200,000
# input X <= 1,000,000,000

# 가능한 큰값을 구하기 위해 Max, Min값을 설정하고 이진탐색 알고리즘을 이용하여
# 주어진 조건에 맞는 값을 찾는다.
import sys

N, C = map(int, input().split())
input_data = list()
for _ in range(N):
    input_data.append(int(sys.stdin.readline()))

input_data.sort()

MIN = input_data[1] - input_data[0]
MAX = input_data[-1] - input_data[0]
result = 0

while MIN <= MAX:
    mid = (MIN + MAX) // 2

    value = input_data[0]
    count = 1
    for idx in range(1, len(input_data)):
        if input_data[idx] >= value + mid:
            value = input_data[idx]
            count += 1

    if count >= C:
        MIN = mid + 1
        result = mid
    else:
        MAX = mid - 1

print(result)
