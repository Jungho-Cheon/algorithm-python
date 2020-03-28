N = 71

ck = [False] * (N + 1)

for i in range(2, N):
    if ck[i]:
        continue
    else:
        for j in range(2 * i, N, i):
            ck[j] = True


for i in range(2, N):
    if not ck[i]:
        print(i)
