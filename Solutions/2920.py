# 구분문자로 공백을 가지는 문자열을 분석하여
# 숫자들이 오름차순인지 내림차순인지 불규칙한지 판별하는 알고리즘
import datetime
import random


def Solution(data):
    # Descending Check
    if data[0] > data[1]:
        for idx in range(1, len(data) - 1):
            if data[idx] < data[idx + 1]:
                return "mixed"
        return "Descending"
    # Ascending Check
    else:
        for idx in range(1, len(data) - 1):
            if data[idx] > data[idx + 1]:
                return "mixed"
        return "Ascending"


def Solution_2(data):
    Asc = True
    Desc = True
    for idx in range(0, len(data) - 1):
        if data[idx] > data[idx + 1]:
            Asc = False
        else:
            Desc = False
    if Asc:
        return "Ascending"
    elif Desc:
        return "Descending"
    else:
        return "mixed"


# input_data = list(map(int, input().split(' ')))
input_data = random.sample(range(1000), 1000)
input_data.sort(reverse=True)

start1 = datetime.datetime.now()
print(Solution_2(input_data))
end1 = datetime.datetime.now()
print("Execution time : ", end1 - start1)
