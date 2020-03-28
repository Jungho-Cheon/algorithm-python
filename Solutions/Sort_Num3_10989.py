# 데이터의 수가 많고 범위가 좁은경우 계수 정렬(Counting Sort) 알고리즘 사용.
# Python의 경우 입력 데이터의 개수가 많을 때 sys.stdin.readline()을 사용해야 빠르다.
import sys

input_num = int(input())

data = list([0 for i in range(10001)])
# data = [0] * 10001

for _ in range(input_num):
    input_data = sys.stdin.readline()
    data[int(input_data)] += 1

for i in range(10001):
    for _ in range(data[i]):
        print(i)
