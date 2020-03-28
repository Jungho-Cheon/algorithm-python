import sys

N = int(input())
Cranes = list(map(int, input().split()))
Cranes.sort(reverse=True)

M = int(input())
Items = list(map(int, input().split()))
Items.sort(reverse=True)

# 크레인이 모든 짐을 옮길 수 없는 경우
if Cranes[0] < Items[0]:
    print(-1)
    sys.exit()

positions = [0] * N
checked = [False] * M
count = 0
result = 0

while True:
    if count == M:
        break
    for i in range(N):
        while positions[i] < M:
            if not checked[positions[i]] and Cranes[i] >= Items[positions[i]]:
                checked[positions[i]] = True
                positions[i] += 1
                count += 1
                break
            positions[i] += 1
    result += 1

print(result)
