# 01타일
# DP -> 점화식 구하기
# 1 => 1 (1)
# 2 => 2 (11, 00)
# 3 => 3 (111, 001, 100)
# 4 => 5 (1111, 1100, 1001, 0011, 0000)

N = int(input())
array = [1, 2]
if N > 2:
    for _ in range(N - 2):
        array[0], array[1] = array[1], (array[0] + array[1]) % 15746
    print(array[1])
else:
    print(array[N - 1])
