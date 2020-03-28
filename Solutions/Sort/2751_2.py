# 수 정렬하기 2
# 병합정렬을 사용 (분할 정복)

# 두개의 조각을 각각의 인덱스에 대해 합병하며 정렬
def Merge(A, B):
    result = []
    idx_A = 0
    idx_B = 0
    while idx_A < len(A) and idx_B < len(B):
        if A[idx_A] > B[idx_B]:
            result.append(B[idx_B])
            idx_B += 1
        else:
            result.append(A[idx_A])
            idx_A += 1

    if len(A) == idx_A:
        while len(B) > idx_B:
            result.append(B[idx_B])
            idx_B += 1
    elif len(B) == idx_B:
        while len(A) > idx_A:
            result.append(A[idx_A])
            idx_A += 1
    return result


def Merge_Sort(A):
    if len(A) == 1:
        return A
    mid = len(A) // 2
    left = Merge_Sort(A[:mid])
    right = Merge_Sort(A[mid:])
    return Merge(left, right)


N = int(input())
array = []
for _ in range(N):
    array.append(int(input()))

array = Merge_Sort(array)
for i in array:
    print(i)
