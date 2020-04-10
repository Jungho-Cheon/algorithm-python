#nums = int(input())
#data = list()
# for i in range(nums):
#    data.append(int(input()))

#nums = 8
#data = list([4, 3, 6, 8, 7, 5, 2, 1])


def Solution(data, nums, result):
    stack = list()
    current = 1
    input_idx = 0

    while True:
        if len(stack) == 0:
            stack.append(current)
            current += 1
            result.append('+')
        else:
            if data[input_idx] > stack[-1]:
                stack.append(current)
                current += 1
                result.append('+')

            elif data[input_idx] == stack[-1]:
                stack.pop()
                result.append('-')
                input_idx += 1
                if input_idx == nums:
                    return True
            elif data[input_idx] < stack[-1]:
                if stack[-1] != data[input_idx]:
                    return False


def Solution_fast(num):
    count = 1
    stack = list()
    result = list()
    for i in range(num):
        data = int(input())
        while count <= data:
            stack.append(count)
            count += 1
            result.append('+')
        if stack[-1] == data:
            stack.pop()
            result.append('-')
        else:
            print('NO')
            return
    print('\n'.join(result))
    return


#result = list()
# if Solution(data, nums, result):
#    for i in result:
#        print(i)
# else:
#    print('NO')

num = int(input())
Solution_fast(num)
