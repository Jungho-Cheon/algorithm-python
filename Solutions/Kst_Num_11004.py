def Merge_Sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = Merge_Sort(data[:mid])
    right = Merge_Sort(data[mid:])

    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1
        k += 1

    if i == len(left):
        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1
    return data


N, K = map(int, input().split())
input_data = list(map(int, input().split()))
input_data = Merge_Sort(input_data)
print(input_data[K - 1])
