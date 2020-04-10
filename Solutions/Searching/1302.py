N = int(input())
data = dict()
for _ in range(N):
    book = input()
    if book in data:
        data[book] += 1
    else:
        data[book] = 1

data = list(zip(data.keys(), data.values()))
data.sort(key=lambda x: (-x[1], x[0]))
print(data[0][0])
