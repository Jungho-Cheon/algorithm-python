# Longest Common Subsequence
# 최장 공통 부분 수열

# 점화식
# D[i][j]는 X[i], Y[j]의 공통 부분 수열의 최대 길이
# D[i][j] = D[i-1][j-1] + 1     if X[i] == Y[j]
#           max(D[i-1][j], D[i][j-1])   if X[i] != Y[j]

string_A = "0" + input()
string_B = "0" + input()

len_A = len(string_A)
len_B = len(string_B)

DP = [[0] * (len_A) for _ in range(len_B)]

for i in range(1, len_B):
    for j in range(1, len_A):
        if string_A[j] == string_B[i]:
            DP[i][j] = DP[i - 1][j - 1] + 1
        else:
            DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])

print(DP[len_B - 1][len_A - 1])
