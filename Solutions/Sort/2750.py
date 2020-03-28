N = int(input())
array = []

for _ in range(N):
    array.append(int(input()))

for i in range(N):
    min_index = i
    for j in range(i + 1, N):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

for i in array:
    print(i)
