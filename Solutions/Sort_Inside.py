input_data = list(map(int, input()))
input_data.sort(reverse=True)
result = ""
for i in range(len(input_data)):
    result += str(input_data[i])
print(result)
