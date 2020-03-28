# 그리디 알고리즘은 정렬을 사용하는 경우가 많다.. 한번쯤 고려해보자
import sys

N = int(input())
grades = []

for _ in range(N):
    grades.append(int(sys.stdin.readline()))

grades.sort()

result = 0
count = 1
for i in grades:
    result += abs(i - count)
    count += 1

print(result)
