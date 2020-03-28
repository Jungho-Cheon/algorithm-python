import sys

N = int(input())
M = int(input())

if M >= N:
    print(0)
    sys.exit()

array = list(map(int, input().split()))
array.sort()


center_array = [array[i + 1] - array[i] for i in range(len(array) - 1)]
center_array.sort(reverse=True)
for i in range(M - 1):
    center_array[i] = 0

print(sum(center_array))
