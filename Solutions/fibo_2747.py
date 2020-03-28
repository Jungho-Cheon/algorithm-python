# DP 사용 (점화식 사용)
# 재귀 함수 사용 시 같은 수를 여러번 구하기 때문에 시간초과가 걸린다. O(2^n)

num = int(input())
data = [0, 1]
if num >= 2:
    for _ in range(num - 1):
        data.append(data[-1] + data[-2])
print(data[-1])
