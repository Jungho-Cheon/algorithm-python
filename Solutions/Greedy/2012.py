# 등수 매기기
import sys

N = int(sys.stdin.readline())
array = []
for i in range(N):
    input_grade = int(sys.stdin.readline())
    array.append(input_grade)

array.sort()

result = 0
grade = 1

for i in range(N):
    result += abs(array[i] - grade)
    grade += 1

print(result)
