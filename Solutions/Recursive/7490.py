# 0 만들기

import copy
import ast

# 연산자의 조합을 만든다.


def solution(array, n):
    if len(array) == n:
        operators.append(copy.deepcopy(array))
        return

    array.append(' ')
    solution(array, n)
    array.pop()

    array.append('+')
    solution(array, n)
    array.pop()

    array.append('-')
    solution(array, n)
    array.pop()


test_case = int(input())
for _ in range(test_case):
    operators = []
    num = int(input())
    solution([], num - 1)

    integers = [i for i in range(1, num + 1)]

    for operator in operators:
        string = ""
        for j in range(num - 1):
            string += str(integers[j]) + operator[j]
        string += str(integers[-1])
        if ast.literal_eval(string.replace(" ", "")) == 0:
            print(string)
    print()
