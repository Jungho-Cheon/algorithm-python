test_case = int(input())


for i in range(test_case):
    input_data = list(input())
    left_data = list()
    right_data = list()
    idx = 0
    for j in range(len(input_data)):
        if input_data[j] == '<':
            if left_data:
                right_data.append(left_data.pop())
        elif input_data[j] == '>':
            if right_data:
                left_data.append(right_data.pop())
        elif input_data[j] == '-':
            if left_data:
                left_data.pop()
        else:
            left_data.append(input_data[j])

    left_data.extend(reversed(right_data))
    print(''.join(left_data))
