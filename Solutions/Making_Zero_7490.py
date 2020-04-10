import copy
import ast


def recursive(array, n):
    if len(array) == n:
        # array를 바로 append()할 경우 call by reference로 인해 최종 값인 []이 저장된다.
        # copy라이브러리의 deepcopy를 사용해 값만 복사해온다.
        operator_list.append(copy.deepcopy(array))
        return

    # 재귀함수로 모든 경우의 수를 구하는 경우 push, pop사이에서 함수를 호출함으로써 해당 값들이 모든 경우대로 들어갈 수 있게 한다.
    array.append(' ')
    recursive(array, n)
    array.pop()
    array.append('+')
    recursive(array, n)
    array.pop()
    array.append('-')
    recursive(array, n)
    array.pop()


test_case = int(input())
for _ in range(test_case):
    n = int(input())
    operator_list = list()
    recursive([], n - 1)

    integers = list([i for i in range(1, n + 1)])

    for operators in operator_list:
        string = ""
        for i in range(n - 1):
            string += str(integers[i]) + operators[i]
        string += str(integers[-1])

        # evel(String s) : 문자열 수식 s를 계산해준다.
        # eval()은 문자열 그대로를 실행시켜 시스템을 노출시킬 수 있다.
        # ast라이브러리의 literal_eval()사용.
        # literal_eval()은 파이썬에서 지원하는 기본 계산식만 계산해준다.
        if ast.literal_eval(string.replace(" ", "")) == 0:
            print(string)

    print()
