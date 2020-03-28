N = int(input())
array = []
for i in range(N):
    A, B = input().split()
    array.append((i, int(A), B))

array.sort(key=lambda x: (x[1], x[0]))
for i in array:
    print(i[1], i[2])
