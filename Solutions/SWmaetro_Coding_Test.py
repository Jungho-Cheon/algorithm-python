N, K = map(int, input().split())
arr = [*map(int, input().split())]

# K등분 한다..
dist_arr = [arr[i] - arr[i-1] for i in range(1, N)]
dist_arr.sort()
res = 0
for i in range(N-K):
    res += dist_arr[i]
print(res)
