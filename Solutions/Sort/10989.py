import sys
N = int(input())
array = [0] * 10001

for _ in range(N):
    array[int(sys.stdin.readline())] += 1

for i in range(len(array)):
    for _ in range(array[i]):
        print(i)
