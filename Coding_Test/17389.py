# 보너스 점수

N = int(input())
data = input()

bonus = 0
result = 0
for i in range(len(data)):
    if data[i] == 'O':
        result += (i + 1) + bonus
        bonus += 1
    else:
        bonus = 0
print(result)
