# 2048(easy)
import copy


N = int(input())
input_data = [[*map(int, input().split())] for _ in range(N)]
directions = []
test = []


def find_direction(lst):
    if len(lst) == 5:
        global directions
        directions.append(copy.deepcopy(lst))
        return

    lst.append('up')
    find_direction(lst)
    lst.pop()

    lst.append('down')
    find_direction(lst)
    lst.pop()

    lst.append('left')
    find_direction(lst)
    lst.pop()

    lst.append('right')
    find_direction(lst)
    lst.pop()


def merge(line):
    idx = 0
    tmp = []
    while idx < len(line):
        if idx == len(line) - 1:
            if line[idx] == 0:
                break
            tmp.append(line[idx])
            break
        if line[idx] == line[idx + 1]:
            tmp.append(line[idx] * 2)
            line[idx + 1] = 0
            idx += 1
        else:
            if line[idx] == 0:
                idx += 1
                continue
            tmp.append(line[idx])
            idx += 1

    return tmp


def move(direction):
    for d in direction:
        if d == 'up':
            for i in range(N):
                temp = []
                for j in range(N):
                    if M[j][i] != 0:
                        temp.append(M[j][i])
                        M[j][i] = 0
                # print("up")
                # print(temp)
                new_line = merge(temp)
                # print(new_line)
                for j in range(len(new_line)):
                    M[j][i] = new_line.pop(0)
        elif d == 'down':
            for i in range(N):
                temp = []
                for j in range(N - 1, -1, -1):
                    if M[j][i] != 0:
                        temp.append(M[j][i])
                        M[j][i] = 0
                # print("down")
                # print(temp)
                new_line = merge(temp)
                # print(new_line)
                for j in range(N - 1, N - len(new_line) - 1, -1):
                    M[j][i] = new_line.pop(0)
        elif d == 'left':
            for i in range(N):
                temp = []
                for j in range(N):
                    if M[i][j] != 0:
                        temp.append(M[i][j])
                        M[i][j] = 0
                # print("left")
                # print(temp)
                new_line = merge(temp)
                # print(new_line)
                for j in range(len(new_line)):
                    M[i][j] = new_line.pop(0)
        elif d == 'right':
            for i in range(N):
                temp = []
                for j in range(N - 1, -1, -1):
                    if M[i][j] != 0:
                        temp.append(M[i][j])
                        M[i][j] = 0
                # print("right")
                # print(temp)
                new_line = merge(temp)
                # print(new_line)
                for j in range(N - 1, N - len(new_line) - 1, -1):
                    M[i][j] = new_line.pop(0)

    #[print(i) for i in M]
    ret = -1
    for row in M:
        temp = copy.deepcopy(row)
        temp.append(ret)
        ret = max(temp)
    return ret


find_direction([])
# print(len(directions))

MAX = -1
for d in directions:
    # print(d)
    M = copy.deepcopy(input_data)
    ret = move(d)
    MAX = max(MAX, ret)
    # print('-----------------------')


print(MAX)
