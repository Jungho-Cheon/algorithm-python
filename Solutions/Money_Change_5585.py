# 그리디 알고리즘

Moneys = [500, 100, 50, 10, 5, 1]
Change = 1000 - int(input())

count = 0
for i in Moneys:
    count += Change // i
    Change %= i

print(count)
