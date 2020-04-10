N = int(input())
array = [0, 1]

if N >= 2:
    for _ in range(N - 1):
        temp = array[0] + array[1]
        array[0], array[1] = array[1], temp
print(array[-1])
