N = int(input())
array = []
for _ in range(N):
    array.append(int(input()))

left_max = array[0]
right_max = array[-1]

left = 1
right = 1
for i in range(len(array)):
    if left_max < array[i]:
        left += 1
        left_max = array[i]
    if right_max < array[N - i - 1]:
        right += 1
        right_max = array[N - i - 1]


print(left)
print(right)
