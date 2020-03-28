# 스택 수열
import sys

N = int(input())
stack = []
result = []
top = 0

for _ in range(N):
    num = int(input())
    if top < num:
        while top < num:
            top += 1
            stack.append(top)
            result.append('+')
        stack.pop()
        result.append('-')
    else:
        if stack.pop() != num:
            print("NO")
            sys.exit()
        result.append('-')

print('\n'.join(result))
