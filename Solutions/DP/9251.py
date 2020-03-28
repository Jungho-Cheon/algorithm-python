string_A = "0" + input()
string_B = "0" + input()

len_A = len(string_A)
len_B = len(string_B)

array = [[0] * (len_A) for _ in range(len_B)]

for i in range(1, len_B):
    for j in range(1, len_A):
        if string_A[j] == string_B[i]:
            array[i][j] = array[i - 1][j - 1] + 1
        else:
            array[i][j] = max(array[i - 1][j], array[i][j - 1])

print(array[len_B - 1][len_A - 1])
