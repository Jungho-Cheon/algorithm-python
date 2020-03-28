N = int(input())

arr = [[*map(int, input().split())] for _ in range(N)]
arr.sort(key=lambda x: (x[1]-x[0], x[0]))
res = 1
for i in range(N):
    count = 0
    if N-i <= res:
        break
    for j in range(i, N):
        if arr[j][1] >= arr[i][1] >= arr[j][0]:
            count += 1
        elif arr[i][1] < arr[j][0]:
            break

    res = max(res, count)
print(res)
