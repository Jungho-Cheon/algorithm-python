input_num = int(input())
data = list()
for i in range(input_num):
    current_input = list(map(str, input().split(' ')))
    data.append((int(current_input[0]), current_input[1]))
    print(type(data[i]))
data = sorted(data, key=lambda x: x[0])
for i in range(len(data)):
    print(data[i][0], data[i][1])
