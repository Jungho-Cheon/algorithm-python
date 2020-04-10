# 늑대와 양

R, C = map(int, input().split())
# 입력을 string으로 받으면 수정이 불가능하므로 문자열을 하나하나 받도록한다.
arr = [list(input()) for _ in range(R)]
#print(arr)

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

result = 1
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'S':
            for dx, dy in direction:
                new_x = j + dx
                new_y = i + dy
                if 0 <= new_x < C and 0 <= new_y < R:
                    if arr[new_y][new_x] == 'W':
                        result = 0
                    elif arr[new_y][new_x] == '.':
                        arr[new_y][new_x] = 'D'

if result == 1:
    print(result)
    for i in arr:
        print(''.join(i))
else:
    print(0)
