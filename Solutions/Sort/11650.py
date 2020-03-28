N = int(input())
array = []
for _ in range(N):
    x, y = map(int, input().split())
    array.append((x, y))
array.sort(key=lambda x: (x[0], x[1]))
for c in array:
    print(c[0], c[1])
