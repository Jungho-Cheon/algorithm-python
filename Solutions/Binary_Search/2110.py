# 공유기 설치
# 이진 탐색

N, C = map(int, input().split())
array = []
for _ in range(N):
    array.append(int(input()))

array.sort()


start = array[1] - array[0]
end = array[-1] - array[0]

result = 0
while start <= end:
    count = 1
    mid = (start + end) // 2
    idx = 1
    fix_idx = 0
    while idx < len(array):
        if array[idx] - array[fix_idx] >= mid:
            count += 1
            fix_idx = idx
        idx += 1
    if count >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)
