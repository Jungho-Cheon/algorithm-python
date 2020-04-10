# 키로거
test_case = int(input())
result = []
for _ in range(test_case):
    input_data = input()
    left_stack = []
    right_stack = []
    for i in input_data:
        if i == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif i == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        elif i == '-':
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(i)

    result1 = ''.join(left_stack)
    result2 = ''.join(reversed(right_stack))
    result.append(result1 + result2)

print('\n'.join(result))
