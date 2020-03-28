N = int(input())
if N < 10:
    print(N)
    exit()
temp = N
dec = 1
res = 0
i = 1
while True:
    if temp < 10:
        N -= dec
        res += (N+1) * i
        break
    res += 9 * dec * i
    dec *= 10
    i += 1
    temp //= 10

print(res)
test_num = 100

# 1 ~ 9 : 1 (9개) => 9
# 10 ~ 99 = 2 (90개) => 180
# 100 ~ 999 = 3 (900개)
# 1000 ~ 9999 = 4 (9000)
