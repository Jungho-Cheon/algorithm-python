# 이름 궁합 테스트


def merge(A, B):
    result = ""
    idx_A = 0
    idx_B = 0
    while idx_A < len(A) and idx_B < len(B):
        result += A[idx_A] + B[idx_B]
        idx_A += 1
        idx_B += 1
    if idx_A == len(A):
        result += B[idx_B:]
    elif idx_B == len(B):
        result += A[idx_A:]
    return result


def name_test(merged_name):
    while len(merged_name) > 2:
        next_value = []
        for i in range(len(merged_name) - 1):
            next_value.append((merged_name[i] + merged_name[i + 1]) % 10)
        merged_name = next_value

    return merged_name[0] * 10 + merged_name[1]


alpha = {"A": 3, "B": 2, "C": 1, "D": 2, "E": 4,
         "F": 3, "G": 1, "H": 3, "I": 1, "J": 1,
         "K": 3, "L": 1, "M": 3, "N": 2, "O": 1,
         "P": 2, "Q": 2, "R": 2, "S": 1, "T": 2,
         "U": 1, "V": 1, "W": 1, "X": 2, "Y": 2,
         "Z": 1
         }

N, M = map(int, input().split())
A, B = input().split()
merged_name = merge(A, B)
arr = [alpha[a] for a in merged_name]
print(name_test(arr) , end= '')
print("%")
