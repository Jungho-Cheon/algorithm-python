import sys

N = int(input())
cranes = [*map(int, input().split())]
M = int(input())
boxes = [*map(int, input().split())]

cranes.sort(reverse=True)
boxes.sort(reverse=True)

# 크레인이 모든 짐을 옮길 수 없는 경우
if cranes[0] < boxes[0]:
    print(-1)
    sys.exit()

# 박스가 옮겨졌는지에 대한 유무
box_check = [False] * M

# i번째 crane이 옮길 수 있는 무게의 box index
crane_accept = [0] * N
for i in range(N):
    if cranes[i] < boxes[-1]:
        crane_accept[i] = M
    else:
        for j in range(M):
            if cranes[i] >= boxes[j]:
                crane_accept[i] = j
                break

result = 0
remain_boxes = M
while remain_boxes > 0:
    for i in range(N):
        temp = 0
        for j in range(crane_accept[i], M):
            if not box_check[j]:
                box_check[j] = True
                crane_accept[i] = j
                remain_boxes -= 1
                break
    result += 1

print(result)
