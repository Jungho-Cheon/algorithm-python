input_data = int(input())

data = dict()
for _ in range(input_data):
    book_name = input()
    if book_name in data:
        data[book_name] += 1
    else:
        data[book_name] = 1

data = list(zip(data.keys(), data.values()))
data = sorted(data, key=lambda x: (-x[1], x[0]))
print(data[0][0])
