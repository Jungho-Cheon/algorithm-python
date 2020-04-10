

import functools


def comparator(a, b):
    lineA = a+b
    lineB = b+a
    return (lineA > lineB) - (lineA < lineB)


def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True, key=functools.cmp_to_key(comparator))
    return str(int(''.join(numbers)))


print(solution([0, 0, 0, 0]))
