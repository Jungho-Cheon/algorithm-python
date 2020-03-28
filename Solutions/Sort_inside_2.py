input_data = input()
num_check = list([0 for i in range(10)])
for idx in range(len(input_data)):
    num_check[int(input_data[idx])] += 1

for i in range(9, -1, -1):
    for j in range(num_check[i]):
        print(i, end='')
print('')
