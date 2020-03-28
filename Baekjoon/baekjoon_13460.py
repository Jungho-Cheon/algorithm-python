result = 987654321
directions = ((-1,0), (0,1), (1,0), (0,-1))

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]


# R의 위치 찾기, B의 위치 찾기.
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            r = (i,j)
            board[i][j] = '.'
        elif board[i][j] == 'B':
            b = (i,j)
            board[i][j] = '.'


#[print(i) for i in board]

def tilt(nRx, nRy, nBx, nBy, Cnt, dir_):
    global result

    if Cnt > 10 or Cnt >= result:
        return

    rx = nRx
    ry = nRy
    bx = nBx
    by = nBy

    r_flag = False
    b_flag = False
    
    while True:
        rx += directions[dir_][0] 
        ry += directions[dir_][1]
        
        
        if board[rx][ry] == '#':
            rx -= directions[dir_][0] 
            ry -= directions[dir_][1]
            break
        elif board[rx][ry] == 'O':
            r_flag = True
            break

    while True:
        bx += directions[dir_][0] 
        by += directions[dir_][1]
        
        
        if board[bx][by] == '#':
            bx -= directions[dir_][0] 
            by -= directions[dir_][1]
            break
        elif board[bx][by] == 'O':
            b_flag = True
            break
    
    if b_flag:
        return
    else:
        if r_flag:
            result = min(result, Cnt)
            return

    if rx == bx and ry == by:
        r_dist = abs(rx - nRx) + abs(ry - nRy)
        b_dist = abs(bx - nBx) + abs(by - nBy)

        if r_dist < b_dist:
            bx -= directions[dir_][0] 
            by -= directions[dir_][1]
        else:
            rx -= directions[dir_][0] 
            ry -= directions[dir_][1]
    
    for i in range(4):
        if i == dir_ or i == (dir_ + 2) % 4:
            continue
        tilt(rx,ry, bx, by, Cnt+1, i)

def start():
    for i in range(4):
        tilt(r[0], r[1], b[0], b[1], 1, i)

    if result > 10 or result == 987654321:
        print(-1)
    else:
        print(result)

start()

