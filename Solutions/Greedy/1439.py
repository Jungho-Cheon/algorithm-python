string = input()
N = len(string)
# 모두 1로 만드는 경우
result_1 = 0
idx = 0
while idx < len(string):
    if string[idx] == '0':
        for i in range(idx, N):
            if string[i] == '1' or i == N - 1:
                idx = i + 1
                result_1 += 1
                break
    else:
        idx += 1


# 모두 0으로 만드는 경우
result_0 = 0
idx = 0
while idx < len(string):
    if string[idx] == '1':
        for i in range(idx, N):
            if string[i] == '0' or i == N - 1:
                idx = i + 1
                result_0 += 1
                break
    else:
        idx += 1

print(min(result_0, result_1))
