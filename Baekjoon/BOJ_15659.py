N = int(input())
nums = list(input().split())
opers = [*map(int, input().split())]
MAX = -2e9
MIN = 2e9
V = []

def toOper(num):
    if num == 0:
        return '+'
    elif num == 1:
        return '-'
    elif num == 2:
        return '*'
    else:
        return '//'

def calculate():
    global MAX, MIN
    string = []
    
    for i in range(0, len(nums) - 1):
        if len(string) >= 1:
            string.append(toOper(V[i]))
            string.append(nums[i+1])
        else:
            string.append(nums[i])
            string.append(toOper(V[i]))
            string.append(nums[i+1])
        
    
    res =  eval(''.join(string))
    MAX = max(MAX, res)
    MIN = min(MIN, res)


def DFS(depth):
    if depth == N - 1:
        calculate()
        return

    for i in range(4):
        if opers[i] >= 1:
            opers[i] -= 1
            V.append(i)
            DFS(depth+1)
            V.pop()
            opers[i] += 1

DFS(0)
print(MAX)
print(MIN)