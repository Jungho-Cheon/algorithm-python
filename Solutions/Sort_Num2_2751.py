# Python은 약 1초에 20,000,000개의 연산이 가능하다고 가정한다.
import sys

# 계수 정렬 알고리즘 사용.


def Solution1(data):
    for _ in range(N):
        input = int(sys.stdin.readline())
        data[input + MAX] += 1

    for i in range(len(data)):
        if data[i] != 0:
            print(i - MAX)

# 병합 정렬 사용.


def Solution2(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = Solution2(data[:mid])
    right = Solution2(data[mid:])

    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1
        k += 1

    if i == len(left):
        while j < len(right):
            data[k] = right[j]
            k += 1
            j += 1
    elif j == len(right):
        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1
    return data


N = int(input())

#MAX = 1000000
#data = [0] * ((MAX * 2) + 1)
# Solution1(data)

MS_data = list()
for _ in range(N):
    MS_data.append(int(sys.stdin.readline()))

MS_data = Solution2(MS_data)

for data in MS_data:
    print(data)
