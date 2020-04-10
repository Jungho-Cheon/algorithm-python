N = int(input())
cur = 1
result = 0
while N >= 0:
    if N < cur:
        cur = 1
    N -= cur
    cur += 1
    result += 1

print(result - 1)
